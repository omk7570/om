import os
import sys
import subprocess



cmd = ("netsh wlan show profiles key=clear")
out = subprocess.check_output(cmd, shell=True)
print(out)
