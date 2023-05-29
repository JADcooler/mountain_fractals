# test pyramid animation works yayyy
from numpy import *
from mayavi import mlab
LEN = 40
x,y = mgrid[0:LEN:1, 0:LEN:1]
z = ones((LEN,LEN))
from time import sleep

mlab.clf()
mlab.surf(x,y,z)
change = mlab.surf(x,y,ones((LEN,LEN)), warp_scale ="auto")

@mlab.animate(delay=10)
def anim():
    for i in range(LEN):
        z[i:-i, i:-i] = i*1.4
        change.mlab_source.scalars = z
        yield
anim()
mlab.show()