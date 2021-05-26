
from os.path import abspath
ignore_list = [
    __file__,
    abspath('russian_roulette.py'),
    abspath('config.py'),
    abspath('run.py'),
    abspath('__pycache__'),
    abspath('README.md'),
    abspath('.git'),
]

last_man_standing = True
