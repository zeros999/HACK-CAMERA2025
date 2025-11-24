import os

try:
    os.chdir("HACK-CAMERA")
except:
    os.system("git clone https://github.com/hackerxphantom/HACK-CAMERA")
    os.chdir("HACK-CAMERA")

os.system("bash hack_camera.sh")
