from setuptools import setup
from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    readme = fh.read()

setup(name='tubemp3',
    version='0.0.1',
    url='https://github.com/perseu912/toddy',
    license='MIT License',
    author='Reinan Br',
    entry_points = {
        'console_scripts': ['getmusic=tube.get_music_line:main'],
    },
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='slimchatuba@gmail.com',
    keywords='kit tools dev works',
    description=u'Library for development with toolskit for more works📈📊📚',
    packages=find_packages(),
    install_requires=['psutil','requests','googlesearch-python',
    'youtube-dl','mp3-tagger','stagger','eyed3'],)
