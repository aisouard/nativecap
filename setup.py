import sys

from setuptools import setup
from distutils.core import Extension


platform_settings = {
    "win32": {
        "macros": [("WIN32", None)],
        "libraries": []
    },
    "cygwin": {
        "macros": [("WIN32", None)],
        "libraries": []
    },
    "msys": {
        "macros": [("WIN32", None)],
        "libraries": []
    },
    "darwin": {
        "macros": [("MACOS", None)],
        "libraries": []
    },
    "linux": {
        "macros": [("UNIX", None)],
        "libraries": ["X11"]
    }
}

platform = sys.platform
if platform not in platform_settings:
    platform = "linux"

settings = platform_settings[platform]
module = Extension("nativecap",
                   sources=[
                       "nativecap_x11.c",
                       "nativecap_win.c",
                       "nativecap_mac.c"
                   ],
                   define_macros=settings["macros"],
                   libraries=settings["libraries"])

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name="nativecap",
      license="MIT",
      url="https://github.com/aisouard/pynativecap",
      version="1.0.1",
      author="Axel Isouard",
      author_email="axel@isouard.fr",
      description="Native screen capture module",
      long_description=long_description,
      long_description_content_type="text/markdown",
      classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8"
      ],
      packages=["nativecap"],
      test_suite="nose.collector",
      tests_require=["nose"],
      ext_modules=[module])
