# -*- coding: utf-8 -*-
import os
import sys
import site
import json


# usercustomize.py
try:
    os.symlink(os.getcwd()+'/python/usercustomize.py', site.USER_SITE+'/usercustomize.py')
except FileExistsError as e:
    print(e)
    print('Check ' + site.USER_SITE + '/usercustomize.py')
