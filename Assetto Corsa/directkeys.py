import time
import ctypes

SendInput = ctypes.windll.user32.SendInput

A = 0x1E
Z = 0x2C
LEFT = 0xCB
RIGHT = 0xCD

PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                #  ("mi", MouseInput),
                #  ("hi", HardwareInput)
                ]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

def pressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def releaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

# def test():
#     time.sleep(3)
#     pressKey(A)
#     time.sleep(3)
#     releaseKey(A)
#     time.sleep(1)

# test()

import pydirectinput
 
def straight():
    pydirectinput.keyUp('z')
    pydirectinput.keyDown('a')
    pydirectinput.keyUp('left')
    pydirectinput.keyUp('right')
    pydirectinput.keyUp('a') 

def left():
    pydirectinput.keyDown('left')
    pydirectinput.keyUp('a')
    pydirectinput.keyUp('right')
    pydirectinput.keyUp('z')
    pydirectinput.keyUp('left')


def right():
    pydirectinput.keyDown('right')
    pydirectinput.keyUp('left')
    pydirectinput.keyUp('a')
    pydirectinput.keyUp('z')
    pydirectinput.keyUp('right')


def brake():
    pydirectinput.keyDown('z')
    pydirectinput.keyUp('left')
    pydirectinput.keyUp('right')
    pydirectinput.keyUp('a')

def test():
    time.sleep(3)
    pydirectinput.keyDown('a')
    time.sleep(1)
    pydirectinput.keyDown('left')
    time.sleep(1)
    pydirectinput.keyUp('a')
    pydirectinput.keyUp('left')

