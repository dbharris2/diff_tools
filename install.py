#!/usr/bin/env python3

import os

destination = '/usr/local/bin/'
cp_command = 'cp ./gh-diff.py ' + destination
print('Executing: ' + cp_command)
os.system(cp_command)
