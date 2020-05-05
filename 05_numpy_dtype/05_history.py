mspacek@Godel:~$ ipython
Python 3.6.7 (default, Oct 22 2018, 11:32:17)
Type 'copyright', 'credits' or 'license' for more information
IPython 7.4.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: import numpy as np

In [2]: np
Out[2]: <module 'numpy' from '/usr/local/lib/python3.6/dist-packages/numpy/__init__.py'>

In [3]:
mspacek@Godel:~$ ipython
Python 3.6.7 (default, Oct 22 2018, 11:32:17)
Type 'copyright', 'credits' or 'license' for more information
IPython 7.4.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: np
Out[1]: <module 'numpy' from '/usr/local/lib/python3.6/dist-packages/numpy/__init__.py'>

In [2]: import numpy as np

In [3]: np.array((1,2,3))
Out[3]: array([1, 2, 3])

In [4]: np.array([1,2,3])
Out[4]: array([1, 2, 3])

In [5]: np.zeros?

In [6]: np.zeros(10)
Out[6]: array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])

In [7]: np.ones(10)
Out[7]: array([1., 1., 1., 1., 1., 1., 1., 1., 1., 1.])

In [8]: np.random.random(10)
Out[8]:
array([0.20594299, 0.9578807 , 0.14598883, 0.11574224, 0.31917638,
       0.3939976 , 0.75771382, 0.33302564, 0.94504933, 0.83452328])

In [9]: a = [1, 2, 3]

In [10]: b = 4, 5

In [11]: c = np.array([6, 7, 8])

In [12]: np.concatenate(a, b, c)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-12-3996cc17b0d8> in <module>
----> 1 np.concatenate(a, b, c)

TypeError: 'tuple' object cannot be interpreted as an integer
> <ipython-input-12-3996cc17b0d8>(1)<module>()
----> 1 np.concatenate(a, b, c)

ipdb> c

In [13]: np.concatenate([a, b, c])
Out[13]: array([1, 2, 3, 4, 5, 6, 7, 8])

In [14]: c = np.concatenate([a, b, c])

In [15]: c
Out[15]: array([1, 2, 3, 4, 5, 6, 7, 8])

In [16]: c[0]
Out[16]: 1

In [17]: c[1]
Out[17]: 2

In [18]: c[-1]
Out[18]: 8

In [19]: c[10]
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-19-ea0c20b3b68b> in <module>
----> 1 c[10]

IndexError: index 10 is out of bounds for axis 0 with size 8
> <ipython-input-19-ea0c20b3b68b>(1)<module>()
----> 1 c[10]

ipdb> c

In [20]: a = np.arange(10)

In [21]: a
Out[21]: array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

In [22]: a > 5
Out[22]:
array([False, False, False, False, False, False,  True,  True,  True,
        True])

In [23]: len(a)
Out[23]: 10

In [24]: len(a > 5)
Out[24]: 10

In [25]: b = a > 5

In [26]: b
Out[26]:
array([False, False, False, False, False, False,  True,  True,  True,
        True])

In [27]: a[b]
Out[27]: array([6, 7, 8, 9])

In [28]: a[a > 5]
Out[28]: array([6, 7, 8, 9])

In [29]: np.where?

In [30]: np.where(a > 5)
Out[30]: (array([6, 7, 8, 9]),)

In [31]: a = np.arange(0, 20, 2)

In [32]: a
Out[32]: array([ 0,  2,  4,  6,  8, 10, 12, 14, 16, 18])

In [33]: a > 10
Out[33]:
array([False, False, False, False, False, False,  True,  True,  True,
        True])

In [34]: np.where(a > 10)
Out[34]: (array([6, 7, 8, 9]),)

In [35]: type(np.where(a > 10))
Out[35]: tuple

In [36]: np.where(a > 10)
Out[36]: (array([6, 7, 8, 9]),)

In [37]: np.where(a > 10)[0]
Out[37]: array([6, 7, 8, 9])

In [38]: i, = np.where(a > 10)

In [39]: i
Out[39]: array([6, 7, 8, 9])

In [40]: i = np.where(a > 10)[0]

In [41]: np.where(a > 10)
Out[41]: (array([6, 7, 8, 9]),)

In [42]: a
Out[42]: array([ 0,  2,  4,  6,  8, 10, 12, 14, 16, 18])

In [43]: a + 1
Out[43]: array([ 1,  3,  5,  7,  9, 11, 13, 15, 17, 19])

In [44]: a ** 2
Out[44]: array([  0,   4,  16,  36,  64, 100, 144, 196, 256, 324])

In [45]: a == 5
Out[45]:
array([False, False, False, False, False, False, False, False, False,
       False])

In [46]: a > 5
Out[46]:
array([False, False, False,  True,  True,  True,  True,  True,  True,
        True])

In [47]: a != 10
Out[47]:
array([ True,  True,  True,  True,  True, False,  True,  True,  True,
        True])

In [48]: np.where(a != 10)
Out[48]: (array([0, 1, 2, 3, 4, 6, 7, 8, 9]),)

In [49]: np.where(a == 10)
Out[49]: (array([5]),)

In [50]: a = np.array([True, False, False])

In [51]: b = np.array([True, True, False])

In [52]: a and b
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-52-61df3bd186ad> in <module>
----> 1 a and b

ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()
> <ipython-input-52-61df3bd186ad>(1)<module>()
----> 1 a and b

ipdb> c

In [53]: a & b
Out[53]: array([ True, False, False])

In [54]: a or b
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-54-51429399a6cf> in <module>
----> 1 a or b

ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()
> <ipython-input-54-51429399a6cf>(1)<module>()
----> 1 a or b

ipdb> c

In [55]: a | b
Out[55]: array([ True,  True, False])

In [56]: a
Out[56]: array([ True, False, False])

In [57]: b
Out[57]: array([ True,  True, False])

In [58]: a | b
Out[58]: array([ True,  True, False])

In [59]: not a
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-59-666acecd4e9c> in <module>
----> 1 not a

ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()
> <ipython-input-59-666acecd4e9c>(1)<module>()
----> 1 not a

ipdb> c

In [60]: ~a
Out[60]: array([False,  True,  True])

In [61]: a
Out[61]: array([ True, False, False])

In [62]: ~a
Out[62]: array([False,  True,  True])

In [63]: a > 5
Out[63]: array([False, False, False])

In [64]: a = np.arange(0, 20, 2)

In [65]: a ? 5
  File "<ipython-input-65-2ecb85a69cf9>", line 1
    a ? 5
      ^
SyntaxError: invalid syntax


In [66]: a > 5
Out[66]:
array([False, False, False,  True,  True,  True,  True,  True,  True,
        True])

In [67]: min(a) > 5
Out[67]: False

In [68]: a
Out[68]: array([ 0,  2,  4,  6,  8, 10, 12, 14, 16, 18])

In [69]: (a > 5).sum()
Out[69]: 7

In [70]: len(a)
Out[70]: 10

In [71]: (a > 5).all()
Out[71]: False

In [72]: a > 5
Out[72]:
array([False, False, False,  True,  True,  True,  True,  True,  True,
        True])

In [73]: a
Out[73]: array([ 0,  2,  4,  6,  8, 10, 12, 14, 16, 18])

In [74]: bool(0)
Out[74]: False

In [75]: a.all()
Out[75]: False

In [76]: a > 5
Out[76]:
array([False, False, False,  True,  True,  True,  True,  True,  True,
        True])

In [77]: (a > 5).all()
Out[77]: False

In [78]: (a > 5).any()
Out[78]: True

In [79]: a.max()
Out[79]: 18

In [80]: a.min()
Out[80]: 0

In [81]: a.ptp()
Out[81]: 18

In [82]: a.mean()
Out[82]: 9.0

In [83]: a.std()
Out[83]: 5.744562646538029

In [84]: a.max()
Out[84]: 18

In [85]: max(a)
Out[85]: 18

In [86]: np.max(a)
Out[86]: 18

In [87]: a.max()
Out[87]: 18

In [88]: max = 5

In [89]: max
Out[89]: 5

In [90]: del max

In [91]: a.median?
Object `a.median` not found.

In [92]: a
Out[92]: array([ 0,  2,  4,  6,  8, 10, 12, 14, 16, 18])

In [93]: a.median?
Object `a.median` not found.

In [94]: a.median
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-94-41ace0f467a2> in <module>
----> 1 a.median

AttributeError: 'numpy.ndarray' object has no attribute 'median'
> <ipython-input-94-41ace0f467a2>(1)<module>()
----> 1 a.median

ipdb> c

In [95]: np.median(a)
Out[95]: 9.0

In [96]: a.min()
Out[96]: 0

In [97]: a
Out[97]: array([ 0,  2,  4,  6,  8, 10, 12, 14, 16, 18])

In [98]: a.mean()
Out[98]: 9.0

In [99]: a -= a.mean()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-99-0edd4ebf7ae7> in <module>
----> 1 a -= a.mean()

TypeError: Cannot cast ufunc subtract output from dtype('float64') to dtype('int64') with casting rule 'same_kind'
> <ipython-input-99-0edd4ebf7ae7>(1)<module>()
----> 1 a -= a.mean()

ipdb> c

In [100]: a
Out[100]: array([ 0,  2,  4,  6,  8, 10, 12, 14, 16, 18])

In [101]: a = np.random.random(10)

In [102]: a -= a.mean()

In [103]: a
Out[103]:
array([-0.13158842,  0.29614284,  0.28793423,  0.21762147, -0.21275203,
        0.03373593, -0.09198643, -0.26064691, -0.10823034, -0.03023033])

In [104]: a
Out[104]:
array([-0.13158842,  0.29614284,  0.28793423,  0.21762147, -0.21275203,
        0.03373593, -0.09198643, -0.26064691, -0.10823034, -0.03023033])

In [105]: a = np.random.random(10)

In [106]: a
Out[106]:
array([0.16701178, 0.18429945, 0.00771115, 0.18323411, 0.97389786,
       0.56662216, 0.30706787, 0.6666131 , 0.28831019, 0.41521168])

In [107]: a -= a.mean()

In [108]: a
Out[108]:
array([-0.20898615, -0.19169849, -0.36828679, -0.19276383,  0.59789993,
        0.19062423, -0.06893007,  0.29061516, -0.08768775,  0.03921374])

In [109]: a = np.random.random(10)

In [110]: a.mean()
Out[110]: 0.533354886003682

In [111]: a -= a.mean()

In [112]: a
Out[112]:
array([ 0.4389619 , -0.15268495,  0.22039992,  0.1332345 , -0.32040935,
       -0.50279514, -0.15932744, -0.34454725,  0.28026062,  0.40690719])

In [113]: a.mean()
Out[113]: -2.2204460492503132e-17

In [114]: a.std()
Out[114]: 0.3203139751185116

In [115]: a / a.std()
Out[115]:
array([ 1.37041132, -0.47667278,  0.68807464,  0.4159497 , -1.00029776,
       -1.56969467, -0.4974102 , -1.07565477,  0.87495597,  1.27033855])

In [116]: s = a / a.std()

In [117]: s.std()
Out[117]: 1.0

In [118]: s.mean()
Out[118]: -8.881784197001253e-17

In [119]: a
Out[119]:
array([ 0.4389619 , -0.15268495,  0.22039992,  0.1332345 , -0.32040935,
       -0.50279514, -0.15932744, -0.34454725,  0.28026062,  0.40690719])

In [120]: a /= a.std()

In [121]: a
Out[121]:
array([ 1.37041132, -0.47667278,  0.68807464,  0.4159497 , -1.00029776,
       -1.56969467, -0.4974102 , -1.07565477,  0.87495597,  1.27033855])

In [122]: a.std()
Out[122]: 1.0

In [123]: a.mean()
Out[123]: -8.881784197001253e-17

In [124]: a
Out[124]:
array([ 1.37041132, -0.47667278,  0.68807464,  0.4159497 , -1.00029776,
       -1.56969467, -0.4974102 , -1.07565477,  0.87495597,  1.27033855])

In [125]: a.sort()

In [126]: a
Out[126]:
array([-1.56969467, -1.07565477, -1.00029776, -0.4974102 , -0.47667278,
        0.4159497 ,  0.68807464,  0.87495597,  1.27033855,  1.37041132])

In [127]: sorted(a)
Out[127]:
[-1.5696946720689213,
 -1.075654768259188,
 -1.0002977562243807,
 -0.4974101969695672,
 -0.47667277772780436,
 0.41594969952102107,
 0.6880746384897884,
 0.8749559657491214,
 1.2703385478461047,
 1.3704113196438252]

In [128]: sorted?
Signature: sorted(iterable, /, *, key=None, reverse=False)
Docstring:
Return a new list containing all items from the iterable in ascending order.

A custom key function can be supplied to customize the sort order, and the
reverse flag can be set to request the result in descending order.
Type:      builtin_function_or_method

In [129]: np.sort(a)
Out[129]:
array([-1.56969467, -1.07565477, -1.00029776, -0.4974102 , -0.47667278,
        0.4159497 ,  0.68807464,  0.87495597,  1.27033855,  1.37041132])

In [130]: np.diff?

In [131]: len(a)
Out[131]: 10

In [132]: a
Out[132]:
array([-1.56969467, -1.07565477, -1.00029776, -0.4974102 , -0.47667278,
        0.4159497 ,  0.68807464,  0.87495597,  1.27033855,  1.37041132])

In [133]: np.diff(a)
Out[133]:
array([0.4940399 , 0.07535701, 0.50288756, 0.02073742, 0.89262248,
       0.27212494, 0.18688133, 0.39538258, 0.10007277])

In [134]: a = np.random.random(10)

In [135]: a
Out[135]:
array([0.95913371, 0.3064155 , 0.37967405, 0.75634597, 0.5949761 ,
       0.42476809, 0.52669081, 0.7064963 , 0.50799078, 0.80718364])

In [136]: i, = np.where(a > 10)

In [137]: i
Out[137]: array([], dtype=int64)

In [138]: i, = np.where(a > 0.5)

In [139]: i
Out[139]: array([0, 3, 4, 6, 7, 8, 9])

In [140]: np.where(a > 0.5)
Out[140]: (array([0, 3, 4, 6, 7, 8, 9]),)

In [141]: i, = np.where(a > 0.5)

In [142]: i
Out[142]: array([0, 3, 4, 6, 7, 8, 9])

In [143]: a = np.arange(0, 20, 2)

In [144]: a
Out[144]: array([ 0,  2,  4,  6,  8, 10, 12, 14, 16, 18])

In [145]: np.where(a > 10)
Out[145]: (array([6, 7, 8, 9]),)

In [146]: i, = np.where(a > 10)

In [147]: i
Out[147]: array([6, 7, 8, 9])

In [148]: np.random.random(10)
Out[148]:
array([0.41874604, 0.27491106, 0.52268002, 0.35769335, 0.43658817,
       0.91904815, 0.85951962, 0.65268579, 0.1414847 , 0.44488865])

In [149]: np.random.randint?

In [150]: np.random.random(10) * 10
Out[150]:
array([3.54304174, 6.45462388, 9.38136135, 0.10676216, 3.73761243,
       7.66849399, 1.97015469, 2.18019808, 1.02317599, 6.34169447])

In [151]: np.random.random(10) * 10
Out[151]:
array([3.19033001, 0.82489379, 9.61344075, 6.4584908 , 9.40965813,
       7.05564924, 2.00655311, 1.02656435, 4.81893729, 8.4517289 ])

In [152]: np.random.random(10) * 10
Out[152]:
array([1.82428733, 7.5001551 , 7.71411732, 6.77011166, 3.18074506,
       5.80345318, 4.88804435, 8.76365243, 4.63410329, 7.68780049])

In [153]: np.random.random(10) * 10
Out[153]:
array([8.94517736, 1.03003341, 5.04594457, 0.50616484, 3.30110463,
       6.19291054, 7.94374703, 0.7954152 , 2.82856952, 4.81726933])

In [154]: b = np.array(a[1], a[4], a[7])
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-154-9c1dfc7bc4f5> in <module>
----> 1 b = np.array(a[1], a[4], a[7])

ValueError: only 2 non-keyword arguments accepted
> <ipython-input-154-9c1dfc7bc4f5>(1)<module>()
----> 1 b = np.array(a[1], a[4], a[7])

ipdb> c

In [155]: b = np.array((a[1], a[4], a[7]))

In [156]: b
Out[156]: array([ 2,  8, 14])

In [157]: a
Out[157]: array([ 0,  2,  4,  6,  8, 10, 12, 14, 16, 18])

In [158]: a = np.random.random(10)

In [159]: a = a * 10

In [160]: a
Out[160]:
array([3.89887648, 5.22919087, 5.65044039, 4.65281109, 8.66041045,
       5.42453728, 0.43368735, 0.06817267, 9.69989417, 5.22348705])

In [161]: b = np.array((a[1], a[4], a[7]))

In [162]: a[[1, 4, 7]]
Out[162]: array([5.22919087, 8.66041045, 0.06817267])

In [163]: a[[1::3]]
  File "<ipython-input-163-15451a1d82f2>", line 1
    a[[1::3]]
        ^
SyntaxError: invalid syntax


In [164]: c
Out[164]: array([1, 2, 3, 4, 5, 6, 7, 8])

In [165]: a[1::3]
Out[165]: array([5.22919087, 8.66041045, 0.06817267])

In [166]: a[[1::3]]
  File "<ipython-input-166-15451a1d82f2>", line 1
    a[[1::3]]
        ^
SyntaxError: invalid syntax


In [167]:

In [167]: a[[1::3]]
  File "<ipython-input-167-15451a1d82f2>", line 1
    a[[1::3]]
        ^
SyntaxError: invalid syntax


In [168]: a[1::3]
Out[168]: array([5.22919087, 8.66041045, 0.06817267])

In [169]: a[[1, 4, 7]]
Out[169]: array([5.22919087, 8.66041045, 0.06817267])

In [170]: b = a[[1, 4, 7]]

In [171]: a > 5
Out[171]:
array([False,  True,  True, False,  True,  True, False, False,  True,
        True])

In [172]: a[a > 5]
Out[172]:
array([5.22919087, 5.65044039, 8.66041045, 5.42453728, 9.69989417,
       5.22348705])

In [173]: a
Out[173]:
array([3.89887648, 5.22919087, 5.65044039, 4.65281109, 8.66041045,
       5.42453728, 0.43368735, 0.06817267, 9.69989417, 5.22348705])

In [174]: a[a > 5]
Out[174]:
array([5.22919087, 5.65044039, 8.66041045, 5.42453728, 9.69989417,
       5.22348705])

In [175]: c = a[a > 5]

In [176]: np.where(a > 5)
Out[176]: (array([1, 2, 4, 5, 8, 9]),)

In [177]: np.where(a > 5)[0]
Out[177]: array([1, 2, 4, 5, 8, 9])

In [178]: c
Out[178]:
array([5.22919087, 5.65044039, 8.66041045, 5.42453728, 9.69989417,
       5.22348705])

In [179]: (c > 5).all()
Out[179]: True

In [180]: (c > 6).all()
Out[180]: False

In [181]: random.random(10)
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-181-c37ac524301d> in <module>
----> 1 random.random(10)

NameError: name 'random' is not defined
> <ipython-input-181-c37ac524301d>(1)<module>()
----> 1 random.random(10)

ipdb> c

In [182]: np.random.random(10)
Out[182]:
array([0.49301869, 0.53739521, 0.99991735, 0.89428786, 0.74737952,
       0.96386852, 0.80702746, 0.3481741 , 0.39289393, 0.17487088])

In [183]: (np.random.random(10) * 2)
Out[183]:
array([1.0262968 , 0.57413767, 0.74105973, 0.09022471, 0.38719956,
       0.27032129, 1.16596135, 1.08244006, 1.07919641, 0.06040265])

In [184]: (np.random.random(10) * 2)
Out[184]:
array([0.47939946, 0.28364705, 1.38389556, 1.74217115, 1.97058229,
       0.94156682, 0.75788159, 1.12304972, 1.98562195, 0.03726431])

In [185]: d = np.random.random(10)

In [186]: d
Out[186]:
array([0.38138745, 0.88135496, 0.8370648 , 0.04109128, 0.07870835,
       0.76728476, 0.62127719, 0.12513428, 0.67807692, 0.09307877])

In [187]: d * 2
Out[187]:
array([0.7627749 , 1.76270992, 1.67412959, 0.08218255, 0.15741669,
       1.53456952, 1.24255439, 0.25026856, 1.35615383, 0.18615754])

In [188]: (d * 2) - 1
Out[188]:
array([-0.2372251 ,  0.76270992,  0.67412959, -0.91781745, -0.84258331,
        0.53456952,  0.24255439, -0.74973144,  0.35615383, -0.81384246])

In [189]: d * 2 - 1
Out[189]:
array([-0.2372251 ,  0.76270992,  0.67412959, -0.91781745, -0.84258331,
        0.53456952,  0.24255439, -0.74973144,  0.35615383, -0.81384246])

In [190]: (d * 2 - 1).max()
Out[190]: 0.7627099202254113

In [191]: (d * 2 - 1).min()
Out[191]: -0.9178174450635104

In [192]: d = (d * 2 - 1)

In [193]: d
Out[193]:
array([-0.2372251 ,  0.76270992,  0.67412959, -0.91781745, -0.84258331,
        0.53456952,  0.24255439, -0.74973144,  0.35615383, -0.81384246])

In [194]: d.max()
Out[194]: 0.7627099202254113

In [195]: d.min()
Out[195]: -0.9178174450635104

In [196]: d[(d > -0.5) & (d < 0.5)]
Out[196]: array([-0.2372251 ,  0.24255439,  0.35615383])

In [197]: (d > -0.5) & (d < 0.5)
Out[197]:
array([ True, False, False, False, False, False,  True, False,  True,
       False])

In [198]: (d > -0.5)
Out[198]:
array([ True,  True,  True, False, False,  True,  True, False,  True,
       False])

In [199]: (d < 0.5)
Out[199]:
array([ True, False, False,  True,  True, False,  True,  True,  True,
        True])

In [200]: (d > -0.5) & (d < 0.5)
Out[200]:
array([ True, False, False, False, False, False,  True, False,  True,
       False])

In [201]: d[(d > -0.5) & (d < 0.5)]
Out[201]: array([-0.2372251 ,  0.24255439,  0.35615383])

In [202]: d > -0.5 & d < 0.5
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-202-42c1ec702b8b> in <module>
----> 1 d > -0.5 & d < 0.5

TypeError: ufunc 'bitwise_and' not supported for the input types, and the inputs could not be safely coerced to any supported types according to the casting rule ''safe''
> <ipython-input-202-42c1ec702b8b>(1)<module>()
----> 1 d > -0.5 & d < 0.5

ipdb> c

In [203]: d[(d > -0.5) & (d < 0.5)]
Out[203]: array([-0.2372251 ,  0.24255439,  0.35615383])

In [204]: e = d[(d > -0.5) & (d < 0.5)]

In [205]: d
Out[205]:
array([-0.2372251 ,  0.76270992,  0.67412959, -0.91781745, -0.84258331,
        0.53456952,  0.24255439, -0.74973144,  0.35615383, -0.81384246])

In [206]: e
Out[206]: array([-0.2372251 ,  0.24255439,  0.35615383])

In [207]: (e > -0.5) & (e < 0.5)
Out[207]: array([ True,  True,  True])

In [208]: ((e > -0.5) & (e < 0.5)).all()
Out[208]: True

In [209]: np.concatenate([a, d])
Out[209]:
array([ 3.89887648,  5.22919087,  5.65044039,  4.65281109,  8.66041045,
        5.42453728,  0.43368735,  0.06817267,  9.69989417,  5.22348705,
       -0.2372251 ,  0.76270992,  0.67412959, -0.91781745, -0.84258331,
        0.53456952,  0.24255439, -0.74973144,  0.35615383, -0.81384246])

In [210]: a
Out[210]:
array([3.89887648, 5.22919087, 5.65044039, 4.65281109, 8.66041045,
       5.42453728, 0.43368735, 0.06817267, 9.69989417, 5.22348705])

In [211]: d
Out[211]:
array([-0.2372251 ,  0.76270992,  0.67412959, -0.91781745, -0.84258331,
        0.53456952,  0.24255439, -0.74973144,  0.35615383, -0.81384246])

In [212]: np.concatenate([a, d])
Out[212]:
array([ 3.89887648,  5.22919087,  5.65044039,  4.65281109,  8.66041045,
        5.42453728,  0.43368735,  0.06817267,  9.69989417,  5.22348705,
       -0.2372251 ,  0.76270992,  0.67412959, -0.91781745, -0.84258331,
        0.53456952,  0.24255439, -0.74973144,  0.35615383, -0.81384246])

In [213]: len(a)
Out[213]: 10

In [214]: len(d)
Out[214]: 10

In [215]: len(np.concatenate([a, d]))
Out[215]: 20

In [216]: f = np.concatenate([a, d])

In [217]: f
Out[217]:
array([ 3.89887648,  5.22919087,  5.65044039,  4.65281109,  8.66041045,
        5.42453728,  0.43368735,  0.06817267,  9.69989417,  5.22348705,
       -0.2372251 ,  0.76270992,  0.67412959, -0.91781745, -0.84258331,
        0.53456952,  0.24255439, -0.74973144,  0.35615383, -0.81384246])

In [218]: f.sort()

In [219]: f
Out[219]:
array([-0.91781745, -0.84258331, -0.81384246, -0.74973144, -0.2372251 ,
        0.06817267,  0.24255439,  0.35615383,  0.43368735,  0.53456952,
        0.67412959,  0.76270992,  3.89887648,  4.65281109,  5.22348705,
        5.22919087,  5.42453728,  5.65044039,  8.66041045,  9.69989417])

In [220]: np.diff(f)
Out[220]:
array([0.07523414, 0.02874085, 0.06411101, 0.51250634, 0.30539777,
       0.17438172, 0.11359945, 0.07753351, 0.10088217, 0.13956007,
       0.08858033, 3.13616656, 0.75393461, 0.57067596, 0.00570382,
       0.1953464 , 0.22590311, 3.00997006, 1.03948372])

In [221]: (np.diff(f) > 0).all()
Out[221]: True

In [222]: np.diff?

In [223]: f
Out[223]:
array([-0.91781745, -0.84258331, -0.81384246, -0.74973144, -0.2372251 ,
        0.06817267,  0.24255439,  0.35615383,  0.43368735,  0.53456952,
        0.67412959,  0.76270992,  3.89887648,  4.65281109,  5.22348705,
        5.22919087,  5.42453728,  5.65044039,  8.66041045,  9.69989417])

In [224]: np.diff?

In [225]: a.all?
Docstring:
a.all(axis=None, out=None, keepdims=False)

Returns True if all elements evaluate to True.

Refer to `numpy.all` for full documentation.

See Also
--------
numpy.all : equivalent function
Type:      builtin_function_or_method

In [226]: a = []

In [227]: for i in range(10):
     ...:     a.append(i**2)
     ...:

In [228]: a
Out[228]: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

In [229]: a = np.array(a)

In [230]: a * 2
Out[230]: array([  0,   2,   8,  18,  32,  50,  72,  98, 128, 162])

In [231]: a > 5
Out[231]:
array([False, False, False,  True,  True,  True,  True,  True,  True,
        True])

In [232]: a = np.arange(10)

In [233]: a
Out[233]: array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

In [234]: a.nbytes
Out[234]: 80

In [235]: a.dtype
Out[235]: dtype('int64')

In [236]: a.dtype
Out[236]: dtype('int64')

In [237]: a.dtype.itemsize
Out[237]: 8

In [238]: len(a) * a.dtype.itemsize
Out[238]: 80

In [239]: a.nbytes
Out[239]: 80

In [240]: n = 8

In [241]: 2**(n-1)
Out[241]: 128

In [242]: 2**n - 1
Out[242]: 255

In [243]: -2 **(n/2)
Out[243]: -16.0

In [244]: -2 **(n-1)
Out[244]: -128

In [245]: 2 **(n-1) - 1
Out[245]: 127

In [246]: np.int8
Out[246]: numpy.int8

In [247]: np.uint8
Out[247]: numpy.uint8

In [248]: a = np.arange(10, dtype=np.uint8)

In [249]: a
Out[249]: array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=uint8)

In [250]: a = np.arange(10)

In [251]: a.dtype
Out[251]: dtype('int64')

In [252]: a = np.arange(10, dtype=np.uint8)

In [253]: a
Out[253]: array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=uint8)

In [254]: a[0] = 10

In [255]: a[0] = 256

In [256]: a
Out[256]: array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=uint8)

In [257]: a[0] = 255

In [258]: a
Out[258]: array([255,   1,   2,   3,   4,   5,   6,   7,   8,   9], dtype=uint8)

In [259]: a[0] = 254

In [260]: a
Out[260]: array([254,   1,   2,   3,   4,   5,   6,   7,   8,   9], dtype=uint8)

In [261]: a[0] = 256

In [262]: a
Out[262]: array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=uint8)

In [263]: a[0] = -1

In [264]: a
Out[264]: array([255,   1,   2,   3,   4,   5,   6,   7,   8,   9], dtype=uint8)

In [265]: a = np.arange(10, dtype=np.int8)

In [266]: a
Out[266]: array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=int8)

In [267]: a[0] = -1

In [268]: a
Out[268]: array([-1,  1,  2,  3,  4,  5,  6,  7,  8,  9], dtype=int8)

In [269]: a[0] = -300

In [270]: a
Out[270]: array([-44,   1,   2,   3,   4,   5,   6,   7,   8,   9], dtype=int8)

In [271]: a = np.arange(10, dtype=np.int64)

In [272]: a
Out[272]: array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

In [273]: a[0] = 300

In [274]: a
Out[274]: array([300,   1,   2,   3,   4,   5,   6,   7,   8,   9])

In [275]: a[0] = -50000

In [276]: a
Out[276]:
array([-50000,      1,      2,      3,      4,      5,      6,      7,
            8,      9])

In [277]: np.iinfo(np.int8)
Out[277]: iinfo(min=-128, max=127, dtype=int8)

In [278]: 300-128
Out[278]: 172

In [279]: 127 - 172
Out[279]: -45

In [280]: 127 - 172+1
Out[280]: -44

In [281]: a = np.arange(10, dtype=np.int8)

In [282]: a
Out[282]: array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=int8)

In [283]: a[0] = -300

In [284]: a
Out[284]: array([-44,   1,   2,   3,   4,   5,   6,   7,   8,   9], dtype=int8)

In [285]: a = np.arange(10, dtype=np.int8)

In [286]: a += 300

In [287]: a
Out[287]: array([44, 45, 46, 47, 48, 49, 50, 51, 52, 53], dtype=int8)

In [288]: a = np.arange(10, dtype=np.int64)

In [289]: a
Out[289]: array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

In [290]: 2**64
Out[290]: 18446744073709551616

In [291]: a = np.arange(10, dtype=np.int8)

In [292]: a
Out[292]: array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=int8)

In [293]: a + 300
Out[293]: array([300, 301, 302, 303, 304, 305, 306, 307, 308, 309], dtype=int16)

In [294]: np.int8
Out[294]: numpy.int8

In [295]: np.int16
Out[295]: numpy.int16

In [296]: np.int32
Out[296]: numpy.int32

In [297]: np.int64
Out[297]: numpy.int64

In [298]: np.iinfo(np.int16)
Out[298]: iinfo(min=-32768, max=32767, dtype=int16)

In [299]: np.iinfo(np.uint16)
Out[299]: iinfo(min=0, max=65535, dtype=uint16)

In [300]: 2**16
Out[300]: 65536

In [301]: 2**16-1
Out[301]: 65535

In [302]: 16e9
Out[302]: 16000000000.0

In [303]: a = np.zeros(100000000000, dtype=np.int8)
---------------------------------------------------------------------------
MemoryError                               Traceback (most recent call last)
<ipython-input-303-b19ca36b1057> in <module>
----> 1 a = np.zeros(100000000000, dtype=np.int8)

MemoryError:
> <ipython-input-303-b19ca36b1057>(1)<module>()
----> 1 a = np.zeros(100000000000, dtype=np.int8)

ipdb> c

In [304]: a = np.zeros(100000000000, dtype=np.uint8)
---------------------------------------------------------------------------
MemoryError                               Traceback (most recent call last)
<ipython-input-304-4a950e96d874> in <module>
----> 1 a = np.zeros(100000000000, dtype=np.uint8)

MemoryError:
> <ipython-input-304-4a950e96d874>(1)<module>()
----> 1 a = np.zeros(100000000000, dtype=np.uint8)

ipdb> c

In [305]: a = np.zeros(20000000000, dtype=np.int8)

In [306]: a
Out[306]: array([0, 0, 0, ..., 0, 0, 0], dtype=int8)

In [307]: a.nbytes
Out[307]: 20000000000

In [308]: a.nbytes / 1e9
Out[308]: 20.0

In [309]: del a

In [310]: a = np.zeros(5000000000, dtype=np.int8)

In [311]: a[:] = 5

In [312]: del a

In [313]: a
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-313-3f786850e387> in <module>
----> 1 a

NameError: name 'a' is not defined
> <ipython-input-313-3f786850e387>(1)<module>()
----> 1 a

ipdb> c

In [314]: a = np.zeros(50000000000, dtype=np.int8)
---------------------------------------------------------------------------
MemoryError                               Traceback (most recent call last)
<ipython-input-314-0832f6a4803a> in <module>
----> 1 a = np.zeros(50000000000, dtype=np.int8)

MemoryError:
> <ipython-input-314-0832f6a4803a>(1)<module>()
----> 1 a = np.zeros(50000000000, dtype=np.int8)

ipdb> c

In [315]: a = np.zeros(40000000000, dtype=np.int8)

In [316]: 1.23456789e02
Out[316]: 123.456789

In [317]: np.float16
Out[317]: numpy.float16

In [318]: a = np.zeros(5, dtype=np.float16)

In [319]: a
Out[319]: array([0., 0., 0., 0., 0.], dtype=float16)

In [320]: b = np.zeros(10)

In [321]: b
Out[321]: array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])

In [322]: b.dtype
Out[322]: dtype('float64')

In [323]: a
Out[323]: array([0., 0., 0., 0., 0.], dtype=float16)

In [324]: np.finfo(np.float16)
Out[324]: finfo(resolution=0.001, min=-6.55040e+04, max=6.55040e+04, dtype=float16)

In [325]: a
Out[325]: array([0., 0., 0., 0., 0.], dtype=float16)

In [326]: a[0] = 50000

In [327]: a
Out[327]: array([50000.,     0.,     0.,     0.,     0.], dtype=float16)

In [328]: a[0] = -50000

In [329]: a
Out[329]: array([-50000.,      0.,      0.,      0.,      0.], dtype=float16)

In [330]: a[0] = 70000

In [331]: a
Out[331]: array([inf,  0.,  0.,  0.,  0.], dtype=float16)

In [332]: a
Out[332]: array([inf,  0.,  0.,  0.,  0.], dtype=float16)

In [333]: a == np.inf
Out[333]: array([ True, False, False, False, False])

In [334]: a
Out[334]: array([inf,  0.,  0.,  0.,  0.], dtype=float16)

In [335]: a.nbytes
Out[335]: 10

In [336]: np.float16(1.23456789e4)
Out[336]: 12344.0

In [337]: np.float32(1.23456789e4)
Out[337]: 12345.679

In [338]: np.float64(1.23456789e4)
Out[338]: 12345.6789

In [339]: np.array([True, True, False])
Out[339]: array([ True,  True, False])

In [340]: b = np.array([True, True, False])

In [341]: b.dtype
Out[341]: dtype('bool')

In [342]: b.nbytes
Out[342]: 3

In [343]: a = np.array([1, 2, 3])

In [344]: a.dtype
Out[344]: dtype('int64')

In [345]: np.float64(a)
Out[345]: array([1., 2., 3.])

In [346]: np.float64(a).dtype
Out[346]: dtype('float64')

In [347]: a = np.array([1.1, 2.2, 3.3])

In [348]: a.dtype
Out[348]: dtype('float64')

In [349]: a.nbytes
Out[349]: 24

In [350]: a
Out[350]: array([1.1, 2.2, 3.3])

In [351]: np.int64(a)
Out[351]: array([1, 2, 3])

In [352]: np.int64(a).dtype
Out[352]: dtype('int64')

In [353]: np.round(a)
Out[353]: array([1., 2., 3.])

In [354]: a = np.array([1.1, 2.2, 3.7])

In [355]: np.round(a)
Out[355]: array([1., 2., 4.])

In [356]: np.int64(np.round(a))
Out[356]: array([1, 2, 4])

In [357]: np.finfo(np.float64)
Out[357]: finfo(resolution=1e-15, min=-1.7976931348623157e+308, max=1.7976931348623157e+308, dtype=float64)

In [358]: np.finfo(np.int16)
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-358-ad98e8a5cd33> in <module>
----> 1 np.finfo(np.int16)

/usr/local/lib/python3.6/dist-packages/numpy/core/getlimits.py in __new__(cls, dtype)
    379             dtype = newdtype
    380         if not issubclass(dtype, numeric.inexact):
--> 381             raise ValueError("data type %r not inexact" % (dtype))
    382         obj = cls._finfo_cache.get(dtype, None)
    383         if obj is not None:

ValueError: data type <class 'numpy.int16'> not inexact
> /usr/local/lib/python3.6/dist-packages/numpy/core/getlimits.py(381)__new__()
    379             dtype = newdtype
    380         if not issubclass(dtype, numeric.inexact):
--> 381             raise ValueError("data type %r not inexact" % (dtype))
    382         obj = cls._finfo_cache.get(dtype, None)
    383         if obj is not None:

ipdb> c

In [359]: np.iinfo(np.int16)
Out[359]: iinfo(min=-32768, max=32767, dtype=int16)

In [360]:
