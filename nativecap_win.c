#ifdef WIN32
#include <stdio.h>
#include <windows.h>

__declspec(dllexport) void __cdecl nativecap(int x, int y, int width, int height, unsigned char* data) {
    HDC desktop_dc = GetDC(0);
    HDC capture_dc = CreateCompatibleDC(desktop_dc);
    HBITMAP bitmap = CreateCompatibleBitmap(desktop_dc, width, height);
    HGDIOBJ old_bitmap = SelectObject(capture_dc, bitmap);

    BitBlt(capture_dc, 0, 0, width, height, desktop_dc, x, y, SRCCOPY);

    BITMAPINFO bitmap_info = { 0 };
    bitmap_info.bmiHeader.biSize = sizeof(bitmap_info.bmiHeader);

    GetDIBits(desktop_dc, bitmap, 0, 0, NULL, &bitmap_info, DIB_RGB_COLORS);
    bitmap_info.bmiHeader.biCompression = BI_RGB;
    GetDIBits(desktop_dc, bitmap, 0, bitmap_info.bmiHeader.biHeight, reinterpret_cast<LPVOID>(data), &bitmap_info, DIB_RGB_COLORS);

    SelectObject(desktop_dc, old_bitmap);
    DeleteDC(capture_dc);
    ReleaseDC(0, desktop_dc);
    DeleteObject(bitmap);
}
#endif
