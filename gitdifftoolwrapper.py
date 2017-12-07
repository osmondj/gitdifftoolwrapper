#!/usr/bin/python3.6

import sys
import shutil
import os
import subprocess

def CopyAndOverwrite(from_path, to_path):
    if os.path.exists(to_path):
        shutil.rmtree(to_path)
    shutil.copytree(from_path, to_path)

left = sys.argv[1]
right = sys.argv[2]

leftTo = '/cygdrive/c/repo/tmp/diffLeft'
rightTo = '/cygdrive/c/repo/tmp/diffRight'

leftToWindows = "C:\\repo\\tmp\\diffLeft"
rightToWindows = "C:\\repo\\tmp\\diffRight"

CopyAndOverwrite(left, leftTo)
CopyAndOverwrite(right, rightTo)

subprocess.call(['/cygdrive/c/Program Files (x86)/Meld/Meld.exe', leftToWindows, rightToWindows])
