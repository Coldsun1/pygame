try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'pygame',
    'author': 'Cold Sun',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'bikingrox@gmail.com',
    'version': '0.1',
    'install_requires': ['pytest', 'pygame'],
    'packages': ['game'],
    'scripts': [],
    'name': 'game'
}

setup(**config)
