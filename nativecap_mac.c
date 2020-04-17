#ifdef MACOS
#import <ApplicationServices/ApplicationServices.h>
void nativecap(int x, int y, int width, int height, unsigned char* data) {
    CGImageRef image = CGDisplayCreateImage(CGMainDisplayID());
    
    size_t src_width = CGImageGetWidth(image);
    size_t src_bits_per_pixel = CGImageGetBitsPerPixel(image);
    size_t src_bytes_per_pixel = src_bits_per_pixel / 8;
    size_t src_bytes_per_row = CGImageGetBytesPerRow(image);
    
    CFDataRef image_data = CGDataProviderCopyData(CGImageGetDataProvider(image));
    const uint8_t *src = CFDataGetBytePtr(image_data) + (x * src_bytes_per_pixel) + (y * src_bytes_per_row);
    
    for (int i = 0; i < height; ++i) {
        memcpy(data, src, width * 4);
        data += width * 4;
        src += src_width * 4;
    }
    
    CFRelease(image_data);
    CFRelease(image);
}
#endif
