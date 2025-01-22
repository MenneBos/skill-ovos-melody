from setuptools import setup

setup(
    name='mycroft-melody-skill',
    version='0.1',
    description='A skill to play a melody',
    url='http://github.com/yourusername/mycroft-melody-skill',
    author='Your Name',
    author_email='your.email@example.com',
    license='Apache-2.0',
    packages=['mycroft-melody-skill'],
    install_requires=[
        'ovos_workshop'
    ],
    include_package_data=True,
    zip_safe=False
)