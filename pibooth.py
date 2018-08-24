from picamera import PiCamera
import time
from datetime import datetime
import tkinter as tk
from PIL import Image, ImageTk
import subprocess
import pyglet
import random
import os
import argparse
from gpiozero import Button, LED
from signal import pause

camera = PiCamera()
led = LED(4)
def update_image(dt):
#    img = pyglet.image.load(random.choice(image_paths))
    randimg = randpics()
    img = pyglet.image.load(randimg)
    sprite.image = img
    sprite.scale = get_scale(window, img)
    sprite.x = 0
    sprite.y = 0
    window.clear()

def get_image_paths(input_dir='/home/pi/pibooth/pics/'):
    paths = []
    for root, dirs, files in os.walk(input_dir, topdown=True):
        for file in sorted(files):
            if file.endswith(('jpg', 'png', 'gif')):
                path = os.path.abspath(os.path.join(root, file))
                paths.append(path)
    return paths

def randpics(input_dir='/home/pi/pibooth/pics/'):
    paths = []
    for root, dirs, files in os.walk(input_dir, topdown=True):
        for file in sorted(files):
            if file.endswith(('jpg', 'png', 'gif')):
                path = os.path.abspath(os.path.join(root, file))
                paths.append(path)
    return random.choice(paths)

def get_scale(window, image):
    if image.width > image.height:
        scale = float(window.width) / image.width
    else:
        scale = float(window.height) / image.height
    return scale
 
def take_pic():
    led.off()
    camera.hflip = True
    camera.start_preview(resolution=(1280,720))
    img = Image.open('/home/pi/pibooth/klart.jpg')
    pad = Image.new('RGB', (
        ((img.size[0] + 31) // 32) * 32,
        ((img.size[1] + 15) // 16) * 16,
        ))
    pad.paste(img, (0,0))
    o = camera.add_overlay(pad.tobytes(), size=img.size, alpha=255, layer=3, fullscreen=True)
    time.sleep(3)
    o.close()
    time.sleep(2)
    i = 1
    ilist = []
    ylist = []
    #cdimgs = ['/home/pi/pibooth/03.png', '/home/pi/pibooth/02.png', '/home/pi/pibooth/01.png']
    cdimgs = ['/home/pi/pibooth/05.png','/home/pi/pibooth/04.png','/home/pi/pibooth/03.png', '/home/pi/pibooth/02.png', '/home/pi/pibooth/01.png']
    #cdimgs = ['/home/pi/pibooth/01.png']
    while i < 5:
        for cdi in cdimgs:
            img = Image.open(cdi)
            pad = Image.new('RGB', (
                ((img.size[0] + 31) // 32) * 32,
                ((img.size[1] + 15) // 16) * 16,
                ))
            pad.paste(img, (0,0))
            o = camera.add_overlay(pad.tobytes(), size=img.size, alpha=64, layer=3, fullscreen=False, window=(710,290,500,500))
            time.sleep(1)
            o.close()
        ts = datetime.now().strftime("%y%m%d%H%M%S")
        ilist.append("/home/pi/pibooth/images/%s.jpg" % ts)
        ylist.append("enkeltbilder/%s.jpg" % ts)
        camera.hflip = False
        camera.capture("/home/pi/pibooth/images/%s.jpg" % ts)
        camera.hflip = True
        i += 1
    img = Image.open('/home/pi/pibooth/vent.jpg')
    pad = Image.new('RGB', (
        ((img.size[0] + 31) // 32) * 32,
        ((img.size[1] + 15) // 16) * 16,
        ))
    pad.paste(img, (0,0))
    oi = camera.add_overlay(pad.tobytes(), size=img.size, alpha=255, layer=3, fullscreen=True)
    time.sleep(3)
    ts2 = datetime.now().strftime("%y%m%d%H%M%S")
    name = ("/home/pi/pibooth/pics/%s.jpg" % ts2)
    image_paths.append(name)
    if image_paths[0] == "black.jpg":
        image_paths.pop(0)
    new = subprocess.check_output( ['/home/pi/pibooth/newframe.sh', ilist[0], ilist[1], ilist[2], ilist[3], name])
    there = "%s.jpg" % ts2    
    img = Image.open(ilist[0])
    pad = Image.new('RGB', (
        ((img.size[0] + 31) // 32) * 32,
        ((img.size[1] + 15) // 16) * 16,
        ))
    pad.paste(img, (0,0))
    o = camera.add_overlay(pad.tobytes(), size=img.size, alpha=255, layer=4, fullscreen=True)
    subprocess.run(['/home/pi/Dropbox-Uploader/dropbox_uploader.sh', 'upload', ilist[0], ylist[0]])
    time.sleep(1)
    o.close()
    img = Image.open(ilist[1])
    pad = Image.new('RGB', (
        ((img.size[0] + 31) // 32) * 32,
        ((img.size[1] + 15) // 16) * 16,
        ))
    pad.paste(img, (0,0))
    o = camera.add_overlay(pad.tobytes(), size=img.size, alpha=255, layer=4, fullscreen=True)
    subprocess.run(['/home/pi/Dropbox-Uploader/dropbox_uploader.sh', 'upload', ilist[1], ylist[1]])
    time.sleep(1)
    o.close()
    img = Image.open(ilist[2])
    pad = Image.new('RGB', (
        ((img.size[0] + 31) // 32) * 32,
        ((img.size[1] + 15) // 16) * 16,
        ))
    pad.paste(img, (0,0))
    o = camera.add_overlay(pad.tobytes(), size=img.size, alpha=255, layer=4, fullscreen=True)
    subprocess.run(['/home/pi/Dropbox-Uploader/dropbox_uploader.sh', 'upload', ilist[2], ylist[2]])
    time.sleep(1)
    o.close()
    img = Image.open(ilist[3])
    pad = Image.new('RGB', (
        ((img.size[0] + 31) // 32) * 32,
        ((img.size[1] + 15) // 16) * 16,
        ))
    pad.paste(img, (0,0))
    o = camera.add_overlay(pad.tobytes(), size=img.size, alpha=255, layer=4, fullscreen=True)
    subprocess.run(['/home/pi/Dropbox-Uploader/dropbox_uploader.sh', 'upload', ilist[3], ylist[3]])
    time.sleep(1)
    o.close()
    img = Image.open(name)
    pad = Image.new('RGB', (
        ((img.size[0] + 31) // 32) * 32,
        ((img.size[1] + 15) // 16) * 16,
        ))
    pad.paste(img, (0,0))
    o = camera.add_overlay(pad.tobytes(), size=img.size, alpha=255, layer=4, fullscreen=True)
    subprocess.run(['/home/pi/Dropbox-Uploader/dropbox_uploader.sh', 'upload', name, there])
    oi.close()
    img = Image.open('/home/pi/pibooth/takk.jpg')
    pad = Image.new('RGB', (
        ((img.size[0] + 31) // 32) * 32,
        ((img.size[1] + 15) // 16) * 16,
        ))
    pad.paste(img, (0,0))
    oi = camera.add_overlay(pad.tobytes(), size=img.size, alpha=255, layer=3, fullscreen=True)
    time.sleep(5)
    o.close()
    time.sleep(7)
    oi.close()
    camera.stop_preview()
    print(new)
    led.on()

window = pyglet.window.Window(fullscreen=True)

@window.event
def on_draw():
    sprite.draw()
    fanta.draw()

if __name__ == '__main__':
    button = Button(2)
    led.on()
#    button.when_pressed = boothit
    image_paths = get_image_paths('/home/pi/pibooth/pics/')
    img = pyglet.image.load(random.choice(image_paths))
    button.when_pressed = take_pic
#    showimg = randpics()
#    img = pyglet.image.load(showimg)
    other = pyglet.image.load('/home/pi/pibooth/start150.png')
    fanta = pyglet.sprite.Sprite(other)
    sprite = pyglet.sprite.Sprite(img)
    sprite.scale = get_scale(window, img)

    pyglet.clock.schedule_interval(update_image, 5.0)
    #pyglet.clock.schedule_interval(update_pan, 1/60.0)
    #pyglet.clock.schedule_interval(update_zoom, 1/60.0)
    pyglet.app.run()
