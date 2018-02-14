#!/usr/bin/env python
import unicornhat, signal
b = (0, 0, 132)
y = (132, 132, 0)

pixels = [[b, b, b, b, b, b, b, b],
          [b, b, y, y, y, b, b, b],
          [b, b, b, y, y, y, b, b],
          [b, b, b, b, y, y, y, b],
          [b, b, b, b, y, y, y, b],
          [b, b, b, y, y, y, b, b],
          [b, b, y, y, y, b, b, b],
          [b, b, b, b, b, b, b, b]]
unicornhat.brightness(0.4)
unicornhat.set_pixels(pixels)
unicornhat.show()
signal.pause()
