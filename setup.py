try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
        'description': 'A Brainfuck Interpreter',
        'author': 'Samvel Stepanyan',
        'url': 'https://github.com/samvelst/py_bfck',
        'download_url': 'https://samvelst@github.com/samvelst/py_bfck.git',
        'author_email': 'samvelst@gmail.com',
        'version': '1.0',
        'install_requires': ['nose'],
        'packages': ['py_bfck'],
        'scripts': [],
        'name': 'py_bfck'
        }

setup(**config)
