import ffmpeg
from os import remove

class ColorCoordsConverter:


    def rgb_to_yuv(r, g, b): #this first method converts RGB to YUV
        y = 0.257 * r + 0.504 * g + 0.098 * b + 16
        u = -0.148 * r - 0.291 * g + 0.439 * b + 128
        v = 0.439 * r - 0.368 * g - 0.071 * b + 128
        return y, u, v

    def yuv_to_rgb(y, u, v): #this second method converts YUV to RGB
        r = 1.164 * (y - 16) + 1.596 * (v - 128)
        g = 1.164 * (y - 16) - 0.813 * (v - 128) - 0.391 * (u - 128)
        b = 1.164 * (y - 16) + 2.018 * (u - 128)

        r = max(0, min(255, round(r))) #we ensure that the values are in the range [0, 255] after rounding them to the nearest integer
        g = max(0, min(255, round(g)))
        b = max(0, min(255, round(b)))

        return r, g, b

class FFmpeg:

    def resize_image(path, new_width, new_height, output_path):
        try:
            remove(output_path)
        except FileNotFoundError:
            pass

        (
            ffmpeg
            .input(path)
            .filter("scale", new_width, new_height)
            .output(output_path)
            .run()
        )
        print(f"Image resized and saved to: {output_path}")



#we test the code

R, G, B = 100, 150, 200
print("RGB:", (R, G, B))

y, u, v = ColorCoordsConverter.rgb_to_yuv(R, G, B)
print("YUV:", (y, u, v))

r2, g2, b2 = ColorCoordsConverter.yuv_to_rgb(y, u, v)
print("Back to RGB:", (r2, g2, b2))



# TESTING EXERCISE 3
FFmpeg.resize_image(
    path="/Users/marretamal/Desktop/video_coding/S1-JPEG-JPEG2000-and-FFMpeg/selfie2.jpeg",
    new_width=320,
    new_height=240,
    output_path="/Users/marretamal/Desktop/video_coding/S1-JPEG-JPEG2000-and-FFMpeg/output_coding.png"
)