import ctypes
import glob
import os
import platform


system = platform.system()
extension = ".pyd" if system == "Windows" else ".so"
glob_str = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), '..', 'nativecap*{}'.format(extension))
library = ctypes.CDLL(glob.glob(glob_str)[0])
library.nativecap.argtypes = [
    ctypes.c_int32,
    ctypes.c_int32,
    ctypes.c_int32,
    ctypes.c_int32,
    ctypes.c_void_p
]


def capture(x, y, width, height):
    buffer = (ctypes.c_ubyte * (width * height * 4))()
    library.nativecap(x, y, width, height, buffer)
    return buffer
