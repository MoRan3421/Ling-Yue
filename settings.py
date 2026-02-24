import os

from client_main import VirtualJoystick

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def asset(path):
    return os.path.join(BASE_DIR, "assets", path)

IS_MOBILE = False
try:
    IS_MOBILE = True
except ImportError:
    IS_MOBILE = False

if IS_MOBILE:
    joystick = VirtualJoystick(100, 600)
else:
    joystick = None  # 鼠标键盘