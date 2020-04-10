import ctypes
import glob
import os
import platform


platform_settings = {
    "Linux": {
        "extension": ".so",
        "channels": 3
    },
    "Windows": {
        "extension": ".dll",
        "channels": 4
    },
    "Darwin": {
        "extension": ".dylib",
        "channels": 3
    }
}

system = platform.system()
if system not in platform_settings:
    raise "Unsupported platform {}".format(system)

settings = platform_settings[system]
glob_str = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..',
                                        'nativecap*{}'.format(settings["extension"]))
library = ctypes.CDLL(glob.glob(glob_str)[0])
library.nativecap.argtypes = [
    ctypes.c_int32,
    ctypes.c_int32,
    ctypes.c_int32,
    ctypes.c_int32,
    ctypes.c_void_p
]

num_channels = settings["channels"]

def capture(x, y, width, height):
    buffer = (ctypes.c_ubyte * (width * height * num_channels))()
    library.nativecap(x, y, width, height, buffer)
    return buffer
