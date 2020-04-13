# nativecap

Take a screenshot with Python, natively, using a method based on
[that answer](https://stackoverflow.com/a/16141058/1025222).

## Setup

```
pip install nativecap
```

## Usage

```python
import nativecap

buffer = nativecap.capture(top_left_x, top_left_y, width, height)
```

## Example

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
