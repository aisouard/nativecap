import ctypes
import glob
import os
import platform


extensions = {
    "Windows": ".pyd",
    "Darwin": ".dylib"
}

system = platform.system()
extension = ".so" if system not in extensions else extensions[system]
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
