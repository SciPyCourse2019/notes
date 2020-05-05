mspacek@Godel:~$ cd SciPyCourse2019/
mspacek@Godel:~/SciPyCourse2019$ cd notes/04_numpy/
mspacek@Godel:~/SciPyCourse2019/notes/04_numpy$ ls
04_numpy.md  04_numpy.pdf
mspacek@Godel:~/SciPyCourse2019/notes/04_numpy$ ipython
Python 3.6.7 (default, Oct 22 2018, 11:32:17)
Type 'copyright', 'credits' or 'license' for more information
IPython 7.4.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: a = [1, 2, 3]

In [2]: b = a

In [3]: b[2] = 100

In [4]: b
Out[4]: [1, 2, 100]

In [5]: a
Out[5]: [1, 2, 100]

In [6]: a = [1, 2, 3]

In [7]: a.copy?
Docstring: L.copy() -> list -- a shallow copy of L
Type:      builtin_function_or_method

In [8]: b = a.copy()

In [9]: b[2] = 100

In [10]: a
Out[10]: [1, 2, 3]

In [11]: b
Out[11]: [1, 2, 100]

In [12]: a
Out[12]: [1, 2, 3]

In [13]: b = a

In [14]: a == b
Out[14]: True

In [15]: a
Out[15]: [1, 2, 3]

In [16]: b
Out[16]: [1, 2, 3]

In [17]: a is b
Out[17]: True

In [18]: a
Out[18]: [1, 2, 3]

In [19]: b = a.copy()

In [20]: a == b
Out[20]: True

In [21]: a
Out[21]: [1, 2, 3]

In [22]: b
Out[22]: [1, 2, 3]

In [23]: a is b
Out[23]: False

In [24]: a is [1, 2, 3]
Out[24]: False

In [25]: b is [1, 2, 3]
Out[25]: False

In [26]: import numpy

In [27]: import numpy as np

In [28]: np
Out[28]: <module 'numpy' from '/usr/local/lib/python3.6/dist-packages/numpy/__init__.py'>

In [29]: a = [1, 4.5, 'hello']

In [30]: a
Out[30]: [1, 4.5, 'hello']

In [31]: np.array()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-31-e4f3b47dc252> in <module>
----> 1 np.array()

TypeError: Required argument 'object' (pos 1) not found
> <ipython-input-31-e4f3b47dc252>(1)<module>()
----> 1 np.array()

ipdb> c

In [32]: np.array((1, 2, 3))
Out[32]: array([1, 2, 3])

In [33]: a = np.array((1, 2, 3))

In [34]: a
Out[34]: array([1, 2, 3])

In [35]: type(a)
Out[35]: numpy.ndarray

In [36]: a = np.array([1, 2, 3])

In [37]: a
Out[37]: array([1, 2, 3])

In [38]: np.arange(10)
Out[38]: array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

In [39]: a = np.zeros(10)

In [40]: a
Out[40]: array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])

In [41]: np.ones(10)
Out[41]: array([1., 1., 1., 1., 1., 1., 1., 1., 1., 1.])

In [42]: np.random.random?

In [43]: np.random.random(10)
Out[43]:
array([0.30402324, 0.07645092, 0.70885598, 0.24281769, 0.24928786,
       0.1508303 , 0.44914775, 0.50985497, 0.66844809, 0.50374305])

In [44]: np.random
Out[44]: <module 'numpy.random' from '/usr/local/lib/python3.6/dist-packages/numpy/random/__init__.py'>

In [45]: np.tile(5, 10)
Out[45]: array([5, 5, 5, 5, 5, 5, 5, 5, 5, 5])

In [46]: np.tile([1, 2], 5)
Out[46]: array([1, 2, 1, 2, 1, 2, 1, 2, 1, 2])

In [47]: a
Out[47]: array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])

In [48]: a.fill?
Docstring:
a.fill(value)

Fill the array with a scalar value.

Parameters
----------
value : scalar
    All elements of `a` will be assigned this value.

Examples
--------
>>> a = np.array([1, 2])
>>> a.fill(0)
>>> a
array([0, 0])
>>> a = np.empty(2)
>>> a.fill(1)
>>> a
array([ 1.,  1.])
Type:      builtin_function_or_method

In [49]: a.fill(7)

In [50]: a
Out[50]: array([7., 7., 7., 7., 7., 7., 7., 7., 7., 7.])

In [51]: a.copy?

In [52]: a = np.random.random(10)

In [53]: a
Out[53]:
array([0.93871284, 0.20650335, 0.3855861 , 0.2363526 , 0.19277571,
       0.13175563, 0.44326138, 0.00182994, 0.93987689, 0.77067437])

In [54]: b = a.copy()

In [55]: b
Out[55]:
array([0.93871284, 0.20650335, 0.3855861 , 0.2363526 , 0.19277571,
       0.13175563, 0.44326138, 0.00182994, 0.93987689, 0.77067437])

In [56]: c = np.copy(b)

In [57]: a
Out[57]:
array([0.93871284, 0.20650335, 0.3855861 , 0.2363526 , 0.19277571,
       0.13175563, 0.44326138, 0.00182994, 0.93987689, 0.77067437])

In [58]: b
Out[58]:
array([0.93871284, 0.20650335, 0.3855861 , 0.2363526 , 0.19277571,
       0.13175563, 0.44326138, 0.00182994, 0.93987689, 0.77067437])

In [59]: c
Out[59]:
array([0.93871284, 0.20650335, 0.3855861 , 0.2363526 , 0.19277571,
       0.13175563, 0.44326138, 0.00182994, 0.93987689, 0.77067437])

In [60]: a == b
Out[60]:
array([ True,  True,  True,  True,  True,  True,  True,  True,  True,
        True])

In [61]: b == c
Out[61]:
array([ True,  True,  True,  True,  True,  True,  True,  True,  True,
        True])

In [62]: a == c
Out[62]:
array([ True,  True,  True,  True,  True,  True,  True,  True,  True,
        True])

In [63]: a is b
Out[63]: False

In [64]: b is c
Out[64]: False

In [65]: d = a

In [66]: d
Out[66]:
array([0.93871284, 0.20650335, 0.3855861 , 0.2363526 , 0.19277571,
       0.13175563, 0.44326138, 0.00182994, 0.93987689, 0.77067437])

In [67]: a
Out[67]:
array([0.93871284, 0.20650335, 0.3855861 , 0.2363526 , 0.19277571,
       0.13175563, 0.44326138, 0.00182994, 0.93987689, 0.77067437])

In [68]: d == a
Out[68]:
array([ True,  True,  True,  True,  True,  True,  True,  True,  True,
        True])

In [69]: d.sort()

In [70]: d
Out[70]:
array([0.00182994, 0.13175563, 0.19277571, 0.20650335, 0.2363526 ,
       0.3855861 , 0.44326138, 0.77067437, 0.93871284, 0.93987689])

In [71]: a
Out[71]:
array([0.00182994, 0.13175563, 0.19277571, 0.20650335, 0.2363526 ,
       0.3855861 , 0.44326138, 0.77067437, 0.93871284, 0.93987689])

In [72]: d is a
Out[72]: True

In [73]: b
Out[73]:
array([0.93871284, 0.20650335, 0.3855861 , 0.2363526 , 0.19277571,
       0.13175563, 0.44326138, 0.00182994, 0.93987689, 0.77067437])

In [74]: e = np.sort(b)

In [75]: e
Out[75]:
array([0.00182994, 0.13175563, 0.19277571, 0.20650335, 0.2363526 ,
       0.3855861 , 0.44326138, 0.77067437, 0.93871284, 0.93987689])

In [76]: d == e
Out[76]:
array([ True,  True,  True,  True,  True,  True,  True,  True,  True,
        True])

In [77]: d is e
Out[77]: False

In [78]: a
Out[78]:
array([0.00182994, 0.13175563, 0.19277571, 0.20650335, 0.2363526 ,
       0.3855861 , 0.44326138, 0.77067437, 0.93871284, 0.93987689])

In [79]: len(a)
Out[79]: 10

In [80]: a.shape
Out[80]: (10,)

In [81]: a.ndim
Out[81]: 1

In [82]: a
Out[82]:
array([0.00182994, 0.13175563, 0.19277571, 0.20650335, 0.2363526 ,
       0.3855861 , 0.44326138, 0.77067437, 0.93871284, 0.93987689])

In [83]: a[0]
Out[83]: 0.0018299350136299353

In [84]: a[1]
Out[84]: 0.13175563140174618

In [85]: a[2]
Out[85]: 0.19277570504591124

In [86]: a[0] = 2

In [87]: a
Out[87]:
array([2.        , 0.13175563, 0.19277571, 0.20650335, 0.2363526 ,
       0.3855861 , 0.44326138, 0.77067437, 0.93871284, 0.93987689])

In [88]: a[-1] = 100

In [89]: a
Out[89]:
array([  2.        ,   0.13175563,   0.19277571,   0.20650335,
         0.2363526 ,   0.3855861 ,   0.44326138,   0.77067437,
         0.93871284, 100.        ])

In [90]: a[-2] = 50

In [91]: a
Out[91]:
array([  2.        ,   0.13175563,   0.19277571,   0.20650335,
         0.2363526 ,   0.3855861 ,   0.44326138,   0.77067437,
        50.        , 100.        ])

In [92]: a
Out[92]:
array([  2.        ,   0.13175563,   0.19277571,   0.20650335,
         0.2363526 ,   0.3855861 ,   0.44326138,   0.77067437,
        50.        , 100.        ])

In [93]: a[0:5]
Out[93]: array([2.        , 0.13175563, 0.19277571, 0.20650335, 0.2363526 ])

In [94]: a[:5]
Out[94]: array([2.        , 0.13175563, 0.19277571, 0.20650335, 0.2363526 ])

In [95]: a[:5] = 99

In [96]: a
Out[96]:
array([ 99.        ,  99.        ,  99.        ,  99.        ,
        99.        ,   0.3855861 ,   0.44326138,   0.77067437,
        50.        , 100.        ])

In [97]: l = list(range(10))

In [98]: l
Out[98]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

In [99]: l[:5]
Out[99]: [0, 1, 2, 3, 4]

In [100]: l[:5] = 99
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-100-90a4aa1d11e2> in <module>
----> 1 l[:5] = 99

TypeError: can only assign an iterable
> <ipython-input-100-90a4aa1d11e2>(1)<module>()
----> 1 l[:5] = 99

ipdb> c

In [101]: a
Out[101]:
array([ 99.        ,  99.        ,  99.        ,  99.        ,
        99.        ,   0.3855861 ,   0.44326138,   0.77067437,
        50.        , 100.        ])

In [102]: a[] = 100
  File "<ipython-input-102-aee320cd9748>", line 1
    a[] = 100
      ^
SyntaxError: invalid syntax


In [103]: a[:]
Out[103]:
array([ 99.        ,  99.        ,  99.        ,  99.        ,
        99.        ,   0.3855861 ,   0.44326138,   0.77067437,
        50.        , 100.        ])

In [104]: a[:] = 1000

In [105]: a
Out[105]:
array([1000., 1000., 1000., 1000., 1000., 1000., 1000., 1000., 1000.,
       1000.])

In [106]: a
Out[106]:
array([1000., 1000., 1000., 1000., 1000., 1000., 1000., 1000., 1000.,
       1000.])

In [107]: a.fill(99)

In [108]: a
Out[108]: array([99., 99., 99., 99., 99., 99., 99., 99., 99., 99.])

In [109]: a[:] = 99

In [110]: a
Out[110]: array([99., 99., 99., 99., 99., 99., 99., 99., 99., 99.])

In [111]: a
Out[111]: array([99., 99., 99., 99., 99., 99., 99., 99., 99., 99.])

In [112]: a[0] = 'hi'
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-112-c15cb4053a1f> in <module>
----> 1 a[0] = 'hi'

ValueError: could not convert string to float: 'hi'
> <ipython-input-112-c15cb4053a1f>(1)<module>()
----> 1 a[0] = 'hi'

ipdb> c

In [113]: np.tile('no', 10)
Out[113]:
array(['no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no'],
      dtype='<U2')

In [114]: a = np.arange(10)

In [115]: a
Out[115]: array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

In [116]: a[:] = 99

In [117]: a
Out[117]: array([99, 99, 99, 99, 99, 99, 99, 99, 99, 99])

In [118]: a = 99

In [119]: a
Out[119]: 99

In [120]: a[0]
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-120-6a1284577a36> in <module>
----> 1 a[0]

TypeError: 'int' object is not subscriptable
> <ipython-input-120-6a1284577a36>(1)<module>()
----> 1 a[0]

ipdb> c

In [121]: a = np.arange(10)

In [122]: a[0]
Out[122]: 0

In [123]: a[::2]
Out[123]: array([0, 2, 4, 6, 8])

In [124]: a
Out[124]: array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

In [125]: a = np.random.random(10)

In [126]: i = [3, 7, 5, 2, 7]

In [127]: a
Out[127]:
array([0.01360727, 0.25425135, 0.19133794, 0.30111801, 0.39483068,
       0.45541513, 0.7811001 , 0.78550333, 0.52920694, 0.19529773])

In [128]: a[i]
Out[128]: array([0.30111801, 0.78550333, 0.45541513, 0.19133794, 0.78550333])

In [129]: l
Out[129]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

In [130]: l[i]
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-130-021c72463b38> in <module>
----> 1 l[i]

TypeError: list indices must be integers or slices, not list
> <ipython-input-130-021c72463b38>(1)<module>()
----> 1 l[i]

ipdb> c

In [131]: l[0]
Out[131]: 0

In [132]: l[::2]
Out[132]: [0, 2, 4, 6, 8]

In [133]: l[i]
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-133-021c72463b38> in <module>
----> 1 l[i]

TypeError: list indices must be integers or slices, not list
> <ipython-input-133-021c72463b38>(1)<module>()
----> 1 l[i]

ipdb> c

In [134]: a[i]
Out[134]: array([0.30111801, 0.78550333, 0.45541513, 0.19133794, 0.78550333])

In [135]: i
Out[135]: [3, 7, 5, 2, 7]

In [136]: a[i]
Out[136]: array([0.30111801, 0.78550333, 0.45541513, 0.19133794, 0.78550333])

In [137]: a[i] = -1

In [138]: a
Out[138]:
array([ 0.01360727,  0.25425135, -1.        , -1.        ,  0.39483068,
       -1.        ,  0.7811001 , -1.        ,  0.52920694,  0.19529773])

In [139]: a = np.arange(10)

In [140]: a
Out[140]: array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

In [141]: a >= 5
Out[141]:
array([False, False, False, False, False,  True,  True,  True,  True,
        True])

In [142]: i = a >= 5

In [143]: i
Out[143]:
array([False, False, False, False, False,  True,  True,  True,  True,
        True])

In [144]: a[i]
Out[144]: array([5, 6, 7, 8, 9])

In [145]: a[a >= 5]
Out[145]: array([5, 6, 7, 8, 9])

In [146]: d =  a[a >= 5]

In [147]: d
Out[147]: array([5, 6, 7, 8, 9])

In [148]: a
Out[148]: array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

In [149]: a[-1] = 100

In [150]: d
Out[150]: array([5, 6, 7, 8, 9])

In [151]: d = (a[a >= 5]).copy()

In [152]: a
Out[152]: array([  0,   1,   2,   3,   4,   5,   6,   7,   8, 100])

In [153]: a[[True, True, False]]
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-153-3ce88fb84694> in <module>
----> 1 a[[True, True, False]]

IndexError: boolean index did not match indexed array along dimension 0; dimension is 10 but corresponding boolean dimension is 3
> <ipython-input-153-3ce88fb84694>(1)<module>()
----> 1 a[[True, True, False]]

ipdb> c

In [154]: i = [3, 7, 5, 2, 7]

In [155]: i = a >= 5

In [156]: i
Out[156]:
array([False, False, False, False, False,  True,  True,  True,  True,
        True])

In [157]: l
Out[157]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

In [158]: l[i]
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-158-021c72463b38> in <module>
----> 1 l[i]

TypeError: only integer scalar arrays can be converted to a scalar index
> <ipython-input-158-021c72463b38>(1)<module>()
----> 1 l[i]

ipdb> c

In [159]: a[True, True, False]
Out[159]: array([], shape=(0, 10), dtype=int64)

In [160]: a = np.array([1, 2, 3])

In [161]: a + 1
Out[161]: array([2, 3, 4])

In [162]: a + 2
Out[162]: array([3, 4, 5])

In [163]: a
Out[163]: array([1, 2, 3])

In [164]: a += 1

In [165]: a
Out[165]: array([2, 3, 4])

In [166]: a -= 100

In [167]: a
Out[167]: array([-98, -97, -96])

In [168]: a = np.array([1, 2, 3])

In [169]: a + 1
Out[169]: array([2, 3, 4])

In [170]: a
Out[170]: array([1, 2, 3])

In [171]: a += 1

In [172]: a
Out[172]: array([2, 3, 4])

In [173]: a
Out[173]: array([2, 3, 4])

In [174]: a = np.array([1, 2, 3])

In [175]: b = np.array([4, 5, 6])

In [176]: a + b
Out[176]: array([5, 7, 9])

In [177]: b = np.array([4, 5, 6, 7])

In [178]: a + b
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-178-bd58363a63fc> in <module>
----> 1 a + b

ValueError: operands could not be broadcast together with shapes (3,) (4,)
> <ipython-input-178-bd58363a63fc>(1)<module>()
----> 1 a + b

ipdb> c

In [179]: l1 = [1,2,3]

In [180]: l2 = [1,2,3]

In [181]: l1 + l2
Out[181]: [1, 2, 3, 1, 2, 3]

In [182]: np.concatenate?

In [183]: a
Out[183]: array([1, 2, 3])

In [184]: b
Out[184]: array([4, 5, 6, 7])

In [185]: np.concatenate(a, b)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-185-3ea434ce7b02> in <module>
----> 1 np.concatenate(a, b)

TypeError: only integer scalar arrays can be converted to a scalar index
> <ipython-input-185-3ea434ce7b02>(1)<module>()
----> 1 np.concatenate(a, b)

ipdb> c

In [186]: np.concatenate((a, b))
Out[186]: array([1, 2, 3, 4, 5, 6, 7])

In [187]: np.concatenate([a, b])
Out[187]: array([1, 2, 3, 4, 5, 6, 7])

In [188]: a * b
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-188-9bc1a869709f> in <module>
----> 1 a * b

ValueError: operands could not be broadcast together with shapes (3,) (4,)
> <ipython-input-188-9bc1a869709f>(1)<module>()
----> 1 a * b

ipdb> c

In [189]: b = np.array([4, 5, 6])

In [190]: a * b
Out[190]: array([ 4, 10, 18])

In [191]: a
Out[191]: array([1, 2, 3])

In [192]: b
Out[192]: array([4, 5, 6])

In [193]: a - b
Out[193]: array([-3, -3, -3])

In [194]: a ** b
Out[194]: array([  1,  32, 729])

In [195]: a == b
Out[195]: array([False, False, False])

In [196]: a > b
Out[196]: array([False, False, False])

In [197]: a != b
Out[197]: array([ True,  True,  True])

In [198]: l = []

In [199]: for i in range(3):
     ...:     l.append(np.zeros(5))
     ...:

In [200]: l
Out[200]:
[array([0., 0., 0., 0., 0.]),
 array([0., 0., 0., 0., 0.]),
 array([0., 0., 0., 0., 0.])]

In [201]: a = np.array([10, 20, 30, 40, 50])
     ...: b = np.array([5, 12, 18, 31, 45])

In [202]: a
Out[202]: array([10, 20, 30, 40, 50])

In [203]: b
Out[203]: array([ 5, 12, 18, 31, 45])

In [204]: a - b
Out[204]: array([ 5,  8, 12,  9,  5])

In [205]: d = a - b

In [206]: b - a
Out[206]: array([ -5,  -8, -12,  -9,  -5])

In [207]: d = a - b

In [208]: d
Out[208]: array([ 5,  8, 12,  9,  5])

In [209]: d.mean()
Out[209]: 7.8

In [210]: np.mean(d)
Out[210]: 7.8

In [211]: def rms(x):
     ...:     return np.sqrt(np.mean(x**2))
     ...:

In [212]: a
Out[212]: array([10, 20, 30, 40, 50])

In [213]: rms(a)
Out[213]: 33.166247903554

In [214]: def rms(x):
     ...:     return np.sqrt((x**2).mean())
     ...:
     ...:

In [215]: rms(a)
Out[215]: 33.166247903554

In [216]: d
Out[216]: array([ 5,  8, 12,  9,  5])

In [217]: rms(d)
Out[217]: 8.23407554009556

In [218]: rms(a-b)
Out[218]: 8.23407554009556

In [219]: rms(b-a)
Out[219]: 8.23407554009556

In [220]: np.concatenate([a, b])
Out[220]: array([10, 20, 30, 40, 50,  5, 12, 18, 31, 45])

In [221]: c = np.concatenate([a, b])

In [222]: c
Out[222]: array([10, 20, 30, 40, 50,  5, 12, 18, 31, 45])

In [223]: c.sort()

In [224]: c
Out[224]: array([ 5, 10, 12, 18, 20, 30, 31, 40, 45, 50])

In [225]: c = np.sort(c)

In [226]: c
Out[226]: array([ 5, 10, 12, 18, 20, 30, 31, 40, 45, 50])

In [227]: c.mean()
Out[227]: 26.1

In [228]: c
Out[228]: array([ 5, 10, 12, 18, 20, 30, 31, 40, 45, 50])

In [229]: c >= 10
Out[229]:
array([False,  True,  True,  True,  True,  True,  True,  True,  True,
        True])

In [230]: c <= 20
Out[230]:
array([ True,  True,  True,  True,  True, False, False, False, False,
       False])

In [231]: c >= 10 and c <= 20
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-231-839d1030fb50> in <module>
----> 1 c >= 10 and c <= 20

ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()
> <ipython-input-231-839d1030fb50>(1)<module>()
----> 1 c >= 10 and c <= 20

ipdb> c

In [232]: True and False
Out[232]: False

In [233]: c <= 20
Out[233]:
array([ True,  True,  True,  True,  True, False, False, False, False,
       False])

In [234]: c >= 10 & c <= 20
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-234-66c08e13a285> in <module>
----> 1 c >= 10 & c <= 20

ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()
> <ipython-input-234-66c08e13a285>(1)<module>()
----> 1 c >= 10 & c <= 20

ipdb> c

In [235]: (c >= 10) & (c <= 20)
Out[235]:
array([False,  True,  True,  True,  True, False, False, False, False,
       False])

In [236]: (c >= 10) * (c <= 20)
Out[236]:
array([False,  True,  True,  True,  True, False, False, False, False,
       False])

In [237]: i = (c >= 10) * (c <= 20)

In [238]: i
Out[238]:
array([False,  True,  True,  True,  True, False, False, False, False,
       False])

In [239]: c >= range(10, 20)
Out[239]:
array([False, False,  True,  True,  True,  True,  True,  True,  True,
        True])

In [240]: c in range(10, 20)
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-240-cdee32634666> in <module>
----> 1 c in range(10, 20)

ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()
> <ipython-input-240-cdee32634666>(1)<module>()
----> 1 c in range(10, 20)

ipdb> c

In [241]: i = (c >= 10) * (c <= 20)

In [242]: i = (c >= 10) & (c <= 20)

In [243]: i
Out[243]:
array([False,  True,  True,  True,  True, False, False, False, False,
       False])

In [244]: c
Out[244]: array([ 5, 10, 12, 18, 20, 30, 31, 40, 45, 50])

In [245]: c[i]
Out[245]: array([10, 12, 18, 20])

In [246]: c[(c >= 10) & (c <= 20)]
Out[246]: array([10, 12, 18, 20])

In [247]: c
Out[247]: array([ 5, 10, 12, 18, 20, 30, 31, 40, 45, 50])

In [248]: c[0, 2, 3]
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-248-4d15e2f4077c> in <module>
----> 1 c[0, 2, 3]

IndexError: too many indices for array
> <ipython-input-248-4d15e2f4077c>(1)<module>()
----> 1 c[0, 2, 3]

ipdb> c

In [249]: c[[0, 2, 3]]
Out[249]: array([ 5, 12, 18])

In [250]: c
Out[250]: array([ 5, 10, 12, 18, 20, 30, 31, 40, 45, 50])

In [251]: c[(0, 2, 3)]
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-251-566b04770a18> in <module>
----> 1 c[(0, 2, 3)]

IndexError: too many indices for array
> <ipython-input-251-566b04770a18>(1)<module>()
----> 1 c[(0, 2, 3)]

ipdb> c

In [252]: c[[0, 2, 3]]
Out[252]: array([ 5, 12, 18])

In [253]: c[[0, 2, 3]]
Out[253]: array([ 5, 12, 18])

In [254]: c[[0, 2, 3]]
Out[254]: array([ 5, 12, 18])

In [255]: c[[0, 2, 3]] = 0

In [256]: c
Out[256]: array([ 0, 10,  0,  0, 20, 30, 31, 40, 45, 50])

In [257]: a
Out[257]: array([10, 20, 30, 40, 50])

In [258]: a[True, False, False, False, True]
Out[258]: array([], shape=(0, 5), dtype=int64)

In [259]: a[[True, False, False, False, True]]
Out[259]: array([10, 50])

In [260]: a[[True, False, False, False, True]] = -1

In [261]: a
Out[261]: array([-1, 20, 30, 40, -1])

In [262]: a = np.array([10, 20, 30, 40, 50])
     ...: b = np.array([5, 12, 18, 31, 45])

In [263]:

In [263]: a
Out[263]: array([10, 20, 30, 40, 50])

In [264]: a[[0, -1]]
Out[264]: array([10, 50])

In [265]: a[[0, -1]] = -1

In [266]: a
Out[266]: array([-1, 20, 30, 40, -1])

In [267]:
