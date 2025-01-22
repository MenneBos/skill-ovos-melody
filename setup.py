from setuptools import setup

setup(
    name='ovos-skill-melody',
    version='0.1',
    description='A skill to play a melody',
    url='http://github.com/MenneBos/ovos-skill-melody',
    author='Menne',
    author_email='your.email@example.com',
    license='Apache-2.0',
    packages=['ovos-skill-melody'],
    install_requires=[
        'ovos_workshop'
    ],
    include_package_data=True,
    zip_safe=False
)
