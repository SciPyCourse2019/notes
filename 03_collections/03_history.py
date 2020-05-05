mspacek@Godel:~/SciPyCourse2019/notes/03_collections$ ipython
Python 3.6.7 (default, Oct 22 2018, 11:32:17)
Type 'copyright', 'credits' or 'license' for more information
IPython 7.4.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: def vowelcount(string):
   ...:     """Returns the number of vowels in the string 'string'"""
   ...:     string = string.upper()
   ...:     i = string.count('A')
   ...:     i = i + string.count('E')
   ...:     i = i + string.count('I')
   ...:     i = i + string.count('O')
   ...:     i = i + string.count('U')
   ...:     i = i + string.count('Ä')
   ...:     i = i + string.count('Ö')
   ...:     i = i + string.count('Ü')
   ...:     print(string, "contains ", i, " vowels")
   ...:

In [2]: vowelcount('Martin')
MARTIN contains  2  vowels

In [3]: a = vowelcount('Martin')
MARTIN contains  2  vowels

In [4]: a

In [5]: type(a)
Out[5]: NoneType

In [6]: print(a)
None

In [7]: 'sdfs'.lower?
Object `lower` not found.

In [8]: s = 'sdlfkjdslfkj'

In [9]: s.lower?
Docstring:
S.lower() -> str

Return a copy of the string S converted to lowercase.
Type:      builtin_function_or_method

In [10]: 1/0
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
<ipython-input-10-9e1622b385b6> in <module>
----> 1 1/0

ZeroDivisionError: division by zero
> <ipython-input-10-9e1622b385b6>(1)<module>()
----> 1 1/0

ipdb> c

In [11]: print?
Docstring:
print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

Prints the values to a stream, or to sys.stdout by default.
Optional keyword arguments:
file:  a file-like object (stream); defaults to the current sys.stdout.
sep:   string inserted between values, default a space.
end:   string appended after the last value, default a newline.
flush: whether to forcibly flush the stream.
Type:      builtin_function_or_method

In [12]: print('')


In [13]: print()


In [14]: a = print('hi')
hi

In [15]: a

In [16]: type(a)
Out[16]: NoneType

In [17]: def multtable(n):
    ...:     for number in range (1,n+1):
    ...:         row=[]
    ...:         for multiplier in range(1,n+1):
    ...:             multiplicationresult= number*multiplier
    ...:             row.append(multiplicationresult)
    ...:         print(row)
    ...:

In [18]: multtable(10)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
[3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
[4, 8, 12, 16, 20, 24, 28, 32, 36, 40]
[5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
[6, 12, 18, 24, 30, 36, 42, 48, 54, 60]
[7, 14, 21, 28, 35, 42, 49, 56, 63, 70]
[8, 16, 24, 32, 40, 48, 56, 64, 72, 80]
[9, 18, 27, 36, 45, 54, 63, 72, 81, 90]
[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

In [19]: # Martin's solution:
    ...: def multtable(n):
    ...:     """Print multiplication table from 1 to n"""
    ...:     for i in range(1, n+1):
    ...:         for j in range(1, n+1):
    ...:             print(i * j, end=' ')
    ...:         print()
    ...:

In [20]: multtable(10)
1 2 3 4 5 6 7 8 9 10
2 4 6 8 10 12 14 16 18 20
3 6 9 12 15 18 21 24 27 30
4 8 12 16 20 24 28 32 36 40
5 10 15 20 25 30 35 40 45 50
6 12 18 24 30 36 42 48 54 60
7 14 21 28 35 42 49 56 63 70
8 16 24 32 40 48 56 64 72 80
9 18 27 36 45 54 63 72 81 90
10 20 30 40 50 60 70 80 90 100

In [21]: def multtable(n):
    ...:     """Print multiplication table from 1 to n"""
    ...:     for i in range(1, n+1):
    ...:         for j in range(1, n+1):
    ...:             print(i * j, end='\t')
    ...:         print()
    ...:

In [22]: multtable(10)
1   2   3   4   5   6   7   8   9   10
2   4   6   8   10  12  14  16  18  20
3   6   9   12  15  18  21  24  27  30
4   8   12  16  20  24  28  32  36  40
5   10  15  20  25  30  35  40  45  50
6   12  18  24  30  36  42  48  54  60
7   14  21  28  35  42  49  56  63  70
8   16  24  32  40  48  56  64  72  80
9   18  27  36  45  54  63  72  81  90
10  20  30  40  50  60  70  80  90  100

In [23]: # Martin's solution:
    ...: def multtable(n):
    ...:     """Print multiplication table from 1 to n"""
    ...:     for i in range(1, n+1):
    ...:         for j in range(1, n+1):
    ...:             print("%2d" % (i * j), end='\t')
    ...:         print()
    ...:

In [24]: multtable(10)
 1   2   3   4   5   6   7   8   9  10
 2   4   6   8  10  12  14  16  18  20
 3   6   9  12  15  18  21  24  27  30
 4   8  12  16  20  24  28  32  36  40
 5  10  15  20  25  30  35  40  45  50
 6  12  18  24  30  36  42  48  54  60
 7  14  21  28  35  42  49  56  63  70
 8  16  24  32  40  48  56  64  72  80
 9  18  27  36  45  54  63  72  81  90
10  20  30  40  50  60  70  80  90  100

In [25]: # Martin's solution:
    ...: def multtable(n):
    ...:     """Print multiplication table from 1 to n"""
    ...:     for i in range(1, n+1):
    ...:         for j in range(1, n+1):
    ...:             print("%2d" % (i * j), end=' ')
    ...:         print()
    ...:

In [26]: multtable(10)
 1  2  3  4  5  6  7  8  9 10
 2  4  6  8 10 12 14 16 18 20
 3  6  9 12 15 18 21 24 27 30
 4  8 12 16 20 24 28 32 36 40
 5 10 15 20 25 30 35 40 45 50
 6 12 18 24 30 36 42 48 54 60
 7 14 21 28 35 42 49 56 63 70
 8 16 24 32 40 48 56 64 72 80
 9 18 27 36 45 54 63 72 81 90
10 20 30 40 50 60 70 80 90 100

In [27]: t = (1, 2, 3)

In [28]: type(t)
Out[28]: tuple

In [29]: t = ('a', True, 3.14)

In [30]: t
Out[30]: ('a', True, 3.14)

In [31]: t = 'a', True, 3.14

In [32]: type(t)
Out[32]: tuple

In [33]: a, b, c = 1, 2, 3

In [34]: a
Out[34]: 1

In [35]: b
Out[35]: 2

In [36]: c
Out[36]: 3

In [37]: a, b, c, d, e, f, g = 1, 2, 3, 4, 5, 6, 7, 8
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-37-81ca951504cd> in <module>
----> 1 a, b, c, d, e, f, g = 1, 2, 3, 4, 5, 6, 7, 8

ValueError: too many values to unpack (expected 7)
> <ipython-input-37-81ca951504cd>(1)<module>()
----> 1 a, b, c, d, e, f, g = 1, 2, 3, 4, 5, 6, 7, 8

ipdb> c

In [38]: t
Out[38]: ('a', True, 3.14)

In [39]: len(t)
Out[39]: 3

In [40]: t[0]
Out[40]: 'a'

In [41]: t[1]
Out[41]: True

In [42]: t[2]
Out[42]: 3.14

In [43]: t[-1]
Out[43]: 3.14

In [44]: t[-2]
Out[44]: True

In [45]: t[-4]
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-45-f827787ee78e> in <module>
----> 1 t[-4]

IndexError: tuple index out of range
> <ipython-input-45-f827787ee78e>(1)<module>()
----> 1 t[-4]

ipdb> c

In [46]: t[:2]
Out[46]: ('a', True)

In [47]: t[0:2]
Out[47]: ('a', True)

In [48]: t[::2]
Out[48]: ('a', 3.14)

In [49]: s = 'abc'

In [50]: s[0]
Out[50]: 'a'

In [51]: s[0] = 'x'
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-51-fa085c53b004> in <module>
----> 1 s[0] = 'x'

TypeError: 'str' object does not support item assignment
> <ipython-input-51-fa085c53b004>(1)<module>()
----> 1 s[0] = 'x'

ipdb> c

In [52]: s
Out[52]: 'abc'

In [53]: t
Out[53]: ('a', True, 3.14)

In [54]: t[0] = 'hi'
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-54-95e62e56bc33> in <module>
----> 1 t[0] = 'hi'

TypeError: 'tuple' object does not support item assignment
> <ipython-input-54-95e62e56bc33>(1)<module>()
----> 1 t[0] = 'hi'

ipdb> c

In [55]: t.count?
Docstring: T.count(value) -> integer -- return number of occurrences of value
Type:      builtin_function_or_method

In [56]: t.count('a')
Out[56]: 1

In [57]: t.index('a')
Out[57]: 0

In [58]: t
Out[58]: ('a', True, 3.14)

In [59]: t[::1]
Out[59]: ('a', True, 3.14)

In [60]: t[::5]
Out[60]: ('a',)

In [61]: t[::2]
Out[61]: ('a', 3.14)

In [62]: t[::5]
Out[62]: ('a',)

In [63]: def mult123(x):
    ...:     return x, 2*x, 3*x
    ...:

In [64]: a, b, c, d = mult123(10)
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-64-594db20cb6bd> in <module>
----> 1 a, b, c, d = mult123(10)

ValueError: not enough values to unpack (expected 4, got 3)
> <ipython-input-64-594db20cb6bd>(1)<module>()
----> 1 a, b, c, d = mult123(10)

ipdb> c

In [65]: a, b, c = mult123(10)

In [66]: a
Out[66]: 10

In [67]: b
Out[67]: 20

In [68]: c
Out[68]: 30

In [69]: l = [1, 2, 3]

In [70]: l
Out[70]: [1, 2, 3]

In [71]: type(l)
Out[71]: list

In [72]: len(l)
Out[72]: 3

In [73]: l[0]
Out[73]: 1

In [74]: l[::2]
Out[74]: [1, 3]

In [75]: l = []

In [76]: l
Out[76]: []

In [77]: l = []

In [78]: l = [1, 2, 3]

In [79]: l[0] = 'hi'

In [80]: l
Out[80]: ['hi', 2, 3]

In [81]: l.append?
Docstring: L.append(object) -> None -- append object to end
Type:      builtin_function_or_method

In [82]: l = []

In [83]: l.append(1)

In [84]: l
Out[84]: [1]

In [85]: l.append(2)

In [86]: l.append('hi')

In [87]: l
Out[87]: [1, 2, 'hi']

In [88]: l = []

In [89]: for i in range(10):
    ...:     l.append(i)
    ...:

In [90]: l
Out[90]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

In [91]: l1 = [1,2,3]

In [92]: l2 = [4,5,6]

In [93]: l1.extend(l2)

In [94]: l1
Out[94]: [1, 2, 3, 4, 5, 6]

In [95]: l1 = [1,2,3]

In [96]: l2 = [4,5,6]

In [97]: l1 + l2
Out[97]: [1, 2, 3, 4, 5, 6]

In [98]: l1 - l2
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-98-e85e3ff6b3e6> in <module>
----> 1 l1 - l2

TypeError: unsupported operand type(s) for -: 'list' and 'list'
> <ipython-input-98-e85e3ff6b3e6>(1)<module>()
----> 1 l1 - l2

ipdb> c

In [99]: l1 * l2
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-99-ec7519df584c> in <module>
----> 1 l1 * l2

TypeError: can't multiply sequence by non-int of type 'list'
> <ipython-input-99-ec7519df584c>(1)<module>()
----> 1 l1 * l2

ipdb> c

In [100]: l1 * 2
Out[100]: [1, 2, 3, 1, 2, 3]

In [101]: l1 + 2
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-101-eb8f1067bc89> in <module>
----> 1 l1 + 2

TypeError: can only concatenate list (not "int") to list
> <ipython-input-101-eb8f1067bc89>(1)<module>()
----> 1 l1 + 2

ipdb> c

In [102]: l1 + [2]
Out[102]: [1, 2, 3, 2]

In [103]: l
Out[103]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

In [104]: l.reverse()

In [105]: l
Out[105]: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

In [106]: a = l.reverse()

In [107]: a

In [108]: print(a)
None

In [109]: l
Out[109]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

In [110]: s
Out[110]: 'abc'

In [111]: s.lower()
Out[111]: 'abc'

In [112]: l = [4, 2, 6, 7, 3, 4]

In [113]: l.sort?
Docstring: L.sort(key=None, reverse=False) -> None -- stable sort *IN PLACE*
Type:      builtin_function_or_method

In [114]: l.sort()

In [115]: l
Out[115]: [2, 3, 4, 4, 6, 7]

In [116]: l.sort(reverse=True)

In [117]: l
Out[117]: [7, 6, 4, 4, 3, 2]

In [118]: range(10)
Out[118]: range(0, 10)

In [119]: list(range(10))
Out[119]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

In [120]: l = list(range(10))

In [121]: l
Out[121]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

In [122]: l = list(range(10, 20, 2))

In [123]: l
Out[123]: [10, 12, 14, 16, 18]

In [124]: t
Out[124]: ('a', True, 3.14)

In [125]: list(t)
Out[125]: ['a', True, 3.14]

In [126]: l
Out[126]: [10, 12, 14, 16, 18]

In [127]: tuple(l)
Out[127]: (10, 12, 14, 16, 18)

In [128]: s
Out[128]: 'abc'

In [129]: for c in s:
     ...:     print(c)
     ...:
a
b
c

In [130]: for o in l:
     ...:     print(o)
     ...:
10
12
14
16
18

In [131]: for o in t:
     ...:     print(o)
     ...:
a
True
3.14

In [132]: enumerate?
Init signature: enumerate(self, /, *args, **kwargs)
Docstring:
enumerate(iterable[, start]) -> iterator for index, value of iterable

Return an enumerate object.  iterable must be another object that supports
iteration.  The enumerate object yields pairs containing a count (from
start, which defaults to zero) and a value yielded by the iterable argument.
enumerate is useful for obtaining an indexed list:
    (0, seq[0]), (1, seq[1]), (2, seq[2]), ...
Type:           type
Subclasses:

In [133]: for o in t:
     ...:     print(o)
     ...:
a
True
3.14

In [134]:

In [134]: for o in l:
     ...:     print(o)
     ...:
10
12
14
16
18

In [135]:

In [135]: for i, v in enumerate(l):
     ...:     print(i, v)
     ...:
     ...:
0 10
1 12
2 14
3 16
4 18

In [136]: for i, v in enumerate(t):
     ...:     print(i, v)
     ...:
     ...:
0 a
1 True
2 3.14

In [137]: zip?
Init signature: zip(self, /, *args, **kwargs)
Docstring:
zip(iter1 [,iter2 [...]]) --> zip object

Return a zip object whose .__next__() method returns a tuple where
the i-th element comes from the i-th iterable argument.  The .__next__()
method continues until the shortest iterable in the argument sequence
is exhausted and then it raises StopIteration.
Type:           type
Subclasses:

In [138]: l
Out[138]: [10, 12, 14, 16, 18]

In [139]: l1
Out[139]: [1, 2, 3]

In [140]: l2
Out[140]: [4, 5, 6]

In [141]: for a, b in zip(l1, l2):
     ...:     print(a, b)
     ...:
1 4
2 5
3 6

In [142]: for a, b in zip(enumerate(l1, l2)):
     ...:     print(a, b)
     ...:
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-142-9ee442e29478> in <module>
----> 1 for a, b in zip(enumerate(l1, l2)):
      2     print(a, b)
      3

TypeError: 'list' object cannot be interpreted as an integer
> <ipython-input-142-9ee442e29478>(1)<module>()
----> 1 for a, b in zip(enumerate(l1, l2)):
      2     print(a, b)
      3

ipdb> c

In [143]: for i, (a, b) in enumerate(zip(l1, l2)):
     ...:     print(i, a, b)
     ...:
     ...:
0 1 4
1 2 5
2 3 6

In [144]: l2
Out[144]: [4, 5, 6]

In [145]: l
Out[145]: [10, 12, 14, 16, 18]

In [146]: l2.append(7)

In [147]: l2
Out[147]: [4, 5, 6, 7]

In [148]: l1
Out[148]: [1, 2, 3]

In [149]: l2
Out[149]: [4, 5, 6, 7]

In [150]: for a, b in zip(l1, l2):
     ...:     print(a, b)
     ...:
1 4
2 5
3 6

In [151]: zip?
Init signature: zip(self, /, *args, **kwargs)
Docstring:
zip(iter1 [,iter2 [...]]) --> zip object

Return a zip object whose .__next__() method returns a tuple where
the i-th element comes from the i-th iterable argument.  The .__next__()
method continues until the shortest iterable in the argument sequence
is exhausted and then it raises StopIteration.
Type:           type
Subclasses:

In [152]: l = []

In [153]: for i in range(10):
     ...:     l.append(i)
     ...:

In [154]: l
Out[154]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

In [155]: l
Out[155]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

In [156]: doubled = []

In [157]: for i in l:
     ...:     doubled.append(i*2)
     ...:

In [158]: doubled
Out[158]: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

In [159]: doubled = [ i*2 for i in l ]

In [160]: doubled
Out[160]: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

In [161]: 1e2
Out[161]: 100.0

In [162]: l =
  File "<ipython-input-162-9db08b9cc700>", line 1
    l =
        ^
SyntaxError: invalid syntax


In [163]: l
Out[163]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

In [164]: l2
Out[164]: [4, 5, 6, 7]

In [165]: del l2[0]

In [166]: l2
Out[166]: [5, 6, 7]

In [167]: t = 3, 5, 1.7, -2.7, 1e2, -50

In [168]: t
Out[168]: (3, 5, 1.7, -2.7, 100.0, -50)

In [169]: t[::2]
Out[169]: (3, 1.7, 100.0)

In [170]: l = list(t)

In [171]: l
Out[171]: [3, 5, 1.7, -2.7, 100.0, -50]

In [172]: l.sort()

In [173]: l
Out[173]: [-50, -2.7, 1.7, 3, 5, 100.0]

In [174]: l.sort()

In [175]: l
Out[175]: [-50, -2.7, 1.7, 3, 5, 100.0]

In [176]: sorted?
Signature: sorted(iterable, /, *, key=None, reverse=False)
Docstring:
Return a new list containing all items from the iterable in ascending order.

A custom key function can be supplied to customize the sort order, and the
reverse flag can be set to request the result in descending order.
Type:      builtin_function_or_method

In [177]: sorted(l)
Out[177]: [-50, -2.7, 1.7, 3, 5, 100.0]

In [178]: l.sort()

In [179]: l = sorted(l)

In [180]: l
Out[180]: [-50, -2.7, 1.7, 3, 5, 100.0]

In [181]: l.sort()

In [182]: l
Out[182]: [-50, -2.7, 1.7, 3, 5, 100.0]

In [183]: l.append('blah')

In [184]: l
Out[184]: [-50, -2.7, 1.7, 3, 5, 100.0, 'blah']

In [185]: l.sort()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-185-fb07ac7c73ab> in <module>
----> 1 l.sort()

TypeError: '<' not supported between instances of 'str' and 'float'
> <ipython-input-185-fb07ac7c73ab>(1)<module>()
----> 1 l.sort()

ipdb> c

In [186]: l.remove?
Docstring:
L.remove(value) -> None -- remove first occurrence of value.
Raises ValueError if the value is not present.
Type:      builtin_function_or_method

In [187]: l.remove('blah')

In [188]: l
Out[188]: [-50, -2.7, 1.7, 3, 5, 100.0]

In [189]: l.append('blah')

In [190]: l
Out[190]: [-50, -2.7, 1.7, 3, 5, 100.0, 'blah']

In [191]: del l[6]

In [192]: l
Out[192]: [-50, -2.7, 1.7, 3, 5, 100.0]

In [193]: l.append('blah')

In [194]: l[:-2]
Out[194]: [-50, -2.7, 1.7, 3, 5]

In [195]: l
Out[195]: [-50, -2.7, 1.7, 3, 5, 100.0, 'blah']

In [196]: l[:-1]
Out[196]: [-50, -2.7, 1.7, 3, 5, 100.0]

In [197]: t
Out[197]: (3, 5, 1.7, -2.7, 100.0, -50)

In [198]: dbl = []

In [199]: for val in t:
     ...:     dbl.append(val*2)
     ...:

In [200]: dbl
Out[200]: [6, 10, 3.4, -5.4, 200.0, -100]

In [201]: dbl = [ i*2 for i in t ]

In [202]: dbl
Out[202]: [6, 10, 3.4, -5.4, 200.0, -100]

In [203]: dbl
Out[203]: [6, 10, 3.4, -5.4, 200.0, -100]

In [204]: def multseq(seq, x):
     ...:     return [i*x for i in seq]
     ...:

In [205]: multseq([1,2,3], 5)
Out[205]: [5, 10, 15]

In [206]: d = {}

In [207]: type(d)
Out[207]: dict

In [208]: len(d)
Out[208]: 0

In [209]: names2ages = {'Alice':25, 'Bob':20, 'Carol':32}

In [210]: names2ages['Alice']
Out[210]: 25

In [211]: names2ages['Bob']
Out[211]: 20

In [212]: names2ages['Carol']
Out[212]: 32

In [213]: ages2names = {25:'Alice', 20:'Bob', 32:'Carol'}

In [214]: ages2names[25]
Out[214]: 'Alice'

In [215]: ages2names[20]
Out[215]: 'Bob'

In [216]: ages2names[32]
Out[216]: 'Carol'

In [217]: names2ages
Out[217]: {'Alice': 25, 'Bob': 20, 'Carol': 32}

In [218]: names2ages['Carol']
Out[218]: 32

In [219]: names2ages['David']
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
<ipython-input-219-8b420b1cc87f> in <module>
----> 1 names2ages['David']

KeyError: 'David'
> <ipython-input-219-8b420b1cc87f>(1)<module>()
----> 1 names2ages['David']

ipdb> c

In [220]: names2ages = {'Alice':25, 'Bob':20, 'Carol':32}

In [221]: names2ages['David'] = 40

In [222]: names2ages
Out[222]: {'Alice': 25, 'Bob': 20, 'Carol': 32, 'David': 40}

In [223]: names2ages['Eli'] = 40

In [224]: names2ages
Out[224]: {'Alice': 25, 'Bob': 20, 'Carol': 32, 'David': 40, 'Eli': 40}

In [225]: names2ages['David'] = 18

In [226]: names2ages
Out[226]: {'Alice': 25, 'Bob': 20, 'Carol': 32, 'David': 18, 'Eli': 40}

In [227]: names2ages = {'Alice':25, 'Bob':20, 'Carol':32, 'Carol':18}

In [228]: names2ages
Out[228]: {'Alice': 25, 'Bob': 20, 'Carol': 18}

In [229]: del names2ages['Alice']

In [230]: names2ages
Out[230]: {'Bob': 20, 'Carol': 18}

In [231]: names2ages = {'Alice':25, 'Bob':20, 'Carol':32}

In [232]: names2ages.keys()
Out[232]: dict_keys(['Alice', 'Bob', 'Carol'])

In [233]: list(names2ages.keys())
Out[233]: ['Alice', 'Bob', 'Carol']

In [234]: list(names2ages.values())
Out[234]: [25, 20, 32]

In [235]: sorted(names2ages)
Out[235]: ['Alice', 'Bob', 'Carol']

In [236]: list(names2ages.keys())
Out[236]: ['Alice', 'Bob', 'Carol']

In [237]: list(names2ages)
Out[237]: ['Alice', 'Bob', 'Carol']

In [238]: sorted(names2ages)
Out[238]: ['Alice', 'Bob', 'Carol']

In [239]:

In [239]: names2ages
Out[239]: {'Alice': 25, 'Bob': 20, 'Carol': 32}

In [240]: for key in names2ages:
     ...:     print(key)
     ...:
Alice
Bob
Carol

In [241]: for key, val in names2ages.items():
     ...:     print(key, val)
     ...:
     ...:
Alice 25
Bob 20
Carol 32

In [242]: for val in names2ages.values():
     ...:     print(val)
     ...:
     ...:
     ...:
25
20
32

In [243]: dblnames2ages = { key:val*2 for key, val in names2ages.items() }

In [244]: dblnames2ages
Out[244]: {'Alice': 50, 'Bob': 40, 'Carol': 64}

In [245]: [(1, 2), (3, 4), (5, 6)]
Out[245]: [(1, 2), (3, 4), (5, 6)]

In [246]: type([(1, 2), (3, 4), (5, 6)])
Out[246]: list

In [247]: l = [(1, 2), (3, 4), (5, 6)]

In [248]: l[0]
Out[248]: (1, 2)

In [249]: tuple(l[0])
Out[249]: (1, 2)

In [250]: {'a':[1,2,3], 'b':[4,5,6]}
Out[250]: {'a': [1, 2, 3], 'b': [4, 5, 6]}

In [251]: d = {'a':[1,2,3], 'b':[4,5,6]}

In [252]: d['a']
Out[252]: [1, 2, 3]

In [253]: d['a'][0]
Out[253]: 1

In [254]: d = [{'a':1, 'b':2}, {'c':3, 'd':4}]

In [255]: d
Out[255]: [{'a': 1, 'b': 2}, {'c': 3, 'd': 4}]

In [256]: d[1]
Out[256]: {'c': 3, 'd': 4}

In [257]: d[1]
Out[257]: {'c': 3, 'd': 4}

In [258]: d[1]['e'] = 5

In [259]: d
Out[259]: [{'a': 1, 'b': 2}, {'c': 3, 'd': 4, 'e': 5}]

In [260]: d
Out[260]: [{'a': 1, 'b': 2}, {'c': 3, 'd': 4, 'e': 5}]

In [261]: d[0]
Out[261]: {'a': 1, 'b': 2}

In [262]: del d[0]['a']

In [263]: d[0]
Out[263]: {'b': 2}

In [264]: d
Out[264]: [{'b': 2}, {'c': 3, 'd': 4, 'e': 5}]

In [265]: d[1]
Out[265]: {'c': 3, 'd': 4, 'e': 5}

In [266]: d
Out[266]: [{'b': 2}, {'c': 3, 'd': 4, 'e': 5}]

In [267]: del d[0]

In [268]: d
Out[268]: [{'c': 3, 'd': 4, 'e': 5}]

In [269]: d[0]
Out[269]: {'c': 3, 'd': 4, 'e': 5}

In [270]: d
Out[270]: [{'c': 3, 'd': 4, 'e': 5}]

In [271]: del d[0]['a']
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
<ipython-input-271-bb64c7eed2a6> in <module>
----> 1 del d[0]['a']

KeyError: 'a'
> <ipython-input-271-bb64c7eed2a6>(1)<module>()
----> 1 del d[0]['a']

ipdb> c

In [272]:

In [272]: d
Out[272]: [{'c': 3, 'd': 4, 'e': 5}]

In [273]: d[0]
Out[273]: {'c': 3, 'd': 4, 'e': 5}

In [274]: d[1] = d[0]
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-274-8abe1f9ddae9> in <module>
----> 1 d[1] = d[0]

IndexError: list assignment index out of range
> <ipython-input-274-8abe1f9ddae9>(1)<module>()
----> 1 d[1] = d[0]

ipdb> c

In [275]: d.append(d[0])

In [276]: d
Out[276]: [{'c': 3, 'd': 4, 'e': 5}, {'c': 3, 'd': 4, 'e': 5}]

In [277]: d[0] = {'a':1, 'b':2}

In [278]: d
Out[278]: [{'a': 1, 'b': 2}, {'c': 3, 'd': 4, 'e': 5}]

In [279]: d.insert?
Docstring: L.insert(index, object) -- insert object before index
Type:      builtin_function_or_method

In [280]:
