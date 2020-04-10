#include <X11/X.h>
#include <X11/Xlib.h>
#include <X11/Xutil.h>

void nativecap(int x, int y, int width, int height, unsigned char* data) {
    Display *display = XOpenDisplay(NULL);
    Window root = DefaultRootWindow(display);

    XImage *image = XGetImage(display, root, x, y, 360, 640, AllPlanes, ZPixmap);

    unsigned long red_mask   = image->red_mask;
    unsigned long green_mask = image->green_mask;
    unsigned long blue_mask  = image->blue_mask;

    int ii = 0;
    int ix = 0;
    int iy = 0;

    for (iy = 0; iy < 640; iy++) {
        for (ix = 0; ix < 360; ix++) {
            unsigned long pixel = XGetPixel(image, ix, iy);
            unsigned char blue  = (pixel & blue_mask);
            unsigned char green = (pixel & green_mask) >> 8;
            unsigned char red   = (pixel & red_mask) >> 16;

            data[ii + 2] = blue;
            data[ii + 1] = green;
            data[ii + 0] = red;
            ii += 3;
        }
    }

    XDestroyImage(image);
    XDestroyWindow(display, root);
    XCloseDisplay(display);
}
