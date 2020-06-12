import pdb
import sys
import traceback


IGNORE = {'NameError',
        'ModuleNotFoundError',
        'KeyboardInterrupt',
        # 'SyntaxError',
        'BdbQuit',
        }


def debug_rescue(_type, _value, _traceback):
    traceback.print_exception(_type, _value, _traceback)
    # for d in dir(_value):
    #     print(getattr(_value, d))
    if _value.__class__.__name__ not in IGNORE:
        pdb.pm()


sys.excepthook = debug_rescue
