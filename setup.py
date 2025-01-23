#!/usr/bin/env python3
from setuptools import setup

URL = "https://github.com/OpenVoiceOS/skill-ovos-hello-world"
SKILL_CLAZZ = "HelloWorldSkill"  # needs to match __init__.py class name
PYPI_NAME = "ovos-skill-hello-world"  # pip install PYPI_NAME

# below derived from github url to ensure standard skill_id
SKILL_AUTHOR, SKILL_NAME = URL.split(".com/")[-1].split("/")
SKILL_PKG = SKILL_NAME.lower().replace('-', '_')
PLUGIN_ENTRY_POINT = f'{SKILL_NAME.lower()}.{SKILL_AUTHOR.lower()}={SKILL_PKG}:{SKILL_CLAZZ}'
# skill_id=package_name:SkillClass

setup(
    name='ovos-skill-melody',
    version='0.1',
    description='A skill to play a melody',
    url='https://github.com/MenneBos/ovos-skill-melody',
    author='Menne',
    author_email='your.email@example.com',
    license='Apache-2.0',
    package_dir={SKILL_PKG: ""},
    package_data={SKILL_PKG: find_resource_files()},
    packages=[SKILL_PKG],
    include_package_data=True,
    keywords='ovos skill plugin',
    entry_points={'ovos.plugin.skill': PLUGIN_ENTRY_POINT}
    # packages=['ovos-skill-melody'],
    #install_requires=[
    #    'ovos_workshop'
    #],
    #include_package_data=True,
    #zip_safe=False
)
