#!/usr/bin/python

# good starting point for working with dem's in python:
#   https://stevendkay.wordpress.com/2009/09/05/beginning-digital-elevation-model-work-with-python/

# source for 3 arcsec dem:
#   http://dds.cr.usgs.gov/srtm/version2_1/SRTM3/

import sys
sys.path.insert(0, "/usr/local/opencv-2.4.11/lib/python2.7/site-packages/")

sys.path.append('../lib')
import SRTM


from pylab import *
import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import scipy.interpolate

if __name__ == '__main__':
    srtm = SRTM.SRTM('../srtm')
    srtm.parse("N45W094")
    pts = np.array([[-93.14530573529404, 45.220697421008396], [-93.2, 45.3]], dtype=float)
    result = srtm.interpolate(pts)
    print result

 
    # logarithm color scale
    zz=np.log1p(zzz)
    imshow(zz, interpolation='bilinear',cmap=cm.gray,alpha=1.0)
    grid(False)
    show()
    