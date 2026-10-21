#!/usr/bin/env python3
"""Clone original PRMA Java project and apply Custom TACZ Automation resources.

Run this script from the extracted overlay ZIP. Python 3.9+ and Git required.
"""
from pathlib import Path
import subprocess, shutil, re, sys

BASE=Path(__file__).resolve().parents[1]
OVERLAY=BASE/'src/main/resources'
TARGET=BASE/'Create-Custom-TACZ-Automation-Source'
REPO='https://github.com/CTRL-Neo-Studios/PreciseManufacturing.git'
BRANCH='1.20.1-simple-create0.6'


def run(cmd, cwd=None):
    print('>', ' '.join(map(str,cmd)))
    subprocess.run(cmd, cwd=cwd, check=True)


def property_value(text,key,value):
    pat=re.compile(r'(?m)^\s*'+re.escape(key)+r'\s*=.*$')
    update=f'{key}={value}'
    if pat.search(text): return pat.sub(update,text)
    return text+'\n'+update+'\n'


def main():
    if TARGET.exists():
        raise SystemExit(f'Target already exists: {TARGET}. Rename or remove it first.')
    run(['git','clone','--branch',BRANCH,'--single-branch',REPO,str(TARGET)])
    resources=TARGET/'src/main/resources'
    if resources.exists(): shutil.rmtree(resources)
    shutil.copytree(OVERLAY,resources)
    # The overlay contains finished/generated recipes. Do not let older recipes
    # under src/generated/resources override or duplicate them in builds.
    generated=TARGET/'src/generated/resources/data/prma/recipes'
    if generated.exists(): shutil.rmtree(generated)
    properties=TARGET/'gradle.properties'
    if properties.exists():
        txt=properties.read_text(encoding='utf-8')
        for key,val in [
            ('minecraft_version','1.20.1'),
            ('forge_version','47.4.26'),
            ('mod_id','prma'),
            ('mod_name','Create: Custom TACZ Automation'),
            ('mod_version','1.2.2'),
            ('create_version','6.0.8-289'),
            ('ponder_version','1.0.91'),
            ('flywheel_version','1.0.5'),
            ('tacz_version_range','[1.1.8-hotfix2,)'),
        ]:
            txt=property_value(txt,key,val)
        properties.write_text(txt,encoding='utf-8')
    license_file=TARGET/'LICENSE'
    if not license_file.exists(): shutil.copy2(BASE/'LICENSE',license_file)
    (TARGET/'CUSTOM_TACZ_AUTOMATION_README.md').write_text((BASE/'README.md').read_text(encoding='utf-8'),encoding='utf-8')
    print('\nSource project prepared:',TARGET)
    print('Java files:',len(list((TARGET/'src/main/java').rglob('*.java'))))
    print('Recipe JSON:',len(list((TARGET/'src/main/resources/data/prma/recipes').rglob('*.json'))))
    print('IMPORTANT: Gradle dependency and compile compatibility were not verified.')
    print('See README.md and GITHUB_STEPS.md.')

if __name__=='__main__':
    try: main()
    except subprocess.CalledProcessError as exc:
        raise SystemExit('Failed. Confirm Git, network access, and the branch URL.') from exc
