/*
 * Taken from https://stackoverflow.com/a/16141058/1025222
 */

#ifdef UNIX
#include <X11/X.h>
#include <X11/Xlib.h>
#include <X11/Xutil.h>

void nativecap(int x, int y, int width, int height, unsigned char* data) {
    Display *display = XOpenDisplay(NULL);
    Window root = DefaultRootWindow(display);

    XImage *image = XGetImage(display, root, x, y, width, height, AllPlanes, ZPixmap);

    unsigned long red_mask = image->red_mask;
    unsigned long green_mask = image->green_mask;
    unsigned long blue_mask = image->blue_mask;

    int ii = 0;
    int ix;
    int iy;

    for (iy = 0; iy < height; iy++) {
        for (ix = 0; ix < width; ix++) {
            unsigned long pixel = XGetPixel(image, ix, iy);
            unsigned char blue  = (pixel & blue_mask);
            unsigned char green = (pixel & green_mask) >> 8;
            unsigned char red   = (pixel & red_mask) >> 16;

            data[ii + 3] = 255;
            data[ii + 2] = red;
            data[ii + 1] = green;
            data[ii + 0] = blue;
            ii += 4;
        }
    }

    XDestroyImage(image);
    XDestroyWindow(display, root);
    XCloseDisplay(display);
}
#endif
