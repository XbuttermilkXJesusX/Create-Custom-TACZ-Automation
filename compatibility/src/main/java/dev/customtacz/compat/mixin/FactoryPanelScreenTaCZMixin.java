package dev.customtacz.compat.mixin;

import com.simibubi.create.AllRecipeTypes;
import com.simibubi.create.content.kinetics.crafter.MechanicalCraftingRecipe;
import com.simibubi.create.content.logistics.BigItemStack;
import java.lang.reflect.Field;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import net.minecraft.client.Minecraft;
import net.minecraft.client.multiplayer.ClientLevel;
import net.minecraft.nbt.CompoundTag;
import net.minecraft.world.item.Item;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.item.crafting.CraftingRecipe;
import net.minecraft.world.item.crafting.Ingredient;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.Shadow;
import org.spongepowered.asm.mixin.Unique;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.Inject;
import org.spongepowered.asm.mixin.injection.callback.CallbackInfo;

/**
 * Applies the known-working GunId recipe fix without modifying Extra Gauges' JAR.
 * This client-side hook executes after Extra Gauges' factory-panel search hook.
 * Only TaCZ gun outputs with nonempty GunId are handled; all others are untouched.
 *
 * Source uses Forge 1.20.1 SRG method names because the distributed mod jars
 * are already compiled against those runtime names.
 */
@Mixin(targets = "com.simibubi.create.content.logistics.factoryBoard.FactoryPanelScreen",
       priority = 900, remap = false)
public abstract class FactoryPanelScreenTaCZMixin {

    @Shadow(remap = false)
    private BigItemStack outputConfig;

    @Shadow(remap = false)
    private List<BigItemStack> inputConfig;

    @Shadow(remap = false)
    private CraftingRecipe availableCraftingRecipe;

    // Extra Gauges adds this @Unique field in a DIFFERENT mixin. It cannot be
    // shadowed here: the target class does not contain the field when this mixin
    // is being validated. Read/write it reflectively only once both mixins
    // have transformed the class, at normal GUI runtime.
    @Unique
    private static final String EXTRA_GAUGES_RECIPE_FIELD = "extra_gauges$availableMechanicalRecipe";
    @Unique
    private static Field customtacz$recipeField;
    @Unique
    private static boolean customtacz$fieldLookupFailed;

    @Unique
    private static Field customtacz$recipeField(Object screen) {
        if (customtacz$recipeField != null) return customtacz$recipeField;
        if (customtacz$fieldLookupFailed) return null;
        try {
            Field f = screen.getClass().getDeclaredField(EXTRA_GAUGES_RECIPE_FIELD);
            if (f.getType() != MechanicalCraftingRecipe.class) {
                throw new NoSuchFieldException("Unexpected field type: " + f.getType());
            }
            f.setAccessible(true);
            customtacz$recipeField = f;
            return f;
        } catch (ReflectiveOperationException | SecurityException ex) {
            customtacz$fieldLookupFailed = true;
            System.err.println("[Extra Gauges x TaCZ Compat] Could not locate the Extra Gauges recipe field; "
                    + "leaving original selection unchanged: " + ex);
            return null;
        }
    }


    @Inject(method = "searchForCraftingRecipe", at = @At("TAIL"), remap = false)
    private void customtacz$matchSpecificGun(CallbackInfo ci) {
        // Extra Gauges itself only searches mechanical recipes when vanilla
        // crafting didn't already provide one.
        if (availableCraftingRecipe != null || outputConfig == null) return;

        ItemStack wanted = outputConfig.stack;
        if (wanted == null || wanted.m_41619_()) return;
        CompoundTag nbt = wanted.m_41783_();
        if (nbt == null) return;
        String gunId = nbt.m_128461_("GunId");
        if (gunId.isEmpty()) return;

        ClientLevel level = Minecraft.m_91087_().f_91073_;
        if (level == null) return;

        Field recipeField = customtacz$recipeField(this);
        if (recipeField == null) return;

        MechanicalCraftingRecipe existing;
        try {
            existing = (MechanicalCraftingRecipe) recipeField.get(this);
        } catch (IllegalAccessException ex) {
            System.err.println("[Extra Gauges x TaCZ Compat] Could not read recipe field: " + ex);
            return;
        }
        if (existing != null && matchesGun(wanted, gunId, existing, level)) return;

        // Choose a recipe for THIS gun, and never silently leave a recipe for
        // another gun with the same underlying tacz:modern_kinetic_gun item.
        MechanicalCraftingRecipe matchingRecipe = null;
        @SuppressWarnings("unchecked")
        List<MechanicalCraftingRecipe> recipes = (List<MechanicalCraftingRecipe>) (List<?>)
                level.m_7465_().m_44013_(AllRecipeTypes.MECHANICAL_CRAFTING.getType());
        for (MechanicalCraftingRecipe recipe : recipes) {
            if (AllRecipeTypes.shouldIgnoreInAutomation(recipe)) continue;
            if (!matchesGun(wanted, gunId, recipe, level)) continue;
            if (!matchesConfiguredInputs(recipe)) continue;
            matchingRecipe = recipe;
            break;
        }
        try {
            recipeField.set(this, matchingRecipe);
        } catch (IllegalAccessException ex) {
            System.err.println("[Extra Gauges x TaCZ Compat] Could not set recipe field: " + ex);
        }
    }

    private static boolean matchesGun(ItemStack wanted, String gunId,
                                       MechanicalCraftingRecipe recipe, ClientLevel level) {
        ItemStack result = recipe.m_8043_(level.m_9598_());
        if (result == null || !ItemStack.m_41656_(wanted, result)) return false;
        CompoundTag resultTag = result.m_41783_();
        return resultTag != null && gunId.equals(resultTag.m_128461_("GunId"));
    }

    /** Match Extra Gauges 2.0.7's original ingredient-availability filter. */
    private boolean matchesConfiguredInputs(MechanicalCraftingRecipe recipe) {
        if (inputConfig == null) return false;
        Set<Item> allConfiguredItems = new HashSet<>();
        for (BigItemStack configured : inputConfig) {
            if (configured != null && configured.stack != null && !configured.stack.m_41619_()) {
                allConfiguredItems.add(configured.stack.m_41720_());
            }
        }
        Set<Item> usedItems = new HashSet<>();
        for (Ingredient ingredient : recipe.m_7527_()) {
            if (ingredient.m_43947_()) continue;
            boolean found = false;
            for (BigItemStack configured : inputConfig) {
                if (configured == null || configured.stack == null || configured.stack.m_41619_()) continue;
                if (ingredient.test(configured.stack)) {
                    found = true;
                    usedItems.add(configured.stack.m_41720_());
                    break;
                }
            }
            if (!found) return false;
        }
        return usedItems.size() >= allConfiguredItems.size();
    }
}
