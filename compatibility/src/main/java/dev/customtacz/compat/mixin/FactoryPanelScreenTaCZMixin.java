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
 * TaCZ gun-id aware recipe selection for Create: Extra Gauges 2.0.7.
 *
 * This runs BEFORE vanilla/Create's recipe search and cancels that search only
 * for a configured TaCZ gun. As a result, Extra Gauges' injected item-ID-only
 * search cannot overwrite the chosen mechanical recipe afterward.
 *
 * The field belongs to Extra Gauges' own mixin, not to Create. Reflective
 * access avoids the invalid @Shadow error that affected the first addon.
 * Other outputs are left to the original recipe logic.
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

    @Unique
    private static final String EXTRA_GAUGES_RECIPE_FIELD = "extra_gauges$availableMechanicalRecipe";

    @Unique
    private static Field customtacz$recipeField;

    @Unique
    private static boolean customtacz$fieldLookupFailed;

    @Unique
    private static Field customtacz$locateRecipeField(Object screen) {
        if (customtacz$recipeField != null) return customtacz$recipeField;
        if (customtacz$fieldLookupFailed) return null;
        try {
            Field found = screen.getClass().getDeclaredField(EXTRA_GAUGES_RECIPE_FIELD);
            if (found.getType() != MechanicalCraftingRecipe.class) {
                throw new NoSuchFieldException("Unexpected Extra Gauges recipe field type: " + found.getType());
            }
            found.setAccessible(true);
            customtacz$recipeField = found;
            return found;
        } catch (ReflectiveOperationException | SecurityException e) {
            customtacz$fieldLookupFailed = true;
            System.err.println("[Custom TACZ Automation] Extra Gauges mechanical recipe field unavailable; "
                + "falling back to default selection: " + e);
            return null;
        }
    }

    @Inject(method = "searchForCraftingRecipe", at = @At("HEAD"),
            remap = false, cancellable = true)
    private void customtacz$selectGunBeforeBaseSearch(CallbackInfo ci) {
        if (outputConfig == null || outputConfig.stack == null || inputConfig == null || inputConfig.isEmpty()) return;
        ItemStack desired = outputConfig.stack;
        if (desired.m_41619_()) return;
        CompoundTag tag = desired.m_41783_();
        if (tag == null) return;
        String requestedGunId = tag.m_128461_("GunId");
        if (requestedGunId.isEmpty()) return;

        ClientLevel level = Minecraft.m_91087_().f_91073_;
        if (level == null) return;

        Field recipeField = customtacz$locateRecipeField(this);
        if (recipeField == null) return;

        // Never select by base item alone. Multiple TaCZ guns are the same
        // minecraft item with different GunId values.
        MechanicalCraftingRecipe selected = null;
        @SuppressWarnings("unchecked")
        List<MechanicalCraftingRecipe> recipes = (List<MechanicalCraftingRecipe>)(List<?>)
                level.m_7465_().m_44013_(AllRecipeTypes.MECHANICAL_CRAFTING.getType());
        for (MechanicalCraftingRecipe recipe : recipes) {
            if (AllRecipeTypes.shouldIgnoreInAutomation(recipe)) continue;
            if (!customtacz$matchesGun(desired, requestedGunId, recipe, level)) continue;
            if (!customtacz$matchesConfiguredInputs(recipe)) continue;
            selected = recipe;
            break;
        }

        try {
            recipeField.set(this, selected);
        } catch (IllegalAccessException e) {
            System.err.println("[Custom TACZ Automation] Could not assign Extra Gauges recipe: " + e);
            return;
        }

        // Disable the vanilla 3x3 fallback for the configured TaCZ gun.
        // Cancelling HEAD also prevents Extra Gauges' TAIL injector from
        // replacing the GunId-matched mechanical crafting recipe.
        availableCraftingRecipe = null;
        ci.cancel();
    }

    @Unique
    private static boolean customtacz$matchesGun(ItemStack desired, String gunId,
            MechanicalCraftingRecipe recipe, ClientLevel level) {
        ItemStack result = recipe.m_8043_(level.m_9598_());
        if (result == null || !ItemStack.m_41656_(desired, result)) return false;
        CompoundTag resultTag = result.m_41783_();
        return resultTag != null && gunId.equals(resultTag.m_128461_("GunId"));
    }

    /** Exact item-presence filter used by Extra Gauges 2.0.7. */
    @Unique
    private boolean customtacz$matchesConfiguredInputs(MechanicalCraftingRecipe recipe) {
        Set<Item> configuredTypes = new HashSet<>();
        for (BigItemStack configured : inputConfig) {
            if (configured != null && configured.stack != null && !configured.stack.m_41619_()) {
                configuredTypes.add(configured.stack.m_41720_());
            }
        }
        Set<Item> usedTypes = new HashSet<>();
        for (Ingredient ingredient : recipe.m_7527_()) {
            if (ingredient.m_43947_()) continue;
            boolean found = false;
            for (BigItemStack configured : inputConfig) {
                if (configured == null || configured.stack == null || configured.stack.m_41619_()) continue;
                if (ingredient.test(configured.stack)) {
                    found = true;
                    usedTypes.add(configured.stack.m_41720_());
                    break;
                }
            }
            if (!found) return false;
        }
        return usedTypes.size() >= configuredTypes.size();
    }
}
