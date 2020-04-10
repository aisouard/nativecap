import platform
from setuptools import setup
from distutils.core import Extension


platform_settings = {
    "Linux": {
        "sources": ["nativecap_x11.c"],
        "libraries": ["X11"]
    },
    "Windows": {
        "sources": ["nativecap_win.c"],
        "libraries": []
    },
    "Darwin": {
        "sources": ["nativecap_mac.c"],
        "libraries": []
    }
}

settings = platform_settings[platform.system()]
module = Extension("nativecap",
                   sources=settings["sources"],
                   libraries=settings["libraries"])

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name="nativecap",
      license="MIT",
      url="https://github.com/aisouard/pynativecap",
      version="1.0",
      author="Axel Isouard",
      author_email="axel@isouard.fr",
      description="Native screen capture module",
      long_description=long_description,
      long_description_content_type="text/markdown",
      classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6"
      ],
      python_requires='>=3.6',
      packages=["nativecap"],
      test_suite='nose.collector',
      tests_require=['nose'],
      ext_modules=[module])
