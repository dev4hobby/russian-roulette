import os
from shutil import rmtree
from random import randint, shuffle
try:
    from config import ignore_list
except ImportError:
    ignore_list = [
        __file__,
        os.path.abspath('russian_roulette.py'),
        os.path.abspath('config.py'),
        os.path.abspath('run.py'),
        os.path.abspath('__pycache__'),
        os.path.abspath('README.md'),
        os.path.abspath('.git'),
    ]
class Gun:
    magazine = list()
    safety_lock = False
    broken = False

    def __init__(self, _path='./'):
        self.load(_path)
        print(self.__class__.__name__)

    
    def shoot_decorator(shoot):
        def shoot_wrapper(self):
            okay = shoot(self)
            if not okay:
                self.load(os.path.dirname(os.path.abspath(__file__)))
            if (len(self.magazine) is 0) and (self.safety_lock is False):
                self.magazine += ignore_list
                self.safety_lock = True
            if self.safety_lock and len(self.magazine) < 1:
                self.broken = True
        return shoot_wrapper

    @shoot_decorator
    def shoot(self, times=1) -> bool:
        try:
            for _ in range(times):
                index = randint(0, len(self.magazine)-1)
                try:
                    target = self.magazine[index]
                    print('target >> {}'.format(target))
                    if os.path.isdir(target):
                        rmtree(target)
                    elif os.path.isfile(target):
                        os.remove(target)
                    else:
                        pass
                    del(self.magazine[index])
                except IndexError:
                    print('click')
        except Exception as e:
            # for unknown exception
            return False
        return True

    def load(self, _path: str):
        _path = _path if os.path.exists(_path) else './'
        self.magazine = list(
            set([os.path.abspath(file_name)
            for file_name
            in [ 
                os.path.join(_path, __path)
                for __path
                in os.listdir(_path)
            ]]) - set(ignore_list)
        )


class Revolver(Gun):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def fanning(self):
        return self.shoot(times=6)

    def spin(self):
        shuffle(self.magazine)
        print('kreek-')
        
class AR(Gun):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def semi_auto(self):
        return self.shoot(times=9)

    def full_auto(self):
        return self.shoot(times=30)
