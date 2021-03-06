# -*- coding: utf-8 -*-
# Copyright (c) 2014, Vispy Development Team.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.

import numpy as np
import vispy.plot as vplt

plot_data = [1, 6, 2, 4, 3, 8, 4, 6, 5, 2]
canvas1 = vplt.plot(plot_data)

image_data = np.random.normal(size=(20, 20), loc=128, scale=60)
canvas2 = vplt.image(image_data.astype(np.ubyte))


# Start up the event loop if this is not an interactive prompt.
import sys
if sys.flags.interactive == 0:
    canvas1.app.run()
