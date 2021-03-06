# -*- coding: utf-8 -*-
# Copyright (c) 2014, Vispy Development Team.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
"""
This is a very minimal example that opens a window and makes the background
color to change from black to white to black ...

The backend (one of 'qt', 'glut', 'pyglet') is chosen automatically depending
on what is available on your machine.
"""

import math
from vispy import app, gloo


class Canvas(app.Canvas):

    def __init__(self, *args, **kwargs):
        app.Canvas.__init__(self, *args, **kwargs)
        self._timer = app.Timer('auto', connect=self.on_timer, start=True)
        self.tick = 0

    def on_draw(self, event):
        gloo.clear(color=True)

    def on_timer(self, event):
        self.tick += 1 / 60.0
        c = abs(math.sin(self.tick))
        gloo.set_clear_color((c, c, c, 1))
        self.update()

    def show_fps(self, fps):
        print("FPS - %.2f" % fps)

if __name__ == '__main__':
    canvas = Canvas(keys='interactive')
    canvas.show()
    canvas.measure_fps(1, canvas.show_fps)
    app.run()
