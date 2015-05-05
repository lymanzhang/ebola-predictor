#!/usr/bin/env python

import os

curr_dir = os.getcwd()
app_dir = os.path.join(curr_dir, 'app/evdcare')
icon_file = os.path.join(app_dir, 'icon.png')
pfora_dir = os.path.abspath('../python-for-android/dist/default')
os.chdir(pfora_dir)

cmd_str = './build.py --package org.sabetilab.evdcare --name "EVD CARE" --version 0.1 --dir ' + app_dir + ' --orientation "sensor" --icon ' + icon_file + ' debug installd'
os.system(cmd_str)
os.chdir(curr_dir)