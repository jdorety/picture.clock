#!/usr/bin/env python
import unicornhat, signal
pixels = [[(0, 0, 0), (0, 0, 0), (0, 0, 0), (255, 255, 0), (255, 255, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 205, 0), (0, 205, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (0, 205, 0), (156, 0, 255), (0, 205, 0), (0, 205, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 205, 0), (0, 205, 0), (0, 205, 0), (0, 205, 0), (0, 221, 212), (0, 205, 0), (0, 0, 0)], [(0, 0, 0), (0, 205, 0), (0, 205, 0), (0, 205, 0), (0, 205, 0), (0, 205, 0), (0, 205, 0), (0, 0, 0)], [(0, 205, 0), (255, 0, 0), (0, 205, 0), (0, 205, 0), (255, 174, 0), (0, 205, 0), (0, 205, 0), (0, 205, 0)], [(0, 205, 0), (0, 205, 0), (0, 0, 255), (0, 205, 0), (0, 205, 0), (0, 205, 0), (255, 0, 255), (0, 205, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (206, 151, 19), (206, 151, 19), (0, 0, 0), (0, 0, 0), (0, 0, 0)]]
unicornhat.set_pixels(pixels)
unicornhat.show()
signal.pause()