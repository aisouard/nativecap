# nativecap

Take a screenshot with Python, natively.

## Setup

```
pip install nativecap
```

## Usage

```python
import numpy as np
import nativecap
import platform


x = 0
y = 0
width = 640
height = 480

buffer = nativecap.capture(x, y, width, height)
image = np.ctypeslib.as_array(buffer)

if platform.system() == "Windows":
    # remove the alpha channel, swap BGR to RGB
    image = image.reshape(width, height, 4)[:, :, -2::-1]
elif platform.system() == "Linux":
    # just reshape it
    image = image.reshape(width, height, 3)
else:
    raise "Unsupported platform {}".format(platform.system())
```
