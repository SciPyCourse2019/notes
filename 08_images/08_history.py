mspacek@Godel:~$ cd SciPyCourse2019/notes/08_images/
mspacek@Godel:~/SciPyCourse2019/notes/08_images$ ipython
Python 3.6.8 (default, Jan 14 2019, 11:02:34)
Type 'copyright', 'credits' or 'license' for more information
IPython 7.4.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: import skimage

In [2]: import scipy.ndimage

In [3]: from skimage import io

In [4]: io.imread?

In [5]: ls
08_images.md   face_alpha.png  face.png   ohki2005.png
08_images.pdf  face_gray.png   movie.avi

In [6]: faceg = io.imread('face_gray.png')

In [7]: faceg
Out[7]:
Array([[255, 255, 255, ..., 255, 255, 255],
       [255, 255, 255, ..., 255, 255, 255],
       [255, 255, 255, ..., 255, 255, 255],
       ...,
       [255, 255, 255, ..., 255, 255, 255],
       [255, 255, 255, ..., 255, 255, 255],
       [255, 255, 255, ..., 255, 255, 255]], dtype=uint8)

In [8]: faceg.shape
Out[8]: (782, 782)

In [9]: np.iinfo(np.uint8)
Out[9]: iinfo(min=0, max=255, dtype=uint8)

In [10]: import matplotlib.pyplot as plt

In [11]: f, ax = plt.subplots()

In [12]: im = ax.imshow(faceg)

In [13]: f.colorbar(im)
Out[13]: <matplotlib.colorbar.Colorbar at 0x7f7cc679a0b8>

In [14]: im.get_cmap()
Out[14]: <matplotlib.colors.ListedColormap at 0x7f7cbda09550>

In [15]: im.get_cmap().name
Out[15]: 'viridis'

In [16]: im.set_cmap('gray')

In [17]: ax.imshow?

In [18]: f, ax = plt.subplots()

In [19]: ax.imshow(faceg, cmap='gray')
Out[19]: <matplotlib.image.AxesImage at 0x7f7cc63f49b0>

In [20]: faceg.shape
Out[20]: (782, 782)

In [21]: faceg[::-1, :]
Out[21]:
Array([[255, 255, 255, ..., 255, 255, 255],
       [255, 255, 255, ..., 255, 255, 255],
       [255, 255, 255, ..., 255, 255, 255],
       ...,
       [255, 255, 255, ..., 255, 255, 255],
       [255, 255, 255, ..., 255, 255, 255],
       [255, 255, 255, ..., 255, 255, 255]], dtype=uint8)

In [22]: ax.imshow(faceg[::-1], cmap='gray')
Out[22]: <matplotlib.image.AxesImage at 0x7f7cc65cd4a8>

In [23]: ax.imshow(faceg, cmap='gray')
Out[23]: <matplotlib.image.AxesImage at 0x7f7cc65cda58>

In [24]: faceg[:10, :10]
Out[24]:
Array([[255, 255, 255, 255, 255, 255, 255, 255, 255, 255],
       [255, 255, 255, 255, 255, 255, 255, 255, 255, 255],
       [255, 255, 255, 255, 255, 255, 255, 255, 255, 255],
       [255, 255, 255, 255, 255, 255, 255, 255, 255, 255],
       [255, 255, 255, 255, 255, 255, 255, 255, 255, 255],
       [255, 255, 255, 255, 255, 255, 255, 255, 255, 255],
       [255, 255, 255, 255, 255, 255, 255, 255, 255, 255],
       [255, 255, 255, 255, 255, 255, 255, 255, 255, 255],
       [255, 255, 255, 255, 255, 255, 255, 255, 255, 255],
       [255, 255, 255, 255, 255, 255, 255, 255, 255, 255]], dtype=uint8)

In [25]: faceg[:10, :10] = 0

In [26]: ax.imshow(faceg, cmap='gray')
Out[26]: <matplotlib.image.AxesImage at 0x7f7cba7528d0>

In [27]: faceg[:100, :100] = 0

In [28]: ax.imshow(faceg, cmap='gray')
Out[28]: <matplotlib.image.AxesImage at 0x7f7cc6669550>

In [29]: ax.imshow(faceg[, ::-1], cmap='gray')
  File "<ipython-input-29-fe85d379de4a>", line 1
    ax.imshow(faceg[, ::-1], cmap='gray')
                    ^
SyntaxError: invalid syntax


In [30]: ax.imshow(faceg[:, ::-1], cmap='gray')
Out[30]: <matplotlib.image.AxesImage at 0x7f7cc6afe7f0>

In [31]: np.rot90?

In [32]: from scipy import ndimage

In [33]: face45 = ndimage.rotate(faceg, 45)

In [34]: face45.shape
Out[34]: (1106, 1106)

In [35]: faceg.shape
Out[35]: (782, 782)

In [36]: ax.imshow(face45, cmap='gray')
Out[36]: <matplotlib.image.AxesImage at 0x7f7cc64b0908>

In [37]: faceg.shape
Out[37]: (782, 782)

In [38]: ax.imshow(faceg, cmap='gray')
Out[38]: <matplotlib.image.AxesImage at 0x7f7cc6806780>

In [39]: faceg[::10, ::10]
Out[39]:
Array([[  0,   0,   0, ..., 255, 255, 255],
       [  0,   0,   0, ..., 255, 255, 255],
       [  0,   0,   0, ..., 255, 255, 255],
       ...,
       [255, 255, 255, ..., 255, 255, 255],
       [255, 255, 255, ..., 255, 255, 255],
       [255, 255, 255, ..., 255, 255, 255]], dtype=uint8)

In [40]: faceg[::10, ::10].shape
Out[40]: (79, 79)

In [41]: lowres = faceg[::10, ::10]

In [42]: ax.imshow(lowres, cmap='gray')
Out[42]: <matplotlib.image.AxesImage at 0x7f7cc65787b8>

In [43]: face45
Out[43]:
array([[0, 0, 0, ..., 0, 0, 0],
       [0, 0, 0, ..., 0, 0, 0],
       [0, 0, 0, ..., 0, 0, 0],
       ...,
       [0, 0, 0, ..., 0, 0, 0],
       [0, 0, 0, ..., 0, 0, 0],
       [0, 0, 0, ..., 0, 0, 0]], dtype=uint8)

In [44]: face45.shape
Out[44]: (1106, 1106)

In [45]: io.imsave('face45.png', face45)

In [46]: ax.imshow(lowres, cmap='gray')
Out[46]: <matplotlib.image.AxesImage at 0x7f7cc6466320>

In [47]: ax.imshow(lowres, cmap='gray', interpolation='gaussian')
Out[47]: <matplotlib.image.AxesImage at 0x7f7cc6514128>

In [48]: ax.imshow(lowres, cmap='gray')
Out[48]: <matplotlib.image.AxesImage at 0x7f7cc64fd1d0>

In [49]: ax.imshow(lowres, cmap='gray', interpol
    ...: ation='gaussian')
Out[49]: <matplotlib.image.AxesImage at 0x7f7cc64fdc88>

In [50]: lowres
Out[50]:
Array([[  0,   0,   0, ..., 255, 255, 255],
       [  0,   0,   0, ..., 255, 255, 255],
       [  0,   0,   0, ..., 255, 255, 255],
       ...,
       [255, 255, 255, ..., 255, 255, 255],
       [255, 255, 255, ..., 255, 255, 255],
       [255, 255, 255, ..., 255, 255, 255]], dtype=uint8)

In [51]: from skimage import filters

In [52]: filters.gaussian(lowres, sigma=2)
Out[52]:
array([[0.00000000e+00, 0.00000000e+00, 6.69162896e-05, ...,
        1.00000000e+00, 1.00000000e+00, 1.00000000e+00],
       [0.00000000e+00, 0.00000000e+00, 6.69162896e-05, ...,
        1.00000000e+00, 1.00000000e+00, 1.00000000e+00],
       [6.69162896e-05, 6.69162896e-05, 1.33828101e-04, ...,
        1.00000000e+00, 1.00000000e+00, 1.00000000e+00],
       ...,
       [9.99999984e-01, 9.99999929e-01, 9.99999722e-01, ...,
        9.99999722e-01, 9.99999929e-01, 9.99999984e-01],
       [9.99999999e-01, 9.99999993e-01, 9.99999965e-01, ...,
        9.99999965e-01, 9.99999993e-01, 9.99999999e-01],
       [1.00000000e+00, 1.00000000e+00, 9.99999997e-01, ...,
        9.99999997e-01, 1.00000000e+00, 1.00000000e+00]])

In [53]: filters.gaussian(lowres, sigma=2).dtype
Out[53]: dtype('float64')

In [54]: filters.gaussian(lowres, sigma=2).max()
Out[54]: 1.0000000000000002

In [55]: filters.gaussian(lowres, sigma=2).min()
Out[55]: 0.0

In [56]: lowresgauss = filters.gaussian(lowres, sigma=2).min()

In [57]: lowresgauss = filters.gaussian(lowres, sigma=2)

In [58]: lowresgauss.shape
Out[58]: (79, 79)

In [59]: lowres.shape
Out[59]: (79, 79)

In [60]: ax.imshow(lowresgauss, cmap='gray')
Out[60]: <matplotlib.image.AxesImage at 0x7f7cc68294e0>

In [61]: ndimage.zoom?

In [62]: lowresgauss.shape
Out[62]: (79, 79)

In [63]: ndimage.zoom(lowresgauss, 10)
Out[63]:
array([[ 4.90261514e-21, -1.12813404e-07, -4.01749000e-07, ...,
         1.00000000e+00,  1.00000000e+00,  1.00000000e+00],
       [-1.12813403e-07, -2.25626820e-07, -5.14562449e-07, ...,
         1.00000000e+00,  1.00000000e+00,  1.00000000e+00],
       [-4.01748998e-07, -5.14562447e-07, -8.03498161e-07, ...,
         1.00000000e+00,  1.00000000e+00,  1.00000000e+00],
       ...,
       [ 1.00000000e+00,  1.00000000e+00,  1.00000000e+00, ...,
         1.00000000e+00,  1.00000000e+00,  1.00000000e+00],
       [ 1.00000000e+00,  1.00000000e+00,  1.00000000e+00, ...,
         1.00000000e+00,  1.00000000e+00,  1.00000000e+00],
       [ 1.00000000e+00,  1.00000000e+00,  1.00000000e+00, ...,
         1.00000000e+00,  1.00000000e+00,  1.00000000e+00]])

In [64]: ndimage.zoom(lowresgauss, 10).shape
Out[64]: (790, 790)

In [65]: f, ax = plt.subplots()

In [66]: biglowresgauss = ndimage.zoom(lowresgauss, 10).shape

In [67]: ax.imshow(biglowresgauss, cmap='gray')
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-67-a14f2d201d44> in <module>
----> 1 ax.imshow(biglowresgauss, cmap='gray')

/usr/local/lib/python3.6/dist-packages/matplotlib/__init__.py in inner(ax, data, *args, **kwargs)
   1808                         "the Matplotlib list!)" % (label_namer, func.__name__),
   1809                         RuntimeWarning, stacklevel=2)
-> 1810             return func(ax, *args, **kwargs)
   1811
   1812         inner.__doc__ = _add_data_doc(inner.__doc__,

/usr/local/lib/python3.6/dist-packages/matplotlib/axes/_axes.py in imshow(self, X, cmap, norm, aspect, interpolation, alpha, vmin, vmax, origin, extent, shape, filternorm, filterrad, imlim, resample, url, **kwargs)
   5492                               resample=resample, **kwargs)
   5493
-> 5494         im.set_data(X)
   5495         im.set_alpha(alpha)
   5496         if im.get_clip_path() is None:

/usr/local/lib/python3.6/dist-packages/matplotlib/image.py in set_data(self, A)
    636         if not (self._A.ndim == 2
    637                 or self._A.ndim == 3 and self._A.shape[-1] in [3, 4]):
--> 638             raise TypeError("Invalid dimensions for image data")
    639
    640         if self._A.ndim == 3:

TypeError: Invalid dimensions for image data
> /usr/local/lib/python3.6/dist-packages/matplotlib/image.py(638)set_data()
    636         if not (self._A.ndim == 2
    637                 or self._A.ndim == 3 and self._A.shape[-1] in [3, 4]):
--> 638             raise TypeError("Invalid dimensions for image data")
    639
    640         if self._A.ndim == 3:

ipdb> c

In [68]: biglowresgauss = ndimage.zoom(lowresgauss, 10)

In [69]: ax.imshow(biglowresgauss, cmap='gray')
Out[69]: <matplotlib.image.AxesImage at 0x7f7ca73d1b70>

In [70]: from skimage import data

In [71]: moon = data.moon()

In [72]: moon.shape
Out[72]: (512, 512)

In [73]: f, ax = plt.subplots()

In [74]: ax.imshow(moon, cmap='gray')
Out[74]: <matplotlib.image.AxesImage at 0x7f7c8f8a5780>

In [75]: f, ax = plt.subplots(1, 2)

In [76]: ax[0].imshow(moon, vmin=0, vmax=255, cmap='gray')
Out[76]: <matplotlib.image.AxesImage at 0x7f7cc5435048>

In [77]: moon.shape
Out[77]: (512, 512)

In [78]: moon.ravel()
Out[78]: array([116, 116, 122, ..., 118, 118, 118], dtype=uint8)

In [79]: moon.ravel().shape
Out[79]: (262144,)

In [80]: 512*512
Out[80]: 262144

In [81]: ax[1].hist(moon.ravel(), bins=np.arange(0, 256+1))
Out[81]:
(array([2.4000e+02, 0.0000e+00, 6.0000e+01, 3.6000e+01, 0.0000e+00,
        6.0000e+01, 5.2000e+01, 0.0000e+00, 5.2000e+01, 0.0000e+00,
        6.0000e+01, 8.0000e+01, 0.0000e+00, 4.0000e+00, 4.4000e+01,
        0.0000e+00, 5.6000e+01, 0.0000e+00, 8.8000e+01, 7.2000e+01,
        0.0000e+00, 8.0000e+01, 7.6000e+01, 0.0000e+00, 5.2000e+01,
        6.8000e+01, 0.0000e+00, 6.4000e+01, 0.0000e+00, 8.8000e+01,
        8.0000e+01, 0.0000e+00, 7.2000e+01, 4.0000e+01, 0.0000e+00,
        7.2000e+01, 3.6000e+01, 0.0000e+00, 4.8000e+01, 6.4000e+01,
        0.0000e+00, 6.4000e+01, 4.8000e+01, 0.0000e+00, 2.8000e+01,
        7.6000e+01, 0.0000e+00, 8.4000e+01, 7.6000e+01, 8.8000e+01,
        0.0000e+00, 8.0000e+01, 1.0800e+02, 0.0000e+00, 5.2000e+01,
        7.6000e+01, 9.2000e+01, 0.0000e+00, 8.8000e+01, 1.0000e+02,
        1.0000e+02, 0.0000e+00, 1.0400e+02, 0.0000e+00, 1.3200e+02,
        1.0800e+02, 0.0000e+00, 1.4800e+02, 1.2400e+02, 1.6800e+02,
        1.6000e+02, 1.6000e+02, 0.0000e+00, 2.1200e+02, 2.0800e+02,
        1.8000e+02, 2.0000e+02, 2.6400e+02, 2.1600e+02, 2.2000e+02,
        3.1200e+02, 2.2400e+02, 2.7200e+02, 2.9600e+02, 2.8400e+02,
        3.1600e+02, 2.5200e+02, 5.3600e+02, 3.6800e+02, 4.0800e+02,
        3.7200e+02, 8.2400e+02, 3.5200e+02, 5.9600e+02, 4.5600e+02,
        8.6000e+02, 9.1600e+02, 4.0000e+02, 8.8000e+02, 9.0800e+02,
        5.8000e+02, 1.8600e+03, 1.4160e+03, 2.5640e+03, 2.0360e+03,
        3.3920e+03, 5.9280e+03, 5.7240e+03, 1.1964e+04, 1.1436e+04,
        1.6256e+04, 1.7772e+04, 2.0324e+04, 2.1444e+04, 1.7484e+04,
        2.3296e+04, 1.6144e+04, 1.2096e+04, 1.1748e+04, 9.4080e+03,
        9.0200e+03, 5.0800e+03, 5.3160e+03, 2.7760e+03, 1.3640e+03,
        2.0560e+03, 8.7200e+02, 1.2600e+03, 8.6800e+02, 3.7600e+02,
        5.5200e+02, 1.7600e+02, 4.3200e+02, 1.9200e+02, 1.5600e+02,
        2.5200e+02, 1.1200e+02, 1.3600e+02, 1.1600e+02, 1.0400e+02,
        8.8000e+01, 1.1600e+02, 1.0000e+02, 8.8000e+01, 6.0000e+01,
        1.0800e+02, 7.6000e+01, 1.1600e+02, 8.8000e+01, 7.6000e+01,
        6.8000e+01, 9.2000e+01, 7.2000e+01, 0.0000e+00, 4.4000e+01,
        6.4000e+01, 5.6000e+01, 0.0000e+00, 1.1200e+02, 7.2000e+01,
        7.6000e+01, 0.0000e+00, 9.6000e+01, 5.2000e+01, 0.0000e+00,
        0.0000e+00, 3.2000e+01, 4.4000e+01, 0.0000e+00, 4.8000e+01,
        0.0000e+00, 7.6000e+01, 2.8000e+01, 0.0000e+00, 3.6000e+01,
        3.6000e+01, 0.0000e+00, 4.4000e+01, 0.0000e+00, 2.8000e+01,
        0.0000e+00, 2.0000e+01, 5.2000e+01, 0.0000e+00, 2.0000e+01,
        0.0000e+00, 3.2000e+01, 0.0000e+00, 1.2000e+01, 0.0000e+00,
        2.0000e+01, 0.0000e+00, 1.2000e+01, 0.0000e+00, 1.2000e+01,
        0.0000e+00, 1.2000e+01, 0.0000e+00, 2.0000e+01, 0.0000e+00,
        4.0000e+00, 0.0000e+00, 2.8000e+01, 0.0000e+00, 8.0000e+00,
        0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 1.6000e+01,
        0.0000e+00, 8.0000e+00, 0.0000e+00, 1.2000e+01, 0.0000e+00,
        0.0000e+00, 1.2000e+01, 0.0000e+00, 2.0000e+01, 0.0000e+00,
        2.8000e+01, 0.0000e+00, 0.0000e+00, 2.0000e+01, 0.0000e+00,
        1.2000e+01, 0.0000e+00, 0.0000e+00, 3.6000e+01, 0.0000e+00,
        4.8000e+01, 0.0000e+00, 0.0000e+00, 2.4000e+01, 0.0000e+00,
        2.4000e+01, 0.0000e+00, 3.6000e+01, 0.0000e+00, 0.0000e+00,
        2.4000e+01, 0.0000e+00, 1.6000e+01, 0.0000e+00, 0.0000e+00,
        1.2000e+01, 0.0000e+00, 1.6000e+01, 0.0000e+00, 0.0000e+00,
        4.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
        4.0000e+00]),
 array([  0,   1,   2,   3,   4,   5,   6,   7,   8,   9,  10,  11,  12,
         13,  14,  15,  16,  17,  18,  19,  20,  21,  22,  23,  24,  25,
         26,  27,  28,  29,  30,  31,  32,  33,  34,  35,  36,  37,  38,
         39,  40,  41,  42,  43,  44,  45,  46,  47,  48,  49,  50,  51,
         52,  53,  54,  55,  56,  57,  58,  59,  60,  61,  62,  63,  64,
         65,  66,  67,  68,  69,  70,  71,  72,  73,  74,  75,  76,  77,
         78,  79,  80,  81,  82,  83,  84,  85,  86,  87,  88,  89,  90,
         91,  92,  93,  94,  95,  96,  97,  98,  99, 100, 101, 102, 103,
        104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116,
        117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129,
        130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142,
        143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155,
        156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168,
        169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181,
        182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194,
        195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207,
        208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220,
        221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233,
        234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246,
        247, 248, 249, 250, 251, 252, 253, 254, 255, 256]),
 <a list of 256 Patch objects>)

In [82]: f, ax = plt.subplots(1, 2)

In [83]: ax.imshow(moon+100, cmap='gray')
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-83-5aaf108cb2ed> in <module>
----> 1 ax.imshow(moon+100, cmap='gray')

AttributeError: 'numpy.ndarray' object has no attribute 'imshow'
> <ipython-input-83-5aaf108cb2ed>(1)<module>()
----> 1 ax.imshow(moon+100, cmap='gray')

ipdb> c

In [84]: f, ax = plt.subplots()

In [85]: ax.imshow(moon+100, cmap='gray')
Out[85]: <matplotlib.image.AxesImage at 0x7f7c72b5de48>

In [86]: from skimage import exposure

In [87]: exposure?
Type:        module
String form: <module 'skimage.exposure' from '/usr/local/lib/python3.6/dist-packages/skimage/exposure/__init__.py'>
File:        /usr/local/lib/python3.6/dist-packages/skimage/exposure/__init__.py
Docstring:   <no docstring>

In [88]: facec = io.image('face.png')
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-88-2d352823e02a> in <module>
----> 1 facec = io.image('face.png')

AttributeError: module 'skimage.io' has no attribute 'image'
> <ipython-input-88-2d352823e02a>(1)<module>()
----> 1 facec = io.image('face.png')

ipdb> c

In [89]: facec = io.imread('face.png')

In [90]: faceg.shape
Out[90]: (782, 782)

In [91]: facec.shape
Out[91]: (782, 782, 3)

In [92]: im = ax.imshow(facec)

In [93]: facec[:, :, 0]
Out[93]:
array([[255, 255, 255, ..., 255, 255, 255],
       [255, 255, 255, ..., 255, 255, 255],
       [255, 255, 255, ..., 255, 255, 255],
       ...,
       [255, 255, 255, ..., 255, 255, 255],
       [255, 255, 255, ..., 255, 255, 255],
       [255, 255, 255, ..., 255, 255, 255]], dtype=uint8)

In [94]: facec[:, :, 0].shape
Out[94]: (782, 782)

In [95]: facec[:, :, 0] = 0

In [96]: im = ax.imshow(facec)

In [97]: plt.close('all')

In [98]: ls
08_images.md   face45.png      face_gray.png  movie.avi
08_images.pdf  face_alpha.png  face.png       ohki2005.png

In [99]: ohki = io.imread('ohki2005.png')

In [100]: ohki.shape
Out[100]: (512, 491)

In [101]: np.rot90?

In [102]: np.rot90?

In [103]: np.rot90(ohki, k=-1)
Out[103]:
array([[1, 1, 1, ..., 1, 1, 1],
       [3, 3, 3, ..., 3, 3, 3],
       [5, 5, 5, ..., 6, 6, 6],
       ...,
       [3, 5, 7, ..., 6, 6, 6],
       [0, 2, 4, ..., 4, 4, 4],
       [0, 1, 2, ..., 2, 2, 2]], dtype=uint8)

In [104]: np.rot90(ohki, k=-1).shape
Out[104]: (491, 512)

In [105]: f, ax = plt.subplots()

In [106]: ax.imshow(np.rot90(ohki, k=-1), cmap='gray')
Out[106]: <matplotlib.image.AxesImage at 0x7f7cc5435908>

In [107]: f, ax = plt.subplots()

In [108]: ax.imshow(ohki, cmap='gray')
Out[108]: <matplotlib.image.AxesImage at 0x7f7ca7be5518>

In [109]: f, ax = plt.subplots()

In [110]: im = ax.imshow(np.rot90(ohki, k=-1), cmap='gray')

In [111]: im.colorbar()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-111-055f8688ea4d> in <module>
----> 1 im.colorbar()

TypeError: 'NoneType' object is not callable
> <ipython-input-111-055f8688ea4d>(1)<module>()
----> 1 im.colorbar()

ipdb> c

In [112]: f.colorbar()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-112-9ab260b4cefa> in <module>
----> 1 f.colorbar()

TypeError: colorbar() missing 1 required positional argument: 'mappable'
> <ipython-input-112-9ab260b4cefa>(1)<module>()
----> 1 f.colorbar()

ipdb> c

In [113]: f.colorbar(im)
Out[113]: <matplotlib.colorbar.Colorbar at 0x7f7ca761c198>

In [114]: im.set_cmap('viridis')

In [115]: im.set_cmap('Spectral')

In [116]: im.set_cmap('coolwarm')

In [117]: im.set_cmap('Dark2')

In [118]: im.set_cmap('Pastel1')

In [119]: f, ax = plt.subplots()

In [120]: ax.hist(ohki, bins=np.arange(0, 256+1))
^C
Program interrupted. (Use 'cont' to resume).
> /usr/local/lib/python3.6/dist-packages/matplotlib/axes/_base.py(2429)autoscale_view()
   2427             x_stickies = sum([sticky.x for sticky in stickies], [])
   2428             y_stickies = sum([sticky.y for sticky in stickies], [])
-> 2429             if self.get_xscale().lower() == 'log':
   2430                 x_stickies = [xs for xs in x_stickies if xs > 0]
   2431             if self.get_yscale().lower() == 'log':

ipdb> c
^C
Program interrupted. (Use 'cont' to resume).
> /usr/local/lib/python3.6/dist-packages/matplotlib/axes/_base.py(2429)autoscale_view()
   2427             x_stickies = sum([sticky.x for sticky in stickies], [])
   2428             y_stickies = sum([sticky.y for sticky in stickies], [])
-> 2429             if self.get_xscale().lower() == 'log':
   2430                 x_stickies = [xs for xs in x_stickies if xs > 0]
   2431             if self.get_yscale().lower() == 'log':

ipdb>
--KeyboardInterrupt--
ipdb>
--KeyboardInterrupt--
ipdb>
--KeyboardInterrupt--
ipdb> c
^C
Program interrupted. (Use 'cont' to resume).
> /usr/local/lib/python3.6/dist-packages/matplotlib/axes/_base.py(2429)autoscale_view()
   2427             x_stickies = sum([sticky.x for sticky in stickies], [])
   2428             y_stickies = sum([sticky.y for sticky in stickies], [])
-> 2429             if self.get_xscale().lower() == 'log':
   2430                 x_stickies = [xs for xs in x_stickies if xs > 0]
   2431             if self.get_yscale().lower() == 'log':

ipdb>
--KeyboardInterrupt--
ipdb> q
---------------------------------------------------------------------------
BdbQuit                                   Traceback (most recent call last)
<ipython-input-120-08771ae7505f> in <module>
----> 1 ax.hist(ohki, bins=np.arange(0, 256+1))

/usr/local/lib/python3.6/dist-packages/matplotlib/__init__.py in inner(ax, data, *args, **kwargs)
   1808                         "the Matplotlib list!)" % (label_namer, func.__name__),
   1809                         RuntimeWarning, stacklevel=2)
-> 1810             return func(ax, *args, **kwargs)
   1811
   1812         inner.__doc__ = _add_data_doc(inner.__doc__,

/usr/local/lib/python3.6/dist-packages/matplotlib/axes/_axes.py in hist(self, x, bins, range, density, weights, cumulative, bottom, histtype, align, orientation, rwidth, log, color, label, stacked, normed, **kwargs)
   6665                 patch = _barfunc(bins[:-1]+boffset, height, width,
   6666                                  align='center', log=log,
-> 6667                                  color=c, **{bottom_kwarg: bottom})
   6668                 patches.append(patch)
   6669                 if stacked:

/usr/local/lib/python3.6/dist-packages/matplotlib/__init__.py in inner(ax, data, *args, **kwargs)
   1808                         "the Matplotlib list!)" % (label_namer, func.__name__),
   1809                         RuntimeWarning, stacklevel=2)
-> 1810             return func(ax, *args, **kwargs)
   1811
   1812         inner.__doc__ = _add_data_doc(inner.__doc__,

/usr/local/lib/python3.6/dist-packages/matplotlib/axes/_axes.py in bar(self, x, height, width, bottom, align, **kwargs)
   2339             ymin = max(ymin * 0.9, 1e-100)
   2340             self.dataLim.intervaly = (ymin, ymax)
-> 2341         self.autoscale_view()
   2342
   2343         bar_container = BarContainer(patches, errorbar, label=label)

/usr/local/lib/python3.6/dist-packages/matplotlib/axes/_base.py in autoscale_view(self, tight, scalex, scaley)
   2427             x_stickies = sum([sticky.x for sticky in stickies], [])
   2428             y_stickies = sum([sticky.y for sticky in stickies], [])
-> 2429             if self.get_xscale().lower() == 'log':
   2430                 x_stickies = [xs for xs in x_stickies if xs > 0]
   2431             if self.get_yscale().lower() == 'log':

/usr/local/lib/python3.6/dist-packages/matplotlib/axes/_base.py in autoscale_view(self, tight, scalex, scaley)
   2427             x_stickies = sum([sticky.x for sticky in stickies], [])
   2428             y_stickies = sum([sticky.y for sticky in stickies], [])
-> 2429             if self.get_xscale().lower() == 'log':
   2430                 x_stickies = [xs for xs in x_stickies if xs > 0]
   2431             if self.get_yscale().lower() == 'log':

/usr/lib/python3.6/bdb.py in trace_dispatch(self, frame, event, arg)
     49             return # None
     50         if event == 'line':
---> 51             return self.dispatch_line(frame)
     52         if event == 'call':
     53             return self.dispatch_call(frame, arg)

/usr/lib/python3.6/bdb.py in dispatch_line(self, frame)
     68         if self.stop_here(frame) or self.break_here(frame):
     69             self.user_line(frame)
---> 70             if self.quitting: raise BdbQuit
     71         return self.trace_dispatch
     72

BdbQuit:
> /usr/lib/python3.6/bdb.py(70)dispatch_line()
     68         if self.stop_here(frame) or self.break_here(frame):
     69             self.user_line(frame)
---> 70             if self.quitting: raise BdbQuit
     71         return self.trace_dispatch
     72

ipdb> c

In [121]:

In [121]:

In [121]:

In [121]:

In [121]:

In [121]:

In [121]: ax.hist(ohki.ravel(), bins=np.arange(0, 256+1))
Out[121]:
(array([1.300e+01, 3.700e+01, 1.400e+02, 1.470e+02, 1.660e+02, 3.420e+02,
        3.080e+02, 6.280e+02, 7.920e+02, 1.606e+03, 1.186e+03, 2.071e+03,
        1.939e+03, 3.274e+03, 2.057e+03, 2.194e+03, 2.859e+03, 2.635e+03,
        2.709e+03, 2.414e+03, 2.316e+03, 1.948e+03, 1.932e+03, 2.083e+03,
        2.121e+03, 2.783e+03, 2.792e+03, 2.860e+03, 2.919e+03, 2.812e+03,
        2.795e+03, 2.848e+03, 2.605e+03, 2.762e+03, 2.479e+03, 2.411e+03,
        2.569e+03, 2.470e+03, 2.367e+03, 2.252e+03, 2.480e+03, 2.522e+03,
        2.428e+03, 2.552e+03, 2.609e+03, 2.567e+03, 2.470e+03, 2.312e+03,
        2.606e+03, 2.439e+03, 2.413e+03, 2.463e+03, 2.252e+03, 2.357e+03,
        2.426e+03, 2.245e+03, 2.385e+03, 2.279e+03, 2.236e+03, 2.322e+03,
        2.174e+03, 2.192e+03, 2.111e+03, 2.191e+03, 2.115e+03, 2.149e+03,
        2.258e+03, 2.128e+03, 2.141e+03, 2.193e+03, 2.161e+03, 2.310e+03,
        2.281e+03, 2.266e+03, 2.233e+03, 2.158e+03, 2.189e+03, 2.139e+03,
        2.136e+03, 2.101e+03, 2.114e+03, 2.066e+03, 2.001e+03, 1.935e+03,
        1.959e+03, 1.864e+03, 1.829e+03, 1.793e+03, 1.768e+03, 1.835e+03,
        1.670e+03, 1.776e+03, 1.716e+03, 1.680e+03, 1.685e+03, 1.629e+03,
        1.649e+03, 1.633e+03, 1.625e+03, 1.513e+03, 1.442e+03, 1.523e+03,
        1.437e+03, 1.426e+03, 1.438e+03, 1.360e+03, 1.254e+03, 1.307e+03,
        1.363e+03, 1.225e+03, 1.219e+03, 1.234e+03, 1.101e+03, 1.071e+03,
        1.120e+03, 1.030e+03, 9.530e+02, 1.015e+03, 9.610e+02, 9.270e+02,
        8.650e+02, 7.930e+02, 7.930e+02, 6.920e+02, 6.930e+02, 6.800e+02,
        5.780e+02, 6.090e+02, 5.490e+02, 5.260e+02, 5.140e+02, 4.960e+02,
        4.810e+02, 4.610e+02, 4.710e+02, 4.220e+02, 4.220e+02, 4.720e+02,
        4.190e+02, 3.630e+02, 3.340e+02, 3.150e+02, 3.050e+02, 3.240e+02,
        2.740e+02, 2.690e+02, 2.560e+02, 2.210e+02, 2.620e+02, 1.960e+02,
        2.000e+02, 1.920e+02, 2.120e+02, 1.710e+02, 2.050e+02, 2.050e+02,
        2.220e+02, 2.100e+02, 1.790e+02, 1.860e+02, 1.670e+02, 1.820e+02,
        1.470e+02, 1.600e+02, 1.260e+02, 1.600e+02, 1.470e+02, 1.260e+02,
        1.410e+02, 1.340e+02, 1.400e+02, 1.240e+02, 1.040e+02, 1.210e+02,
        1.030e+02, 1.080e+02, 9.500e+01, 9.300e+01, 1.140e+02, 8.400e+01,
        9.900e+01, 7.700e+01, 8.500e+01, 7.300e+01, 4.800e+01, 7.900e+01,
        6.800e+01, 5.700e+01, 7.300e+01, 5.500e+01, 7.700e+01, 6.300e+01,
        6.200e+01, 6.600e+01, 5.100e+01, 5.400e+01, 5.100e+01, 4.400e+01,
        4.600e+01, 4.100e+01, 4.300e+01, 5.300e+01, 4.100e+01, 5.900e+01,
        3.800e+01, 4.200e+01, 4.900e+01, 4.100e+01, 4.000e+01, 4.100e+01,
        3.500e+01, 5.000e+01, 4.900e+01, 4.000e+01, 4.600e+01, 4.800e+01,
        5.700e+01, 6.000e+01, 5.200e+01, 7.900e+01, 5.800e+01, 4.800e+01,
        3.600e+01, 6.000e+01, 3.600e+01, 5.000e+01, 4.600e+01, 3.900e+01,
        3.500e+01, 3.000e+01, 3.100e+01, 3.400e+01, 2.700e+01, 3.600e+01,
        2.000e+01, 1.100e+01, 1.100e+01, 5.000e+00, 0.000e+00, 5.000e+00,
        2.000e+00, 5.000e+00, 4.000e+00, 8.000e+00, 6.000e+00, 3.000e+00,
        7.000e+00, 4.000e+00, 1.000e+01, 1.000e+01, 1.000e+01, 2.200e+01,
        1.700e+01, 1.600e+01, 2.600e+01, 3.000e+00]),
 array([  0,   1,   2,   3,   4,   5,   6,   7,   8,   9,  10,  11,  12,
         13,  14,  15,  16,  17,  18,  19,  20,  21,  22,  23,  24,  25,
         26,  27,  28,  29,  30,  31,  32,  33,  34,  35,  36,  37,  38,
         39,  40,  41,  42,  43,  44,  45,  46,  47,  48,  49,  50,  51,
         52,  53,  54,  55,  56,  57,  58,  59,  60,  61,  62,  63,  64,
         65,  66,  67,  68,  69,  70,  71,  72,  73,  74,  75,  76,  77,
         78,  79,  80,  81,  82,  83,  84,  85,  86,  87,  88,  89,  90,
         91,  92,  93,  94,  95,  96,  97,  98,  99, 100, 101, 102, 103,
        104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116,
        117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129,
        130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142,
        143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155,
        156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168,
        169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181,
        182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194,
        195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207,
        208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220,
        221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233,
        234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246,
        247, 248, 249, 250, 251, 252, 253, 254, 255, 256]),
 <a list of 256 Patch objects>)

In [122]: f, ax = plt.subplots()

In [123]: ax.hist(ohki.ravel(), bins=np.arange(0, 256+1))
Out[123]:
(array([1.300e+01, 3.700e+01, 1.400e+02, 1.470e+02, 1.660e+02, 3.420e+02,
        3.080e+02, 6.280e+02, 7.920e+02, 1.606e+03, 1.186e+03, 2.071e+03,
        1.939e+03, 3.274e+03, 2.057e+03, 2.194e+03, 2.859e+03, 2.635e+03,
        2.709e+03, 2.414e+03, 2.316e+03, 1.948e+03, 1.932e+03, 2.083e+03,
        2.121e+03, 2.783e+03, 2.792e+03, 2.860e+03, 2.919e+03, 2.812e+03,
        2.795e+03, 2.848e+03, 2.605e+03, 2.762e+03, 2.479e+03, 2.411e+03,
        2.569e+03, 2.470e+03, 2.367e+03, 2.252e+03, 2.480e+03, 2.522e+03,
        2.428e+03, 2.552e+03, 2.609e+03, 2.567e+03, 2.470e+03, 2.312e+03,
        2.606e+03, 2.439e+03, 2.413e+03, 2.463e+03, 2.252e+03, 2.357e+03,
        2.426e+03, 2.245e+03, 2.385e+03, 2.279e+03, 2.236e+03, 2.322e+03,
        2.174e+03, 2.192e+03, 2.111e+03, 2.191e+03, 2.115e+03, 2.149e+03,
        2.258e+03, 2.128e+03, 2.141e+03, 2.193e+03, 2.161e+03, 2.310e+03,
        2.281e+03, 2.266e+03, 2.233e+03, 2.158e+03, 2.189e+03, 2.139e+03,
        2.136e+03, 2.101e+03, 2.114e+03, 2.066e+03, 2.001e+03, 1.935e+03,
        1.959e+03, 1.864e+03, 1.829e+03, 1.793e+03, 1.768e+03, 1.835e+03,
        1.670e+03, 1.776e+03, 1.716e+03, 1.680e+03, 1.685e+03, 1.629e+03,
        1.649e+03, 1.633e+03, 1.625e+03, 1.513e+03, 1.442e+03, 1.523e+03,
        1.437e+03, 1.426e+03, 1.438e+03, 1.360e+03, 1.254e+03, 1.307e+03,
        1.363e+03, 1.225e+03, 1.219e+03, 1.234e+03, 1.101e+03, 1.071e+03,
        1.120e+03, 1.030e+03, 9.530e+02, 1.015e+03, 9.610e+02, 9.270e+02,
        8.650e+02, 7.930e+02, 7.930e+02, 6.920e+02, 6.930e+02, 6.800e+02,
        5.780e+02, 6.090e+02, 5.490e+02, 5.260e+02, 5.140e+02, 4.960e+02,
        4.810e+02, 4.610e+02, 4.710e+02, 4.220e+02, 4.220e+02, 4.720e+02,
        4.190e+02, 3.630e+02, 3.340e+02, 3.150e+02, 3.050e+02, 3.240e+02,
        2.740e+02, 2.690e+02, 2.560e+02, 2.210e+02, 2.620e+02, 1.960e+02,
        2.000e+02, 1.920e+02, 2.120e+02, 1.710e+02, 2.050e+02, 2.050e+02,
        2.220e+02, 2.100e+02, 1.790e+02, 1.860e+02, 1.670e+02, 1.820e+02,
        1.470e+02, 1.600e+02, 1.260e+02, 1.600e+02, 1.470e+02, 1.260e+02,
        1.410e+02, 1.340e+02, 1.400e+02, 1.240e+02, 1.040e+02, 1.210e+02,
        1.030e+02, 1.080e+02, 9.500e+01, 9.300e+01, 1.140e+02, 8.400e+01,
        9.900e+01, 7.700e+01, 8.500e+01, 7.300e+01, 4.800e+01, 7.900e+01,
        6.800e+01, 5.700e+01, 7.300e+01, 5.500e+01, 7.700e+01, 6.300e+01,
        6.200e+01, 6.600e+01, 5.100e+01, 5.400e+01, 5.100e+01, 4.400e+01,
        4.600e+01, 4.100e+01, 4.300e+01, 5.300e+01, 4.100e+01, 5.900e+01,
        3.800e+01, 4.200e+01, 4.900e+01, 4.100e+01, 4.000e+01, 4.100e+01,
        3.500e+01, 5.000e+01, 4.900e+01, 4.000e+01, 4.600e+01, 4.800e+01,
        5.700e+01, 6.000e+01, 5.200e+01, 7.900e+01, 5.800e+01, 4.800e+01,
        3.600e+01, 6.000e+01, 3.600e+01, 5.000e+01, 4.600e+01, 3.900e+01,
        3.500e+01, 3.000e+01, 3.100e+01, 3.400e+01, 2.700e+01, 3.600e+01,
        2.000e+01, 1.100e+01, 1.100e+01, 5.000e+00, 0.000e+00, 5.000e+00,
        2.000e+00, 5.000e+00, 4.000e+00, 8.000e+00, 6.000e+00, 3.000e+00,
        7.000e+00, 4.000e+00, 1.000e+01, 1.000e+01, 1.000e+01, 2.200e+01,
        1.700e+01, 1.600e+01, 2.600e+01, 3.000e+00]),
 array([  0,   1,   2,   3,   4,   5,   6,   7,   8,   9,  10,  11,  12,
         13,  14,  15,  16,  17,  18,  19,  20,  21,  22,  23,  24,  25,
         26,  27,  28,  29,  30,  31,  32,  33,  34,  35,  36,  37,  38,
         39,  40,  41,  42,  43,  44,  45,  46,  47,  48,  49,  50,  51,
         52,  53,  54,  55,  56,  57,  58,  59,  60,  61,  62,  63,  64,
         65,  66,  67,  68,  69,  70,  71,  72,  73,  74,  75,  76,  77,
         78,  79,  80,  81,  82,  83,  84,  85,  86,  87,  88,  89,  90,
         91,  92,  93,  94,  95,  96,  97,  98,  99, 100, 101, 102, 103,
        104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116,
        117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129,
        130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142,
        143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155,
        156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168,
        169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181,
        182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194,
        195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207,
        208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220,
        221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233,
        234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246,
        247, 248, 249, 250, 251, 252, 253, 254, 255, 256]),
 <a list of 256 Patch objects>)

In [124]: np.float64(ohki) + 50
Out[124]:
array([[51., 53., 56., ..., 56., 54., 52.],
       [51., 53., 56., ..., 56., 54., 52.],
       [51., 53., 56., ..., 56., 54., 52.],
       ...,
       [51., 53., 55., ..., 57., 54., 52.],
       [51., 53., 55., ..., 55., 52., 51.],
       [51., 53., 55., ..., 53., 50., 50.]])

In [125]: ohki2 = np.float64(ohki) + 50

In [126]: f, ax = plt.subplots(1, 2)

In [127]: ax[0].imshow(ohki2, cmap='gray')
Out[127]: <matplotlib.image.AxesImage at 0x7f7c52292b00>

In [128]: ax[0].imshow(ohki2, cmap='gray', vmin=0, vmax=255)
Out[128]: <matplotlib.image.AxesImage at 0x7f7ca75b7b00>

In [129]: ax[1].hist(ohki2.ravel(), bins=np.arange(0, 256+1))
Out[129]:
(array([   0.,    0.,    0.,    0.,    0.,    0.,    0.,    0.,    0.,
           0.,    0.,    0.,    0.,    0.,    0.,    0.,    0.,    0.,
           0.,    0.,    0.,    0.,    0.,    0.,    0.,    0.,    0.,
           0.,    0.,    0.,    0.,    0.,    0.,    0.,    0.,    0.,
           0.,    0.,    0.,    0.,    0.,    0.,    0.,    0.,    0.,
           0.,    0.,    0.,    0.,    0.,   13.,   37.,  140.,  147.,
         166.,  342.,  308.,  628.,  792., 1606., 1186., 2071., 1939.,
        3274., 2057., 2194., 2859., 2635., 2709., 2414., 2316., 1948.,
        1932., 2083., 2121., 2783., 2792., 2860., 2919., 2812., 2795.,
        2848., 2605., 2762., 2479., 2411., 2569., 2470., 2367., 2252.,
        2480., 2522., 2428., 2552., 2609., 2567., 2470., 2312., 2606.,
        2439., 2413., 2463., 2252., 2357., 2426., 2245., 2385., 2279.,
        2236., 2322., 2174., 2192., 2111., 2191., 2115., 2149., 2258.,
        2128., 2141., 2193., 2161., 2310., 2281., 2266., 2233., 2158.,
        2189., 2139., 2136., 2101., 2114., 2066., 2001., 1935., 1959.,
        1864., 1829., 1793., 1768., 1835., 1670., 1776., 1716., 1680.,
        1685., 1629., 1649., 1633., 1625., 1513., 1442., 1523., 1437.,
        1426., 1438., 1360., 1254., 1307., 1363., 1225., 1219., 1234.,
        1101., 1071., 1120., 1030.,  953., 1015.,  961.,  927.,  865.,
         793.,  793.,  692.,  693.,  680.,  578.,  609.,  549.,  526.,
         514.,  496.,  481.,  461.,  471.,  422.,  422.,  472.,  419.,
         363.,  334.,  315.,  305.,  324.,  274.,  269.,  256.,  221.,
         262.,  196.,  200.,  192.,  212.,  171.,  205.,  205.,  222.,
         210.,  179.,  186.,  167.,  182.,  147.,  160.,  126.,  160.,
         147.,  126.,  141.,  134.,  140.,  124.,  104.,  121.,  103.,
         108.,   95.,   93.,  114.,   84.,   99.,   77.,   85.,   73.,
          48.,   79.,   68.,   57.,   73.,   55.,   77.,   63.,   62.,
          66.,   51.,   54.,   51.,   44.,   46.,   41.,   43.,   53.,
          41.,   59.,   38.,   91.]),
 array([  0,   1,   2,   3,   4,   5,   6,   7,   8,   9,  10,  11,  12,
         13,  14,  15,  16,  17,  18,  19,  20,  21,  22,  23,  24,  25,
         26,  27,  28,  29,  30,  31,  32,  33,  34,  35,  36,  37,  38,
         39,  40,  41,  42,  43,  44,  45,  46,  47,  48,  49,  50,  51,
         52,  53,  54,  55,  56,  57,  58,  59,  60,  61,  62,  63,  64,
         65,  66,  67,  68,  69,  70,  71,  72,  73,  74,  75,  76,  77,
         78,  79,  80,  81,  82,  83,  84,  85,  86,  87,  88,  89,  90,
         91,  92,  93,  94,  95,  96,  97,  98,  99, 100, 101, 102, 103,
        104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116,
        117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129,
        130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142,
        143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155,
        156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168,
        169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181,
        182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194,
        195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207,
        208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220,
        221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233,
        234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246,
        247, 248, 249, 250, 251, 252, 253, 254, 255, 256]),
 <a list of 256 Patch objects>)

In [130]: ohki2 > 255
Out[130]:
array([[False, False, False, ..., False, False, False],
       [False, False, False, ..., False, False, False],
       [False, False, False, ..., False, False, False],
       ...,
       [False, False, False, ..., False, False, False],
       [False, False, False, ..., False, False, False],
       [False, False, False, ..., False, False, False]])

In [131]: (ohki2 > 255).sum()
Out[131]: 1458

In [132]: from skimage import exposure

In [133]: ohki3 = exposure.rescale_intensity(ohki, (16, 75))

In [134]: ohki3.min()
Out[134]: 0

In [135]: ohki3.max()
Out[135]: 255

In [136]: f, ax = plt.subplots(1, 2)

In [137]: ax[0].imshow(ohki3, cmap='gray', vmin=0, vmax=255)
Out[137]: <matplotlib.image.AxesImage at 0x7f7c521a9400>

In [138]: ax[1].hist(ohki3.ravel(), bins=np.arange(0, 256+1))
Out[138]:
(array([19759.,     0.,     0.,     0.,  2635.,     0.,     0.,     0.,
         2709.,     0.,     0.,     0.,  2414.,     0.,     0.,     0.,
            0.,  2316.,     0.,     0.,     0.,  1948.,     0.,     0.,
            0.,  1932.,     0.,     0.,     0.,     0.,  2083.,     0.,
            0.,     0.,  2121.,     0.,     0.,     0.,  2783.,     0.,
            0.,     0.,     0.,  2792.,     0.,     0.,     0.,  2860.,
            0.,     0.,     0.,  2919.,     0.,     0.,     0.,     0.,
         2812.,     0.,     0.,     0.,  2795.,     0.,     0.,     0.,
         2848.,     0.,     0.,     0.,     0.,  2605.,     0.,     0.,
            0.,  2762.,     0.,     0.,     0.,  2479.,     0.,     0.,
            0.,     0.,  2411.,     0.,     0.,     0.,  2569.,     0.,
            0.,     0.,  2470.,     0.,     0.,     0.,     0.,  2367.,
            0.,     0.,     0.,  2252.,     0.,     0.,     0.,  2480.,
            0.,     0.,     0.,     0.,  2522.,     0.,     0.,     0.,
         2428.,     0.,     0.,     0.,  2552.,     0.,     0.,     0.,
            0.,  2609.,     0.,     0.,     0.,  2567.,     0.,     0.,
            0.,  2470.,     0.,     0.,     0.,  2312.,     0.,     0.,
            0.,     0.,  2606.,     0.,     0.,     0.,  2439.,     0.,
            0.,     0.,  2413.,     0.,     0.,     0.,     0.,  2463.,
            0.,     0.,     0.,  2252.,     0.,     0.,     0.,  2357.,
            0.,     0.,     0.,     0.,  2426.,     0.,     0.,     0.,
         2245.,     0.,     0.,     0.,  2385.,     0.,     0.,     0.,
            0.,  2279.,     0.,     0.,     0.,  2236.,     0.,     0.,
            0.,  2322.,     0.,     0.,     0.,     0.,  2174.,     0.,
            0.,     0.,  2192.,     0.,     0.,     0.,  2111.,     0.,
            0.,     0.,     0.,  2191.,     0.,     0.,     0.,  2115.,
            0.,     0.,     0.,  2149.,     0.,     0.,     0.,     0.,
         2258.,     0.,     0.,     0.,  2128.,     0.,     0.,     0.,
         2141.,     0.,     0.,     0.,     0.,  2193.,     0.,     0.,
            0.,  2161.,     0.,     0.,     0.,  2310.,     0.,     0.,
            0.,     0.,  2281.,     0.,     0.,     0.,  2266.,     0.,
            0.,     0.,  2233.,     0.,     0.,     0.,     0., 92485.]),
 array([  0,   1,   2,   3,   4,   5,   6,   7,   8,   9,  10,  11,  12,
         13,  14,  15,  16,  17,  18,  19,  20,  21,  22,  23,  24,  25,
         26,  27,  28,  29,  30,  31,  32,  33,  34,  35,  36,  37,  38,
         39,  40,  41,  42,  43,  44,  45,  46,  47,  48,  49,  50,  51,
         52,  53,  54,  55,  56,  57,  58,  59,  60,  61,  62,  63,  64,
         65,  66,  67,  68,  69,  70,  71,  72,  73,  74,  75,  76,  77,
         78,  79,  80,  81,  82,  83,  84,  85,  86,  87,  88,  89,  90,
         91,  92,  93,  94,  95,  96,  97,  98,  99, 100, 101, 102, 103,
        104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116,
        117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129,
        130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142,
        143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155,
        156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168,
        169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181,
        182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194,
        195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207,
        208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220,
        221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233,
        234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246,
        247, 248, 249, 250, 251, 252, 253, 254, 255, 256]),
 <a list of 256 Patch objects>)

In [139]: ohki.shape
Out[139]: (512, 491)

In [140]: ohki[200:300, 200:300]
Out[140]:
array([[149, 149, 146, ...,  70,  69,  66],
       [155, 154, 151, ...,  70,  69,  66],
       [158, 157, 154, ...,  71,  71,  69],
       ...,
       [123, 127, 129, ..., 125, 121, 117],
       [120, 125, 127, ..., 117, 113, 112],
       [118, 122, 123, ..., 108, 105, 105]], dtype=uint8)

In [141]: ohki[200:300, 200:300].shape
Out[141]: (100, 100)

In [142]: subset = ohki[200:300, 200:300]

In [143]: f, ax = plt.subplots()

In [144]: ax.imshow(subset)
Out[144]: <matplotlib.image.AxesImage at 0x7f7c514661d0>

In [145]: ax.imshow(subset, cmap='gray')
Out[145]: <matplotlib.image.AxesImage at 0x7f7c51466e48>

In [146]: f, ax = plt.subplots()

In [147]: ax.imshow(subset, cmap='gray')
Out[147]: <matplotlib.image.AxesImage at 0x7f7c51184780>

In [148]: f, ax = plt.subplots()

In [149]: ax.hist(subset.ravel(), bins=np.arange(0, 256+1))
Out[149]:
(array([  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,
          0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,
          0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,
          0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,
          0.,   0.,   0.,   0.,   0.,   0.,   0.,   1.,   3.,   2.,   7.,
          5.,   6.,   8.,   9.,   9.,   6.,  10.,  10.,  19.,  22.,  23.,
         17.,  24.,  77.,  72.,  55.,  72.,  61.,  72.,  92.,  88., 127.,
        105., 119.,  80., 103., 116., 115., 125., 136., 180., 188., 161.,
        186., 183., 178., 178., 146., 154., 163., 187., 178., 141., 149.,
        149., 135., 171., 129., 159., 148., 149., 142., 138., 126., 177.,
        137., 191., 146., 146., 166., 147., 145., 138., 129., 119., 121.,
        110., 126.,  96.,  95.,  90.,  83.,  91.,  74.,  74.,  48.,  65.,
         48.,  51.,  41.,  46.,  45.,  46.,  48.,  57.,  39.,  32.,  39.,
         42.,  43.,  30.,  32.,  31.,  27.,  33.,  30.,  23.,  30.,  27.,
         30.,  35.,  24.,  29.,  21.,  24.,  15.,  20.,  13.,  16.,  14.,
         15.,  19.,  20.,   8.,  12.,  17.,  15.,   8.,  21.,  12.,  12.,
         12.,  15.,  25.,  16.,  13.,  12.,   2.,   5.,   1.,   4.,   4.,
          3.,   5.,   4.,   5.,   1.,   5.,   2.,   2.,   2.,   5.,   6.,
          3.,   5.,   4.,   6.,   3.,   2.,   2.,   1.,   1.,   1.,   2.,
          1.,   4.,   4.,   2.,   1.,   5.,   3.,   1.,   3.,   3.,   2.,
          5.,   3.,   4.,   2.,   5.,   3.,   3.,   3.,   2.,   1.,   2.,
          4.,   4.,   7.,   7.,   3.,   6.,   4.,   0.,   3.,   2.,   5.,
          4.,   8.,   6.,   3.,   7.,   4.,  10.,  10.,  10.,  22.,  17.,
         16.,  26.,   3.]),
 array([  0,   1,   2,   3,   4,   5,   6,   7,   8,   9,  10,  11,  12,
         13,  14,  15,  16,  17,  18,  19,  20,  21,  22,  23,  24,  25,
         26,  27,  28,  29,  30,  31,  32,  33,  34,  35,  36,  37,  38,
         39,  40,  41,  42,  43,  44,  45,  46,  47,  48,  49,  50,  51,
         52,  53,  54,  55,  56,  57,  58,  59,  60,  61,  62,  63,  64,
         65,  66,  67,  68,  69,  70,  71,  72,  73,  74,  75,  76,  77,
         78,  79,  80,  81,  82,  83,  84,  85,  86,  87,  88,  89,  90,
         91,  92,  93,  94,  95,  96,  97,  98,  99, 100, 101, 102, 103,
        104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116,
        117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129,
        130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142,
        143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155,
        156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168,
        169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181,
        182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194,
        195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207,
        208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220,
        221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233,
        234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246,
        247, 248, 249, 250, 251, 252, 253, 254, 255, 256]),
 <a list of 256 Patch objects>)

In [150]: ndimage.zoom?

In [151]: ndimage.zoom(subset, 2)
Out[151]:
array([[149, 149, 149, ...,  69,  67,  66],
       [151, 151, 151, ...,  69,  67,  66],
       [155, 155, 154, ...,  69,  67,  66],
       ...,
       [120, 122, 125, ..., 113, 112, 112],
       [119, 120, 123, ..., 108, 107, 107],
       [118, 120, 122, ..., 105, 105, 105]], dtype=uint8)

In [152]: ndimage.zoom(subset, 2).shape
Out[152]: (200, 200)

In [153]: f, ax = plt.subplots()

In [154]: ax.hist(ndimage.zoom(subset, 2), bins=np.arange(0, 256+1))
^C
Program interrupted. (Use 'cont' to resume).
> /usr/local/lib/python3.6/dist-packages/matplotlib/transforms.py(171)set_children()
    169         # parents are destroyed, references from the children won't
    170         # keep them alive.
--> 171         for child in children:
    172             child._parents[id(self)] = weakref.ref(self)
    173

ipdb> c
^C
Program interrupted. (Use 'cont' to resume).
> /usr/local/lib/python3.6/dist-packages/matplotlib/axes/_base.py(2429)autoscale_view()
   2427             x_stickies = sum([sticky.x for sticky in stickies], [])
   2428             y_stickies = sum([sticky.y for sticky in stickies], [])
-> 2429             if self.get_xscale().lower() == 'log':
   2430                 x_stickies = [xs for xs in x_stickies if xs > 0]
   2431             if self.get_yscale().lower() == 'log':

ipdb>
--KeyboardInterrupt--
ipdb>
--KeyboardInterrupt--
ipdb> q
---------------------------------------------------------------------------
BdbQuit                                   Traceback (most recent call last)
<ipython-input-154-cd18a3bd0397> in <module>
----> 1 ax.hist(ndimage.zoom(subset, 2), bins=np.arange(0, 256+1))

/usr/local/lib/python3.6/dist-packages/matplotlib/__init__.py in inner(ax, data, *args, **kwargs)
   1808                         "the Matplotlib list!)" % (label_namer, func.__name__),
   1809                         RuntimeWarning, stacklevel=2)
-> 1810             return func(ax, *args, **kwargs)
   1811
   1812         inner.__doc__ = _add_data_doc(inner.__doc__,

/usr/local/lib/python3.6/dist-packages/matplotlib/axes/_axes.py in hist(self, x, bins, range, density, weights, cumulative, bottom, histtype, align, orientation, rwidth, log, color, label, stacked, normed, **kwargs)
   6665                 patch = _barfunc(bins[:-1]+boffset, height, width,
   6666                                  align='center', log=log,
-> 6667                                  color=c, **{bottom_kwarg: bottom})
   6668                 patches.append(patch)
   6669                 if stacked:

/usr/local/lib/python3.6/dist-packages/matplotlib/__init__.py in inner(ax, data, *args, **kwargs)
   1808                         "the Matplotlib list!)" % (label_namer, func.__name__),
   1809                         RuntimeWarning, stacklevel=2)
-> 1810             return func(ax, *args, **kwargs)
   1811
   1812         inner.__doc__ = _add_data_doc(inner.__doc__,

/usr/local/lib/python3.6/dist-packages/matplotlib/axes/_axes.py in bar(self, x, height, width, bottom, align, **kwargs)
   2339             ymin = max(ymin * 0.9, 1e-100)
   2340             self.dataLim.intervaly = (ymin, ymax)
-> 2341         self.autoscale_view()
   2342
   2343         bar_container = BarContainer(patches, errorbar, label=label)

/usr/local/lib/python3.6/dist-packages/matplotlib/axes/_base.py in autoscale_view(self, tight, scalex, scaley)
   2427             x_stickies = sum([sticky.x for sticky in stickies], [])
   2428             y_stickies = sum([sticky.y for sticky in stickies], [])
-> 2429             if self.get_xscale().lower() == 'log':
   2430                 x_stickies = [xs for xs in x_stickies if xs > 0]
   2431             if self.get_yscale().lower() == 'log':

/usr/local/lib/python3.6/dist-packages/matplotlib/axes/_base.py in autoscale_view(self, tight, scalex, scaley)
   2427             x_stickies = sum([sticky.x for sticky in stickies], [])
   2428             y_stickies = sum([sticky.y for sticky in stickies], [])
-> 2429             if self.get_xscale().lower() == 'log':
   2430                 x_stickies = [xs for xs in x_stickies if xs > 0]
   2431             if self.get_yscale().lower() == 'log':

/usr/lib/python3.6/bdb.py in trace_dispatch(self, frame, event, arg)
     49             return # None
     50         if event == 'line':
---> 51             return self.dispatch_line(frame)
     52         if event == 'call':
     53             return self.dispatch_call(frame, arg)

/usr/lib/python3.6/bdb.py in dispatch_line(self, frame)
     68         if self.stop_here(frame) or self.break_here(frame):
     69             self.user_line(frame)
---> 70             if self.quitting: raise BdbQuit
     71         return self.trace_dispatch
     72

BdbQuit:
> /usr/lib/python3.6/bdb.py(70)dispatch_line()
     68         if self.stop_here(frame) or self.break_here(frame):
     69             self.user_line(frame)
---> 70             if self.quitting: raise BdbQuit
     71         return self.trace_dispatch
     72

ipdb> c

In [155]: f, ax = plt.subplots()

In [156]: ax.hist(ndimage.zoom(subset, 2).ravel(), bins=np.arange(0, 256+1))
Out[156]:
(array([  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,
          0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,
          0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,
          0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,
          0.,   0.,   0.,   0.,   0.,   0.,   0.,   6.,   8.,  13.,  19.,
         26.,  34.,  27.,  31.,  30.,  27.,  39.,  50.,  70.,  99.,  86.,
         67., 129., 244., 275., 242., 277., 258., 261., 361., 388., 460.,
        446., 395., 386., 404., 467., 461., 480., 578., 726., 696., 681.,
        703., 772., 692., 683., 627., 615., 671., 751., 646., 623., 599.,
        578., 618., 563., 586., 630., 568., 584., 577., 569., 594., 578.,
        653., 680., 610., 639., 657., 572., 581., 488., 513., 532., 475.,
        446., 442., 432., 399., 373., 332., 324., 285., 304., 234., 209.,
        206., 195., 196., 207., 163., 181., 188., 209., 170., 161., 152.,
        134., 140., 131., 136., 139., 127., 126., 129., 118., 109., 109.,
        115., 129.,  94.,  95.,  90., 104.,  73.,  75.,  65.,  54.,  63.,
         62.,  60.,  61.,  53.,  58.,  51.,  51.,  59.,  51.,  43.,  61.,
         62.,  81.,  67.,  67.,  52.,  41.,  22.,  25.,  15.,  15.,  15.,
         13.,  18.,  22.,  11.,   9.,  11.,  14.,  17.,   6.,  13.,  12.,
         14.,  14.,   8.,  13.,  13.,  10.,  16.,  10.,   7.,  11.,  10.,
         10.,   9.,   9.,  11.,  15.,  13.,  11.,   9.,  14.,  15.,  10.,
         11.,   9.,  16.,  13.,  11.,  13.,   6.,  13.,  22.,  15.,   8.,
         14.,  15.,  19.,  15.,  17.,   9.,  15.,  19.,  15.,  18.,  16.,
         18.,  22.,  25.,  17.,  22.,  28.,  30.,  29.,  64.,  81.,  65.,
         78.,  90.,  15.]),
 array([  0,   1,   2,   3,   4,   5,   6,   7,   8,   9,  10,  11,  12,
         13,  14,  15,  16,  17,  18,  19,  20,  21,  22,  23,  24,  25,
         26,  27,  28,  29,  30,  31,  32,  33,  34,  35,  36,  37,  38,
         39,  40,  41,  42,  43,  44,  45,  46,  47,  48,  49,  50,  51,
         52,  53,  54,  55,  56,  57,  58,  59,  60,  61,  62,  63,  64,
         65,  66,  67,  68,  69,  70,  71,  72,  73,  74,  75,  76,  77,
         78,  79,  80,  81,  82,  83,  84,  85,  86,  87,  88,  89,  90,
         91,  92,  93,  94,  95,  96,  97,  98,  99, 100, 101, 102, 103,
        104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116,
        117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129,
        130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142,
        143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155,
        156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168,
        169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181,
        182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194,
        195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207,
        208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220,
        221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233,
        234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246,
        247, 248, 249, 250, 251, 252, 253, 254, 255, 256]),
 <a list of 256 Patch objects>)

In [157]: plt.close('all')

In [158]: from skimage import data

In [159]: immun = data.immunohistochemistry()

In [160]: immun.shape
Out[160]: (512, 512, 3)

In [161]: f, ax = plt.subplots()

In [162]: ax.imshow(immun)
Out[162]: <matplotlib.image.AxesImage at 0x7f7c53a69e10>

In [163]: temp = immun.copy()

In [164]: temp[:, :, 0]
Out[164]:
array([[156, 163, 156, ..., 152, 169, 189],
       [141, 144, 141, ..., 164, 167, 175],
       [125, 132, 138, ..., 172, 164, 164],
       ...,
       [221, 226, 234, ..., 212, 214, 217],
       [217, 222, 230, ..., 214, 211, 215],
       [222, 222, 224, ..., 210, 210, 215]], dtype=uint8)

In [165]: temp[:, :, 0] = 0

In [166]: ax.imshow(temp)
Out[166]: <matplotlib.image.AxesImage at 0x7f7c5387c7b8>

In [167]: temp[:, :, 1] = 0

In [168]: ax.imshow(temp)
Out[168]: <matplotlib.image.AxesImage at 0x7f7c33a98fd0>

In [169]: from skimage import color

In [170]: color.rgb2gray?

In [171]: immung = color.rgb2gray(immun)

In [172]: immun.shape
Out[172]: (512, 512, 3)

In [173]: immung.shape
Out[173]: (512, 512)

In [174]: ax.imshow(immun, cmap='gray')
Out[174]: <matplotlib.image.AxesImage at 0x7f7c33a1b710>

In [175]: ax.imshow(immung, cmap='gray')
Out[175]: <matplotlib.image.AxesImage at 0x7f7c0fb417f0>

In [176]:
