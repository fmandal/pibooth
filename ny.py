import time
from datetime import datetime
from picamera import PiCamera
from gpiozero import Button
from PIL import Image
import subprocess
from signal import pause
import pyglet


camera = PiCamera()
img = pyglet.image.load('vent.jpg')
sprite = pyglet.sprite.Sprite(img)
lol = 'black.jpg'

def takePic():
    camera.start_preview()
    img = Image.open('klar.jpg')
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
    #cdimgs = ['05.png','04.png','03.png', '02.png', '01.png']
    cdimgs = ['01.png']
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
        camera.capture("/home/pi/pibooth/images/%s.jpg" % ts)
        i += 1
    img = Image.open('vent.jpg')
    pad = Image.new('RGB', (
        ((img.size[0] + 31) // 32) * 32,
        ((img.size[1] + 15) // 16) * 16,
        ))
    pad.paste(img, (0,0))
    oi = camera.add_overlay(pad.tobytes(), size=img.size, alpha=255, layer=3, fullscreen=True)
    time.sleep(3)
    ts2 = datetime.now().strftime("%y%m%d%H%M%S")
    name = ("/home/pi/pibooth/pics/%s.jpg" % ts2)
    new = subprocess.check_output( ['/home/pi/pibooth/newframe.sh', ilist[0], ilist[1], ilist[2], ilist[3], name])
    img = Image.open(ilist[0])
    pad = Image.new('RGB', (
        ((img.size[0] + 31) // 32) * 32,
        ((img.size[1] + 15) // 16) * 16,
        ))
    pad.paste(img, (0,0))
    o = camera.add_overlay(pad.tobytes(), size=img.size, alpha=255, layer=4, fullscreen=True)
    time.sleep(3)
    o.close()
    img = Image.open(ilist[1])
    pad = Image.new('RGB', (
        ((img.size[0] + 31) // 32) * 32,
        ((img.size[1] + 15) // 16) * 16,
        ))
    pad.paste(img, (0,0))
    o = camera.add_overlay(pad.tobytes(), size=img.size, alpha=255, layer=4, fullscreen=True)
    time.sleep(3)
    o.close()
    img = Image.open(ilist[2])
    pad = Image.new('RGB', (
        ((img.size[0] + 31) // 32) * 32,
        ((img.size[1] + 15) // 16) * 16,
        ))
    pad.paste(img, (0,0))
    o = camera.add_overlay(pad.tobytes(), size=img.size, alpha=255, layer=4, fullscreen=True)
    time.sleep(3)
    o.close()
    img = Image.open(ilist[3])
    pad = Image.new('RGB', (
        ((img.size[0] + 31) // 32) * 32,
        ((img.size[1] + 15) // 16) * 16,
        ))
    pad.paste(img, (0,0))
    o = camera.add_overlay(pad.tobytes(), size=img.size, alpha=255, layer=4, fullscreen=True)
    time.sleep(3)
    o.close()
    img = Image.open(name)
    pad = Image.new('RGB', (
        ((img.size[0] + 31) // 32) * 32,
        ((img.size[1] + 15) // 16) * 16,
        ))
    pad.paste(img, (0,0))
    o = camera.add_overlay(pad.tobytes(), size=img.size, alpha=255, layer=4, fullscreen=True)
    time.sleep(7)
    o.close()
    img = Image.open('takk.jpg')
    pad = Image.new('RGB', (
        ((img.size[0] + 31) // 32) * 32,
        ((img.size[1] + 15) // 16) * 16,
        ))
    pad.paste(img, (0,0))
    o = camera.add_overlay(pad.tobytes(), size=img.size, alpha=255, layer=4, fullscreen=True)
    time.sleep(7)
    o.close()
    oi.close()
    camera.stop_preview()
    print(new)

def get_scale(window, image):
    if image.width > image.height:
        scale = float(window.width) / image.width
    else:
        scale = float(window.height) / image.height
    return scale

def get_image_paths(input_dir='/home/pi/pibooth/pics/'):
    paths = []
    for root, dirs, files in os.walk(input_dir, topdown=True):
        for file in sorted(files):
            if file.endswith(('jpg', 'png', 'gif')):
                path = os.path.abspath(os.path.join(root, file))
                paths.append(path)
    return paths

def show_image(image = lol):
    print("Changing")
    image_paths = get_image_paths('/home/pi/pibooth/pics/')
    img = pyglet.image.load(random.choice(image_paths))
    sprite.scale = get_scale(window, img)
    sprite.image = img
    sprite.x = 0
    sprite.y = 0
    window.clear()

def black():
    show_image('black.jpg')
    
window = pyglet.window.Window(fullscreen=True)

@window.event
def on_draw():
    sprite.draw()
    print("Changed")

if __name__ == '__main__':
    print("Listo")
    pyglet.clock.schedule_interval(show_image, 5.0)
    button = Button(2)
    button.when_pressed = takePic
    pyglet.app.run()                          
