import unicornhat as unicorn
import time
import datetime

moon = [[(0, 0, 132), (0, 0, 132), (0, 0, 132), (0, 0, 132), (0, 0, 132), (0, 0, 132), (0, 0, 132), (0, 0, 132)],
          [(0, 0, 132), (0, 0, 132), (132, 132, 0), (132, 132, 0), (132, 132, 0), (0, 0, 132), (0, 0, 132), (0, 0, 132)],
          [(0, 0, 132), (0, 0, 132), (0, 0, 132), (132, 132, 0), (132, 132, 0), (132, 132, 0), (0, 0, 132), (0, 0, 132)],
          [(0, 0, 132), (0, 0, 132), (0, 0, 132), (0, 0, 132), (132, 132, 0), (132, 132, 0), (132, 132, 0), (0, 0, 132)],
          [(0, 0, 132), (0, 0, 132), (0, 0, 132), (0, 0, 132), (132, 132, 0), (132, 132, 0), (132, 132, 0), (0, 0, 132)],
          [(0, 0, 132), (0, 0, 132), (0, 0, 132), (132, 132, 0), (132, 132, 0), (132, 132, 0), (0, 0, 132), (0, 0, 132)],
          [(0, 0, 132), (0, 0, 132), (132, 132, 0), (132, 132, 0), (132, 132, 0), (0, 0, 132), (0, 0, 132), (0, 0, 132)],
          [(0, 0, 132), (0, 0, 132), (0, 0, 132), (0, 0, 132), (0, 0, 132), (0, 0, 132), (0, 0, 132), (0, 0, 132)]]

sun = [[(255, 255, 30), (0, 158, 158), (0, 158, 158), (255, 255, 30), (0, 158, 158), (0, 158, 158), (0, 158, 158), (255, 255, 30)],
          [(0, 158, 158), (255, 255, 30), (0, 158, 158), (255, 255, 30), (0, 158, 158), (0, 158, 158), (255, 255, 30), (0, 158, 158)],
          [(0, 158, 158), (0, 158, 158), (255, 255, 30), (255, 255, 30), (255, 255, 30), (255, 255, 30), (0, 158, 158), (0, 158, 158)],
          [(0, 158, 158), (0, 158, 158), (255, 255, 30), (255, 255, 30), (255, 255, 30), (255, 255, 30), (255, 255, 30), (255, 255, 30)],
          [(255, 255, 30), (255, 255, 30), (255, 255, 30), (255, 255, 30), (255, 255, 30), (255, 255, 30), (0, 158, 158), (0, 158, 158)],
          [(0, 158, 158), (0, 158, 158), (255, 255, 30), (255, 255, 30), (255, 255, 30), (255, 255, 30), (0, 158, 158), (0, 158, 158)],
          [(0, 158, 158), (255, 255, 30), (0, 158, 158), (0, 158, 158), (255, 255, 30), (0, 158, 158), (255, 255, 30), (0, 158, 158)],
          [(255, 255, 30), (0, 158, 158), (0, 158, 158), (0, 158, 158), (255, 255, 30), (0, 158, 158), (0, 158, 158), (255, 255, 30)]]

unicorn.brightness(0.4)
def time_checker():
    """
    Checks the current time
    """
    global current_time
    current_time = time.localtime()
    global disp_time
    disp_time = time.strftime("%H%M", current_time)
    #disp_time = "0000"
    global check_time
    check_time = int(disp_time)

def day_or_night():
    """
    Changes the LED display to the appropriate picture
    depending on ime of day
    """
    if 0000 <= check_time < 800 or 2000 <= check_time <= 2359:
        unicorn.clear()
        unicorn.set_pixels(moon)
        unicorn.show()
    elif 800 <= check_time < 2000:
        unicorn.clear()
        unicorn.set_pixels(sun)
        unicorn.show()
    else:
        unicorn.clear()
        unicorn.set_all(255, 255, 255)
        unicorn.show()

while True:
    time_checker()
    day_or_night()
