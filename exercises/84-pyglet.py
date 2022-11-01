# print helloworld in a screen
#https://github.com/pyglet/pyglet/blob/master/examples/hello_world.py
import pyglet
window=pyglet.window.Window()
label=pyglet.text.Label('Hello World')
@window.event
def on_draw():
    window.clear()
    label.draw()
pyglet.app.run()
