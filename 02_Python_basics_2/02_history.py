
mspacek@Godel:~/SciPyCourse2019/notes/02_Python_basics_2$ python
Python 2.7.15rc1 (default, Nov 12 2018, 14:31:15) 
[GCC 7.3.0] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> for i range(5):
  File "<stdin>", line 1
    for i range(5):
              ^
SyntaxError: invalid syntax
>>> for i in range(5):
...     print(i)
... 
0
1
2
3
4
>>> for i in [0, 1, 2, 3, 4]:
...     print(i)
... 
0
1
2
3
4
>>> genius = 2 + 2
>>> genius
4
>>> for something in range(10):
...     print(something)
... 
0
1
2
3
4
5
6
7
8
9
>>> 
mspacek@Godel:~/SciPyCourse2019/notes/02_Python_basics_2$ ls
01_exercises.py  02_Python_basics_2.md  02_Python_basics_2.pdf  basics.py  example_functions.py
mspacek@Godel:~/SciPyCourse2019/notes/02_Python_basics_2$ python basics.py 
0
1
2
3
4
5
6
7
8
9
mspacek@Godel:~/SciPyCourse2019/notes/02_Python_basics_2$ python basics.py 
0
1
4
9
16
25
36
49
64
81
mspacek@Godel:~/SciPyCourse2019/notes/02_Python_basics_2$ python basics.py 
0
1
4
9
16
25
36
49
64
81
mspacek@Godel:~/SciPyCourse2019/notes/02_Python_basics_2$ python basics.py 
0
1
4
9
16
25
36
49
64
81
45
mspacek@Godel:~/SciPyCourse2019/notes/02_Python_basics_2$ python basics.py 
0.0
1.0
1.41421356237
1.73205080757
2.0
2.2360679775
2.44948974278
2.64575131106
2.82842712475
3.0
mspacek@Godel:~/SciPyCourse2019/notes/02_Python_basics_2$ python basics.py 
0
1
2
3
4
5
6
7
seven
8
9
mspacek@Godel:~/SciPyCourse2019/notes/02_Python_basics_2$ python basics.py 
0
1
2
3
three
4
5
6
7
seven
8
9
mspacek@Godel:~/SciPyCourse2019/notes/02_Python_basics_2$ python basics.py 
0
1
2
3
three
4
5
6
7
seven
8
9
mspacek@Godel:~/SciPyCourse2019/notes/02_Python_basics_2$ python basics.py 
0
(0, 'is even', 'wow!')
1
(1, 'is odd')
2
(2, 'is even', 'wow!')
3
(3, 'is odd')
4
(4, 'is even', 'wow!')
5
(5, 'is odd')
6
(6, 'is even', 'wow!')
7
(7, 'is odd')
8
(8, 'is even', 'wow!')
9
(9, 'is odd')
mspacek@Godel:~/SciPyCourse2019/notes/02_Python_basics_2$ python basics.py 
(0, 'is even', 'wow!')
(1, 'is odd')
(2, 'is even', 'wow!')
(3, 'is odd')
(4, 'is even', 'wow!')
(5, 'is odd')
(6, 'is even', 'wow!')
(7, 'is odd')
(8, 'is even', 'wow!')
(9, 'is odd')
mspacek@Godel:~/SciPyCourse2019/notes/02_Python_basics_2$ python basics.py 
(0, 'is even')
(1, 'is odd')
(2, 'is even')
(3, 'is odd')
(4, 'is even')
(5, 'is odd')
(6, 'is even')
(7, 'is odd')
(8, 'is even')
(9, 'is odd')
mspacek@Godel:~/SciPyCourse2019/notes/02_Python_basics_2$ python basics.py 
(0, 'is even')
(1, 'is odd')
(2, 'is even')
(3, 'is odd')
(4, 'is even')
(5, 'is odd')
(6, 'is even')
(8, 'is even')
(9, 'is odd')
mspacek@Godel:~/SciPyCourse2019/notes/02_Python_basics_2$ python basics.py 
(1, 'is odd')
(2, 'is even')
(3, 'is odd')
(4, 'is even')
(5, 'is odd')
(6, 'is even')
(8, 'is even')
(9, 'is odd')
mspacek@Godel:~/SciPyCourse2019/notes/02_Python_basics_2$ python basics.py 
(1, 'is odd')
(2, 'is even')
(3, 'is odd')
(4, 'is even')
(5, 'is odd')
(6, 'is even')
(8, 'is even')
(9, 'is odd')
(10, 'is even')
mspacek@Godel:~/SciPyCourse2019/notes/02_Python_basics_2$ python basics.py 
(1, 'is odd')
(2, 'is even')
(3, 'is odd')
(4, 'is even')
(5, 'is odd')
(6, 'is even')
(8, 'is even')
(9, 'is odd')
(10, 'is even')
mspacek@Godel:~/SciPyCourse2019/notes/02_Python_basics_2$ python basics.py 
(1, 'is odd')
(2, 'is even')
(3, 'is odd')
(4, 'is even')
(5, 'is odd')
(6, 'is even')
(8, 'is even')
(9, 'is odd')
(10, 'is even')
mspacek@Godel:~/SciPyCourse2019/notes/02_Python_basics_2$ python basics.py 
(11, 'is odd')
(10, 'is even')
(9, 'is odd')
(8, 'is even')
(6, 'is even')
(5, 'is odd')
(4, 'is even')
(3, 'is odd')
(2, 'is even')
mspacek@Godel:~/SciPyCourse2019/notes/02_Python_basics_2$ python basics.py 
(10, 'is even')
(9, 'is odd')
(8, 'is even')
(6, 'is even')
(5, 'is odd')
(4, 'is even')
(3, 'is odd')
(2, 'is even')
(1, 'is odd')
mspacek@Godel:~/SciPyCourse2019/notes/02_Python_basics_2$ python
Python 2.7.15rc1 (default, Nov 12 2018, 14:31:15) 
[GCC 7.3.0] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> 
mspacek@Godel:~/SciPyCourse2019/notes/02_Python_basics_2$ ipython
Python 3.6.7 (default, Oct 22 2018, 11:32:17) 
Type 'copyright', 'credits' or 'license' for more information
IPython 7.4.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: a = 1                                                                                          

In [2]: print('sdfsdf')                                                                                
sdfsdf

In [3]: a                                                                                              
Out[3]: 1

In [4]: _3                                                                                             
Out[4]: 1

In [5]: _i2                                                                                            
Out[5]: "print('sdfsdf')"

In [6]: _3                                                                                             
Out[6]: 1

In [7]: help(print)                                                                                    


In [8]: print?                                                                                         
Docstring:
print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

Prints the values to a stream, or to sys.stdout by default.
Optional keyword arguments:
file:  a file-like object (stream); defaults to the current sys.stdout.
sep:   string inserted between values, default a space.
end:   string appended after the last value, default a newline.
flush: whether to forcibly flush the stream.
Type:      builtin_function_or_method

In [9]: something = 1                                                                                                                            

In [10]: something                                                                                                                               
Out[10]: 1

In [11]: whos                                                                                                                                    
Variable    Type      Data/Info
-------------------------------
a           int       1
np          module    <module 'numpy' from '/us<...>kages/numpy/__init__.py'>
plt         module    <module 'matplotlib.pyplo<...>es/matplotlib/pyplot.py'>
something   int       1

In [12]: np                                                                                                                                      
Out[12]: <module 'numpy' from '/usr/local/lib/python3.6/dist-packages/numpy/__init__.py'>

In [13]: plt                                                                                                                                     
Out[13]: <module 'matplotlib.pyplot' from '/usr/local/lib/python3.6/dist-packages/matplotlib/pyplot.py'>

In [14]: whos                                                                                                                                    
Variable    Type      Data/Info
-------------------------------
a           int       1
np          module    <module 'numpy' from '/us<...>kages/numpy/__init__.py'>
plt         module    <module 'matplotlib.pyplo<...>es/matplotlib/pyplot.py'>
something   int       1

In [15]: del a                                                                                                                                   

In [16]: whos                                                                                                                                    
Variable    Type      Data/Info
-------------------------------
np          module    <module 'numpy' from '/us<...>kages/numpy/__init__.py'>
plt         module    <module 'matplotlib.pyplo<...>es/matplotlib/pyplot.py'>
something   int       1

In [17]: a                                                                                                                                       
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-17-3f786850e387> in <module>
----> 1 a

NameError: name 'a' is not defined
> <ipython-input-17-3f786850e387>(1)<module>()
----> 1 a

ipdb> c                                                                                                                                          

In [18]: reset                                                                                                                                   
Once deleted, variables cannot be recovered. Proceed (y/[n])? y

In [19]: whos                                                                                                                                    
Interactive namespace is empty.

In [20]: for i in range(10, 0, -1): 
    ...:     #print(i) 
    ...:     if i == 7: 
    ...:         continue 
    ...:     if i % 2 == 0: 
    ...:         print(i, 'is even') 
    ...:     else: 
    ...:         print(i, 'is odd') 
    ...:                                                                                                                                         
10 is even
9 is odd
8 is even
6 is even
5 is odd
4 is even
3 is odd
2 is even
1 is odd

In [21]: for i in range(10, 0, -1): 
    ...:     #print(i) 
    ...:     if i == 7: 
    ...:         continue 
    ...:     if i % 2 == 0: 
    ...:         print(i, 'is even') 
    ...:     else: 
    ...:         print(i, 'is odd') 
    ...:                                                                                                                                         
10 is even
9 is odd
8 is even
6 is even
5 is odd
4 is even
3 is odd
2 is even
1 is odd

In [22]:                                                                                                                                         
mspacek@Godel:~/SciPyCourse2019/notes/02_Python_basics_2$ ipython
Python 3.6.7 (default, Oct 22 2018, 11:32:17) 
Type 'copyright', 'credits' or 'license' for more information
IPython 7.4.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: pwd                                                                                                                                      
Out[1]: '/home/mspacek/SciPyCourse2019/notes/02_Python_basics_2'

In [2]: ls                                                                                                                                       
01_exercises.py  02_Python_basics_2.md  02_Python_basics_2.pdf  basics.py  example_functions.py

In [3]: run basics.py                                                                                                                            
10 is even
9 is odd
8 is even
6 is even
5 is odd
4 is even
3 is odd
2 is even
1 is odd

In [4]: whos                                                                                                                                     
Variable   Type      Data/Info
------------------------------
i          int       1
np         module    <module 'numpy' from '/us<...>kages/numpy/__init__.py'>
plt        module    <module 'matplotlib.pyplo<...>es/matplotlib/pyplot.py'>

In [5]: run basics.py                                                                                                                            
10 is even
9 is odd
8 is even
6 is even
5 is odd
4 is even
3 is odd
2 is even
1 is odd

In [6]: myname = "Martin"                                                                                                                        

In [7]: run basics.py                                                                                                                            
10 is even
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
~/SciPyCourse2019/notes/02_Python_basics_2/basics.py in <module>
      7     else:
      8         print(i, 'is odd')
----> 9     print(myname)

NameError: name 'myname' is not defined
> /home/mspacek/SciPyCourse2019/notes/02_Python_basics_2/basics.py(9)<module>()
      5     if i % 2 == 0:
      6         print(i, 'is even')
      7     else:
      8         print(i, 'is odd')
----> 9     print(myname)

ipdb> c                                                                                                                                          

In [8]: run -i basics.py                                                                                                                         
10 is even
Martin
9 is odd
Martin
8 is even
Martin
6 is even
Martin
5 is odd
Martin
4 is even
Martin
3 is odd
Martin
2 is even
Martin
1 is odd
Martin

In [9]:                                                                                                                                          
mspacek@Godel:~/SciPyCourse2019/notes/02_Python_basics_2$ ipython
Python 3.6.7 (default, Oct 22 2018, 11:32:17) 
Type 'copyright', 'credits' or 'license' for more information
IPython 7.4.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: s = 'Martin'                                                                                                                             

In [2]: type(s)                                                                                                                                  
Out[2]: str

In [3]: s = "Martin"                                                                                                                             

In [4]: s                                                                                                                                        
Out[4]: 'Martin'

In [5]: type(s)                                                                                                                                  
Out[5]: str

In [6]: s = "Martin's"                                                                                                                           

In [7]: s                                                                                                                                        
Out[7]: "Martin's"

In [8]: s = ''                                                                                                                                   

In [9]: s                                                                                                                                        
Out[9]: ''

In [10]: s = 'Hello' + ' ' + 'world'                                                                                                             

In [11]: s                                                                                                                                       
Out[11]: 'Hello world'

In [12]: 1 + 1                                                                                                                                   
Out[12]: 2

In [13]: 'a' + 'b'                                                                                                                               
Out[13]: 'ab'

In [14]: 'a' + 1                                                                                                                                 
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-14-076d4fba1eac> in <module>
----> 1 'a' + 1

TypeError: must be str, not int
> <ipython-input-14-076d4fba1eac>(1)<module>()
----> 1 'a' + 1

ipdb> c                                                                                                                                          

In [15]: s                                                                                                                                       
Out[15]: 'Hello world'

In [16]: s += '!'                                                                                                                                

In [17]: s                                                                                                                                       
Out[17]: 'Hello world!'

In [18]: s += 1                                                                                                                                  
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-18-fae459add732> in <module>
----> 1 s += 1

TypeError: must be str, not int
> <ipython-input-18-fae459add732>(1)<module>()
----> 1 s += 1

ipdb> c                                                                                                                                          

In [19]: s += 'sdfsdfsdf'                                                                                                                        

In [20]: s                                                                                                                                       
Out[20]: 'Hello world!sdfsdfsdf'

In [21]: s += 'abc'+'def'                                                                                                                        

In [22]:                                                                                                                                         

In [22]: s                                                                                                                                       
Out[22]: 'Hello world!sdfsdfsdfabcdef'

In [23]: s = 'Hello' + ' ' + 'world'                                                                                                             

In [24]: s                                                                                                                                       
Out[24]: 'Hello world'

In [25]: a = 2                                                                                                                                   

In [26]: a                                                                                                                                       
Out[26]: 2

In [27]: a *= 2                                                                                                                                  

In [28]: a                                                                                                                                       
Out[28]: 4

In [29]: s                                                                                                                                       
Out[29]: 'Hello world'

In [30]: s *= 2                                                                                                                                  

In [31]: s                                                                                                                                       
Out[31]: 'Hello worldHello world'

In [32]: print(s)                                                                                                                                
Hello worldHello world

In [33]: s = 'Hello' + ' ' + 'world'                                                                                                             

In [34]: s                                                                                                                                       
Out[34]: 'Hello world'

In [35]: s = 'Hello world\n\n\n'                                                                                                                 

In [36]: s                                                                                                                                       
Out[36]: 'Hello world\n\n\n'

In [37]: print(s)                                                                                                                                
Hello world




In [38]: value = 'world'                                                                                                                         

In [39]: value                                                                                                                                   
Out[39]: 'world'

In [40]: 'Hello %s' % value                                                                                                                      
Out[40]: 'Hello world'

In [41]: s = 'Hello %s' % value                                                                                                                  

In [42]: s                                                                                                                                       
Out[42]: 'Hello world'

In [43]: pi = 3.14159                                                                                                                            

In [44]: 'pi is %s' pi                                                                                                                           
  File "<ipython-input-44-b84a68f563d6>", line 1
    'pi is %s' pi
                ^
SyntaxError: invalid syntax


In [45]: 'pi is %s' % pi                                                                                                                         
Out[45]: 'pi is 3.14159'

In [46]: 'pi is %.3f' % pi                                                                                                                       
Out[46]: 'pi is 3.142'

In [47]: 'Hello %d' % value                                                                                                                      
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-47-aeff292eba1f> in <module>
----> 1 'Hello %d' % value

TypeError: %d format: a number is required, not str
> <ipython-input-47-aeff292eba1f>(1)<module>()
----> 1 'Hello %d' % value

ipdb> c                                                                                                                                          

In [48]: 'Hello %d' % 'world'                                                                                                                    
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-48-d4f55ef4a9e7> in <module>
----> 1 'Hello %d' % 'world'

TypeError: %d format: a number is required, not str
> <ipython-input-48-d4f55ef4a9e7>(1)<module>()
----> 1 'Hello %d' % 'world'

ipdb> c                                                                                                                                          

In [49]: 'Hello %d' % '1'                                                                                                                        
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-49-cb1fd6a8e2ae> in <module>
----> 1 'Hello %d' % '1'

TypeError: %d format: a number is required, not str
> <ipython-input-49-cb1fd6a8e2ae>(1)<module>()
----> 1 'Hello %d' % '1'

ipdb> c                                                                                                                                          

In [50]: 'Hello %d' % 1                                                                                                                          
Out[50]: 'Hello 1'

In [51]: 'Hello %d' % 3.14159                                                                                                                    
Out[51]: 'Hello 3'

In [52]: 'Hello %d' % 3.6                                                                                                                        
Out[52]: 'Hello 3'

In [53]: 'Hello %d' % 3.6                                                                                                                        
Out[53]: 'Hello 3'

In [54]: 'Today is %s %d, %d' % ('May', 7, 2019)                                                                                                 
Out[54]: 'Today is May 7, 2019'

In [55]: 'May 7, 2019'                                                                                                                           
Out[55]: 'May 7, 2019'

In [56]: s = 'abcdefg'                                                                                                                           

In [57]: s                                                                                                                                       
Out[57]: 'abcdefg'

In [58]: len                                                                                                                                     
Out[58]: <function len(obj, /)>

In [59]: len?                                                                                                                                    
Signature: len(obj, /)
Docstring: Return the number of items in a container.
Type:      builtin_function_or_method

In [60]: len(s)                                                                                                                                  
Out[60]: 7

In [61]: s                                                                                                                                       
Out[61]: 'abcdefg'

In [62]: h in s                                                                                                                                  
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-62-c52218c9a653> in <module>
----> 1 h in s

NameError: name 'h' is not defined
> <ipython-input-62-c52218c9a653>(1)<module>()
----> 1 h in s

ipdb> c                                                                                                                                          

In [63]: 'h' in s                                                                                                                                
Out[63]: False

In [64]: 'h' in s                                                                                                                                
Out[64]: False

In [65]: 'cde' in s                                                                                                                              
Out[65]: True

In [66]: s                                                                                                                                       
Out[66]: 'abcdefg'

In [67]: 'edc' in s                                                                                                                              
Out[67]: False

In [68]: for char in s: 
    ...:     print(char) 
    ...:                                                                                                                                         
a
b
c
d
e
f
g

In [69]: s                                                                                                                                       
Out[69]: 'abcdefg'

In [70]: s[0]                                                                                                                                    
Out[70]: 'a'

In [71]: s[1]                                                                                                                                    
Out[71]: 'b'

In [72]: s[-1]                                                                                                                                   
Out[72]: 'g'

In [73]: s[-0]                                                                                                                                   
Out[73]: 'a'

In [74]: s[-1]                                                                                                                                   
Out[74]: 'g'

In [75]: s[-2]                                                                                                                                   
Out[75]: 'f'

In [76]: s[-3]                                                                                                                                   
Out[76]: 'e'

In [77]: s[0:2]                                                                                                                                  
Out[77]: 'ab'

In [78]: s[0:4]                                                                                                                                  
Out[78]: 'abcd'

In [79]: s[4:5]                                                                                                                                  
Out[79]: 'e'

In [80]: s[:4]                                                                                                                                   
Out[80]: 'abcd'

In [81]: list(range(5))                                                                                                                          
Out[81]: [0, 1, 2, 3, 4]

In [82]: s[:4]                                                                                                                                   
Out[82]: 'abcd'

In [83]: a[0:7:2]                                                                                                                                
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-83-142e39716f8a> in <module>
----> 1 a[0:7:2]

TypeError: 'int' object is not subscriptable
> <ipython-input-83-142e39716f8a>(1)<module>()
----> 1 a[0:7:2]

ipdb> c                                                                                                                                          

In [84]: s[0:7:2]                                                                                                                                
Out[84]: 'aceg'

In [85]: s[0:7:3]                                                                                                                                
Out[85]: 'adg'

In [86]: s[0:7:4]                                                                                                                                
Out[86]: 'ae'

In [87]: s[::2]                                                                                                                                  
Out[87]: 'aceg'

In [88]: s[0:7:2]                                                                                                                                
Out[88]: 'aceg'

In [89]: s[::2]                                                                                                                                  
Out[89]: 'aceg'

In [90]: s[::-1]                                                                                                                                 
Out[90]: 'gfedcba'

In [91]: s[::-2]                                                                                                                                 
Out[91]: 'geca'

In [92]: s[0:7:2]                                                                                                                                
Out[92]: 'aceg'

In [93]: a = 1                                                                                                                                   

In [94]: a                                                                                                                                       
Out[94]: 1

In [95]: a = 1.0                                                                                                                                 

In [96]: a.real                                                                                                                                  
Out[96]: 1.0

In [97]: a.imag                                                                                                                                  
Out[97]: 0.0

In [98]: a                                                                                                                                       
Out[98]: 1.0

In [99]: a = 1.1                                                                                                                                 

In [100]: a.is_integer?                                                                                                                          
Docstring: Return True if the float is an integer.
Type:      builtin_function_or_method

In [101]: a.is_integer()                                                                                                                         
Out[101]: False

In [102]: is_integer                                                                                                                             
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-102-6377038d55ba> in <module>
----> 1 is_integer

NameError: name 'is_integer' is not defined
> <ipython-input-102-6377038d55ba>(1)<module>()
----> 1 is_integer

ipdb> c                                                                                                                                          

In [103]: print                                                                                                                                  
Out[103]: <function print>

In [104]: range                                                                                                                                  
Out[104]: range

In [105]: s                                                                                                                                      
Out[105]: 'abcdefg'

In [106]: s.count?                                                                                                                               
Docstring:
S.count(sub[, start[, end]]) -> int

Return the number of non-overlapping occurrences of substring sub in
string S[start:end].  Optional arguments start and end are
interpreted as in slice notation.
Type:      builtin_function_or_method

In [107]: s.count('w')                                                                                                                           
Out[107]: 0

In [108]: s.count('a')                                                                                                                           
Out[108]: 1

In [109]: s.count('abc')                                                                                                                         
Out[109]: 1

In [110]: s.count('abce')                                                                                                                        
Out[110]: 0

In [111]: s.index('c')                                                                                                                           
Out[111]: 2

In [112]: s.index?                                                                                                                               
Docstring:
S.index(sub[, start[, end]]) -> int

Return the lowest index in S where substring sub is found, 
such that sub is contained within S[start:end].  Optional
arguments start and end are interpreted as in slice notation.

Raises ValueError when the substring is not found.
Type:      builtin_function_or_method

In [113]: s.find?                                                                                                                                
Docstring:
S.find(sub[, start[, end]]) -> int

Return the lowest index in S where substring sub is found,
such that sub is contained within S[start:end].  Optional
arguments start and end are interpreted as in slice notation.

Return -1 on failure.
Type:      builtin_function_or_method

In [114]: s.index('w')                                                                                                                           
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-114-75c8d59625e8> in <module>
----> 1 s.index('w')

ValueError: substring not found
> <ipython-input-114-75c8d59625e8>(1)<module>()
----> 1 s.index('w')

ipdb> c                                                                                                                                          

In [115]: s.find('w')                                                                                                                            
Out[115]: -1

In [116]: s =                                                                                                                                    
  File "<ipython-input-116-063da17ce760>", line 1
    s =
        ^
SyntaxError: invalid syntax


In [117]: s = 'abcdefg'                                                                                                                          

In [118]: s += 'a'                                                                                                                               

In [119]: s                                                                                                                                      
Out[119]: 'abcdefga'

In [120]: s.index('a')                                                                                                                           
Out[120]: 0

In [121]: s.find('a')                                                                                                                            
Out[121]: 0

In [122]: s.split('c')                                                                                                                           
Out[122]: ['ab', 'defga']

In [123]: ','.join('abc', 'def')                                                                                                                 
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-123-977baac78e6a> in <module>
----> 1 ','.join('abc', 'def')

TypeError: join() takes exactly one argument (2 given)
> <ipython-input-123-977baac78e6a>(1)<module>()
----> 1 ','.join('abc', 'def')

ipdb> c                                                                                                                                          

In [124]: ','.join(('abc', 'def'))                                                                                                               
Out[124]: 'abc,def'

In [125]: s.split?                                                                                                                               
Docstring:
S.split(sep=None, maxsplit=-1) -> list of strings

Return a list of the words in S, using sep as the
delimiter string.  If maxsplit is given, at most maxsplit
splits are done. If sep is not specified or is None, any
whitespace string is a separator and empty strings are
removed from the result.
Type:      builtin_function_or_method

In [126]: s.replace?                                                                                                                             
Docstring:
S.replace(old, new[, count]) -> str

Return a copy of S with all occurrences of substring
old replaced by new.  If the optional argument count is
given, only the first count occurrences are replaced.
Type:      builtin_function_or_method

In [127]: s                                                                                                                                      
Out[127]: 'abcdefga'

In [128]: s.replace('a', 'w')                                                                                                                    
Out[128]: 'wbcdefgw'

In [129]: s                                                                                                                                      
Out[129]: 'abcdefga'

In [130]: s.replace('a', 'w')                                                                                                                    
Out[130]: 'wbcdefgw'

In [131]: s.strip?                                                                                                                               
Docstring:
S.strip([chars]) -> str

Return a copy of the string S with leading and trailing
whitespace removed.
If chars is given and not None, remove characters in chars instead.
Type:      builtin_function_or_method

In [132]: s                                                                                                                                      
Out[132]: 'abcdefga'

In [133]: s.strip('a')                                                                                                                           
Out[133]: 'bcdefg'

In [134]: s.lstrip('a')                                                                                                                          
Out[134]: 'bcdefga'

In [135]: s.rstrip('a')                                                                                                                          
Out[135]: 'abcdefg'

In [136]: s                                                                                                                                      
Out[136]: 'abcdefga'

In [137]: s[0:6]                                                                                                                                 
Out[137]: 'abcdef'

In [138]: s                                                                                                                                      
Out[138]: 'abcdefga'

In [139]: len(s)                                                                                                                                 
Out[139]: 8

In [140]: s[0:-2]                                                                                                                                
Out[140]: 'abcdef'

In [141]: s.upper()                                                                                                                              
Out[141]: 'ABCDEFGA'

In [142]: s.lower()                                                                                                                              
Out[142]: 'abcdefga'

In [143]: s.upper()                                                                                                                              
Out[143]: 'ABCDEFGA'

In [144]: s.upper().lower()                                                                                                                      
Out[144]: 'abcdefga'

In [145]: s.replace?                                                                                                                                                                    
Docstring:
S.replace(old, new[, count]) -> str

Return a copy of S with all occurrences of substring
old replaced by new.  If the optional argument count is
given, only the first count occurrences are replaced.
Type:      builtin_function_or_method

In [146]: s                                                                                                                                                                             
Out[146]: 'abcdefga'

In [147]: s = 'abcdefghijklmnopqrstuvwxyz'                                                                                                                                              

In [148]: s                                                                                                                                                                             
Out[148]: 'abcdefghijklmnopqrstuvwxyz'

In [149]: for i in s[::-1]: 
     ...:     print(i) 
     ...:                                                                                                                                                                               
z
y
x
w
v
u
t
s
r
q
p
o
n
m
l
k
j
i
h
g
f
e
d
c
b
a

In [150]: s[::-1]                                                                                                                                                                       
Out[150]: 'zyxwvutsrqponmlkjihgfedcba'

In [151]: for i in range(len(s), 0, -1) 
     ...:     print(s[i]) 
     ...:  
     ...:                                                                                                                                                                               
  File "<ipython-input-151-d5acfe4ab30c>", line 1
    for i in range(len(s), 0, -1)
                                 ^
SyntaxError: invalid syntax


In [152]: for i in range(len(s), 0, -1): 
     ...:     print(s[i]) 
     ...:      
     ...:  
     ...:                                                                                                                                                                               
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-152-66474481459c> in <module>
      1 for i in range(len(s), 0, -1):
----> 2     print(s[i])
      3 
      4 
      5 

IndexError: string index out of range
> <ipython-input-152-66474481459c>(2)<module>()
      1 for i in range(len(s), 0, -1):
----> 2     print(s[i])
      3 
      4 
      5 

ipdb> c                                                                                                                                                                                 

In [153]: for i in range(len(s)-1, 0, -1): 
     ...:     print(s[i]) 
     ...:      
     ...:  
     ...:                                                                                                                                                                               
z
y
x
w
v
u
t
s
r
q
p
o
n
m
l
k
j
i
h
g
f
e
d
c
b

In [154]: for i in range(len(s)-1, -1, -1): 
     ...:     print(s[i]) 
     ...:      
     ...:      
     ...:  
     ...:                                                                                                                                                                               
z
y
x
w
v
u
t
s
r
q
p
o
n
m
l
k
j
i
h
g
f
e
d
c
b
a

In [155]: s[::-1]                                                                                                                                                                       
Out[155]: 'zyxwvutsrqponmlkjihgfedcba'

In [156]: s                                                                                                                                                                             
Out[156]: 'abcdefghijklmnopqrstuvwxyz'

In [157]: s[::2]                                                                                                                                                                        
Out[157]: 'acegikmoqsuwy'

In [158]: s2 = s[::2]                                                                                                                                                                   

In [159]: s2                                                                                                                                                                            
Out[159]: 'acegikmoqsuwy'

In [160]: s2                                                                                                                                                                            
Out[160]: 'acegikmoqsuwy'

In [161]: s2.replace('a', '4').replace('e', '3').replace('i', '1')                                                                                                                      
Out[161]: '4c3g1kmoqsuwy'

In [162]: s3 = ''                                                                                                                                                                       

In [163]: s3 = s2.replace('a', '4')                                                                                                                                                     

In [164]: s3                                                                                                                                                                            
Out[164]: '4cegikmoqsuwy'

In [165]: s3.replace('e', '3')                                                                                                                                                          
Out[165]: '4c3gikmoqsuwy'

In [166]: def add(x, y): 
     ...:     """Return sum of x and y""" 
     ...:     result = x + y 
     ...:     return result 
     ...:                                                                                                                                                                               

In [167]: add?                                                                                                                                                                          
Signature: add(x, y)
Docstring: Return sum of x and y
File:      ~/SciPyCourse2019/notes/02_Python_basics_2/<ipython-input-166-e36ec8ebf313>
Type:      function

In [168]: add(5, 3)                                                                                                                                                                     
Out[168]: 8

In [169]: add(3, 5)                                                                                                                                                                     
Out[169]: 8

In [170]: def add(x, y): 
     ...:     """Return sum of x and y""" 
     ...:     result = x + y + 2 
     ...:     return result 
     ...:                                                                                                                                                                               

In [171]:                                                                                                                                                                               

In [171]: add(3, 5)                                                                                                                                                                     
Out[171]: 10

In [172]: def add(x, y): 
     ...:     """Return sum of x and y""" 
     ...:     result = x + y 
     ...:     return result 
     ...:                                                                                                                                                                               

In [173]:                                                                                                                                                                               

In [173]: add(3, 5)                                                                                                                                                                     
Out[173]: 8

In [174]: print                                                                                                                                                                         
Out[174]: <function print>

In [175]: def print(x): 
     ...:     result = x**2 
     ...:     return result 
     ...:                                                                                                                                                                               

In [176]: print(4)                                                                                                                                                                      
Out[176]: 16

In [177]: print('sdfsdf')                                                                                                                                                               
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-177-295b26a8666c> in <module>
----> 1 print('sdfsdf')

<ipython-input-175-37438d5ef179> in print(x)
      1 def print(x):
----> 2     result = x**2
      3     return result
      4 

TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
> <ipython-input-175-37438d5ef179>(2)print()
      1 def print(x):
----> 2     result = x**2
      3     return result
      4 

ipdb> c                                                                                                                                                                                 

In [178]: whos                                                                                                                                                                          
Variable   Type        Data/Info
--------------------------------
a          float       1.1
add        function    <function add at 0x7f2634dedf28>
char       str         g
i          int         0
np         module      <module 'numpy' from '/us<...>kages/numpy/__init__.py'>
pi         float       3.14159
plt        module      <module 'matplotlib.pyplo<...>es/matplotlib/pyplot.py'>
print      function    <function print at 0x7f2644050e18>
s          str         abcdefghijklmnopqrstuvwxyz
s2         str         acegikmoqsuwy
s3         str         4cegikmoqsuwy
value      str         world

In [179]: del print                                                                                                                                                                     

In [180]: whos                                                                                                                                                                          
Variable   Type        Data/Info
--------------------------------
a          float       1.1
add        function    <function add at 0x7f2634dedf28>
char       str         g
i          int         0
np         module      <module 'numpy' from '/us<...>kages/numpy/__init__.py'>
pi         float       3.14159
plt        module      <module 'matplotlib.pyplo<...>es/matplotlib/pyplot.py'>
s          str         abcdefghijklmnopqrstuvwxyz
s2         str         acegikmoqsuwy
s3         str         4cegikmoqsuwy
value      str         world

In [181]: print('sdfsdfdsf')                                                                                                                                                            
sdfsdfdsf

In [182]: sum                                                                                                                                                                           
Out[182]: <function sum(iterable, start=0, /)>

In [183]: sum?                                                                                                                                                                          
Signature: sum(iterable, start=0, /)
Docstring:
Return the sum of a 'start' value (default: 0) plus an iterable of numbers

When the iterable is empty, return the start value.
This function is intended specifically for use with numeric values and may
reject non-numeric types.
Type:      builtin_function_or_method

In [184]: sum = 2                                                                                                                                                                       

In [185]: sum([1,2,3,4])                                                                                                                                                                
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-185-b00a85a50b66> in <module>
----> 1 sum([1,2,3,4])

TypeError: 'int' object is not callable
> <ipython-input-185-b00a85a50b66>(1)<module>()
----> 1 sum([1,2,3,4])

ipdb> c                                                                                                                                                                                 

In [186]: del sum                                                                                                                                                                       

In [187]: sum                                                                                                                                                                           
Out[187]: <function sum(iterable, start=0, /)>

In [188]: sum?                                                                                                                                                                          
Signature: sum(iterable, start=0, /)
Docstring:
Return the sum of a 'start' value (default: 0) plus an iterable of numbers

When the iterable is empty, return the start value.
This function is intended specifically for use with numeric values and may
reject non-numeric types.
Type:      builtin_function_or_method

In [189]: def subtract(x, y): 
     ...:     """Subtracts y from x""" 
     ...:     result = x - y 
     ...:     return result 
     ...:                                                                                                                                                                               

In [190]: subtract?                                                                                                                                                                     
Signature: subtract(x, y)
Docstring: Subtracts y from x
File:      ~/SciPyCourse2019/notes/02_Python_basics_2/<ipython-input-189-47b4dae18dd7>
Type:      function

In [191]: subtract(10, 2)                                                                                                                                                               
Out[191]: 8

In [192]: subtract(2, 10)                                                                                                                                                               
Out[192]: -8

In [193]: def subtract(x, y): 
     ...:     """Subtracts y from x""" 
     ...:     return x - y 
     ...:      
     ...:                                                                                                                                                                               

In [194]: subtract(10, 2)                                                                                                                                                               
Out[194]: 8

In [195]: subtract(10)                                                                                                                                                                  
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-195-1167d058adaf> in <module>
----> 1 subtract(10)

TypeError: subtract() missing 1 required positional argument: 'y'
> <ipython-input-195-1167d058adaf>(1)<module>()
----> 1 subtract(10)

ipdb> c                                                                                                                                                                                 

In [196]: subtract(10, 10, 10)                                                                                                                                                          
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-196-4dc26a16687b> in <module>
----> 1 subtract(10, 10, 10)

TypeError: subtract() takes 2 positional arguments but 3 were given
> <ipython-input-196-4dc26a16687b>(1)<module>()
----> 1 subtract(10, 10, 10)

ipdb> c                                                                                                                                                                                 

In [197]: def add3(x, y, z=0): 
     ...:     """Add two numbers x and y, and optionally z""" 
     ...:     return x + y + z 
     ...:                                                                                                                                                                               

In [198]: add3(1, 2)                                                                                                                                                                    
Out[198]: 3

In [199]: add3(1, 2, 3)                                                                                                                                                                 
Out[199]: 6

In [200]: add3(1, 2, 3, 4)                                                                                                                                                              
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-200-e1052c2c96ab> in <module>
----> 1 add3(1, 2, 3, 4)

TypeError: add3() takes from 2 to 3 positional arguments but 4 were given
> <ipython-input-200-e1052c2c96ab>(1)<module>()
----> 1 add3(1, 2, 3, 4)

ipdb> c                                                                                                                                                                                 

In [201]: add3(1)                                                                                                                                                                       
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-201-fff0ed3d5c68> in <module>
----> 1 add3(1)

TypeError: add3() missing 1 required positional argument: 'y'
> <ipython-input-201-fff0ed3d5c68>(1)<module>()
----> 1 add3(1)

ipdb> c                                                                                                                                                                                 

In [202]: add?                                                                                                                                                                          
Signature: add(x, y)
Docstring: Return sum of x and y
File:      ~/SciPyCourse2019/notes/02_Python_basics_2/<ipython-input-172-e36ec8ebf313>
Type:      function

In [203]: add3?                                                                                                                                                                         
Signature: add3(x, y, z=0)
Docstring: Add two numbers x and y, and optionally z
File:      ~/SciPyCourse2019/notes/02_Python_basics_2/<ipython-input-197-216e99f8bbe6>
Type:      function

In [204]: def addsubtract(x, y): 
     ...:     """Return sum and difference of x and y""" 
     ...:     s = x + y 
     ...:     d = x - y 
     ...:     return s, d 
     ...:                                                                                                                                                                               

In [205]: addsubtract?                                                                                                                                                                  
Signature: addsubtract(x, y)
Docstring: Return sum and difference of x and y
File:      ~/SciPyCourse2019/notes/02_Python_basics_2/<ipython-input-204-2c510ad8d209>
Type:      function

In [206]: addsubtract(2, 3)                                                                                                                                                             
Out[206]: (5, -1)

In [207]: result = addsubtract(2, 3)                                                                                                                                                    

In [208]: type(result)                                                                                                                                                                  
Out[208]: tuple

In [209]: a, b = addsubtract(2, 3)                                                                                                                                                      

In [210]: a                                                                                                                                                                             
Out[210]: 5

In [211]: b                                                                                                                                                                             
Out[211]: -1

In [212]: d                                                                                                                                                                             
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-212-e983f374794d> in <module>
----> 1 d

NameError: name 'd' is not defined
> <ipython-input-212-e983f374794d>(1)<module>()
----> 1 d

ipdb> c                                                                                                                                                                                 

In [213]:                                                                                                                                                                               
