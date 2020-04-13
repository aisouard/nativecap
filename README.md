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

# outputs an array containing pixel colors in the BGRA format
buffer = nativecap.capture(top_left_x, top_left_y, width, height)
```

## Example

```python
import cv2
import numpy as np
import nativecap
import platform


x = 0
y = 0
width = 640
height = 480

buffer = nativecap.capture(x, y, width, height)
image = np.ctypeslib.as_array(buffer)
image = image.reshape(width, height, 4)

cv2.imshow("image", image)
cv2.waitKey(0)
```
