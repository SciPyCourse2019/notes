mspacek@Godel:~$ cd SciPyCourse2019/notes/09_pandas/
mspacek@Godel:~/SciPyCourse2019/notes/09_pandas$ ipython
Python 3.6.8 (default, Jan 14 2019, 11:02:34)
Type 'copyright', 'credits' or 'license' for more information
IPython 7.4.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: np.array()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-1-e4f3b47dc252> in <module>
----> 1 np.array()

TypeError: Required argument 'object' (pos 1) not found
> <ipython-input-1-e4f3b47dc252>(1)<module>()
----> 1 np.array()

ipdb> c

In [2]: np.array([])
Out[2]: array([], dtype=float64)

In [3]: []
Out[3]: []

In [4]: ()
Out[4]: ()

In [5]: {}
Out[5]: {}

In [6]: import pandas as pd

In [7]: pd.Series
Out[7]: pandas.core.series.Series

In [8]: pd.DataFrame
Out[8]: pandas.core.frame.DataFrame

In [9]: fl = np.random.random(20)

In [10]: fl
Out[10]:
array([0.86252955, 0.16757813, 0.22726017, 0.24952105, 0.12523088,
       0.69809883, 0.17886111, 0.32194767, 0.41603503, 0.87643397,
       0.21532235, 0.81808888, 0.44872634, 0.85447514, 0.09316861,
       0.89096388, 0.93672722, 0.16888308, 0.73198359, 0.61163595])

In [11]: t = np.arange(0, 400, 20)

In [12]: t
Out[12]:
array([  0,  20,  40,  60,  80, 100, 120, 140, 160, 180, 200, 220, 240,
       260, 280, 300, 320, 340, 360, 380])

In [13]: fl.shape
Out[13]: (20,)

In [14]: t.shape
Out[14]: (20,)

In [15]: fl[:5]
Out[15]: array([0.86252955, 0.16757813, 0.22726017, 0.24952105, 0.12523088])

In [16]: t[:5]
Out[16]: array([ 0, 20, 40, 60, 80])

In [17]: np.where(t == 60)
Out[17]: (array([3]),)

In [18]: np.where(t == 60)[0]
Out[18]: array([3])

In [19]: fl[np.where(t == 60)[0]]
Out[19]: array([0.24952105])

In [20]: s = pd.Series(data=fl, index=t)

In [21]: s
Out[21]:
0      0.862530
20     0.167578
40     0.227260
60     0.249521
80     0.125231
100    0.698099
120    0.178861
140    0.321948
160    0.416035
180    0.876434
200    0.215322
220    0.818089
240    0.448726
260    0.854475
280    0.093169
300    0.890964
320    0.936727
340    0.168883
360    0.731984
380    0.611636
dtype: float64

In [22]: s.iloc[4]
Out[22]: 0.1252308755943432

In [23]: s.iloc[3]
Out[23]: 0.24952104656855656

In [24]: fl[3]
Out[24]: 0.24952104656855656

In [25]: s.iloc[:5]
Out[25]:
0     0.862530
20    0.167578
40    0.227260
60    0.249521
80    0.125231
dtype: float64

In [26]: type(s)
Out[26]: pandas.core.series.Series

In [27]: s.iloc[3]
Out[27]: 0.24952104656855656

In [28]: type(s.iloc[3])
Out[28]: numpy.float64

In [29]: s.iloc[:5]
Out[29]:
0     0.862530
20    0.167578
40    0.227260
60    0.249521
80    0.125231
dtype: float64

In [30]: type(s.iloc[:5])
Out[30]: pandas.core.series.Series

In [31]: np.hstack([t, fl])
Out[31]:
array([0.00000000e+00, 2.00000000e+01, 4.00000000e+01, 6.00000000e+01,
       8.00000000e+01, 1.00000000e+02, 1.20000000e+02, 1.40000000e+02,
       1.60000000e+02, 1.80000000e+02, 2.00000000e+02, 2.20000000e+02,
       2.40000000e+02, 2.60000000e+02, 2.80000000e+02, 3.00000000e+02,
       3.20000000e+02, 3.40000000e+02, 3.60000000e+02, 3.80000000e+02,
       8.62529550e-01, 1.67578132e-01, 2.27260169e-01, 2.49521047e-01,
       1.25230876e-01, 6.98098826e-01, 1.78861108e-01, 3.21947667e-01,
       4.16035029e-01, 8.76433967e-01, 2.15322348e-01, 8.18088879e-01,
       4.48726337e-01, 8.54475143e-01, 9.31686053e-02, 8.90963876e-01,
       9.36727220e-01, 1.68883085e-01, 7.31983588e-01, 6.11635951e-01])

In [32]: np.vstack([t, fl])
Out[32]:
array([[0.00000000e+00, 2.00000000e+01, 4.00000000e+01, 6.00000000e+01,
        8.00000000e+01, 1.00000000e+02, 1.20000000e+02, 1.40000000e+02,
        1.60000000e+02, 1.80000000e+02, 2.00000000e+02, 2.20000000e+02,
        2.40000000e+02, 2.60000000e+02, 2.80000000e+02, 3.00000000e+02,
        3.20000000e+02, 3.40000000e+02, 3.60000000e+02, 3.80000000e+02],
       [8.62529550e-01, 1.67578132e-01, 2.27260169e-01, 2.49521047e-01,
        1.25230876e-01, 6.98098826e-01, 1.78861108e-01, 3.21947667e-01,
        4.16035029e-01, 8.76433967e-01, 2.15322348e-01, 8.18088879e-01,
        4.48726337e-01, 8.54475143e-01, 9.31686053e-02, 8.90963876e-01,
        9.36727220e-01, 1.68883085e-01, 7.31983588e-01, 6.11635951e-01]])

In [33]: np.vstack([t, fl]).shape
Out[33]: (2, 20)

In [34]: np.column_stack([t, fl])
Out[34]:
array([[0.00000000e+00, 8.62529550e-01],
       [2.00000000e+01, 1.67578132e-01],
       [4.00000000e+01, 2.27260169e-01],
       [6.00000000e+01, 2.49521047e-01],
       [8.00000000e+01, 1.25230876e-01],
       [1.00000000e+02, 6.98098826e-01],
       [1.20000000e+02, 1.78861108e-01],
       [1.40000000e+02, 3.21947667e-01],
       [1.60000000e+02, 4.16035029e-01],
       [1.80000000e+02, 8.76433967e-01],
       [2.00000000e+02, 2.15322348e-01],
       [2.20000000e+02, 8.18088879e-01],
       [2.40000000e+02, 4.48726337e-01],
       [2.60000000e+02, 8.54475143e-01],
       [2.80000000e+02, 9.31686053e-02],
       [3.00000000e+02, 8.90963876e-01],
       [3.20000000e+02, 9.36727220e-01],
       [3.40000000e+02, 1.68883085e-01],
       [3.60000000e+02, 7.31983588e-01],
       [3.80000000e+02, 6.11635951e-01]])

In [35]: s
Out[35]:
0      0.862530
20     0.167578
40     0.227260
60     0.249521
80     0.125231
100    0.698099
120    0.178861
140    0.321948
160    0.416035
180    0.876434
200    0.215322
220    0.818089
240    0.448726
260    0.854475
280    0.093169
300    0.890964
320    0.936727
340    0.168883
360    0.731984
380    0.611636
dtype: float64

In [36]: s.loc[60]
Out[36]: 0.24952104656855656

In [37]: s[60]
Out[37]: 0.24952104656855656

In [38]: s[61]
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
<ipython-input-38-564a150b59f3> in <module>
----> 1 s[61]

/usr/local/lib/python3.6/dist-packages/pandas/core/series.py in __getitem__(self, key)
    866         key = com.apply_if_callable(key, self)
    867         try:
--> 868             result = self.index.get_value(self, key)
    869
    870             if not is_scalar(result):

/usr/local/lib/python3.6/dist-packages/pandas/core/indexes/base.py in get_value(self, series, key)
   4373         try:
   4374             return self._engine.get_value(s, k,
-> 4375                                           tz=getattr(series.dtype, 'tz', None))
   4376         except KeyError as e1:
   4377             if len(self) > 0 and (self.holds_integer() or self.is_boolean()):

pandas/_libs/index.pyx in pandas._libs.index.IndexEngine.get_value()

pandas/_libs/index.pyx in pandas._libs.index.IndexEngine.get_value()

pandas/_libs/index.pyx in pandas._libs.index.IndexEngine.get_loc()

pandas/_libs/hashtable_class_helper.pxi in pandas._libs.hashtable.Int64HashTable.get_item()

pandas/_libs/hashtable_class_helper.pxi in pandas._libs.hashtable.Int64HashTable.get_item()

KeyError: 61
> /home/mspacek/SciPyCourse2019/notes/09_pandas/pandas/_libs/hashtable_class_helper.pxi(993)pandas._libs.hashtable.Int64HashTable.get_item()

ipdb> c

In [39]: s
Out[39]:
0      0.862530
20     0.167578
40     0.227260
60     0.249521
80     0.125231
100    0.698099
120    0.178861
140    0.321948
160    0.416035
180    0.876434
200    0.215322
220    0.818089
240    0.448726
260    0.854475
280    0.093169
300    0.890964
320    0.936727
340    0.168883
360    0.731984
380    0.611636
dtype: float64

In [40]: s.head()
Out[40]:
0     0.862530
20    0.167578
40    0.227260
60    0.249521
80    0.125231
dtype: float64

In [41]: s.tail()
Out[41]:
300    0.890964
320    0.936727
340    0.168883
360    0.731984
380    0.611636
dtype: float64

In [42]: s.head(3)
Out[42]:
0     0.862530
20    0.167578
40    0.227260
dtype: float64

In [43]: s.tail(3)
Out[43]:
340    0.168883
360    0.731984
380    0.611636
dtype: float64

In [44]: s.iloc[:5]
Out[44]:
0     0.862530
20    0.167578
40    0.227260
60    0.249521
80    0.125231
dtype: float64

In [45]: s.iloc[-5:]
Out[45]:
300    0.890964
320    0.936727
340    0.168883
360    0.731984
380    0.611636
dtype: float64

In [46]: s.iloc[3:7]
Out[46]:
60     0.249521
80     0.125231
100    0.698099
120    0.178861
dtype: float64

In [47]: s
Out[47]:
0      0.862530
20     0.167578
40     0.227260
60     0.249521
80     0.125231
100    0.698099
120    0.178861
140    0.321948
160    0.416035
180    0.876434
200    0.215322
220    0.818089
240    0.448726
260    0.854475
280    0.093169
300    0.890964
320    0.936727
340    0.168883
360    0.731984
380    0.611636
dtype: float64

In [48]: s.loc[60]
Out[48]: 0.24952104656855656

In [49]: s.loc[30:70]
Out[49]:
40    0.227260
60    0.249521
dtype: float64

In [50]: s.loc[40:60]
Out[50]:
40    0.227260
60    0.249521
dtype: float64

In [51]: s.iloc[2:3]
Out[51]:
40    0.22726
dtype: float64

In [52]: s.iloc[2:4]
Out[52]:
40    0.227260
60    0.249521
dtype: float64

In [53]: s.loc[40:60]
Out[53]:
40    0.227260
60    0.249521
dtype: float64

In [54]: s[60]
Out[54]: 0.24952104656855656

In [55]: s.loc[40:60]
Out[55]:
40    0.227260
60    0.249521
dtype: float64

In [56]: s
Out[56]:
0      0.862530
20     0.167578
40     0.227260
60     0.249521
80     0.125231
100    0.698099
120    0.178861
140    0.321948
160    0.416035
180    0.876434
200    0.215322
220    0.818089
240    0.448726
260    0.854475
280    0.093169
300    0.890964
320    0.936727
340    0.168883
360    0.731984
380    0.611636
dtype: float64

In [57]: s2 = pd.Series(data=t, index=fl)

In [58]: s2
Out[58]:
0.862530      0
0.167578     20
0.227260     40
0.249521     60
0.125231     80
0.698099    100
0.178861    120
0.321948    140
0.416035    160
0.876434    180
0.215322    200
0.818089    220
0.448726    240
0.854475    260
0.093169    280
0.890964    300
0.936727    320
0.168883    340
0.731984    360
0.611636    380
dtype: int64

In [59]: s2[0.862530]
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
/usr/local/lib/python3.6/dist-packages/pandas/core/indexes/base.py in get_loc(self, key, method, tolerance)
   2656             try:
-> 2657                 return self._engine.get_loc(key)
   2658             except KeyError:

pandas/_libs/index.pyx in pandas._libs.index.IndexEngine.get_loc()

pandas/_libs/index.pyx in pandas._libs.index.IndexEngine.get_loc()

pandas/_libs/hashtable_class_helper.pxi in pandas._libs.hashtable.Float64HashTable.get_item()

pandas/_libs/hashtable_class_helper.pxi in pandas._libs.hashtable.Float64HashTable.get_item()

KeyError: 0.86253

During handling of the above exception, another exception occurred:

KeyError                                  Traceback (most recent call last)
<ipython-input-59-a8f7f7e550b8> in <module>
----> 1 s2[0.862530]

/usr/local/lib/python3.6/dist-packages/pandas/core/series.py in __getitem__(self, key)
    866         key = com.apply_if_callable(key, self)
    867         try:
--> 868             result = self.index.get_value(self, key)
    869
    870             if not is_scalar(result):

/usr/local/lib/python3.6/dist-packages/pandas/core/indexes/numeric.py in get_value(self, series, key)
    373
    374         k = com.values_from_object(key)
--> 375         loc = self.get_loc(k)
    376         new_values = com.values_from_object(series)[loc]
    377

/usr/local/lib/python3.6/dist-packages/pandas/core/indexes/numeric.py in get_loc(self, key, method, tolerance)
    434             pass
    435         return super(Float64Index, self).get_loc(key, method=method,
--> 436                                                  tolerance=tolerance)
    437
    438     @cache_readonly

/usr/local/lib/python3.6/dist-packages/pandas/core/indexes/base.py in get_loc(self, key, method, tolerance)
   2657                 return self._engine.get_loc(key)
   2658             except KeyError:
-> 2659                 return self._engine.get_loc(self._maybe_cast_indexer(key))
   2660         indexer = self.get_indexer([key], method=method, tolerance=tolerance)
   2661         if indexer.ndim > 1 or indexer.size > 1:

pandas/_libs/index.pyx in pandas._libs.index.IndexEngine.get_loc()

pandas/_libs/index.pyx in pandas._libs.index.IndexEngine.get_loc()

pandas/_libs/hashtable_class_helper.pxi in pandas._libs.hashtable.Float64HashTable.get_item()

pandas/_libs/hashtable_class_helper.pxi in pandas._libs.hashtable.Float64HashTable.get_item()

KeyError: 0.86253
> /home/mspacek/SciPyCourse2019/notes/09_pandas/pandas/_libs/hashtable_class_helper.pxi(388)pandas._libs.hashtable.Float64HashTable.get_item()

ipdb> c

In [60]: s2
Out[60]:
0.862530      0
0.167578     20
0.227260     40
0.249521     60
0.125231     80
0.698099    100
0.178861    120
0.321948    140
0.416035    160
0.876434    180
0.215322    200
0.818089    220
0.448726    240
0.854475    260
0.093169    280
0.890964    300
0.936727    320
0.168883    340
0.731984    360
0.611636    380
dtype: int64

In [61]: s
Out[61]:
0      0.862530
20     0.167578
40     0.227260
60     0.249521
80     0.125231
100    0.698099
120    0.178861
140    0.321948
160    0.416035
180    0.876434
200    0.215322
220    0.818089
240    0.448726
260    0.854475
280    0.093169
300    0.890964
320    0.936727
340    0.168883
360    0.731984
380    0.611636
dtype: float64

In [62]: tfloat = np.arange(0, 2, 0.1)

In [63]: tfloat
Out[63]:
array([0. , 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1. , 1.1, 1.2,
       1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9])

In [64]: sfloat = pd.Series(data=fl, index=tfloat)

In [65]: sfloat
Out[65]:
0.0    0.862530
0.1    0.167578
0.2    0.227260
0.3    0.249521
0.4    0.125231
0.5    0.698099
0.6    0.178861
0.7    0.321948
0.8    0.416035
0.9    0.876434
1.0    0.215322
1.1    0.818089
1.2    0.448726
1.3    0.854475
1.4    0.093169
1.5    0.890964
1.6    0.936727
1.7    0.168883
1.8    0.731984
1.9    0.611636
dtype: float64

In [66]: sfloat[0.0]
Out[66]: 0.8625295496472274

In [67]: sfloat[0.1]
Out[67]: 0.16757813226517615

In [68]: sfloat[0.2]
Out[68]: 0.22726016866116938

In [69]: sfloat[0.3]
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
/usr/local/lib/python3.6/dist-packages/pandas/core/indexes/base.py in get_loc(self, key, method, tolerance)
   2656             try:
-> 2657                 return self._engine.get_loc(key)
   2658             except KeyError:

pandas/_libs/index.pyx in pandas._libs.index.IndexEngine.get_loc()

pandas/_libs/index.pyx in pandas._libs.index.IndexEngine.get_loc()

pandas/_libs/hashtable_class_helper.pxi in pandas._libs.hashtable.Float64HashTable.get_item()

pandas/_libs/hashtable_class_helper.pxi in pandas._libs.hashtable.Float64HashTable.get_item()

KeyError: 0.3

During handling of the above exception, another exception occurred:

KeyError                                  Traceback (most recent call last)
<ipython-input-69-feb3d725fcf0> in <module>
----> 1 sfloat[0.3]

/usr/local/lib/python3.6/dist-packages/pandas/core/series.py in __getitem__(self, key)
    866         key = com.apply_if_callable(key, self)
    867         try:
--> 868             result = self.index.get_value(self, key)
    869
    870             if not is_scalar(result):

/usr/local/lib/python3.6/dist-packages/pandas/core/indexes/numeric.py in get_value(self, series, key)
    373
    374         k = com.values_from_object(key)
--> 375         loc = self.get_loc(k)
    376         new_values = com.values_from_object(series)[loc]
    377

/usr/local/lib/python3.6/dist-packages/pandas/core/indexes/numeric.py in get_loc(self, key, method, tolerance)
    434             pass
    435         return super(Float64Index, self).get_loc(key, method=method,
--> 436                                                  tolerance=tolerance)
    437
    438     @cache_readonly

/usr/local/lib/python3.6/dist-packages/pandas/core/indexes/base.py in get_loc(self, key, method, tolerance)
   2657                 return self._engine.get_loc(key)
   2658             except KeyError:
-> 2659                 return self._engine.get_loc(self._maybe_cast_indexer(key))
   2660         indexer = self.get_indexer([key], method=method, tolerance=tolerance)
   2661         if indexer.ndim > 1 or indexer.size > 1:

pandas/_libs/index.pyx in pandas._libs.index.IndexEngine.get_loc()

pandas/_libs/index.pyx in pandas._libs.index.IndexEngine.get_loc()

pandas/_libs/hashtable_class_helper.pxi in pandas._libs.hashtable.Float64HashTable.get_item()

pandas/_libs/hashtable_class_helper.pxi in pandas._libs.hashtable.Float64HashTable.get_item()

KeyError: 0.3
> /home/mspacek/SciPyCourse2019/notes/09_pandas/pandas/_libs/hashtable_class_helper.pxi(388)pandas._libs.hashtable.Float64HashTable.get_item()

ipdb> c

In [70]: s.index
Out[70]:
Int64Index([  0,  20,  40,  60,  80, 100, 120, 140, 160, 180, 200, 220, 240,
            260, 280, 300, 320, 340, 360, 380],
           dtype='int64')

In [71]: sfloat.index
Out[71]:
Float64Index([                0.0,                 0.1,                 0.2,
              0.30000000000000004,                 0.4,                 0.5,
               0.6000000000000001,  0.7000000000000001,                 0.8,
                              0.9,                 1.0,                 1.1,
               1.2000000000000002,                 1.3,  1.4000000000000001,
                              1.5,                 1.6,  1.7000000000000002,
                              1.8,  1.9000000000000001],
             dtype='float64')

In [72]: sfloat[0.30000000000000004]
Out[72]: 0.24952104656855656

In [73]: s
Out[73]:
0      0.862530
20     0.167578
40     0.227260
60     0.249521
80     0.125231
100    0.698099
120    0.178861
140    0.321948
160    0.416035
180    0.876434
200    0.215322
220    0.818089
240    0.448726
260    0.854475
280    0.093169
300    0.890964
320    0.936727
340    0.168883
360    0.731984
380    0.611636
dtype: float64

In [74]: s - 5
Out[74]:
0     -4.137470
20    -4.832422
40    -4.772740
60    -4.750479
80    -4.874769
100   -4.301901
120   -4.821139
140   -4.678052
160   -4.583965
180   -4.123566
200   -4.784678
220   -4.181911
240   -4.551274
260   -4.145525
280   -4.906831
300   -4.109036
320   -4.063273
340   -4.831117
360   -4.268016
380   -4.388364
dtype: float64

In [75]: s > 0.5
Out[75]:
0       True
20     False
40     False
60     False
80     False
100     True
120    False
140    False
160    False
180     True
200    False
220     True
240    False
260     True
280    False
300     True
320     True
340    False
360     True
380     True
dtype: bool

In [76]: (s > 0.5).index
Out[76]:
Int64Index([  0,  20,  40,  60,  80, 100, 120, 140, 160, 180, 200, 220, 240,
            260, 280, 300, 320, 340, 360, 380],
           dtype='int64')

In [77]: np.where(s > 0.5)
Out[77]: (array([ 0,  5,  9, 11, 13, 15, 16, 18, 19]),)

In [78]: s > 0.5
Out[78]:
0       True
20     False
40     False
60     False
80     False
100     True
120    False
140    False
160    False
180     True
200    False
220     True
240    False
260     True
280    False
300     True
320     True
340    False
360     True
380     True
dtype: bool

In [79]: s > 0.5
Out[79]:
0       True
20     False
40     False
60     False
80     False
100     True
120    False
140    False
160    False
180     True
200    False
220     True
240    False
260     True
280    False
300     True
320     True
340    False
360     True
380     True
dtype: bool

In [80]: s
Out[80]:
0      0.862530
20     0.167578
40     0.227260
60     0.249521
80     0.125231
100    0.698099
120    0.178861
140    0.321948
160    0.416035
180    0.876434
200    0.215322
220    0.818089
240    0.448726
260    0.854475
280    0.093169
300    0.890964
320    0.936727
340    0.168883
360    0.731984
380    0.611636
dtype: float64

In [81]: s.plot()
Out[81]: <matplotlib.axes._subplots.AxesSubplot at 0x7fd2932cb400>

In [82]: ax = s.plot()

In [83]: ax.set_xlabel('Time (ms)')
Out[83]: Text(0.5, 13.94444444444443, 'Time (ms)')

In [84]: ax = s.plot()

In [85]: ax = s.plot()

In [86]: ax = s.plot()

In [87]: f, ax = plt.subplots()

In [88]: s.plot?

In [89]: s.plot(ax=ax)
Out[89]: <matplotlib.axes._subplots.AxesSubplot at 0x7fd2563f4d30>

In [90]: s.plot.hist()
Out[90]: <matplotlib.axes._subplots.AxesSubplot at 0x7fd2561a42e8>

In [91]: s.plot.bar()
Out[91]: <matplotlib.axes._subplots.AxesSubplot at 0x7fd2b7871908>

In [92]: s.plot.area()
Out[92]: <matplotlib.axes._subplots.AxesSubplot at 0x7fd2561a4898>

In [93]: s.min()
Out[93]: 0.09316860534485494

In [94]: s
Out[94]:
0      0.862530
20     0.167578
40     0.227260
60     0.249521
80     0.125231
100    0.698099
120    0.178861
140    0.321948
160    0.416035
180    0.876434
200    0.215322
220    0.818089
240    0.448726
260    0.854475
280    0.093169
300    0.890964
320    0.936727
340    0.168883
360    0.731984
380    0.611636
dtype: float64

In [95]: s.min()
Out[95]: 0.09316860534485494

In [96]: s.max()
Out[96]: 0.93672722011468

In [97]: s.mean()
Out[97]: 0.4946735701178372

In [98]: s.median()
Out[98]: 0.4323806829615321

In [99]: s.std()
Out[99]: 0.31096521096887153

In [100]: s.describe()
Out[100]:
count    20.000000
mean      0.494674
std       0.310965
min       0.093169
25%       0.206207
50%       0.432381
75%       0.827185
max       0.936727
dtype: float64

In [101]: type(s.describe())
Out[101]: pandas.core.series.Series

In [102]: s.describe()
Out[102]:
count    20.000000
mean      0.494674
std       0.310965
min       0.093169
25%       0.206207
50%       0.432381
75%       0.827185
max       0.936727
dtype: float64

In [103]: pd.date_range('2017-06-01', periods=10, freq='D')
Out[103]:
DatetimeIndex(['2017-06-01', '2017-06-02', '2017-06-03', '2017-06-04',
               '2017-06-05', '2017-06-06', '2017-06-07', '2017-06-08',
               '2017-06-09', '2017-06-10'],
              dtype='datetime64[ns]', freq='D')

In [104]: dr = pd.date_range('2017-06-01', periods=10, freq='D')

In [105]: fl.shape
Out[105]: (20,)

In [106]: dr = pd.date_range('2017-06-01', periods=20, freq='D')

In [107]: sdate = pd.Series(data=fl, index=dr)

In [108]: sdate
Out[108]:
2017-06-01    0.862530
2017-06-02    0.167578
2017-06-03    0.227260
2017-06-04    0.249521
2017-06-05    0.125231
2017-06-06    0.698099
2017-06-07    0.178861
2017-06-08    0.321948
2017-06-09    0.416035
2017-06-10    0.876434
2017-06-11    0.215322
2017-06-12    0.818089
2017-06-13    0.448726
2017-06-14    0.854475
2017-06-15    0.093169
2017-06-16    0.890964
2017-06-17    0.936727
2017-06-18    0.168883
2017-06-19    0.731984
2017-06-20    0.611636
Freq: D, dtype: float64

In [109]: sdate['2017-06-10']
Out[109]: 0.8764339667075756

In [110]:

In [110]: t2 = np.array([ 50,  70,  40,  20,  10,  80,  90,  30,  0,  60])

In [111]: s2 = pd.Series(data=fl[:10], index=t2)

In [112]: s2
Out[112]:
50    0.862530
70    0.167578
40    0.227260
20    0.249521
10    0.125231
80    0.698099
90    0.178861
30    0.321948
0     0.416035
60    0.876434
dtype: float64

In [113]: s2[50:40]
Out[113]: Series([], dtype: float64)

In [114]: s2.loc[50:40]
Out[114]:
50    0.862530
70    0.167578
40    0.227260
dtype: float64

In [115]: s
Out[115]:
0      0.862530
20     0.167578
40     0.227260
60     0.249521
80     0.125231
100    0.698099
120    0.178861
140    0.321948
160    0.416035
180    0.876434
200    0.215322
220    0.818089
240    0.448726
260    0.854475
280    0.093169
300    0.890964
320    0.936727
340    0.168883
360    0.731984
380    0.611636
dtype: float64

In [116]: s[20:100]
Out[116]: Series([], dtype: float64)

In [117]: s[20]
Out[117]: 0.16757813226517615

In [118]: s[20:100]
Out[118]: Series([], dtype: float64)

In [119]: s.loc[20:100]
Out[119]:
20     0.167578
40     0.227260
60     0.249521
80     0.125231
100    0.698099
dtype: float64

In [120]: s2[50:40]
Out[120]: Series([], dtype: float64)

In [121]: s2.loc[50:40]
Out[121]:
50    0.862530
70    0.167578
40    0.227260
dtype: float64

In [122]: s2
Out[122]:
50    0.862530
70    0.167578
40    0.227260
20    0.249521
10    0.125231
80    0.698099
90    0.178861
30    0.321948
0     0.416035
60    0.876434
dtype: float64

In [123]: s2.loc[50:40]
Out[123]:
50    0.862530
70    0.167578
40    0.227260
dtype: float64

In [124]: s.loc[1]
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
/usr/local/lib/python3.6/dist-packages/pandas/core/indexes/base.py in get_loc(self, key, method, tolerance)
   2656             try:
-> 2657                 return self._engine.get_loc(key)
   2658             except KeyError:

pandas/_libs/index.pyx in pandas._libs.index.IndexEngine.get_loc()

pandas/_libs/index.pyx in pandas._libs.index.IndexEngine.get_loc()

pandas/_libs/hashtable_class_helper.pxi in pandas._libs.hashtable.Int64HashTable.get_item()

pandas/_libs/hashtable_class_helper.pxi in pandas._libs.hashtable.Int64HashTable.get_item()

KeyError: 1

During handling of the above exception, another exception occurred:

KeyError                                  Traceback (most recent call last)
<ipython-input-124-a7c868f8fb38> in <module>
----> 1 s.loc[1]

/usr/local/lib/python3.6/dist-packages/pandas/core/indexing.py in __getitem__(self, key)
   1498
   1499             maybe_callable = com.apply_if_callable(key, self.obj)
-> 1500             return self._getitem_axis(maybe_callable, axis=axis)
   1501
   1502     def _is_scalar_access(self, key):

/usr/local/lib/python3.6/dist-packages/pandas/core/indexing.py in _getitem_axis(self, key, axis)
   1911         # fall thru to straight lookup
   1912         self._validate_key(key, axis)
-> 1913         return self._get_label(key, axis=axis)
   1914
   1915

/usr/local/lib/python3.6/dist-packages/pandas/core/indexing.py in _get_label(self, label, axis)
    135             # but will fail when the index is not present
    136             # see GH5667
--> 137             return self.obj._xs(label, axis=axis)
    138         elif isinstance(label, tuple) and isinstance(label[axis], slice):
    139             raise IndexingError('no slices here, handle elsewhere')

/usr/local/lib/python3.6/dist-packages/pandas/core/generic.py in xs(self, key, axis, level, drop_level)
   3583                                                       drop_level=drop_level)
   3584         else:
-> 3585             loc = self.index.get_loc(key)
   3586
   3587             if isinstance(loc, np.ndarray):

/usr/local/lib/python3.6/dist-packages/pandas/core/indexes/base.py in get_loc(self, key, method, tolerance)
   2657                 return self._engine.get_loc(key)
   2658             except KeyError:
-> 2659                 return self._engine.get_loc(self._maybe_cast_indexer(key))
   2660         indexer = self.get_indexer([key], method=method, tolerance=tolerance)
   2661         if indexer.ndim > 1 or indexer.size > 1:

pandas/_libs/index.pyx in pandas._libs.index.IndexEngine.get_loc()

pandas/_libs/index.pyx in pandas._libs.index.IndexEngine.get_loc()

pandas/_libs/hashtable_class_helper.pxi in pandas._libs.hashtable.Int64HashTable.get_item()

pandas/_libs/hashtable_class_helper.pxi in pandas._libs.hashtable.Int64HashTable.get_item()

KeyError: 1
> /home/mspacek/SciPyCourse2019/notes/09_pandas/pandas/_libs/hashtable_class_helper.pxi(993)pandas._libs.hashtable.Int64HashTable.get_item()

ipdb> c

In [125]: s.iloc[1]
Out[125]: 0.16757813226517615

In [126]: s
Out[126]:
0      0.862530
20     0.167578
40     0.227260
60     0.249521
80     0.125231
100    0.698099
120    0.178861
140    0.321948
160    0.416035
180    0.876434
200    0.215322
220    0.818089
240    0.448726
260    0.854475
280    0.093169
300    0.890964
320    0.936727
340    0.168883
360    0.731984
380    0.611636
dtype: float64

In [127]: s2
Out[127]:
50    0.862530
70    0.167578
40    0.227260
20    0.249521
10    0.125231
80    0.698099
90    0.178861
30    0.321948
0     0.416035
60    0.876434
dtype: float64

In [128]: s.index
Out[128]:
Int64Index([  0,  20,  40,  60,  80, 100, 120, 140, 160, 180, 200, 220, 240,
            260, 280, 300, 320, 340, 360, 380],
           dtype='int64')

In [129]: s.index < 60
Out[129]:
array([ True,  True,  True, False, False, False, False, False, False,
       False, False, False, False, False, False, False, False, False,
       False, False])

In [130]: s.iloc[s.index < 60]
Out[130]:
0     0.862530
20    0.167578
40    0.227260
dtype: float64

In [131]: np.open
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-131-161b1983058c> in <module>
----> 1 np.open

AttributeError: module 'numpy' has no attribute 'open'
> <ipython-input-131-161b1983058c>(1)<module>()
----> 1 np.open

ipdb> c

In [132]: np.load?

In [133]: s
Out[133]:
0      0.862530
20     0.167578
40     0.227260
60     0.249521
80     0.125231
100    0.698099
120    0.178861
140    0.321948
160    0.416035
180    0.876434
200    0.215322
220    0.818089
240    0.448726
260    0.854475
280    0.093169
300    0.890964
320    0.936727
340    0.168883
360    0.731984
380    0.611636
dtype: float64

In [134]: s.index
Out[134]:
Int64Index([  0,  20,  40,  60,  80, 100, 120, 140, 160, 180, 200, 220, 240,
            260, 280, 300, 320, 340, 360, 380],
           dtype='int64')

In [135]: s.values
Out[135]:
array([0.86252955, 0.16757813, 0.22726017, 0.24952105, 0.12523088,
       0.69809883, 0.17886111, 0.32194767, 0.41603503, 0.87643397,
       0.21532235, 0.81808888, 0.44872634, 0.85447514, 0.09316861,
       0.89096388, 0.93672722, 0.16888308, 0.73198359, 0.61163595])

In [136]: ls
09_pandas.md   exp1.csv  exp.xlsx    t.npy
09_pandas.pdf  exp2.csv  Galton.csv  V.npy

In [137]: np.load('t.npy')
Out[137]:
array([0.  , 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1 ,
       0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2 , 0.21,
       0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3 , 0.31, 0.32,
       0.33, 0.34, 0.35, 0.36, 0.37, 0.38, 0.39, 0.4 , 0.41, 0.42, 0.43,
       0.44, 0.45, 0.46, 0.47, 0.48, 0.49, 0.5 , 0.51, 0.52, 0.53, 0.54,
       0.55, 0.56, 0.57, 0.58, 0.59, 0.6 , 0.61, 0.62, 0.63, 0.64, 0.65,
       0.66, 0.67, 0.68, 0.69, 0.7 , 0.71, 0.72, 0.73, 0.74, 0.75, 0.76,
       0.77, 0.78, 0.79, 0.8 , 0.81, 0.82, 0.83, 0.84, 0.85, 0.86, 0.87,
       0.88, 0.89, 0.9 , 0.91, 0.92, 0.93, 0.94, 0.95, 0.96, 0.97, 0.98,
       0.99])

In [138]: np.load('V.npy')
Out[138]:
array([8.24777758e+01, 6.02342590e+01, 3.08380753e+01, 8.64603373e+01,
       3.56536647e+00, 2.00348496e+01, 5.91368637e+01, 4.15162129e+01,
       5.06776828e+01, 1.00000000e+03, 7.54405999e+01, 6.86314204e+01,
       2.61417936e+01, 3.51484713e+01, 2.58092387e+01, 1.04773450e+01,
       1.32408917e+01, 3.18672503e+01, 5.94482817e+01, 2.66580904e+01,
       5.91594717e+01, 6.53570651e+00, 8.58836573e+00, 1.00000000e+03,
       1.00000000e+03, 8.38927097e+01, 2.21202156e+01, 4.25819646e+01,
       3.83306221e+01, 2.09746967e+01, 7.53824835e+01, 4.45993633e+01,
       2.80853871e+01, 4.17249415e+01, 1.00000000e+03, 7.02201328e+01,
       3.63630564e+01, 5.22943367e+01, 1.00000000e+03, 6.16236716e+01,
       3.81947390e+01, 4.38238019e+01, 6.11110182e+01, 5.44227315e+01,
       2.45454038e+01, 4.02545425e+01, 2.14279017e+01, 6.62861764e+01,
       2.82545726e+01, 1.68717858e+01, 7.61757221e+01, 9.97308451e+00,
       4.37940989e+01, 8.95652919e+01, 3.18723823e+00, 8.79707384e+01,
       4.75663828e+01, 5.34237421e+01, 7.42926799e+01, 1.82295787e+01,
       5.64432797e+01, 5.74893311e+01, 1.00000000e+03, 7.39651359e+01,
       2.21320752e+01, 1.00000000e+03, 1.09191910e+01, 2.26514960e+01,
       1.69261930e+01, 4.44302184e+00, 8.89804525e+01, 8.77941436e+01,
       1.32775860e+01, 8.02132297e+01, 4.58869800e+01, 1.54311492e+01,
       7.52881650e+01, 3.07195208e+01, 3.12770187e+01, 3.49414948e+01,
       8.72803186e+01, 4.22898083e+01, 6.60830128e+01, 7.20574664e+01,
       1.00000000e+03, 5.18257219e+00, 6.97242785e+01, 4.99391302e+01,
       7.90815702e+01, 7.60846665e+01, 2.80442394e+01, 1.00118143e+01,
       5.65604354e+01, 8.32990442e+01, 4.40094004e+01, 5.55926930e+01,
       7.09025454e+01, 2.90419840e+01, 3.45839593e+01, 7.90880387e-01])

In [139]: np.version.version
Out[139]: '1.16.2'

In [140]: s
Out[140]:
0      0.862530
20     0.167578
40     0.227260
60     0.249521
80     0.125231
100    0.698099
120    0.178861
140    0.321948
160    0.416035
180    0.876434
200    0.215322
220    0.818089
240    0.448726
260    0.854475
280    0.093169
300    0.890964
320    0.936727
340    0.168883
360    0.731984
380    0.611636
dtype: float64

In [141]: s > 0.5
Out[141]:
0       True
20     False
40     False
60     False
80     False
100     True
120    False
140    False
160    False
180     True
200    False
220     True
240    False
260     True
280    False
300     True
320     True
340    False
360     True
380     True
dtype: bool

In [142]: plt.show()

In [143]: s[s > 0.5]
Out[143]:
0      0.862530
100    0.698099
180    0.876434
220    0.818089
260    0.854475
300    0.890964
320    0.936727
360    0.731984
380    0.611636
dtype: float64

In [144]: s[s > 0.5].index
Out[144]: Int64Index([0, 100, 180, 220, 260, 300, 320, 360, 380], dtype='int64')

In [145]: s[s > 0.5].values
Out[145]:
array([0.86252955, 0.69809883, 0.87643397, 0.81808888, 0.85447514,
       0.89096388, 0.93672722, 0.73198359, 0.61163595])

In [146]: ax.get_figure?
Signature: ax.get_figure()
Docstring: Return the `.Figure` instance the artist belongs to.
File:      /usr/local/lib/python3.6/dist-packages/matplotlib/artist.py
Type:      method

In [147]: np.load?

In [148]: ls
09_pandas.md   exp1.csv  exp.xlsx    t.npy
09_pandas.pdf  exp2.csv  Galton.csv  V.npy

In [149]: t = np.load('t.npy')

In [150]: V = np.load('V.npy')

In [151]: t.shape
Out[151]: (100,)

In [152]: V.shape
Out[152]: (100,)

In [153]: vd = pd.Series(index=t, data=V)

In [154]: vd
Out[154]:
0.00      82.477776
0.01      60.234259
0.02      30.838075
0.03      86.460337
0.04       3.565366
0.05      20.034850
0.06      59.136864
0.07      41.516213
0.08      50.677683
0.09    1000.000000
0.10      75.440600
0.11      68.631420
0.12      26.141794
0.13      35.148471
0.14      25.809239
0.15      10.477345
0.16      13.240892
0.17      31.867250
0.18      59.448282
0.19      26.658090
0.20      59.159472
0.21       6.535707
0.22       8.588366
0.23    1000.000000
0.24    1000.000000
0.25      83.892710
0.26      22.120216
0.27      42.581965
0.28      38.330622
0.29      20.974697
           ...
0.70      88.980452
0.71      87.794144
0.72      13.277586
0.73      80.213230
0.74      45.886980
0.75      15.431149
0.76      75.288165
0.77      30.719521
0.78      31.277019
0.79      34.941495
0.80      87.280319
0.81      42.289808
0.82      66.083013
0.83      72.057466
0.84    1000.000000
0.85       5.182572
0.86      69.724278
0.87      49.939130
0.88      79.081570
0.89      76.084666
0.90      28.044239
0.91      10.011814
0.92      56.560435
0.93      83.299044
0.94      44.009400
0.95      55.592693
0.96      70.902545
0.97      29.041984
0.98      34.583959
0.99       0.790880
Length: 100, dtype: float64

In [155]: vd.plot()
Out[155]: <matplotlib.axes._subplots.AxesSubplot at 0x7fd2561a4898>

In [156]: vd.plot()
Out[156]: <matplotlib.axes._subplots.AxesSubplot at 0x7fd2b7f5cc18>

In [157]: ax = vd.plot()

In [158]: ax.set_xlabel('Time (s)')
Out[158]: Text(0.5, 13.94444444444443, 'Time (s)')

In [159]: ax.set_ylabel('Voltage (mV)')
Out[159]: Text(13.944444444444438, 0.5, 'Voltage (mV)')

In [160]: vd
Out[160]:
0.00      82.477776
0.01      60.234259
0.02      30.838075
0.03      86.460337
0.04       3.565366
0.05      20.034850
0.06      59.136864
0.07      41.516213
0.08      50.677683
0.09    1000.000000
0.10      75.440600
0.11      68.631420
0.12      26.141794
0.13      35.148471
0.14      25.809239
0.15      10.477345
0.16      13.240892
0.17      31.867250
0.18      59.448282
0.19      26.658090
0.20      59.159472
0.21       6.535707
0.22       8.588366
0.23    1000.000000
0.24    1000.000000
0.25      83.892710
0.26      22.120216
0.27      42.581965
0.28      38.330622
0.29      20.974697
           ...
0.70      88.980452
0.71      87.794144
0.72      13.277586
0.73      80.213230
0.74      45.886980
0.75      15.431149
0.76      75.288165
0.77      30.719521
0.78      31.277019
0.79      34.941495
0.80      87.280319
0.81      42.289808
0.82      66.083013
0.83      72.057466
0.84    1000.000000
0.85       5.182572
0.86      69.724278
0.87      49.939130
0.88      79.081570
0.89      76.084666
0.90      28.044239
0.91      10.011814
0.92      56.560435
0.93      83.299044
0.94      44.009400
0.95      55.592693
0.96      70.902545
0.97      29.041984
0.98      34.583959
0.99       0.790880
Length: 100, dtype: float64

In [161]: vd > 500
Out[161]:
0.00    False
0.01    False
0.02    False
0.03    False
0.04    False
0.05    False
0.06    False
0.07    False
0.08    False
0.09     True
0.10    False
0.11    False
0.12    False
0.13    False
0.14    False
0.15    False
0.16    False
0.17    False
0.18    False
0.19    False
0.20    False
0.21    False
0.22    False
0.23     True
0.24     True
0.25    False
0.26    False
0.27    False
0.28    False
0.29    False
        ...
0.70    False
0.71    False
0.72    False
0.73    False
0.74    False
0.75    False
0.76    False
0.77    False
0.78    False
0.79    False
0.80    False
0.81    False
0.82    False
0.83    False
0.84     True
0.85    False
0.86    False
0.87    False
0.88    False
0.89    False
0.90    False
0.91    False
0.92    False
0.93    False
0.94    False
0.95    False
0.96    False
0.97    False
0.98    False
0.99    False
Length: 100, dtype: bool

In [162]: vd[vd > 500]
Out[162]:
0.09    1000.0
0.23    1000.0
0.24    1000.0
0.34    1000.0
0.38    1000.0
0.62    1000.0
0.65    1000.0
0.84    1000.0
dtype: float64

In [163]: vd[vd > 500].shape
Out[163]: (8,)

In [164]: vd[vd > 500].plot(ls='', marker='.')
Out[164]: <matplotlib.axes._subplots.AxesSubplot at 0x7fd2b7742780>

In [165]: vd[vd > 500].plot(ls='', marker='.', ax=ax)
Out[165]: <matplotlib.axes._subplots.AxesSubplot at 0x7fd2b7742780>

In [166]: vd[vd > 500].plot(ls='', marker='.', ax=ax)
Out[166]: <matplotlib.axes._subplots.AxesSubplot at 0x7fd2b7742780>

In [167]: vd[vd > 500]
Out[167]:
0.09    1000.0
0.23    1000.0
0.24    1000.0
0.34    1000.0
0.38    1000.0
0.62    1000.0
0.65    1000.0
0.84    1000.0
dtype: float64

In [168]: vd[vd > 500].index
Out[168]: Float64Index([0.09, 0.23, 0.24, 0.34, 0.38, 0.62, 0.65, 0.84], dtype='float64')

In [169]: type(vd[vd > 500].index)
Out[169]: pandas.core.indexes.numeric.Float64Index

In [170]: vd[vd > 500].index.values
Out[170]: array([0.09, 0.23, 0.24, 0.34, 0.38, 0.62, 0.65, 0.84])

In [171]: np.array(vd[vd > 500].index)
Out[171]: array([0.09, 0.23, 0.24, 0.34, 0.38, 0.62, 0.65, 0.84])

In [172]: vd[vd > 500].index.values
Out[172]: array([0.09, 0.23, 0.24, 0.34, 0.38, 0.62, 0.65, 0.84])

In [173]: np.save('spike_times.npy', vd[vd > 500].index.values)

In [174]: ls
09_pandas.md   exp1.csv  exp.xlsx    spike_times.npy  V.npy
09_pandas.pdf  exp2.csv  Galton.csv  t.npy

In [175]: st = np.load('spike_times.npy')

In [176]: st
Out[176]: array([0.09, 0.23, 0.24, 0.34, 0.38, 0.62, 0.65, 0.84])

In [177]: ax
Out[177]: <matplotlib.axes._subplots.AxesSubplot at 0x7fd2b7742780>

In [178]: ax.get_figure()
Out[178]: <Figure size 700x700 with 1 Axes>

In [179]: ax.get_figure().savefig('spikes.png')

In [180]: ls
09_pandas.md   exp1.csv  exp.xlsx    spikes.png       t.npy
09_pandas.pdf  exp2.csv  Galton.csv  spike_times.npy  V.npy

In [181]: pd.DataFrame()
Out[181]:
Empty DataFrame
Columns: []
Index: []

In [182]: eeg = np.random.random((20, 3))

In [183]: eeg
Out[183]:
array([[0.82423931, 0.40363666, 0.46674127],
       [0.14769483, 0.90632707, 0.83361611],
       [0.07477041, 0.48375198, 0.27482012],
       [0.57136069, 0.23374492, 0.479321  ],
       [0.71168459, 0.79053294, 0.78892288],
       [0.45317456, 0.61274216, 0.80048966],
       [0.46117541, 0.09524395, 0.0919612 ],
       [0.5123662 , 0.3853213 , 0.13928247],
       [0.76131794, 0.42745912, 0.87733801],
       [0.29058143, 0.19880539, 0.45169392],
       [0.70237612, 0.31227693, 0.37146885],
       [0.56531864, 0.72786403, 0.82831618],
       [0.66432604, 0.82931662, 0.36255505],
       [0.83517306, 0.05810051, 0.62137585],
       [0.70226983, 0.61496093, 0.51276448],
       [0.09921954, 0.63027868, 0.00440784],
       [0.46106032, 0.07044372, 0.06140223],
       [0.65778765, 0.70283573, 0.2469024 ],
       [0.59832047, 0.08942819, 0.96771752],
       [0.76138772, 0.42296575, 0.04774289]])

In [184]: eeg.shape
Out[184]: (20, 3)

In [185]: t = np.arange(0, 20*50, 50)

In [186]: t
Out[186]:
array([  0,  50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600,
       650, 700, 750, 800, 850, 900, 950])

In [187]: t.shape
Out[187]: (20,)

In [188]: eeg.shape
Out[188]: (20, 3)

In [189]: chans = ['Fz', 'Cz', 'Pz']

In [190]: df = pd.DataFrame(index=t, data=eeg, columns=chans)

In [191]: df
Out[191]:
           Fz        Cz        Pz
0    0.824239  0.403637  0.466741
50   0.147695  0.906327  0.833616
100  0.074770  0.483752  0.274820
150  0.571361  0.233745  0.479321
200  0.711685  0.790533  0.788923
250  0.453175  0.612742  0.800490
300  0.461175  0.095244  0.091961
350  0.512366  0.385321  0.139282
400  0.761318  0.427459  0.877338
450  0.290581  0.198805  0.451694
500  0.702376  0.312277  0.371469
550  0.565319  0.727864  0.828316
600  0.664326  0.829317  0.362555
650  0.835173  0.058101  0.621376
700  0.702270  0.614961  0.512764
750  0.099220  0.630279  0.004408
800  0.461060  0.070444  0.061402
850  0.657788  0.702836  0.246902
900  0.598320  0.089428  0.967718
950  0.761388  0.422966  0.047743

In [192]: type(df)
Out[192]: pandas.core.frame.DataFrame

In [193]: df.iloc[0, 0]
Out[193]: 0.824239311058547

In [194]: df.iloc[-1, -1]
Out[194]: 0.04774289037487123

In [195]: df.head()
Out[195]:
           Fz        Cz        Pz
0    0.824239  0.403637  0.466741
50   0.147695  0.906327  0.833616
100  0.074770  0.483752  0.274820
150  0.571361  0.233745  0.479321
200  0.711685  0.790533  0.788923

In [196]: df[:5, :]
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-196-2c82effa7e2f> in <module>
----> 1 df[:5, :]

/usr/local/lib/python3.6/dist-packages/pandas/core/frame.py in __getitem__(self, key)
   2925             if self.columns.nlevels > 1:
   2926                 return self._getitem_multilevel(key)
-> 2927             indexer = self.columns.get_loc(key)
   2928             if is_integer(indexer):
   2929                 indexer = [indexer]

/usr/local/lib/python3.6/dist-packages/pandas/core/indexes/base.py in get_loc(self, key, method, tolerance)
   2655                                  'backfill or nearest lookups')
   2656             try:
-> 2657                 return self._engine.get_loc(key)
   2658             except KeyError:
   2659                 return self._engine.get_loc(self._maybe_cast_indexer(key))

pandas/_libs/index.pyx in pandas._libs.index.IndexEngine.get_loc()

pandas/_libs/index.pyx in pandas._libs.index.IndexEngine.get_loc()

TypeError: '(slice(None, 5, None), slice(None, None, None))' is an invalid key
> /home/mspacek/SciPyCourse2019/notes/09_pandas/pandas/_libs/index.pyx(110)pandas._libs.index.IndexEngine.get_loc()

ipdb> c

In [197]: df.iloc[:5, :]
Out[197]:
           Fz        Cz        Pz
0    0.824239  0.403637  0.466741
50   0.147695  0.906327  0.833616
100  0.074770  0.483752  0.274820
150  0.571361  0.233745  0.479321
200  0.711685  0.790533  0.788923

In [198]: df.iloc[:5]
Out[198]:
           Fz        Cz        Pz
0    0.824239  0.403637  0.466741
50   0.147695  0.906327  0.833616
100  0.074770  0.483752  0.274820
150  0.571361  0.233745  0.479321
200  0.711685  0.790533  0.788923

In [199]: df['Fz']
Out[199]:
0      0.824239
50     0.147695
100    0.074770
150    0.571361
200    0.711685
250    0.453175
300    0.461175
350    0.512366
400    0.761318
450    0.290581
500    0.702376
550    0.565319
600    0.664326
650    0.835173
700    0.702270
750    0.099220
800    0.461060
850    0.657788
900    0.598320
950    0.761388
Name: Fz, dtype: float64

In [200]: type(df['Fz'])
Out[200]: pandas.core.series.Series

In [201]: df.iloc
Out[201]: <pandas.core.indexing._iLocIndexer at 0x7fd2b6856ef8>

In [202]: df.loc[50]
Out[202]:
Fz    0.147695
Cz    0.906327
Pz    0.833616
Name: 50, dtype: float64

In [203]: df
Out[203]:
           Fz        Cz        Pz
0    0.824239  0.403637  0.466741
50   0.147695  0.906327  0.833616
100  0.074770  0.483752  0.274820
150  0.571361  0.233745  0.479321
200  0.711685  0.790533  0.788923
250  0.453175  0.612742  0.800490
300  0.461175  0.095244  0.091961
350  0.512366  0.385321  0.139282
400  0.761318  0.427459  0.877338
450  0.290581  0.198805  0.451694
500  0.702376  0.312277  0.371469
550  0.565319  0.727864  0.828316
600  0.664326  0.829317  0.362555
650  0.835173  0.058101  0.621376
700  0.702270  0.614961  0.512764
750  0.099220  0.630279  0.004408
800  0.461060  0.070444  0.061402
850  0.657788  0.702836  0.246902
900  0.598320  0.089428  0.967718
950  0.761388  0.422966  0.047743

In [204]: df.loc[50]
Out[204]:
Fz    0.147695
Cz    0.906327
Pz    0.833616
Name: 50, dtype: float64

In [205]: df.loc[50]['Fz']
Out[205]: 0.1476948333056941

In [206]: df.loc[50]['Pz']
Out[206]: 0.8336161106371227

In [207]: df.loc
Out[207]: <pandas.core.indexing._LocIndexer at 0x7fd2935c2bd8>

In [208]: df['Fz'][50]
Out[208]: 0.1476948333056941

In [209]: df.loc[50]['Pz']
Out[209]: 0.8336161106371227

In [210]: df['Fz'][50]
Out[210]: 0.1476948333056941

In [211]: df
Out[211]:
           Fz        Cz        Pz
0    0.824239  0.403637  0.466741
50   0.147695  0.906327  0.833616
100  0.074770  0.483752  0.274820
150  0.571361  0.233745  0.479321
200  0.711685  0.790533  0.788923
250  0.453175  0.612742  0.800490
300  0.461175  0.095244  0.091961
350  0.512366  0.385321  0.139282
400  0.761318  0.427459  0.877338
450  0.290581  0.198805  0.451694
500  0.702376  0.312277  0.371469
550  0.565319  0.727864  0.828316
600  0.664326  0.829317  0.362555
650  0.835173  0.058101  0.621376
700  0.702270  0.614961  0.512764
750  0.099220  0.630279  0.004408
800  0.461060  0.070444  0.061402
850  0.657788  0.702836  0.246902
900  0.598320  0.089428  0.967718
950  0.761388  0.422966  0.047743

In [212]: df.loc[50]['Fz']
Out[212]: 0.1476948333056941

In [213]: df['Fz'][50]
Out[213]: 0.1476948333056941

In [214]: df['Fz']
Out[214]:
0      0.824239
50     0.147695
100    0.074770
150    0.571361
200    0.711685
250    0.453175
300    0.461175
350    0.512366
400    0.761318
450    0.290581
500    0.702376
550    0.565319
600    0.664326
650    0.835173
700    0.702270
750    0.099220
800    0.461060
850    0.657788
900    0.598320
950    0.761388
Name: Fz, dtype: float64

In [215]: df['Fz']
Out[215]:
0      0.824239
50     0.147695
100    0.074770
150    0.571361
200    0.711685
250    0.453175
300    0.461175
350    0.512366
400    0.761318
450    0.290581
500    0.702376
550    0.565319
600    0.664326
650    0.835173
700    0.702270
750    0.099220
800    0.461060
850    0.657788
900    0.598320
950    0.761388
Name: Fz, dtype: float64

In [216]: df['Pz']
Out[216]:
0      0.466741
50     0.833616
100    0.274820
150    0.479321
200    0.788923
250    0.800490
300    0.091961
350    0.139282
400    0.877338
450    0.451694
500    0.371469
550    0.828316
600    0.362555
650    0.621376
700    0.512764
750    0.004408
800    0.061402
850    0.246902
900    0.967718
950    0.047743
Name: Pz, dtype: float64

In [217]: df.index
Out[217]:
Int64Index([  0,  50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600,
            650, 700, 750, 800, 850, 900, 950],
           dtype='int64')

In [218]: s
Out[218]:
0      0.862530
20     0.167578
40     0.227260
60     0.249521
80     0.125231
100    0.698099
120    0.178861
140    0.321948
160    0.416035
180    0.876434
200    0.215322
220    0.818089
240    0.448726
260    0.854475
280    0.093169
300    0.890964
320    0.936727
340    0.168883
360    0.731984
380    0.611636
dtype: float64

In [219]: ls
09_pandas.md  09_pandas.pdf  exp1.csv  exp2.csv  exp.xlsx  Galton.csv  spikes.png  spike_times.npy  t.npy  V.npy

In [220]: pd.read_csv?

In [221]: exp1 = pd.read_csv('exp1.csv')

In [222]: type(exp1)
Out[222]: pandas.core.frame.DataFrame

In [223]: exp1
Out[223]:
  subject  start_time  end_time stimulus outcome
0     A01         2.3       5.6        L    pass
1     A01         1.6       2.1        R    pass
2     A01         2.3       5.6        R    pass
3     A01         4.0      10.2        R    fail
4     A01         2.8       4.5        L    pass
5     A01         0.7       6.1        L    pass
6     A01         3.5      11.2        R    fail
7     A01         2.7       5.6        L    pass

In [224]: exp1['subject']
Out[224]:
0    A01
1    A01
2    A01
3    A01
4    A01
5    A01
6    A01
7    A01
Name: subject, dtype: object

In [225]: exp1['subject'][0]
Out[225]: 'A01'

In [226]: type(exp1['subject'][0])
Out[226]: str

In [227]: exp1['outcome']
Out[227]:
0    pass
1    pass
2    pass
3    fail
4    pass
5    pass
6    fail
7    pass
Name: outcome, dtype: object

In [228]: exp1
Out[228]:
  subject  start_time  end_time stimulus outcome
0     A01         2.3       5.6        L    pass
1     A01         1.6       2.1        R    pass
2     A01         2.3       5.6        R    pass
3     A01         4.0      10.2        R    fail
4     A01         2.8       4.5        L    pass
5     A01         0.7       6.1        L    pass
6     A01         3.5      11.2        R    fail
7     A01         2.7       5.6        L    pass

In [229]: exp1.plot?

In [230]:

In [230]: exp1.plot()
Out[230]: <matplotlib.axes._subplots.AxesSubplot at 0x7fd2b711ecf8>

In [231]: exp1.hist()
Out[231]:
array([[<matplotlib.axes._subplots.AxesSubplot object at 0x7fd2b70e9b00>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x7fd2b6e88780>]],
      dtype=object)

In [232]: exp1.plot.hist()
Out[232]: <matplotlib.axes._subplots.AxesSubplot at 0x7fd25e7e8a58>

In [233]: exp1.plot.bar()
Out[233]: <matplotlib.axes._subplots.AxesSubplot at 0x7fd25665e550>

In [234]: exp1.plot.bar?

In [235]: exp1.plot.hist?

In [236]: exp1.plot.hist(by='outcome')
Out[236]: <matplotlib.axes._subplots.AxesSubplot at 0x7fd2935d9668>

In [237]: exp2 = pd.load_csv('exp2.csv')
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-237-700f80a20063> in <module>
----> 1 exp2 = pd.load_csv('exp2.csv')

AttributeError: module 'pandas' has no attribute 'load_csv'
> <ipython-input-237-700f80a20063>(1)<module>()
----> 1 exp2 = pd.load_csv('exp2.csv')

ipdb> c

In [238]: exp2 = pd.read_csv('exp2.csv')

In [239]: exp2
Out[239]:
   subject  start_time  end_time stimulus outcome
0      A02         2.7       5.6        L    pass
1      A02         1.2       4.3        L    pass
2      A02         4.0      10.4        R    fail
3      A02         2.3       5.6        R    pass
4      A02         4.1      10.0        R    fail
5      A02         3.9      12.1        R    fail
6      A02         2.8       4.5        L    pass
7      A02         1.3       3.1        R    pass
8      A02         0.8       4.1        L    pass
9      A02         3.6      12.4        R    fail
10     A02         5.5      13.3        R    fail

In [240]: exp1
Out[240]:
  subject  start_time  end_time stimulus outcome
0     A01         2.3       5.6        L    pass
1     A01         1.6       2.1        R    pass
2     A01         2.3       5.6        R    pass
3     A01         4.0      10.2        R    fail
4     A01         2.8       4.5        L    pass
5     A01         0.7       6.1        L    pass
6     A01         3.5      11.2        R    fail
7     A01         2.7       5.6        L    pass

In [241]: exp2
Out[241]:
   subject  start_time  end_time stimulus outcome
0      A02         2.7       5.6        L    pass
1      A02         1.2       4.3        L    pass
2      A02         4.0      10.4        R    fail
3      A02         2.3       5.6        R    pass
4      A02         4.1      10.0        R    fail
5      A02         3.9      12.1        R    fail
6      A02         2.8       4.5        L    pass
7      A02         1.3       3.1        R    pass
8      A02         0.8       4.1        L    pass
9      A02         3.6      12.4        R    fail
10     A02         5.5      13.3        R    fail

In [242]: pd.concat
Out[242]: <function pandas.core.reshape.concat.concat(objs, axis=0, join='outer', join_axes=None, ignore_index=False, keys=None, levels=None, names=None, verify_integrity=False, sort=None, copy=True)>

In [243]: np.concatenate
Out[243]: <function numpy.concatenate>

In [244]: exps = pd.concat([exp1, exp2])

In [245]: exps
Out[245]:
   subject  start_time  end_time stimulus outcome
0      A01         2.3       5.6        L    pass
1      A01         1.6       2.1        R    pass
2      A01         2.3       5.6        R    pass
3      A01         4.0      10.2        R    fail
4      A01         2.8       4.5        L    pass
5      A01         0.7       6.1        L    pass
6      A01         3.5      11.2        R    fail
7      A01         2.7       5.6        L    pass
0      A02         2.7       5.6        L    pass
1      A02         1.2       4.3        L    pass
2      A02         4.0      10.4        R    fail
3      A02         2.3       5.6        R    pass
4      A02         4.1      10.0        R    fail
5      A02         3.9      12.1        R    fail
6      A02         2.8       4.5        L    pass
7      A02         1.3       3.1        R    pass
8      A02         0.8       4.1        L    pass
9      A02         3.6      12.4        R    fail
10     A02         5.5      13.3        R    fail

In [246]: exps.shape
Out[246]: (19, 5)

In [247]: exps.plot.scatter?

In [248]: exps.plot.scatter('start_time', 'end_time')
Out[248]: <matplotlib.axes._subplots.AxesSubplot at 0x7fd2b69916a0>

In [249]: ax = exps.plot.scatter('start_time', 'end_time')

In [250]: ax.set_xlabel('Start time (s)')
Out[250]: Text(0.5, 37.50000000000002, 'Start time (s)')

In [251]: exps.corr()
Out[251]:
            start_time  end_time
start_time    1.000000  0.841829
end_time      0.841829  1.000000

In [252]: exps
Out[252]:
   subject  start_time  end_time stimulus outcome
0      A01         2.3       5.6        L    pass
1      A01         1.6       2.1        R    pass
2      A01         2.3       5.6        R    pass
3      A01         4.0      10.2        R    fail
4      A01         2.8       4.5        L    pass
5      A01         0.7       6.1        L    pass
6      A01         3.5      11.2        R    fail
7      A01         2.7       5.6        L    pass
0      A02         2.7       5.6        L    pass
1      A02         1.2       4.3        L    pass
2      A02         4.0      10.4        R    fail
3      A02         2.3       5.6        R    pass
4      A02         4.1      10.0        R    fail
5      A02         3.9      12.1        R    fail
6      A02         2.8       4.5        L    pass
7      A02         1.3       3.1        R    pass
8      A02         0.8       4.1        L    pass
9      A02         3.6      12.4        R    fail
10     A02         5.5      13.3        R    fail

In [253]: exps.sort_values('start_time')
Out[253]:
   subject  start_time  end_time stimulus outcome
5      A01         0.7       6.1        L    pass
8      A02         0.8       4.1        L    pass
1      A02         1.2       4.3        L    pass
7      A02         1.3       3.1        R    pass
1      A01         1.6       2.1        R    pass
3      A02         2.3       5.6        R    pass
0      A01         2.3       5.6        L    pass
2      A01         2.3       5.6        R    pass
7      A01         2.7       5.6        L    pass
0      A02         2.7       5.6        L    pass
4      A01         2.8       4.5        L    pass
6      A02         2.8       4.5        L    pass
6      A01         3.5      11.2        R    fail
9      A02         3.6      12.4        R    fail
5      A02         3.9      12.1        R    fail
2      A02         4.0      10.4        R    fail
3      A01         4.0      10.2        R    fail
4      A02         4.1      10.0        R    fail
10     A02         5.5      13.3        R    fail

In [254]: exps.sort_values('outcome')
Out[254]:
   subject  start_time  end_time stimulus outcome
10     A02         5.5      13.3        R    fail
3      A01         4.0      10.2        R    fail
5      A02         3.9      12.1        R    fail
6      A01         3.5      11.2        R    fail
4      A02         4.1      10.0        R    fail
9      A02         3.6      12.4        R    fail
2      A02         4.0      10.4        R    fail
8      A02         0.8       4.1        L    pass
7      A02         1.3       3.1        R    pass
6      A02         2.8       4.5        L    pass
3      A02         2.3       5.6        R    pass
0      A01         2.3       5.6        L    pass
7      A01         2.7       5.6        L    pass
5      A01         0.7       6.1        L    pass
4      A01         2.8       4.5        L    pass
2      A01         2.3       5.6        R    pass
1      A01         1.6       2.1        R    pass
0      A02         2.7       5.6        L    pass
1      A02         1.2       4.3        L    pass

In [255]: ls
09_pandas.md  09_pandas.pdf  exp1.csv  exp2.csv  exp.xlsx  Galton.csv  spikes.png  spike_times.npy  t.npy  V.npy

In [256]: exp1 = pd.read_excel('exp.xlsx', sheet_name='exp1')

In [257]: exp2 = pd.read_excel('exp.xlsx', sheet_name='exp2')

In [258]: exp1
Out[258]:
  subject  start_time  end_time stimulus outcome
0     A01         2.3       5.6        L    pass
1     A01         1.6       2.1        R    pass
2     A01         2.3       5.6        R    pass
3     A01         4.0      10.2        R    fail
4     A01         2.8       4.5        L    pass
5     A01         0.7       6.1        L    pass
6     A01         3.5      11.2        R    fail
7     A01         2.7       5.6        L    pass

In [259]: pd.read_excel('exp.xlsx')
Out[259]:
  subject  start_time  end_time stimulus outcome
0     A01         2.3       5.6        L    pass
1     A01         1.6       2.1        R    pass
2     A01         2.3       5.6        R    pass
3     A01         4.0      10.2        R    fail
4     A01         2.8       4.5        L    pass
5     A01         0.7       6.1        L    pass
6     A01         3.5      11.2        R    fail
7     A01         2.7       5.6        L    pass

In [260]: exp1
Out[260]:
  subject  start_time  end_time stimulus outcome
0     A01         2.3       5.6        L    pass
1     A01         1.6       2.1        R    pass
2     A01         2.3       5.6        R    pass
3     A01         4.0      10.2        R    fail
4     A01         2.8       4.5        L    pass
5     A01         0.7       6.1        L    pass
6     A01         3.5      11.2        R    fail
7     A01         2.7       5.6        L    pass

In [261]: exp1.to_csv('my_exp1.csv')

In [262]: exps
Out[262]:
   subject  start_time  end_time stimulus outcome
0      A01         2.3       5.6        L    pass
1      A01         1.6       2.1        R    pass
2      A01         2.3       5.6        R    pass
3      A01         4.0      10.2        R    fail
4      A01         2.8       4.5        L    pass
5      A01         0.7       6.1        L    pass
6      A01         3.5      11.2        R    fail
7      A01         2.7       5.6        L    pass
0      A02         2.7       5.6        L    pass
1      A02         1.2       4.3        L    pass
2      A02         4.0      10.4        R    fail
3      A02         2.3       5.6        R    pass
4      A02         4.1      10.0        R    fail
5      A02         3.9      12.1        R    fail
6      A02         2.8       4.5        L    pass
7      A02         1.3       3.1        R    pass
8      A02         0.8       4.1        L    pass
9      A02         3.6      12.4        R    fail
10     A02         5.5      13.3        R    fail

In [263]: exp1.to_csv('my_exps.csv')

In [264]: exps.to_csv('my_exps.csv')

In [265]: exps.to_excel('my_exps.xlsx')

In [266]: exps
Out[266]:
   subject  start_time  end_time stimulus outcome
0      A01         2.3       5.6        L    pass
1      A01         1.6       2.1        R    pass
2      A01         2.3       5.6        R    pass
3      A01         4.0      10.2        R    fail
4      A01         2.8       4.5        L    pass
5      A01         0.7       6.1        L    pass
6      A01         3.5      11.2        R    fail
7      A01         2.7       5.6        L    pass
0      A02         2.7       5.6        L    pass
1      A02         1.2       4.3        L    pass
2      A02         4.0      10.4        R    fail
3      A02         2.3       5.6        R    pass
4      A02         4.1      10.0        R    fail
5      A02         3.9      12.1        R    fail
6      A02         2.8       4.5        L    pass
7      A02         1.3       3.1        R    pass
8      A02         0.8       4.1        L    pass
9      A02         3.6      12.4        R    fail
10     A02         5.5      13.3        R    fail

In [267]: exps.min()
Out[267]:
subject        A01
start_time     0.7
end_time       2.1
stimulus         L
outcome       fail
dtype: object

In [268]: exps.max()
Out[268]:
subject        A02
start_time     5.5
end_time      13.3
stimulus         R
outcome       pass
dtype: object

In [269]: s
Out[269]:
0      0.862530
20     0.167578
40     0.227260
60     0.249521
80     0.125231
100    0.698099
120    0.178861
140    0.321948
160    0.416035
180    0.876434
200    0.215322
220    0.818089
240    0.448726
260    0.854475
280    0.093169
300    0.890964
320    0.936727
340    0.168883
360    0.731984
380    0.611636
dtype: float64

In [270]: s.min()
Out[270]: 0.09316860534485494

In [271]: exps.min()
Out[271]:
subject        A01
start_time     0.7
end_time       2.1
stimulus         L
outcome       fail
dtype: object

In [272]: exps.max()
Out[272]:
subject        A02
start_time     5.5
end_time      13.3
stimulus         R
outcome       pass
dtype: object

In [273]: exps.mean()
Out[273]:
start_time    2.742105
end_time      7.173684
dtype: float64

In [274]: exps.median()
Out[274]:
start_time    2.7
end_time      5.6
dtype: float64

In [275]: exps.std()
Out[275]:
start_time    1.281629
end_time      3.502038
dtype: float64

In [276]: exps.max()
Out[276]:
subject        A02
start_time     5.5
end_time      13.3
stimulus         R
outcome       pass
dtype: object

In [277]: exps
Out[277]:
   subject  start_time  end_time stimulus outcome
0      A01         2.3       5.6        L    pass
1      A01         1.6       2.1        R    pass
2      A01         2.3       5.6        R    pass
3      A01         4.0      10.2        R    fail
4      A01         2.8       4.5        L    pass
5      A01         0.7       6.1        L    pass
6      A01         3.5      11.2        R    fail
7      A01         2.7       5.6        L    pass
0      A02         2.7       5.6        L    pass
1      A02         1.2       4.3        L    pass
2      A02         4.0      10.4        R    fail
3      A02         2.3       5.6        R    pass
4      A02         4.1      10.0        R    fail
5      A02         3.9      12.1        R    fail
6      A02         2.8       4.5        L    pass
7      A02         1.3       3.1        R    pass
8      A02         0.8       4.1        L    pass
9      A02         3.6      12.4        R    fail
10     A02         5.5      13.3        R    fail

In [278]: exps['subject']
Out[278]:
0     A01
1     A01
2     A01
3     A01
4     A01
5     A01
6     A01
7     A01
0     A02
1     A02
2     A02
3     A02
4     A02
5     A02
6     A02
7     A02
8     A02
9     A02
10    A02
Name: subject, dtype: object

In [279]: exps['subject'] == 'A01'
Out[279]:
0      True
1      True
2      True
3      True
4      True
5      True
6      True
7      True
0     False
1     False
2     False
3     False
4     False
5     False
6     False
7     False
8     False
9     False
10    False
Name: subject, dtype: bool

In [280]: exps[exps['subject'] == 'A01']
Out[280]:
  subject  start_time  end_time stimulus outcome
0     A01         2.3       5.6        L    pass
1     A01         1.6       2.1        R    pass
2     A01         2.3       5.6        R    pass
3     A01         4.0      10.2        R    fail
4     A01         2.8       4.5        L    pass
5     A01         0.7       6.1        L    pass
6     A01         3.5      11.2        R    fail
7     A01         2.7       5.6        L    pass

In [281]: exps[exps['subject'] == 'A01'].max()
Out[281]:
subject        A01
start_time       4
end_time      11.2
stimulus         R
outcome       pass
dtype: object

In [282]: exps[exps['subject'] == 'A01']['start_time']
Out[282]:
0    2.3
1    1.6
2    2.3
3    4.0
4    2.8
5    0.7
6    3.5
7    2.7
Name: start_time, dtype: float64

In [283]: exps[exps['subject'] == 'A01']['start_time'].max()
Out[283]: 4.0

In [284]: exps[exps['subject'] == 'A01']['start_time']
Out[284]:
0    2.3
1    1.6
2    2.3
3    4.0
4    2.8
5    0.7
6    3.5
7    2.7
Name: start_time, dtype: float64

In [285]: exps
Out[285]:
   subject  start_time  end_time stimulus outcome
0      A01         2.3       5.6        L    pass
1      A01         1.6       2.1        R    pass
2      A01         2.3       5.6        R    pass
3      A01         4.0      10.2        R    fail
4      A01         2.8       4.5        L    pass
5      A01         0.7       6.1        L    pass
6      A01         3.5      11.2        R    fail
7      A01         2.7       5.6        L    pass
0      A02         2.7       5.6        L    pass
1      A02         1.2       4.3        L    pass
2      A02         4.0      10.4        R    fail
3      A02         2.3       5.6        R    pass
4      A02         4.1      10.0        R    fail
5      A02         3.9      12.1        R    fail
6      A02         2.8       4.5        L    pass
7      A02         1.3       3.1        R    pass
8      A02         0.8       4.1        L    pass
9      A02         3.6      12.4        R    fail
10     A02         5.5      13.3        R    fail

In [286]: exps.loc[0]
Out[286]:
  subject  start_time  end_time stimulus outcome
0     A01         2.3       5.6        L    pass
0     A02         2.7       5.6        L    pass

In [287]: exps.describe()
Out[287]:
       start_time   end_time
count   19.000000  19.000000
mean     2.742105   7.173684
std      1.281629   3.502038
min      0.700000   2.100000
25%      1.950000   4.500000
50%      2.700000   5.600000
75%      3.750000  10.300000
max      5.500000  13.300000

In [288]: s
Out[288]:
0      0.862530
20     0.167578
40     0.227260
60     0.249521
80     0.125231
100    0.698099
120    0.178861
140    0.321948
160    0.416035
180    0.876434
200    0.215322
220    0.818089
240    0.448726
260    0.854475
280    0.093169
300    0.890964
320    0.936727
340    0.168883
360    0.731984
380    0.611636
dtype: float64

In [289]: s.describe()
Out[289]:
count    20.000000
mean      0.494674
std       0.310965
min       0.093169
25%       0.206207
50%       0.432381
75%       0.827185
max       0.936727
dtype: float64

In [290]: exps.describe()
Out[290]:
       start_time   end_time
count   19.000000  19.000000
mean     2.742105   7.173684
std      1.281629   3.502038
min      0.700000   2.100000
25%      1.950000   4.500000
50%      2.700000   5.600000
75%      3.750000  10.300000
max      5.500000  13.300000

In [291]: exps.nunique()
Out[291]:
subject        2
start_time    14
end_time      14
stimulus       2
outcome        2
dtype: int64

In [292]: exps['subject']
Out[292]:
0     A01
1     A01
2     A01
3     A01
4     A01
5     A01
6     A01
7     A01
0     A02
1     A02
2     A02
3     A02
4     A02
5     A02
6     A02
7     A02
8     A02
9     A02
10    A02
Name: subject, dtype: object

In [293]: exps['subject'].nunique()
Out[293]: 2

In [294]: exps
Out[294]:
   subject  start_time  end_time stimulus outcome
0      A01         2.3       5.6        L    pass
1      A01         1.6       2.1        R    pass
2      A01         2.3       5.6        R    pass
3      A01         4.0      10.2        R    fail
4      A01         2.8       4.5        L    pass
5      A01         0.7       6.1        L    pass
6      A01         3.5      11.2        R    fail
7      A01         2.7       5.6        L    pass
0      A02         2.7       5.6        L    pass
1      A02         1.2       4.3        L    pass
2      A02         4.0      10.4        R    fail
3      A02         2.3       5.6        R    pass
4      A02         4.1      10.0        R    fail
5      A02         3.9      12.1        R    fail
6      A02         2.8       4.5        L    pass
7      A02         1.3       3.1        R    pass
8      A02         0.8       4.1        L    pass
9      A02         3.6      12.4        R    fail
10     A02         5.5      13.3        R    fail

In [295]: exps.groubpy('outcome')
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-295-280afc4ad915> in <module>
----> 1 exps.groubpy('outcome')

/usr/local/lib/python3.6/dist-packages/pandas/core/generic.py in __getattr__(self, name)
   5065             if self._info_axis._can_hold_identifiers_and_holds_name(name):
   5066                 return self[name]
-> 5067             return object.__getattribute__(self, name)
   5068
   5069     def __setattr__(self, name, value):

AttributeError: 'DataFrame' object has no attribute 'groubpy'
> /usr/local/lib/python3.6/dist-packages/pandas/core/generic.py(5067)__getattr__()
   5065             if self._info_axis._can_hold_identifiers_and_holds_name(name):
   5066                 return self[name]
-> 5067             return object.__getattribute__(self, name)
   5068
   5069     def __setattr__(self, name, value):

ipdb> c

In [296]: exps.groupby('outcome')
Out[296]: <pandas.core.groupby.generic.DataFrameGroupBy object at 0x7fd2402f0f60>

In [297]: gb = exps.groupby('outcome')

In [298]: exps.groupby('outcome').mean()
Out[298]:
         start_time   end_time
outcome
fail       4.085714  11.371429
pass       1.958333   4.725000

In [299]: exps
Out[299]:
   subject  start_time  end_time stimulus outcome
0      A01         2.3       5.6        L    pass
1      A01         1.6       2.1        R    pass
2      A01         2.3       5.6        R    pass
3      A01         4.0      10.2        R    fail
4      A01         2.8       4.5        L    pass
5      A01         0.7       6.1        L    pass
6      A01         3.5      11.2        R    fail
7      A01         2.7       5.6        L    pass
0      A02         2.7       5.6        L    pass
1      A02         1.2       4.3        L    pass
2      A02         4.0      10.4        R    fail
3      A02         2.3       5.6        R    pass
4      A02         4.1      10.0        R    fail
5      A02         3.9      12.1        R    fail
6      A02         2.8       4.5        L    pass
7      A02         1.3       3.1        R    pass
8      A02         0.8       4.1        L    pass
9      A02         3.6      12.4        R    fail
10     A02         5.5      13.3        R    fail

In [300]: exps.groupby('outcome').mean()
Out[300]:
         start_time   end_time
outcome
fail       4.085714  11.371429
pass       1.958333   4.725000

In [301]: missd = [[1, 2, 3],
     ...:          [4, 5],
     ...:          [7, 8, 9]]

In [302]: np.array(missd)
Out[302]: array([list([1, 2, 3]), list([4, 5]), list([7, 8, 9])], dtype=object)

In [303]: missd = [[1, 2, 3],
     ...:          [4, 5, np.nan],
     ...:          [7, 8, 9]]

In [304]: np.array(missd)
Out[304]:
array([[ 1.,  2.,  3.],
       [ 4.,  5., nan],
       [ 7.,  8.,  9.]])

In [305]: np.array(missd).shape
Out[305]: (3, 3)

In [306]: pd.DataFrame(missd)
Out[306]:
   0  1    2
0  1  2  3.0
1  4  5  NaN
2  7  8  9.0

In [307]: pd.DataFrame(missd).mean()
Out[307]:
0    4.0
1    5.0
2    6.0
dtype: float64

In [308]: ls
09_pandas.md   exp1.csv  exp.xlsx    my_exp1.csv  my_exps.xlsx  spike_times.npy  V.npy
09_pandas.pdf  exp2.csv  Galton.csv  my_exps.csv  spikes.png    t.npy

In [309]: gdf = pd.read_csv('Galton.csv')

In [310]: gdf
Out[310]:
    Family  Father  Mother Gender  Height  Kids
0        1    78.5    67.0      M    73.2     4
1        1    78.5    67.0      F    69.2     4
2        1    78.5    67.0      F    69.0     4
3        1    78.5    67.0      F    69.0     4
4        2    75.5    66.5      M    73.5     4
5        2    75.5    66.5      M    72.5     4
6        2    75.5    66.5      F    65.5     4
7        2    75.5    66.5      F    65.5     4
8        3    75.0    64.0      M    71.0     2
9        3    75.0    64.0      F    68.0     2
10       4    75.0    64.0      M    70.5     5
11       4    75.0    64.0      M    68.5     5
12       4    75.0    64.0      F    67.0     5
13       4    75.0    64.0      F    64.5     5
14       4    75.0    64.0      F    63.0     5
15       5    75.0    58.5      M    72.0     6
16       5    75.0    58.5      M    69.0     6
17       5    75.0    58.5      M    68.0     6
18       5    75.0    58.5      F    66.5     6
19       5    75.0    58.5      F    62.5     6
20       5    75.0    58.5      F    62.5     6
21       6    74.0    68.0      F    69.5     1
22       7    74.0    68.0      M    76.5     6
23       7    74.0    68.0      M    74.0     6
24       7    74.0    68.0      M    73.0     6
25       7    74.0    68.0      M    73.0     6
26       7    74.0    68.0      F    70.5     6
27       7    74.0    68.0      F    64.0     6
28       8    74.0    66.5      F    70.5     3
29       8    74.0    66.5      F    68.0     3
..     ...     ...     ...    ...     ...   ...
868    198    64.0    64.0      M    71.5     7
869    198    64.0    64.0      M    68.0     7
870    198    64.0    64.0      F    65.5     7
871    198    64.0    64.0      F    64.0     7
872    198    64.0    64.0      F    62.0     7
873    198    64.0    64.0      F    62.0     7
874    198    64.0    64.0      F    61.0     7
875    199    64.0    64.0      M    70.5     7
876    199    64.0    64.0      M    68.0     7
877    199    64.0    64.0      F    67.0     7
878    199    64.0    64.0      F    65.0     7
879    199    64.0    64.0      F    64.0     7
880    199    64.0    64.0      F    64.0     7
881    199    64.0    64.0      F    60.0     7
882    200    64.0    63.0      M    64.5     1
883    201    64.0    60.0      M    66.0     2
884    201    64.0    60.0      F    60.0     2
885    203    62.0    66.0      M    64.0     3
886    203    62.0    66.0      F    62.0     3
887    203    62.0    66.0      F    61.0     3
888    204    62.5    63.0      M    66.5     2
889    204    62.5    63.0      F    57.0     2
890   136A    68.5    65.0      M    72.0     8
891   136A    68.5    65.0      M    70.5     8
892   136A    68.5    65.0      M    68.7     8
893   136A    68.5    65.0      M    68.5     8
894   136A    68.5    65.0      M    67.7     8
895   136A    68.5    65.0      F    64.0     8
896   136A    68.5    65.0      F    63.5     8
897   136A    68.5    65.0      F    63.0     8

[898 rows x 6 columns]

In [311]: gdf.groupby('Family')
Out[311]: <pandas.core.groupby.generic.DataFrameGroupBy object at 0x7fd2514d97f0>

In [312]: gdf.groupby('Family').sum()
Out[312]:
        Father  Mother  Height  Kids
Family
1        314.0   268.0   280.4    16
10        74.0    65.5    65.5     1
100      207.0   198.0   212.2     9
101      414.0   400.2   422.5    36
102      414.0   396.0   397.0    36
103      345.0   332.5   346.0    25
104      278.0   266.0   266.5    16
105      414.0   399.0   399.0    36
106      486.5   462.0   479.5    49
107      621.0   594.0   609.5    81
108      483.0   455.0   459.0    49
109      486.5   451.5   451.1    49
11       592.0   496.0   538.5    64
110      276.8   256.0   266.7    16
112      207.0   189.0   200.0     9
113       69.0    63.0    72.0     1
114      414.0   378.0   405.0    36
115      483.0   444.5   454.5    49
116      207.0   190.5   197.2     9
117       69.7    62.0    62.5     1
118      208.5   186.0   214.0     9
119      345.0   310.0   347.0    25
12        74.0    61.0    65.0     1
121      552.0   500.0   530.5    64
122      276.0   248.0   272.0    16
123      347.5   305.0   333.5    25
124      621.0   549.0   581.0    81
125      207.0   180.0   201.0     9
126      276.0   240.0   257.2    16
127       69.0    60.5    69.5     1
...        ...     ...     ...   ...
71       420.0   390.0   400.0    36
72       490.0   455.0   488.7    49
73       210.0   195.0   210.5     9
74       140.0   130.0   138.0     4
75       490.0   452.9   471.9    49
76       490.0   448.0   473.7    49
77       280.0   256.0   270.2    16
78       350.0   321.0   325.8    25
79       564.0   512.0   547.0    64
8        222.0   199.5   204.5     9
80        70.5    64.5    60.0     1
81       280.0   256.0   259.0    16
82       630.0   576.0   617.0    81
83       560.0   509.6   515.1    64
85       352.5   315.0   337.0    25
86       280.0   254.0   269.5    16
87       280.0   252.0   260.7    16
88       280.0   252.0   259.5    16
89       564.0   496.0   541.0    64
9         74.5    66.0    66.0     1
90       492.1   438.9   465.5    49
91       211.5   186.0   204.0     9
92       140.0   122.0   138.2     4
93       280.0   240.0   259.5    16
94       140.0   120.0   130.0     4
95       210.0   175.5   199.0     9
96       350.0   290.0   332.0    25
97       690.0   685.0   671.5   100
98        69.0    67.0    64.0     1
99       552.0   528.0   543.9    64

[197 rows x 4 columns]

In [313]: gdf.groupby('Family').min()
Out[313]:
        Father  Mother Gender  Height  Kids
Family
1         78.5    67.0      F    69.0     4
10        74.0    65.5      F    65.5     1
100       69.0    66.0      M    70.0     3
101       69.0    66.7      M    66.0     6
102       69.0    66.0      F    62.5     6
103       69.0    66.5      F    61.0     5
104       69.5    66.5      F    64.0     4
105       69.0    66.5      F    63.0     6
106       69.5    66.0      F    64.5     7
107       69.0    66.0      F    64.0     9
108       69.0    65.0      F    61.0     7
109       69.5    64.5      F    60.0     7
11        74.0    62.0      F    63.0     8
110       69.2    64.0      F    63.5     4
112       69.0    63.0      F    63.5     3
113       69.0    63.0      M    72.0     1
114       69.0    63.0      F    62.0     6
115       69.0    63.5      F    61.0     7
116       69.0    63.5      F    63.0     3
117       69.7    62.0      F    62.5     1
118       69.5    62.0      M    69.0     3
119       69.0    62.0      F    63.0     5
12        74.0    61.0      F    65.0     1
121       69.0    62.5      F    62.0     8
122       69.0    62.0      F    66.0     4
123       69.5    61.0      F    62.0     5
124       69.0    61.0      F    62.0     9
125       69.0    60.0      F    62.5     3
126       69.0    60.0      F    60.5     4
127       69.0    60.5      M    69.5     1
...        ...     ...    ...     ...   ...
71        70.0    65.0      F    63.0     6
72        70.0    65.0      F    62.0     7
73        70.0    65.0      F    65.0     3
74        70.0    65.0      M    69.0     2
75        70.0    64.7      F    64.5     7
76        70.0    64.0      F    65.0     7
77        70.0    64.0      F    65.5     4
78        70.0    64.2      F    60.1     5
79        70.5    64.0      F    65.0     8
8         74.0    66.5      F    66.0     3
80        70.5    64.5      F    60.0     1
81        70.0    64.0      F    62.0     4
82        70.0    64.0      F    64.0     9
83        70.0    63.7      F    61.0     8
85        70.5    63.0      F    64.0     5
86        70.0    63.5      F    63.5     4
87        70.0    63.0      F    62.0     4
88        70.0    63.0      F    61.0     4
89        70.5    62.0      F    63.0     8
9         74.5    66.0      F    66.0     1
90        70.3    62.7      F    63.2     7
91        70.5    62.0      F    60.0     3
92        70.0    61.0      M    67.0     2
93        70.0    60.0      F    63.0     4
94        70.0    60.0      F    65.0     2
95        70.0    58.5      F    63.0     3
96        70.0    58.0      F    63.0     5
97        69.0    68.5      F    64.0    10
98        69.0    67.0      F    64.0     1
99        69.0    66.0      F    62.5     8

[197 rows x 5 columns]

In [314]: gdf.groupby('Family')
Out[314]: <pandas.core.groupby.generic.DataFrameGroupBy object at 0x7fd223965eb8>

In [315]: gdf.groupby('Family').describe()
^C
Program interrupted. (Use 'cont' to resume).
> <frozen importlib._bootstrap>(1032)_handle_fromlist()

ipdb> c
Out[315]:
       Father                                          Mother  ... Height  Kids
        count  mean  std   min   25%   50%   75%   max  count  ...    max count  mean  std   min   25%   50%   75%   max
Family                                                         ...
1         4.0  78.5  0.0  78.5  78.5  78.5  78.5  78.5    4.0  ...   73.2   4.0   4.0  0.0   4.0   4.0   4.0   4.0   4.0
10        1.0  74.0  NaN  74.0  74.0  74.0  74.0  74.0    1.0  ...   65.5   1.0   1.0  NaN   1.0   1.0   1.0   1.0   1.0
100       3.0  69.0  0.0  69.0  69.0  69.0  69.0  69.0    3.0  ...   71.2   3.0   3.0  0.0   3.0   3.0   3.0   3.0   3.0
101       6.0  69.0  0.0  69.0  69.0  69.0  69.0  69.0    6.0  ...   75.0   6.0   6.0  0.0   6.0   6.0   6.0   6.0   6.0
102       6.0  69.0  0.0  69.0  69.0  69.0  69.0  69.0    6.0  ...   70.0   6.0   6.0  0.0   6.0   6.0   6.0   6.0   6.0
103       5.0  69.0  0.0  69.0  69.0  69.0  69.0  69.0    5.0  ...   73.0   5.0   5.0  0.0   5.0   5.0   5.0   5.0   5.0
104       4.0  69.5  0.0  69.5  69.5  69.5  69.5  69.5    4.0  ...   70.5   4.0   4.0  0.0   4.0   4.0   4.0   4.0   4.0
105       6.0  69.0  0.0  69.0  69.0  69.0  69.0  69.0    6.0  ...   71.0   6.0   6.0  0.0   6.0   6.0   6.0   6.0   6.0
106       7.0  69.5  0.0  69.5  69.5  69.5  69.5  69.5    7.0  ...   71.0   7.0   7.0  0.0   7.0   7.0   7.0   7.0   7.0
107       9.0  69.0  0.0  69.0  69.0  69.0  69.0  69.0    9.0  ...   73.0   9.0   9.0  0.0   9.0   9.0   9.0   9.0   9.0
108       7.0  69.0  0.0  69.0  69.0  69.0  69.0  69.0    7.0  ...   70.0   7.0   7.0  0.0   7.0   7.0   7.0   7.0   7.0
109       7.0  69.5  0.0  69.5  69.5  69.5  69.5  69.5    7.0  ...   69.7   7.0   7.0  0.0   7.0   7.0   7.0   7.0   7.0
11        8.0  74.0  0.0  74.0  74.0  74.0  74.0  74.0    8.0  ...   74.0   8.0   8.0  0.0   8.0   8.0   8.0   8.0   8.0
110       4.0  69.2  0.0  69.2  69.2  69.2  69.2  69.2    4.0  ...   71.7   4.0   4.0  0.0   4.0   4.0   4.0   4.0   4.0
112       3.0  69.0  0.0  69.0  69.0  69.0  69.0  69.0    3.0  ...   69.0   3.0   3.0  0.0   3.0   3.0   3.0   3.0   3.0
113       1.0  69.0  NaN  69.0  69.0  69.0  69.0  69.0    1.0  ...   72.0   1.0   1.0  NaN   1.0   1.0   1.0   1.0   1.0
114       6.0  69.0  0.0  69.0  69.0  69.0  69.0  69.0    6.0  ...   73.0   6.0   6.0  0.0   6.0   6.0   6.0   6.0   6.0
115       7.0  69.0  0.0  69.0  69.0  69.0  69.0  69.0    7.0  ...   70.5   7.0   7.0  0.0   7.0   7.0   7.0   7.0   7.0
116       3.0  69.0  0.0  69.0  69.0  69.0  69.0  69.0    3.0  ...   70.5   3.0   3.0  0.0   3.0   3.0   3.0   3.0   3.0
117       1.0  69.7  NaN  69.7  69.7  69.7  69.7  69.7    1.0  ...   62.5   1.0   1.0  NaN   1.0   1.0   1.0   1.0   1.0
118       3.0  69.5  0.0  69.5  69.5  69.5  69.5  69.5    3.0  ...   73.0   3.0   3.0  0.0   3.0   3.0   3.0   3.0   3.0
119       5.0  69.0  0.0  69.0  69.0  69.0  69.0  69.0    5.0  ...   73.0   5.0   5.0  0.0   5.0   5.0   5.0   5.0   5.0
12        1.0  74.0  NaN  74.0  74.0  74.0  74.0  74.0    1.0  ...   65.0   1.0   1.0  NaN   1.0   1.0   1.0   1.0   1.0
121       8.0  69.0  0.0  69.0  69.0  69.0  69.0  69.0    8.0  ...   71.0   8.0   8.0  0.0   8.0   8.0   8.0   8.0   8.0
122       4.0  69.0  0.0  69.0  69.0  69.0  69.0  69.0    4.0  ...   72.0   4.0   4.0  0.0   4.0   4.0   4.0   4.0   4.0
123       5.0  69.5  0.0  69.5  69.5  69.5  69.5  69.5    5.0  ...   70.0   5.0   5.0  0.0   5.0   5.0   5.0   5.0   5.0
124       9.0  69.0  0.0  69.0  69.0  69.0  69.0  69.0    9.0  ...   68.0   9.0   9.0  0.0   9.0   9.0   9.0   9.0   9.0
125       3.0  69.0  0.0  69.0  69.0  69.0  69.0  69.0    3.0  ...   70.5   3.0   3.0  0.0   3.0   3.0   3.0   3.0   3.0
126       4.0  69.0  0.0  69.0  69.0  69.0  69.0  69.0    4.0  ...   69.0   4.0   4.0  0.0   4.0   4.0   4.0   4.0   4.0
127       1.0  69.0  NaN  69.0  69.0  69.0  69.0  69.0    1.0  ...   69.5   1.0   1.0  NaN   1.0   1.0   1.0   1.0   1.0
...       ...   ...  ...   ...   ...   ...   ...   ...    ...  ...    ...   ...   ...  ...   ...   ...   ...   ...   ...
71        6.0  70.0  0.0  70.0  70.0  70.0  70.0  70.0    6.0  ...   70.0   6.0   6.0  0.0   6.0   6.0   6.0   6.0   6.0
72        7.0  70.0  0.0  70.0  70.0  70.0  70.0  70.0    7.0  ...   79.0   7.0   7.0  0.0   7.0   7.0   7.0   7.0   7.0
73        3.0  70.0  0.0  70.0  70.0  70.0  70.0  70.0    3.0  ...   73.0   3.0   3.0  0.0   3.0   3.0   3.0   3.0   3.0
74        2.0  70.0  0.0  70.0  70.0  70.0  70.0  70.0    2.0  ...   69.0   2.0   2.0  0.0   2.0   2.0   2.0   2.0   2.0
75        7.0  70.0  0.0  70.0  70.0  70.0  70.0  70.0    7.0  ...   72.0   7.0   7.0  0.0   7.0   7.0   7.0   7.0   7.0
76        7.0  70.0  0.0  70.0  70.0  70.0  70.0  70.0    7.0  ...   70.7   7.0   7.0  0.0   7.0   7.0   7.0   7.0   7.0
77        4.0  70.0  0.0  70.0  70.0  70.0  70.0  70.0    4.0  ...   70.0   4.0   4.0  0.0   4.0   4.0   4.0   4.0   4.0
78        5.0  70.0  0.0  70.0  70.0  70.0  70.0  70.0    5.0  ...   72.0   5.0   5.0  0.0   5.0   5.0   5.0   5.0   5.0
79        8.0  70.5  0.0  70.5  70.5  70.5  70.5  70.5    8.0  ...   74.0   8.0   8.0  0.0   8.0   8.0   8.0   8.0   8.0
8         3.0  74.0  0.0  74.0  74.0  74.0  74.0  74.0    3.0  ...   70.5   3.0   3.0  0.0   3.0   3.0   3.0   3.0   3.0
80        1.0  70.5  NaN  70.5  70.5  70.5  70.5  70.5    1.0  ...   60.0   1.0   1.0  NaN   1.0   1.0   1.0   1.0   1.0
81        4.0  70.0  0.0  70.0  70.0  70.0  70.0  70.0    4.0  ...   68.0   4.0   4.0  0.0   4.0   4.0   4.0   4.0   4.0
82        9.0  70.0  0.0  70.0  70.0  70.0  70.0  70.0    9.0  ...   71.0   9.0   9.0  0.0   9.0   9.0   9.0   9.0   9.0
83        8.0  70.0  0.0  70.0  70.0  70.0  70.0  70.0    8.0  ...   70.0   8.0   8.0  0.0   8.0   8.0   8.0   8.0   8.0
85        5.0  70.5  0.0  70.5  70.5  70.5  70.5  70.5    5.0  ...   72.5   5.0   5.0  0.0   5.0   5.0   5.0   5.0   5.0
86        4.0  70.0  0.0  70.0  70.0  70.0  70.0  70.0    4.0  ...   71.0   4.0   4.0  0.0   4.0   4.0   4.0   4.0   4.0
87        4.0  70.0  0.0  70.0  70.0  70.0  70.0  70.0    4.0  ...   68.0   4.0   4.0  0.0   4.0   4.0   4.0   4.0   4.0
88        4.0  70.0  0.0  70.0  70.0  70.0  70.0  70.0    4.0  ...   70.0   4.0   4.0  0.0   4.0   4.0   4.0   4.0   4.0
89        8.0  70.5  0.0  70.5  70.5  70.5  70.5  70.5    8.0  ...   72.0   8.0   8.0  0.0   8.0   8.0   8.0   8.0   8.0
9         1.0  74.5  NaN  74.5  74.5  74.5  74.5  74.5    1.0  ...   66.0   1.0   1.0  NaN   1.0   1.0   1.0   1.0   1.0
90        7.0  70.3  0.0  70.3  70.3  70.3  70.3  70.3    7.0  ...   70.7   7.0   7.0  0.0   7.0   7.0   7.0   7.0   7.0
91        3.0  70.5  0.0  70.5  70.5  70.5  70.5  70.5    3.0  ...   72.0   3.0   3.0  0.0   3.0   3.0   3.0   3.0   3.0
92        2.0  70.0  0.0  70.0  70.0  70.0  70.0  70.0    2.0  ...   71.2   2.0   2.0  0.0   2.0   2.0   2.0   2.0   2.0
93        4.0  70.0  0.0  70.0  70.0  70.0  70.0  70.0    4.0  ...   67.0   4.0   4.0  0.0   4.0   4.0   4.0   4.0   4.0
94        2.0  70.0  0.0  70.0  70.0  70.0  70.0  70.0    2.0  ...   65.0   2.0   2.0  0.0   2.0   2.0   2.0   2.0   2.0
95        3.0  70.0  0.0  70.0  70.0  70.0  70.0  70.0    3.0  ...   71.5   3.0   3.0  0.0   3.0   3.0   3.0   3.0   3.0
96        5.0  70.0  0.0  70.0  70.0  70.0  70.0  70.0    5.0  ...   72.0   5.0   5.0  0.0   5.0   5.0   5.0   5.0   5.0
97       10.0  69.0  0.0  69.0  69.0  69.0  69.0  69.0   10.0  ...   75.0  10.0  10.0  0.0  10.0  10.0  10.0  10.0  10.0
98        1.0  69.0  NaN  69.0  69.0  69.0  69.0  69.0    1.0  ...   64.0   1.0   1.0  NaN   1.0   1.0   1.0   1.0   1.0
99        8.0  69.0  0.0  69.0  69.0  69.0  69.0  69.0    8.0  ...   73.0   8.0   8.0  0.0   8.0   8.0   8.0   8.0   8.0

[197 rows x 32 columns]

In [316]: gdf.describe()
Out[316]:
           Father      Mother      Height        Kids
count  898.000000  898.000000  898.000000  898.000000
mean    69.232851   64.084410   66.760690    6.135857
std      2.470256    2.307025    3.582918    2.685156
min     62.000000   58.000000   56.000000    1.000000
25%     68.000000   63.000000   64.000000    4.000000
50%     69.000000   64.000000   66.500000    6.000000
75%     71.000000   65.500000   69.700000    8.000000
max     78.500000   70.500000   79.000000   15.000000

In [317]: gdf
Out[317]:
    Family  Father  Mother Gender  Height  Kids
0        1    78.5    67.0      M    73.2     4
1        1    78.5    67.0      F    69.2     4
2        1    78.5    67.0      F    69.0     4
3        1    78.5    67.0      F    69.0     4
4        2    75.5    66.5      M    73.5     4
5        2    75.5    66.5      M    72.5     4
6        2    75.5    66.5      F    65.5     4
7        2    75.5    66.5      F    65.5     4
8        3    75.0    64.0      M    71.0     2
9        3    75.0    64.0      F    68.0     2
10       4    75.0    64.0      M    70.5     5
11       4    75.0    64.0      M    68.5     5
12       4    75.0    64.0      F    67.0     5
13       4    75.0    64.0      F    64.5     5
14       4    75.0    64.0      F    63.0     5
15       5    75.0    58.5      M    72.0     6
16       5    75.0    58.5      M    69.0     6
17       5    75.0    58.5      M    68.0     6
18       5    75.0    58.5      F    66.5     6
19       5    75.0    58.5      F    62.5     6
20       5    75.0    58.5      F    62.5     6
21       6    74.0    68.0      F    69.5     1
22       7    74.0    68.0      M    76.5     6
23       7    74.0    68.0      M    74.0     6
24       7    74.0    68.0      M    73.0     6
25       7    74.0    68.0      M    73.0     6
26       7    74.0    68.0      F    70.5     6
27       7    74.0    68.0      F    64.0     6
28       8    74.0    66.5      F    70.5     3
29       8    74.0    66.5      F    68.0     3
..     ...     ...     ...    ...     ...   ...
868    198    64.0    64.0      M    71.5     7
869    198    64.0    64.0      M    68.0     7
870    198    64.0    64.0      F    65.5     7
871    198    64.0    64.0      F    64.0     7
872    198    64.0    64.0      F    62.0     7
873    198    64.0    64.0      F    62.0     7
874    198    64.0    64.0      F    61.0     7
875    199    64.0    64.0      M    70.5     7
876    199    64.0    64.0      M    68.0     7
877    199    64.0    64.0      F    67.0     7
878    199    64.0    64.0      F    65.0     7
879    199    64.0    64.0      F    64.0     7
880    199    64.0    64.0      F    64.0     7
881    199    64.0    64.0      F    60.0     7
882    200    64.0    63.0      M    64.5     1
883    201    64.0    60.0      M    66.0     2
884    201    64.0    60.0      F    60.0     2
885    203    62.0    66.0      M    64.0     3
886    203    62.0    66.0      F    62.0     3
887    203    62.0    66.0      F    61.0     3
888    204    62.5    63.0      M    66.5     2
889    204    62.5    63.0      F    57.0     2
890   136A    68.5    65.0      M    72.0     8
891   136A    68.5    65.0      M    70.5     8
892   136A    68.5    65.0      M    68.7     8
893   136A    68.5    65.0      M    68.5     8
894   136A    68.5    65.0      M    67.7     8
895   136A    68.5    65.0      F    64.0     8
896   136A    68.5    65.0      F    63.5     8
897   136A    68.5    65.0      F    63.0     8

[898 rows x 6 columns]

In [318]: gdf.groupby('Family').describe()
^C
Program interrupted. (Use 'cont' to resume).
> /usr/local/lib/python3.6/dist-packages/pandas/core/dtypes/common.py(1866)_is_dtype_type()
   1864     if isinstance(arr_or_dtype, np.dtype):
   1865         return condition(arr_or_dtype.type)
-> 1866     elif isinstance(arr_or_dtype, type):
   1867         if issubclass(arr_or_dtype, (PandasExtensionDtype, ExtensionDtype)):
   1868             arr_or_dtype = arr_or_dtype.type

ipdb> c
Out[318]:
       Father                                          Mother  ... Height  Kids
        count  mean  std   min   25%   50%   75%   max  count  ...    max count  mean  std   min   25%   50%   75%   max
Family                                                         ...
1         4.0  78.5  0.0  78.5  78.5  78.5  78.5  78.5    4.0  ...   73.2   4.0   4.0  0.0   4.0   4.0   4.0   4.0   4.0
10        1.0  74.0  NaN  74.0  74.0  74.0  74.0  74.0    1.0  ...   65.5   1.0   1.0  NaN   1.0   1.0   1.0   1.0   1.0
100       3.0  69.0  0.0  69.0  69.0  69.0  69.0  69.0    3.0  ...   71.2   3.0   3.0  0.0   3.0   3.0   3.0   3.0   3.0
101       6.0  69.0  0.0  69.0  69.0  69.0  69.0  69.0    6.0  ...   75.0   6.0   6.0  0.0   6.0   6.0   6.0   6.0   6.0
102       6.0  69.0  0.0  69.0  69.0  69.0  69.0  69.0    6.0  ...   70.0   6.0   6.0  0.0   6.0   6.0   6.0   6.0   6.0
103       5.0  69.0  0.0  69.0  69.0  69.0  69.0  69.0    5.0  ...   73.0   5.0   5.0  0.0   5.0   5.0   5.0   5.0   5.0
104       4.0  69.5  0.0  69.5  69.5  69.5  69.5  69.5    4.0  ...   70.5   4.0   4.0  0.0   4.0   4.0   4.0   4.0   4.0
105       6.0  69.0  0.0  69.0  69.0  69.0  69.0  69.0    6.0  ...   71.0   6.0   6.0  0.0   6.0   6.0   6.0   6.0   6.0
106       7.0  69.5  0.0  69.5  69.5  69.5  69.5  69.5    7.0  ...   71.0   7.0   7.0  0.0   7.0   7.0   7.0   7.0   7.0
107       9.0  69.0  0.0  69.0  69.0  69.0  69.0  69.0    9.0  ...   73.0   9.0   9.0  0.0   9.0   9.0   9.0   9.0   9.0
108       7.0  69.0  0.0  69.0  69.0  69.0  69.0  69.0    7.0  ...   70.0   7.0   7.0  0.0   7.0   7.0   7.0   7.0   7.0
109       7.0  69.5  0.0  69.5  69.5  69.5  69.5  69.5    7.0  ...   69.7   7.0   7.0  0.0   7.0   7.0   7.0   7.0   7.0
11        8.0  74.0  0.0  74.0  74.0  74.0  74.0  74.0    8.0  ...   74.0   8.0   8.0  0.0   8.0   8.0   8.0   8.0   8.0
110       4.0  69.2  0.0  69.2  69.2  69.2  69.2  69.2    4.0  ...   71.7   4.0   4.0  0.0   4.0   4.0   4.0   4.0   4.0
112       3.0  69.0  0.0  69.0  69.0  69.0  69.0  69.0    3.0  ...   69.0   3.0   3.0  0.0   3.0   3.0   3.0   3.0   3.0
113       1.0  69.0  NaN  69.0  69.0  69.0  69.0  69.0    1.0  ...   72.0   1.0   1.0  NaN   1.0   1.0   1.0   1.0   1.0
114       6.0  69.0  0.0  69.0  69.0  69.0  69.0  69.0    6.0  ...   73.0   6.0   6.0  0.0   6.0   6.0   6.0   6.0   6.0
115       7.0  69.0  0.0  69.0  69.0  69.0  69.0  69.0    7.0  ...   70.5   7.0   7.0  0.0   7.0   7.0   7.0   7.0   7.0
116       3.0  69.0  0.0  69.0  69.0  69.0  69.0  69.0    3.0  ...   70.5   3.0   3.0  0.0   3.0   3.0   3.0   3.0   3.0
117       1.0  69.7  NaN  69.7  69.7  69.7  69.7  69.7    1.0  ...   62.5   1.0   1.0  NaN   1.0   1.0   1.0   1.0   1.0
118       3.0  69.5  0.0  69.5  69.5  69.5  69.5  69.5    3.0  ...   73.0   3.0   3.0  0.0   3.0   3.0   3.0   3.0   3.0
119       5.0  69.0  0.0  69.0  69.0  69.0  69.0  69.0    5.0  ...   73.0   5.0   5.0  0.0   5.0   5.0   5.0   5.0   5.0
12        1.0  74.0  NaN  74.0  74.0  74.0  74.0  74.0    1.0  ...   65.0   1.0   1.0  NaN   1.0   1.0   1.0   1.0   1.0
121       8.0  69.0  0.0  69.0  69.0  69.0  69.0  69.0    8.0  ...   71.0   8.0   8.0  0.0   8.0   8.0   8.0   8.0   8.0
122       4.0  69.0  0.0  69.0  69.0  69.0  69.0  69.0    4.0  ...   72.0   4.0   4.0  0.0   4.0   4.0   4.0   4.0   4.0
123       5.0  69.5  0.0  69.5  69.5  69.5  69.5  69.5    5.0  ...   70.0   5.0   5.0  0.0   5.0   5.0   5.0   5.0   5.0
124       9.0  69.0  0.0  69.0  69.0  69.0  69.0  69.0    9.0  ...   68.0   9.0   9.0  0.0   9.0   9.0   9.0   9.0   9.0
125       3.0  69.0  0.0  69.0  69.0  69.0  69.0  69.0    3.0  ...   70.5   3.0   3.0  0.0   3.0   3.0   3.0   3.0   3.0
126       4.0  69.0  0.0  69.0  69.0  69.0  69.0  69.0    4.0  ...   69.0   4.0   4.0  0.0   4.0   4.0   4.0   4.0   4.0
127       1.0  69.0  NaN  69.0  69.0  69.0  69.0  69.0    1.0  ...   69.5   1.0   1.0  NaN   1.0   1.0   1.0   1.0   1.0
...       ...   ...  ...   ...   ...   ...   ...   ...    ...  ...    ...   ...   ...  ...   ...   ...   ...   ...   ...
71        6.0  70.0  0.0  70.0  70.0  70.0  70.0  70.0    6.0  ...   70.0   6.0   6.0  0.0   6.0   6.0   6.0   6.0   6.0
72        7.0  70.0  0.0  70.0  70.0  70.0  70.0  70.0    7.0  ...   79.0   7.0   7.0  0.0   7.0   7.0   7.0   7.0   7.0
73        3.0  70.0  0.0  70.0  70.0  70.0  70.0  70.0    3.0  ...   73.0   3.0   3.0  0.0   3.0   3.0   3.0   3.0   3.0
74        2.0  70.0  0.0  70.0  70.0  70.0  70.0  70.0    2.0  ...   69.0   2.0   2.0  0.0   2.0   2.0   2.0   2.0   2.0
75        7.0  70.0  0.0  70.0  70.0  70.0  70.0  70.0    7.0  ...   72.0   7.0   7.0  0.0   7.0   7.0   7.0   7.0   7.0
76        7.0  70.0  0.0  70.0  70.0  70.0  70.0  70.0    7.0  ...   70.7   7.0   7.0  0.0   7.0   7.0   7.0   7.0   7.0
77        4.0  70.0  0.0  70.0  70.0  70.0  70.0  70.0    4.0  ...   70.0   4.0   4.0  0.0   4.0   4.0   4.0   4.0   4.0
78        5.0  70.0  0.0  70.0  70.0  70.0  70.0  70.0    5.0  ...   72.0   5.0   5.0  0.0   5.0   5.0   5.0   5.0   5.0
79        8.0  70.5  0.0  70.5  70.5  70.5  70.5  70.5    8.0  ...   74.0   8.0   8.0  0.0   8.0   8.0   8.0   8.0   8.0
8         3.0  74.0  0.0  74.0  74.0  74.0  74.0  74.0    3.0  ...   70.5   3.0   3.0  0.0   3.0   3.0   3.0   3.0   3.0
80        1.0  70.5  NaN  70.5  70.5  70.5  70.5  70.5    1.0  ...   60.0   1.0   1.0  NaN   1.0   1.0   1.0   1.0   1.0
81        4.0  70.0  0.0  70.0  70.0  70.0  70.0  70.0    4.0  ...   68.0   4.0   4.0  0.0   4.0   4.0   4.0   4.0   4.0
82        9.0  70.0  0.0  70.0  70.0  70.0  70.0  70.0    9.0  ...   71.0   9.0   9.0  0.0   9.0   9.0   9.0   9.0   9.0
83        8.0  70.0  0.0  70.0  70.0  70.0  70.0  70.0    8.0  ...   70.0   8.0   8.0  0.0   8.0   8.0   8.0   8.0   8.0
85        5.0  70.5  0.0  70.5  70.5  70.5  70.5  70.5    5.0  ...   72.5   5.0   5.0  0.0   5.0   5.0   5.0   5.0   5.0
86        4.0  70.0  0.0  70.0  70.0  70.0  70.0  70.0    4.0  ...   71.0   4.0   4.0  0.0   4.0   4.0   4.0   4.0   4.0
87        4.0  70.0  0.0  70.0  70.0  70.0  70.0  70.0    4.0  ...   68.0   4.0   4.0  0.0   4.0   4.0   4.0   4.0   4.0
88        4.0  70.0  0.0  70.0  70.0  70.0  70.0  70.0    4.0  ...   70.0   4.0   4.0  0.0   4.0   4.0   4.0   4.0   4.0
89        8.0  70.5  0.0  70.5  70.5  70.5  70.5  70.5    8.0  ...   72.0   8.0   8.0  0.0   8.0   8.0   8.0   8.0   8.0
9         1.0  74.5  NaN  74.5  74.5  74.5  74.5  74.5    1.0  ...   66.0   1.0   1.0  NaN   1.0   1.0   1.0   1.0   1.0
90        7.0  70.3  0.0  70.3  70.3  70.3  70.3  70.3    7.0  ...   70.7   7.0   7.0  0.0   7.0   7.0   7.0   7.0   7.0
91        3.0  70.5  0.0  70.5  70.5  70.5  70.5  70.5    3.0  ...   72.0   3.0   3.0  0.0   3.0   3.0   3.0   3.0   3.0
92        2.0  70.0  0.0  70.0  70.0  70.0  70.0  70.0    2.0  ...   71.2   2.0   2.0  0.0   2.0   2.0   2.0   2.0   2.0
93        4.0  70.0  0.0  70.0  70.0  70.0  70.0  70.0    4.0  ...   67.0   4.0   4.0  0.0   4.0   4.0   4.0   4.0   4.0
94        2.0  70.0  0.0  70.0  70.0  70.0  70.0  70.0    2.0  ...   65.0   2.0   2.0  0.0   2.0   2.0   2.0   2.0   2.0
95        3.0  70.0  0.0  70.0  70.0  70.0  70.0  70.0    3.0  ...   71.5   3.0   3.0  0.0   3.0   3.0   3.0   3.0   3.0
96        5.0  70.0  0.0  70.0  70.0  70.0  70.0  70.0    5.0  ...   72.0   5.0   5.0  0.0   5.0   5.0   5.0   5.0   5.0
97       10.0  69.0  0.0  69.0  69.0  69.0  69.0  69.0   10.0  ...   75.0  10.0  10.0  0.0  10.0  10.0  10.0  10.0  10.0
98        1.0  69.0  NaN  69.0  69.0  69.0  69.0  69.0    1.0  ...   64.0   1.0   1.0  NaN   1.0   1.0   1.0   1.0   1.0
99        8.0  69.0  0.0  69.0  69.0  69.0  69.0  69.0    8.0  ...   73.0   8.0   8.0  0.0   8.0   8.0   8.0   8.0   8.0

[197 rows x 32 columns]

In [319]: gdf.groupby('Family').count()
Out[319]:
        Father  Mother  Gender  Height  Kids
Family
1            4       4       4       4     4
10           1       1       1       1     1
100          3       3       3       3     3
101          6       6       6       6     6
102          6       6       6       6     6
103          5       5       5       5     5
104          4       4       4       4     4
105          6       6       6       6     6
106          7       7       7       7     7
107          9       9       9       9     9
108          7       7       7       7     7
109          7       7       7       7     7
11           8       8       8       8     8
110          4       4       4       4     4
112          3       3       3       3     3
113          1       1       1       1     1
114          6       6       6       6     6
115          7       7       7       7     7
116          3       3       3       3     3
117          1       1       1       1     1
118          3       3       3       3     3
119          5       5       5       5     5
12           1       1       1       1     1
121          8       8       8       8     8
122          4       4       4       4     4
123          5       5       5       5     5
124          9       9       9       9     9
125          3       3       3       3     3
126          4       4       4       4     4
127          1       1       1       1     1
...        ...     ...     ...     ...   ...
71           6       6       6       6     6
72           7       7       7       7     7
73           3       3       3       3     3
74           2       2       2       2     2
75           7       7       7       7     7
76           7       7       7       7     7
77           4       4       4       4     4
78           5       5       5       5     5
79           8       8       8       8     8
8            3       3       3       3     3
80           1       1       1       1     1
81           4       4       4       4     4
82           9       9       9       9     9
83           8       8       8       8     8
85           5       5       5       5     5
86           4       4       4       4     4
87           4       4       4       4     4
88           4       4       4       4     4
89           8       8       8       8     8
9            1       1       1       1     1
90           7       7       7       7     7
91           3       3       3       3     3
92           2       2       2       2     2
93           4       4       4       4     4
94           2       2       2       2     2
95           3       3       3       3     3
96           5       5       5       5     5
97          10      10      10      10    10
98           1       1       1       1     1
99           8       8       8       8     8

[197 rows x 5 columns]

In [320]: gdf
Out[320]:
    Family  Father  Mother Gender  Height  Kids
0        1    78.5    67.0      M    73.2     4
1        1    78.5    67.0      F    69.2     4
2        1    78.5    67.0      F    69.0     4
3        1    78.5    67.0      F    69.0     4
4        2    75.5    66.5      M    73.5     4
5        2    75.5    66.5      M    72.5     4
6        2    75.5    66.5      F    65.5     4
7        2    75.5    66.5      F    65.5     4
8        3    75.0    64.0      M    71.0     2
9        3    75.0    64.0      F    68.0     2
10       4    75.0    64.0      M    70.5     5
11       4    75.0    64.0      M    68.5     5
12       4    75.0    64.0      F    67.0     5
13       4    75.0    64.0      F    64.5     5
14       4    75.0    64.0      F    63.0     5
15       5    75.0    58.5      M    72.0     6
16       5    75.0    58.5      M    69.0     6
17       5    75.0    58.5      M    68.0     6
18       5    75.0    58.5      F    66.5     6
19       5    75.0    58.5      F    62.5     6
20       5    75.0    58.5      F    62.5     6
21       6    74.0    68.0      F    69.5     1
22       7    74.0    68.0      M    76.5     6
23       7    74.0    68.0      M    74.0     6
24       7    74.0    68.0      M    73.0     6
25       7    74.0    68.0      M    73.0     6
26       7    74.0    68.0      F    70.5     6
27       7    74.0    68.0      F    64.0     6
28       8    74.0    66.5      F    70.5     3
29       8    74.0    66.5      F    68.0     3
..     ...     ...     ...    ...     ...   ...
868    198    64.0    64.0      M    71.5     7
869    198    64.0    64.0      M    68.0     7
870    198    64.0    64.0      F    65.5     7
871    198    64.0    64.0      F    64.0     7
872    198    64.0    64.0      F    62.0     7
873    198    64.0    64.0      F    62.0     7
874    198    64.0    64.0      F    61.0     7
875    199    64.0    64.0      M    70.5     7
876    199    64.0    64.0      M    68.0     7
877    199    64.0    64.0      F    67.0     7
878    199    64.0    64.0      F    65.0     7
879    199    64.0    64.0      F    64.0     7
880    199    64.0    64.0      F    64.0     7
881    199    64.0    64.0      F    60.0     7
882    200    64.0    63.0      M    64.5     1
883    201    64.0    60.0      M    66.0     2
884    201    64.0    60.0      F    60.0     2
885    203    62.0    66.0      M    64.0     3
886    203    62.0    66.0      F    62.0     3
887    203    62.0    66.0      F    61.0     3
888    204    62.5    63.0      M    66.5     2
889    204    62.5    63.0      F    57.0     2
890   136A    68.5    65.0      M    72.0     8
891   136A    68.5    65.0      M    70.5     8
892   136A    68.5    65.0      M    68.7     8
893   136A    68.5    65.0      M    68.5     8
894   136A    68.5    65.0      M    67.7     8
895   136A    68.5    65.0      F    64.0     8
896   136A    68.5    65.0      F    63.5     8
897   136A    68.5    65.0      F    63.0     8

[898 rows x 6 columns]

In [321]: gdf.groupby('Family').count()
Out[321]:
        Father  Mother  Gender  Height  Kids
Family
1            4       4       4       4     4
10           1       1       1       1     1
100          3       3       3       3     3
101          6       6       6       6     6
102          6       6       6       6     6
103          5       5       5       5     5
104          4       4       4       4     4
105          6       6       6       6     6
106          7       7       7       7     7
107          9       9       9       9     9
108          7       7       7       7     7
109          7       7       7       7     7
11           8       8       8       8     8
110          4       4       4       4     4
112          3       3       3       3     3
113          1       1       1       1     1
114          6       6       6       6     6
115          7       7       7       7     7
116          3       3       3       3     3
117          1       1       1       1     1
118          3       3       3       3     3
119          5       5       5       5     5
12           1       1       1       1     1
121          8       8       8       8     8
122          4       4       4       4     4
123          5       5       5       5     5
124          9       9       9       9     9
125          3       3       3       3     3
126          4       4       4       4     4
127          1       1       1       1     1
...        ...     ...     ...     ...   ...
71           6       6       6       6     6
72           7       7       7       7     7
73           3       3       3       3     3
74           2       2       2       2     2
75           7       7       7       7     7
76           7       7       7       7     7
77           4       4       4       4     4
78           5       5       5       5     5
79           8       8       8       8     8
8            3       3       3       3     3
80           1       1       1       1     1
81           4       4       4       4     4
82           9       9       9       9     9
83           8       8       8       8     8
85           5       5       5       5     5
86           4       4       4       4     4
87           4       4       4       4     4
88           4       4       4       4     4
89           8       8       8       8     8
9            1       1       1       1     1
90           7       7       7       7     7
91           3       3       3       3     3
92           2       2       2       2     2
93           4       4       4       4     4
94           2       2       2       2     2
95           3       3       3       3     3
96           5       5       5       5     5
97          10      10      10      10    10
98           1       1       1       1     1
99           8       8       8       8     8

[197 rows x 5 columns]

In [322]: gdf.groupby('Family').count().sort_values('Family')
Out[322]:
        Father  Mother  Gender  Height  Kids
Family
1            4       4       4       4     4
10           1       1       1       1     1
100          3       3       3       3     3
101          6       6       6       6     6
102          6       6       6       6     6
103          5       5       5       5     5
104          4       4       4       4     4
105          6       6       6       6     6
106          7       7       7       7     7
107          9       9       9       9     9
108          7       7       7       7     7
109          7       7       7       7     7
11           8       8       8       8     8
110          4       4       4       4     4
112          3       3       3       3     3
113          1       1       1       1     1
114          6       6       6       6     6
115          7       7       7       7     7
116          3       3       3       3     3
117          1       1       1       1     1
118          3       3       3       3     3
119          5       5       5       5     5
12           1       1       1       1     1
121          8       8       8       8     8
122          4       4       4       4     4
123          5       5       5       5     5
124          9       9       9       9     9
125          3       3       3       3     3
126          4       4       4       4     4
127          1       1       1       1     1
...        ...     ...     ...     ...   ...
71           6       6       6       6     6
72           7       7       7       7     7
73           3       3       3       3     3
74           2       2       2       2     2
75           7       7       7       7     7
76           7       7       7       7     7
77           4       4       4       4     4
78           5       5       5       5     5
79           8       8       8       8     8
8            3       3       3       3     3
80           1       1       1       1     1
81           4       4       4       4     4
82           9       9       9       9     9
83           8       8       8       8     8
85           5       5       5       5     5
86           4       4       4       4     4
87           4       4       4       4     4
88           4       4       4       4     4
89           8       8       8       8     8
9            1       1       1       1     1
90           7       7       7       7     7
91           3       3       3       3     3
92           2       2       2       2     2
93           4       4       4       4     4
94           2       2       2       2     2
95           3       3       3       3     3
96           5       5       5       5     5
97          10      10      10      10    10
98           1       1       1       1     1
99           8       8       8       8     8

[197 rows x 5 columns]

In [323]: gdf.groupby('Family').count()
Out[323]:
        Father  Mother  Gender  Height  Kids
Family
1            4       4       4       4     4
10           1       1       1       1     1
100          3       3       3       3     3
101          6       6       6       6     6
102          6       6       6       6     6
103          5       5       5       5     5
104          4       4       4       4     4
105          6       6       6       6     6
106          7       7       7       7     7
107          9       9       9       9     9
108          7       7       7       7     7
109          7       7       7       7     7
11           8       8       8       8     8
110          4       4       4       4     4
112          3       3       3       3     3
113          1       1       1       1     1
114          6       6       6       6     6
115          7       7       7       7     7
116          3       3       3       3     3
117          1       1       1       1     1
118          3       3       3       3     3
119          5       5       5       5     5
12           1       1       1       1     1
121          8       8       8       8     8
122          4       4       4       4     4
123          5       5       5       5     5
124          9       9       9       9     9
125          3       3       3       3     3
126          4       4       4       4     4
127          1       1       1       1     1
...        ...     ...     ...     ...   ...
71           6       6       6       6     6
72           7       7       7       7     7
73           3       3       3       3     3
74           2       2       2       2     2
75           7       7       7       7     7
76           7       7       7       7     7
77           4       4       4       4     4
78           5       5       5       5     5
79           8       8       8       8     8
8            3       3       3       3     3
80           1       1       1       1     1
81           4       4       4       4     4
82           9       9       9       9     9
83           8       8       8       8     8
85           5       5       5       5     5
86           4       4       4       4     4
87           4       4       4       4     4
88           4       4       4       4     4
89           8       8       8       8     8
9            1       1       1       1     1
90           7       7       7       7     7
91           3       3       3       3     3
92           2       2       2       2     2
93           4       4       4       4     4
94           2       2       2       2     2
95           3       3       3       3     3
96           5       5       5       5     5
97          10      10      10      10    10
98           1       1       1       1     1
99           8       8       8       8     8

[197 rows x 5 columns]

In [324]: gdf.groupby('Family').count().sum()
Out[324]:
Father    898
Mother    898
Gender    898
Height    898
Kids      898
dtype: int64

In [325]: gdf.groupby('Family').count().sum()['Kids']
Out[325]: 898

In [326]: gdf.shape
Out[326]: (898, 6)

In [327]: gdf.groupby('Family').sum()['Kids']
Out[327]:
Family
1       16
10       1
100      9
101     36
102     36
103     25
104     16
105     36
106     49
107     81
108     49
109     49
11      64
110     16
112      9
113      1
114     36
115     49
116      9
117      1
118      9
119     25
12       1
121     64
122     16
123     25
124     81
125      9
126     16
127      1
      ...
71      36
72      49
73       9
74       4
75      49
76      49
77      16
78      25
79      64
8        9
80       1
81      16
82      81
83      64
85      25
86      16
87      16
88      16
89      64
9        1
90      49
91       9
92       4
93      16
94       4
95       9
96      25
97     100
98       1
99      64
Name: Kids, Length: 197, dtype: int64

In [328]: gdf.groupby('Family').count()['Kids']
Out[328]:
Family
1       4
10      1
100     3
101     6
102     6
103     5
104     4
105     6
106     7
107     9
108     7
109     7
11      8
110     4
112     3
113     1
114     6
115     7
116     3
117     1
118     3
119     5
12      1
121     8
122     4
123     5
124     9
125     3
126     4
127     1
       ..
71      6
72      7
73      3
74      2
75      7
76      7
77      4
78      5
79      8
8       3
80      1
81      4
82      9
83      8
85      5
86      4
87      4
88      4
89      8
9       1
90      7
91      3
92      2
93      4
94      2
95      3
96      5
97     10
98      1
99      8
Name: Kids, Length: 197, dtype: int64

In [329]: gdf.groupby('Family').count()
Out[329]:
        Father  Mother  Gender  Height  Kids
Family
1            4       4       4       4     4
10           1       1       1       1     1
100          3       3       3       3     3
101          6       6       6       6     6
102          6       6       6       6     6
103          5       5       5       5     5
104          4       4       4       4     4
105          6       6       6       6     6
106          7       7       7       7     7
107          9       9       9       9     9
108          7       7       7       7     7
109          7       7       7       7     7
11           8       8       8       8     8
110          4       4       4       4     4
112          3       3       3       3     3
113          1       1       1       1     1
114          6       6       6       6     6
115          7       7       7       7     7
116          3       3       3       3     3
117          1       1       1       1     1
118          3       3       3       3     3
119          5       5       5       5     5
12           1       1       1       1     1
121          8       8       8       8     8
122          4       4       4       4     4
123          5       5       5       5     5
124          9       9       9       9     9
125          3       3       3       3     3
126          4       4       4       4     4
127          1       1       1       1     1
...        ...     ...     ...     ...   ...
71           6       6       6       6     6
72           7       7       7       7     7
73           3       3       3       3     3
74           2       2       2       2     2
75           7       7       7       7     7
76           7       7       7       7     7
77           4       4       4       4     4
78           5       5       5       5     5
79           8       8       8       8     8
8            3       3       3       3     3
80           1       1       1       1     1
81           4       4       4       4     4
82           9       9       9       9     9
83           8       8       8       8     8
85           5       5       5       5     5
86           4       4       4       4     4
87           4       4       4       4     4
88           4       4       4       4     4
89           8       8       8       8     8
9            1       1       1       1     1
90           7       7       7       7     7
91           3       3       3       3     3
92           2       2       2       2     2
93           4       4       4       4     4
94           2       2       2       2     2
95           3       3       3       3     3
96           5       5       5       5     5
97          10      10      10      10    10
98           1       1       1       1     1
99           8       8       8       8     8

[197 rows x 5 columns]

In [330]: gdf.shape
Out[330]: (898, 6)

In [331]: gdf = pd.read_csv('Galton.csv')

In [332]: gdf
Out[332]:
    Family  Father  Mother Gender  Height  Kids
0        1    78.5    67.0      M    73.2     4
1        1    78.5    67.0      F    69.2     4
2        1    78.5    67.0      F    69.0     4
3        1    78.5    67.0      F    69.0     4
4        2    75.5    66.5      M    73.5     4
5        2    75.5    66.5      M    72.5     4
6        2    75.5    66.5      F    65.5     4
7        2    75.5    66.5      F    65.5     4
8        3    75.0    64.0      M    71.0     2
9        3    75.0    64.0      F    68.0     2
10       4    75.0    64.0      M    70.5     5
11       4    75.0    64.0      M    68.5     5
12       4    75.0    64.0      F    67.0     5
13       4    75.0    64.0      F    64.5     5
14       4    75.0    64.0      F    63.0     5
15       5    75.0    58.5      M    72.0     6
16       5    75.0    58.5      M    69.0     6
17       5    75.0    58.5      M    68.0     6
18       5    75.0    58.5      F    66.5     6
19       5    75.0    58.5      F    62.5     6
20       5    75.0    58.5      F    62.5     6
21       6    74.0    68.0      F    69.5     1
22       7    74.0    68.0      M    76.5     6
23       7    74.0    68.0      M    74.0     6
24       7    74.0    68.0      M    73.0     6
25       7    74.0    68.0      M    73.0     6
26       7    74.0    68.0      F    70.5     6
27       7    74.0    68.0      F    64.0     6
28       8    74.0    66.5      F    70.5     3
29       8    74.0    66.5      F    68.0     3
..     ...     ...     ...    ...     ...   ...
868    198    64.0    64.0      M    71.5     7
869    198    64.0    64.0      M    68.0     7
870    198    64.0    64.0      F    65.5     7
871    198    64.0    64.0      F    64.0     7
872    198    64.0    64.0      F    62.0     7
873    198    64.0    64.0      F    62.0     7
874    198    64.0    64.0      F    61.0     7
875    199    64.0    64.0      M    70.5     7
876    199    64.0    64.0      M    68.0     7
877    199    64.0    64.0      F    67.0     7
878    199    64.0    64.0      F    65.0     7
879    199    64.0    64.0      F    64.0     7
880    199    64.0    64.0      F    64.0     7
881    199    64.0    64.0      F    60.0     7
882    200    64.0    63.0      M    64.5     1
883    201    64.0    60.0      M    66.0     2
884    201    64.0    60.0      F    60.0     2
885    203    62.0    66.0      M    64.0     3
886    203    62.0    66.0      F    62.0     3
887    203    62.0    66.0      F    61.0     3
888    204    62.5    63.0      M    66.5     2
889    204    62.5    63.0      F    57.0     2
890   136A    68.5    65.0      M    72.0     8
891   136A    68.5    65.0      M    70.5     8
892   136A    68.5    65.0      M    68.7     8
893   136A    68.5    65.0      M    68.5     8
894   136A    68.5    65.0      M    67.7     8
895   136A    68.5    65.0      F    64.0     8
896   136A    68.5    65.0      F    63.5     8
897   136A    68.5    65.0      F    63.0     8

[898 rows x 6 columns]

In [333]: gdf.shape
Out[333]: (898, 6)

In [334]: len(gdf)
Out[334]: 898

In [335]: gdf
Out[335]:
    Family  Father  Mother Gender  Height  Kids
0        1    78.5    67.0      M    73.2     4
1        1    78.5    67.0      F    69.2     4
2        1    78.5    67.0      F    69.0     4
3        1    78.5    67.0      F    69.0     4
4        2    75.5    66.5      M    73.5     4
5        2    75.5    66.5      M    72.5     4
6        2    75.5    66.5      F    65.5     4
7        2    75.5    66.5      F    65.5     4
8        3    75.0    64.0      M    71.0     2
9        3    75.0    64.0      F    68.0     2
10       4    75.0    64.0      M    70.5     5
11       4    75.0    64.0      M    68.5     5
12       4    75.0    64.0      F    67.0     5
13       4    75.0    64.0      F    64.5     5
14       4    75.0    64.0      F    63.0     5
15       5    75.0    58.5      M    72.0     6
16       5    75.0    58.5      M    69.0     6
17       5    75.0    58.5      M    68.0     6
18       5    75.0    58.5      F    66.5     6
19       5    75.0    58.5      F    62.5     6
20       5    75.0    58.5      F    62.5     6
21       6    74.0    68.0      F    69.5     1
22       7    74.0    68.0      M    76.5     6
23       7    74.0    68.0      M    74.0     6
24       7    74.0    68.0      M    73.0     6
25       7    74.0    68.0      M    73.0     6
26       7    74.0    68.0      F    70.5     6
27       7    74.0    68.0      F    64.0     6
28       8    74.0    66.5      F    70.5     3
29       8    74.0    66.5      F    68.0     3
..     ...     ...     ...    ...     ...   ...
868    198    64.0    64.0      M    71.5     7
869    198    64.0    64.0      M    68.0     7
870    198    64.0    64.0      F    65.5     7
871    198    64.0    64.0      F    64.0     7
872    198    64.0    64.0      F    62.0     7
873    198    64.0    64.0      F    62.0     7
874    198    64.0    64.0      F    61.0     7
875    199    64.0    64.0      M    70.5     7
876    199    64.0    64.0      M    68.0     7
877    199    64.0    64.0      F    67.0     7
878    199    64.0    64.0      F    65.0     7
879    199    64.0    64.0      F    64.0     7
880    199    64.0    64.0      F    64.0     7
881    199    64.0    64.0      F    60.0     7
882    200    64.0    63.0      M    64.5     1
883    201    64.0    60.0      M    66.0     2
884    201    64.0    60.0      F    60.0     2
885    203    62.0    66.0      M    64.0     3
886    203    62.0    66.0      F    62.0     3
887    203    62.0    66.0      F    61.0     3
888    204    62.5    63.0      M    66.5     2
889    204    62.5    63.0      F    57.0     2
890   136A    68.5    65.0      M    72.0     8
891   136A    68.5    65.0      M    70.5     8
892   136A    68.5    65.0      M    68.7     8
893   136A    68.5    65.0      M    68.5     8
894   136A    68.5    65.0      M    67.7     8
895   136A    68.5    65.0      F    64.0     8
896   136A    68.5    65.0      F    63.5     8
897   136A    68.5    65.0      F    63.0     8

[898 rows x 6 columns]

In [336]: gdf.groupby('Family')
Out[336]: <pandas.core.groupby.generic.DataFrameGroupBy object at 0x7fd223703eb8>

In [337]: gdf.groupby('Family').count()
Out[337]:
        Father  Mother  Gender  Height  Kids
Family
1            4       4       4       4     4
10           1       1       1       1     1
100          3       3       3       3     3
101          6       6       6       6     6
102          6       6       6       6     6
103          5       5       5       5     5
104          4       4       4       4     4
105          6       6       6       6     6
106          7       7       7       7     7
107          9       9       9       9     9
108          7       7       7       7     7
109          7       7       7       7     7
11           8       8       8       8     8
110          4       4       4       4     4
112          3       3       3       3     3
113          1       1       1       1     1
114          6       6       6       6     6
115          7       7       7       7     7
116          3       3       3       3     3
117          1       1       1       1     1
118          3       3       3       3     3
119          5       5       5       5     5
12           1       1       1       1     1
121          8       8       8       8     8
122          4       4       4       4     4
123          5       5       5       5     5
124          9       9       9       9     9
125          3       3       3       3     3
126          4       4       4       4     4
127          1       1       1       1     1
...        ...     ...     ...     ...   ...
71           6       6       6       6     6
72           7       7       7       7     7
73           3       3       3       3     3
74           2       2       2       2     2
75           7       7       7       7     7
76           7       7       7       7     7
77           4       4       4       4     4
78           5       5       5       5     5
79           8       8       8       8     8
8            3       3       3       3     3
80           1       1       1       1     1
81           4       4       4       4     4
82           9       9       9       9     9
83           8       8       8       8     8
85           5       5       5       5     5
86           4       4       4       4     4
87           4       4       4       4     4
88           4       4       4       4     4
89           8       8       8       8     8
9            1       1       1       1     1
90           7       7       7       7     7
91           3       3       3       3     3
92           2       2       2       2     2
93           4       4       4       4     4
94           2       2       2       2     2
95           3       3       3       3     3
96           5       5       5       5     5
97          10      10      10      10    10
98           1       1       1       1     1
99           8       8       8       8     8

[197 rows x 5 columns]

In [338]: gdf.groupby('Family').count()['Kids']
Out[338]:
Family
1       4
10      1
100     3
101     6
102     6
103     5
104     4
105     6
106     7
107     9
108     7
109     7
11      8
110     4
112     3
113     1
114     6
115     7
116     3
117     1
118     3
119     5
12      1
121     8
122     4
123     5
124     9
125     3
126     4
127     1
       ..
71      6
72      7
73      3
74      2
75      7
76      7
77      4
78      5
79      8
8       3
80      1
81      4
82      9
83      8
85      5
86      4
87      4
88      4
89      8
9       1
90      7
91      3
92      2
93      4
94      2
95      3
96      5
97     10
98      1
99      8
Name: Kids, Length: 197, dtype: int64

In [339]: gdf.groupby('Family').count()['Kids'].sum()
Out[339]: 898

In [340]: gdf.shape
Out[340]: (898, 6)

In [341]: gdf
Out[341]:
    Family  Father  Mother Gender  Height  Kids
0        1    78.5    67.0      M    73.2     4
1        1    78.5    67.0      F    69.2     4
2        1    78.5    67.0      F    69.0     4
3        1    78.5    67.0      F    69.0     4
4        2    75.5    66.5      M    73.5     4
5        2    75.5    66.5      M    72.5     4
6        2    75.5    66.5      F    65.5     4
7        2    75.5    66.5      F    65.5     4
8        3    75.0    64.0      M    71.0     2
9        3    75.0    64.0      F    68.0     2
10       4    75.0    64.0      M    70.5     5
11       4    75.0    64.0      M    68.5     5
12       4    75.0    64.0      F    67.0     5
13       4    75.0    64.0      F    64.5     5
14       4    75.0    64.0      F    63.0     5
15       5    75.0    58.5      M    72.0     6
16       5    75.0    58.5      M    69.0     6
17       5    75.0    58.5      M    68.0     6
18       5    75.0    58.5      F    66.5     6
19       5    75.0    58.5      F    62.5     6
20       5    75.0    58.5      F    62.5     6
21       6    74.0    68.0      F    69.5     1
22       7    74.0    68.0      M    76.5     6
23       7    74.0    68.0      M    74.0     6
24       7    74.0    68.0      M    73.0     6
25       7    74.0    68.0      M    73.0     6
26       7    74.0    68.0      F    70.5     6
27       7    74.0    68.0      F    64.0     6
28       8    74.0    66.5      F    70.5     3
29       8    74.0    66.5      F    68.0     3
..     ...     ...     ...    ...     ...   ...
868    198    64.0    64.0      M    71.5     7
869    198    64.0    64.0      M    68.0     7
870    198    64.0    64.0      F    65.5     7
871    198    64.0    64.0      F    64.0     7
872    198    64.0    64.0      F    62.0     7
873    198    64.0    64.0      F    62.0     7
874    198    64.0    64.0      F    61.0     7
875    199    64.0    64.0      M    70.5     7
876    199    64.0    64.0      M    68.0     7
877    199    64.0    64.0      F    67.0     7
878    199    64.0    64.0      F    65.0     7
879    199    64.0    64.0      F    64.0     7
880    199    64.0    64.0      F    64.0     7
881    199    64.0    64.0      F    60.0     7
882    200    64.0    63.0      M    64.5     1
883    201    64.0    60.0      M    66.0     2
884    201    64.0    60.0      F    60.0     2
885    203    62.0    66.0      M    64.0     3
886    203    62.0    66.0      F    62.0     3
887    203    62.0    66.0      F    61.0     3
888    204    62.5    63.0      M    66.5     2
889    204    62.5    63.0      F    57.0     2
890   136A    68.5    65.0      M    72.0     8
891   136A    68.5    65.0      M    70.5     8
892   136A    68.5    65.0      M    68.7     8
893   136A    68.5    65.0      M    68.5     8
894   136A    68.5    65.0      M    67.7     8
895   136A    68.5    65.0      F    64.0     8
896   136A    68.5    65.0      F    63.5     8
897   136A    68.5    65.0      F    63.0     8

[898 rows x 6 columns]

In [342]: gdf.columns
Out[342]: Index(['Family', 'Father', 'Mother', 'Gender', 'Height', 'Kids'], dtype='object')

In [343]: gdf['Height']
Out[343]:
0      73.2
1      69.2
2      69.0
3      69.0
4      73.5
5      72.5
6      65.5
7      65.5
8      71.0
9      68.0
10     70.5
11     68.5
12     67.0
13     64.5
14     63.0
15     72.0
16     69.0
17     68.0
18     66.5
19     62.5
20     62.5
21     69.5
22     76.5
23     74.0
24     73.0
25     73.0
26     70.5
27     64.0
28     70.5
29     68.0
       ...
868    71.5
869    68.0
870    65.5
871    64.0
872    62.0
873    62.0
874    61.0
875    70.5
876    68.0
877    67.0
878    65.0
879    64.0
880    64.0
881    60.0
882    64.5
883    66.0
884    60.0
885    64.0
886    62.0
887    61.0
888    66.5
889    57.0
890    72.0
891    70.5
892    68.7
893    68.5
894    67.7
895    64.0
896    63.5
897    63.0
Name: Height, Length: 898, dtype: float64

In [344]: gdf['Height'].mean()
Out[344]: 66.76069042316259

In [345]: gdf.mean()
Out[345]:
Father    69.232851
Mother    64.084410
Height    66.760690
Kids       6.135857
dtype: float64

In [346]: gdf.mean()['Height']
Out[346]: 66.76069042316252

In [347]: gdf['Height'].hist()
Out[347]: <matplotlib.axes._subplots.AxesSubplot at 0x7fd2516ec198>

In [348]: gdf['Family'].nunique()
Out[348]: 197

In [349]: gdf['Family'] != '136A'
Out[349]:
0       True
1       True
2       True
3       True
4       True
5       True
6       True
7       True
8       True
9       True
10      True
11      True
12      True
13      True
14      True
15      True
16      True
17      True
18      True
19      True
20      True
21      True
22      True
23      True
24      True
25      True
26      True
27      True
28      True
29      True
       ...
868     True
869     True
870     True
871     True
872     True
873     True
874     True
875     True
876     True
877     True
878     True
879     True
880     True
881     True
882     True
883     True
884     True
885     True
886     True
887     True
888     True
889     True
890    False
891    False
892    False
893    False
894    False
895    False
896    False
897    False
Name: Family, Length: 898, dtype: bool

In [350]: gdf[gdf['Family'] != '136A']
Out[350]:
    Family  Father  Mother Gender  Height  Kids
0        1    78.5    67.0      M    73.2     4
1        1    78.5    67.0      F    69.2     4
2        1    78.5    67.0      F    69.0     4
3        1    78.5    67.0      F    69.0     4
4        2    75.5    66.5      M    73.5     4
5        2    75.5    66.5      M    72.5     4
6        2    75.5    66.5      F    65.5     4
7        2    75.5    66.5      F    65.5     4
8        3    75.0    64.0      M    71.0     2
9        3    75.0    64.0      F    68.0     2
10       4    75.0    64.0      M    70.5     5
11       4    75.0    64.0      M    68.5     5
12       4    75.0    64.0      F    67.0     5
13       4    75.0    64.0      F    64.5     5
14       4    75.0    64.0      F    63.0     5
15       5    75.0    58.5      M    72.0     6
16       5    75.0    58.5      M    69.0     6
17       5    75.0    58.5      M    68.0     6
18       5    75.0    58.5      F    66.5     6
19       5    75.0    58.5      F    62.5     6
20       5    75.0    58.5      F    62.5     6
21       6    74.0    68.0      F    69.5     1
22       7    74.0    68.0      M    76.5     6
23       7    74.0    68.0      M    74.0     6
24       7    74.0    68.0      M    73.0     6
25       7    74.0    68.0      M    73.0     6
26       7    74.0    68.0      F    70.5     6
27       7    74.0    68.0      F    64.0     6
28       8    74.0    66.5      F    70.5     3
29       8    74.0    66.5      F    68.0     3
..     ...     ...     ...    ...     ...   ...
860    196    65.5    63.0      M    71.0     4
861    196    65.5    63.0      M    69.0     4
862    196    65.5    63.0      F    63.5     4
863    197    65.5    60.0      M    68.0     5
864    197    65.5    60.0      M    68.0     5
865    197    65.5    60.0      M    67.0     5
866    197    65.5    60.0      M    67.0     5
867    197    65.5    60.0      F    62.0     5
868    198    64.0    64.0      M    71.5     7
869    198    64.0    64.0      M    68.0     7
870    198    64.0    64.0      F    65.5     7
871    198    64.0    64.0      F    64.0     7
872    198    64.0    64.0      F    62.0     7
873    198    64.0    64.0      F    62.0     7
874    198    64.0    64.0      F    61.0     7
875    199    64.0    64.0      M    70.5     7
876    199    64.0    64.0      M    68.0     7
877    199    64.0    64.0      F    67.0     7
878    199    64.0    64.0      F    65.0     7
879    199    64.0    64.0      F    64.0     7
880    199    64.0    64.0      F    64.0     7
881    199    64.0    64.0      F    60.0     7
882    200    64.0    63.0      M    64.5     1
883    201    64.0    60.0      M    66.0     2
884    201    64.0    60.0      F    60.0     2
885    203    62.0    66.0      M    64.0     3
886    203    62.0    66.0      F    62.0     3
887    203    62.0    66.0      F    61.0     3
888    204    62.5    63.0      M    66.5     2
889    204    62.5    63.0      F    57.0     2

[890 rows x 6 columns]

In [351]: gdf['Father'].mean()
Out[351]: 69.23285077951002

In [352]: gdf.groupby('Father')
Out[352]: <pandas.core.groupby.generic.DataFrameGroupBy object at 0x7fd2515d9eb8>

In [353]: gdf.groupby('Father').mean()
Out[353]:
           Mother     Height      Kids
Father
62.0    66.000000  62.333333  3.000000
62.5    63.000000  61.750000  2.000000
64.0    63.470588  64.882353  6.058824
65.0    64.972973  64.935135  5.486486
65.5    61.333333  67.388889  4.555556
66.0    63.666667  65.170175  8.403509
66.5    63.595238  64.423810  7.095238
67.0    64.650000  67.017500  5.050000
67.5    64.062500  65.656250  9.125000
68.0    62.786275  65.499020  6.764706
68.2    63.500000  67.200000  5.000000
68.5    65.214286  67.405714  7.571429
68.7    66.250000  65.525000  2.000000
69.0    64.410435  67.056522  6.547826
69.2    64.000000  66.675000  4.000000
69.5    64.250000  67.100000  5.692308
69.7    62.000000  62.500000  1.000000
70.0    64.362595  66.948855  6.053435
70.3    62.700000  66.500000  7.000000
70.5    63.485294  67.211765  6.000000
71.0    64.123596  67.715730  5.516854
71.2    63.000000  66.000000  2.000000
71.5    64.772727  67.672727  5.181818
71.7    64.700000  70.200000  3.400000
72.0    63.773810  68.247619  4.619048
72.5    62.500000  67.600000  5.000000
72.7    69.000000  70.050000  8.000000
73.0    65.108696  67.947826  6.043478
73.2    63.000000  62.700000  1.000000
74.0    64.900000  68.700000  5.600000
74.5    66.000000  66.000000  1.000000
75.0    61.461538  67.153846  5.000000
75.5    66.500000  69.250000  4.000000
78.5    67.000000  70.100000  4.000000

In [354]: gdf.groupby('Family').mean()
Out[354]:
        Father  Mother     Height  Kids
Family
1         78.5    67.0  70.100000     4
10        74.0    65.5  65.500000     1
100       69.0    66.0  70.733333     3
101       69.0    66.7  70.416667     6
102       69.0    66.0  66.166667     6
103       69.0    66.5  69.200000     5
104       69.5    66.5  66.625000     4
105       69.0    66.5  66.500000     6
106       69.5    66.0  68.500000     7
107       69.0    66.0  67.722222     9
108       69.0    65.0  65.571429     7
109       69.5    64.5  64.442857     7
11        74.0    62.0  67.312500     8
110       69.2    64.0  66.675000     4
112       69.0    63.0  66.666667     3
113       69.0    63.0  72.000000     1
114       69.0    63.0  67.500000     6
115       69.0    63.5  64.928571     7
116       69.0    63.5  65.733333     3
117       69.7    62.0  62.500000     1
118       69.5    62.0  71.333333     3
119       69.0    62.0  69.400000     5
12        74.0    61.0  65.000000     1
121       69.0    62.5  66.312500     8
122       69.0    62.0  68.000000     4
123       69.5    61.0  66.700000     5
124       69.0    61.0  64.555556     9
125       69.0    60.0  67.000000     3
126       69.0    60.0  64.300000     4
127       69.0    60.5  69.500000     1
...        ...     ...        ...   ...
71        70.0    65.0  66.666667     6
72        70.0    65.0  69.814286     7
73        70.0    65.0  70.166667     3
74        70.0    65.0  69.000000     2
75        70.0    64.7  67.414286     7
76        70.0    64.0  67.671429     7
77        70.0    64.0  67.550000     4
78        70.0    64.2  65.160000     5
79        70.5    64.0  68.375000     8
8         74.0    66.5  68.166667     3
80        70.5    64.5  60.000000     1
81        70.0    64.0  64.750000     4
82        70.0    64.0  68.555556     9
83        70.0    63.7  64.387500     8
85        70.5    63.0  67.400000     5
86        70.0    63.5  67.375000     4
87        70.0    63.0  65.175000     4
88        70.0    63.0  64.875000     4
89        70.5    62.0  67.625000     8
9         74.5    66.0  66.000000     1
90        70.3    62.7  66.500000     7
91        70.5    62.0  68.000000     3
92        70.0    61.0  69.100000     2
93        70.0    60.0  64.875000     4
94        70.0    60.0  65.000000     2
95        70.0    58.5  66.333333     3
96        70.0    58.0  66.400000     5
97        69.0    68.5  67.150000    10
98        69.0    67.0  64.000000     1
99        69.0    66.0  67.987500     8

[197 rows x 4 columns]

In [355]: gdf.groupby('Family')
Out[355]: <pandas.core.groupby.generic.DataFrameGroupBy object at 0x7fd2515ed828>

In [356]: gdf
Out[356]:
    Family  Father  Mother Gender  Height  Kids
0        1    78.5    67.0      M    73.2     4
1        1    78.5    67.0      F    69.2     4
2        1    78.5    67.0      F    69.0     4
3        1    78.5    67.0      F    69.0     4
4        2    75.5    66.5      M    73.5     4
5        2    75.5    66.5      M    72.5     4
6        2    75.5    66.5      F    65.5     4
7        2    75.5    66.5      F    65.5     4
8        3    75.0    64.0      M    71.0     2
9        3    75.0    64.0      F    68.0     2
10       4    75.0    64.0      M    70.5     5
11       4    75.0    64.0      M    68.5     5
12       4    75.0    64.0      F    67.0     5
13       4    75.0    64.0      F    64.5     5
14       4    75.0    64.0      F    63.0     5
15       5    75.0    58.5      M    72.0     6
16       5    75.0    58.5      M    69.0     6
17       5    75.0    58.5      M    68.0     6
18       5    75.0    58.5      F    66.5     6
19       5    75.0    58.5      F    62.5     6
20       5    75.0    58.5      F    62.5     6
21       6    74.0    68.0      F    69.5     1
22       7    74.0    68.0      M    76.5     6
23       7    74.0    68.0      M    74.0     6
24       7    74.0    68.0      M    73.0     6
25       7    74.0    68.0      M    73.0     6
26       7    74.0    68.0      F    70.5     6
27       7    74.0    68.0      F    64.0     6
28       8    74.0    66.5      F    70.5     3
29       8    74.0    66.5      F    68.0     3
..     ...     ...     ...    ...     ...   ...
868    198    64.0    64.0      M    71.5     7
869    198    64.0    64.0      M    68.0     7
870    198    64.0    64.0      F    65.5     7
871    198    64.0    64.0      F    64.0     7
872    198    64.0    64.0      F    62.0     7
873    198    64.0    64.0      F    62.0     7
874    198    64.0    64.0      F    61.0     7
875    199    64.0    64.0      M    70.5     7
876    199    64.0    64.0      M    68.0     7
877    199    64.0    64.0      F    67.0     7
878    199    64.0    64.0      F    65.0     7
879    199    64.0    64.0      F    64.0     7
880    199    64.0    64.0      F    64.0     7
881    199    64.0    64.0      F    60.0     7
882    200    64.0    63.0      M    64.5     1
883    201    64.0    60.0      M    66.0     2
884    201    64.0    60.0      F    60.0     2
885    203    62.0    66.0      M    64.0     3
886    203    62.0    66.0      F    62.0     3
887    203    62.0    66.0      F    61.0     3
888    204    62.5    63.0      M    66.5     2
889    204    62.5    63.0      F    57.0     2
890   136A    68.5    65.0      M    72.0     8
891   136A    68.5    65.0      M    70.5     8
892   136A    68.5    65.0      M    68.7     8
893   136A    68.5    65.0      M    68.5     8
894   136A    68.5    65.0      M    67.7     8
895   136A    68.5    65.0      F    64.0     8
896   136A    68.5    65.0      F    63.5     8
897   136A    68.5    65.0      F    63.0     8

[898 rows x 6 columns]

In [357]: gdf.groupby('Family').mean()
Out[357]:
        Father  Mother     Height  Kids
Family
1         78.5    67.0  70.100000     4
10        74.0    65.5  65.500000     1
100       69.0    66.0  70.733333     3
101       69.0    66.7  70.416667     6
102       69.0    66.0  66.166667     6
103       69.0    66.5  69.200000     5
104       69.5    66.5  66.625000     4
105       69.0    66.5  66.500000     6
106       69.5    66.0  68.500000     7
107       69.0    66.0  67.722222     9
108       69.0    65.0  65.571429     7
109       69.5    64.5  64.442857     7
11        74.0    62.0  67.312500     8
110       69.2    64.0  66.675000     4
112       69.0    63.0  66.666667     3
113       69.0    63.0  72.000000     1
114       69.0    63.0  67.500000     6
115       69.0    63.5  64.928571     7
116       69.0    63.5  65.733333     3
117       69.7    62.0  62.500000     1
118       69.5    62.0  71.333333     3
119       69.0    62.0  69.400000     5
12        74.0    61.0  65.000000     1
121       69.0    62.5  66.312500     8
122       69.0    62.0  68.000000     4
123       69.5    61.0  66.700000     5
124       69.0    61.0  64.555556     9
125       69.0    60.0  67.000000     3
126       69.0    60.0  64.300000     4
127       69.0    60.5  69.500000     1
...        ...     ...        ...   ...
71        70.0    65.0  66.666667     6
72        70.0    65.0  69.814286     7
73        70.0    65.0  70.166667     3
74        70.0    65.0  69.000000     2
75        70.0    64.7  67.414286     7
76        70.0    64.0  67.671429     7
77        70.0    64.0  67.550000     4
78        70.0    64.2  65.160000     5
79        70.5    64.0  68.375000     8
8         74.0    66.5  68.166667     3
80        70.5    64.5  60.000000     1
81        70.0    64.0  64.750000     4
82        70.0    64.0  68.555556     9
83        70.0    63.7  64.387500     8
85        70.5    63.0  67.400000     5
86        70.0    63.5  67.375000     4
87        70.0    63.0  65.175000     4
88        70.0    63.0  64.875000     4
89        70.5    62.0  67.625000     8
9         74.5    66.0  66.000000     1
90        70.3    62.7  66.500000     7
91        70.5    62.0  68.000000     3
92        70.0    61.0  69.100000     2
93        70.0    60.0  64.875000     4
94        70.0    60.0  65.000000     2
95        70.0    58.5  66.333333     3
96        70.0    58.0  66.400000     5
97        69.0    68.5  67.150000    10
98        69.0    67.0  64.000000     1
99        69.0    66.0  67.987500     8

[197 rows x 4 columns]

In [358]: gdf.groupby('Family').mean()['Father']
Out[358]:
Family
1      78.5
10     74.0
100    69.0
101    69.0
102    69.0
103    69.0
104    69.5
105    69.0
106    69.5
107    69.0
108    69.0
109    69.5
11     74.0
110    69.2
112    69.0
113    69.0
114    69.0
115    69.0
116    69.0
117    69.7
118    69.5
119    69.0
12     74.0
121    69.0
122    69.0
123    69.5
124    69.0
125    69.0
126    69.0
127    69.0
       ...
71     70.0
72     70.0
73     70.0
74     70.0
75     70.0
76     70.0
77     70.0
78     70.0
79     70.5
8      74.0
80     70.5
81     70.0
82     70.0
83     70.0
85     70.5
86     70.0
87     70.0
88     70.0
89     70.5
9      74.5
90     70.3
91     70.5
92     70.0
93     70.0
94     70.0
95     70.0
96     70.0
97     69.0
98     69.0
99     69.0
Name: Father, Length: 197, dtype: float64

In [359]: gdf.groupby('Family').mean()['Father'].mean()
Out[359]: 69.3492385786802

In [360]: gdf.groupby('Family').mean()
Out[360]:
        Father  Mother     Height  Kids
Family
1         78.5    67.0  70.100000     4
10        74.0    65.5  65.500000     1
100       69.0    66.0  70.733333     3
101       69.0    66.7  70.416667     6
102       69.0    66.0  66.166667     6
103       69.0    66.5  69.200000     5
104       69.5    66.5  66.625000     4
105       69.0    66.5  66.500000     6
106       69.5    66.0  68.500000     7
107       69.0    66.0  67.722222     9
108       69.0    65.0  65.571429     7
109       69.5    64.5  64.442857     7
11        74.0    62.0  67.312500     8
110       69.2    64.0  66.675000     4
112       69.0    63.0  66.666667     3
113       69.0    63.0  72.000000     1
114       69.0    63.0  67.500000     6
115       69.0    63.5  64.928571     7
116       69.0    63.5  65.733333     3
117       69.7    62.0  62.500000     1
118       69.5    62.0  71.333333     3
119       69.0    62.0  69.400000     5
12        74.0    61.0  65.000000     1
121       69.0    62.5  66.312500     8
122       69.0    62.0  68.000000     4
123       69.5    61.0  66.700000     5
124       69.0    61.0  64.555556     9
125       69.0    60.0  67.000000     3
126       69.0    60.0  64.300000     4
127       69.0    60.5  69.500000     1
...        ...     ...        ...   ...
71        70.0    65.0  66.666667     6
72        70.0    65.0  69.814286     7
73        70.0    65.0  70.166667     3
74        70.0    65.0  69.000000     2
75        70.0    64.7  67.414286     7
76        70.0    64.0  67.671429     7
77        70.0    64.0  67.550000     4
78        70.0    64.2  65.160000     5
79        70.5    64.0  68.375000     8
8         74.0    66.5  68.166667     3
80        70.5    64.5  60.000000     1
81        70.0    64.0  64.750000     4
82        70.0    64.0  68.555556     9
83        70.0    63.7  64.387500     8
85        70.5    63.0  67.400000     5
86        70.0    63.5  67.375000     4
87        70.0    63.0  65.175000     4
88        70.0    63.0  64.875000     4
89        70.5    62.0  67.625000     8
9         74.5    66.0  66.000000     1
90        70.3    62.7  66.500000     7
91        70.5    62.0  68.000000     3
92        70.0    61.0  69.100000     2
93        70.0    60.0  64.875000     4
94        70.0    60.0  65.000000     2
95        70.0    58.5  66.333333     3
96        70.0    58.0  66.400000     5
97        69.0    68.5  67.150000    10
98        69.0    67.0  64.000000     1
99        69.0    66.0  67.987500     8

[197 rows x 4 columns]

In [361]: gdf.groupby('Family').max()
Out[361]:
        Father  Mother Gender  Height  Kids
Family
1         78.5    67.0      M    73.2     4
10        74.0    65.5      F    65.5     1
100       69.0    66.0      M    71.2     3
101       69.0    66.7      M    75.0     6
102       69.0    66.0      M    70.0     6
103       69.0    66.5      M    73.0     5
104       69.5    66.5      M    70.5     4
105       69.0    66.5      M    71.0     6
106       69.5    66.0      M    71.0     7
107       69.0    66.0      M    73.0     9
108       69.0    65.0      M    70.0     7
109       69.5    64.5      M    69.7     7
11        74.0    62.0      M    74.0     8
110       69.2    64.0      M    71.7     4
112       69.0    63.0      M    69.0     3
113       69.0    63.0      M    72.0     1
114       69.0    63.0      M    73.0     6
115       69.0    63.5      M    70.5     7
116       69.0    63.5      M    70.5     3
117       69.7    62.0      F    62.5     1
118       69.5    62.0      M    73.0     3
119       69.0    62.0      M    73.0     5
12        74.0    61.0      F    65.0     1
121       69.0    62.5      M    71.0     8
122       69.0    62.0      M    72.0     4
123       69.5    61.0      M    70.0     5
124       69.0    61.0      M    68.0     9
125       69.0    60.0      M    70.5     3
126       69.0    60.0      M    69.0     4
127       69.0    60.5      M    69.5     1
...        ...     ...    ...     ...   ...
71        70.0    65.0      M    70.0     6
72        70.0    65.0      M    79.0     7
73        70.0    65.0      M    73.0     3
74        70.0    65.0      M    69.0     2
75        70.0    64.7      M    72.0     7
76        70.0    64.0      M    70.7     7
77        70.0    64.0      M    70.0     4
78        70.0    64.2      M    72.0     5
79        70.5    64.0      M    74.0     8
8         74.0    66.5      F    70.5     3
80        70.5    64.5      F    60.0     1
81        70.0    64.0      M    68.0     4
82        70.0    64.0      M    71.0     9
83        70.0    63.7      M    70.0     8
85        70.5    63.0      M    72.5     5
86        70.0    63.5      M    71.0     4
87        70.0    63.0      M    68.0     4
88        70.0    63.0      M    70.0     4
89        70.5    62.0      M    72.0     8
9         74.5    66.0      F    66.0     1
90        70.3    62.7      M    70.7     7
91        70.5    62.0      M    72.0     3
92        70.0    61.0      M    71.2     2
93        70.0    60.0      M    67.0     4
94        70.0    60.0      F    65.0     2
95        70.0    58.5      M    71.5     3
96        70.0    58.0      M    72.0     5
97        69.0    68.5      M    75.0    10
98        69.0    67.0      F    64.0     1
99        69.0    66.0      M    73.0     8

[197 rows x 5 columns]

In [362]: gdf.groupby('Family').max()['Father']
Out[362]:
Family
1      78.5
10     74.0
100    69.0
101    69.0
102    69.0
103    69.0
104    69.5
105    69.0
106    69.5
107    69.0
108    69.0
109    69.5
11     74.0
110    69.2
112    69.0
113    69.0
114    69.0
115    69.0
116    69.0
117    69.7
118    69.5
119    69.0
12     74.0
121    69.0
122    69.0
123    69.5
124    69.0
125    69.0
126    69.0
127    69.0
       ...
71     70.0
72     70.0
73     70.0
74     70.0
75     70.0
76     70.0
77     70.0
78     70.0
79     70.5
8      74.0
80     70.5
81     70.0
82     70.0
83     70.0
85     70.5
86     70.0
87     70.0
88     70.0
89     70.5
9      74.5
90     70.3
91     70.5
92     70.0
93     70.0
94     70.0
95     70.0
96     70.0
97     69.0
98     69.0
99     69.0
Name: Father, Length: 197, dtype: float64

In [363]: gdf.groupby('Family').max()['Father'].mean()
Out[363]: 69.3492385786802

In [364]: gdf.groupby('Family').max().mean()
Out[364]:
Father    69.349239
Mother    63.984264
Height    69.818782
Kids       4.563452
dtype: float64

In [365]: gdf.groupby('Family').max()['Father']
Out[365]:
Family
1      78.5
10     74.0
100    69.0
101    69.0
102    69.0
103    69.0
104    69.5
105    69.0
106    69.5
107    69.0
108    69.0
109    69.5
11     74.0
110    69.2
112    69.0
113    69.0
114    69.0
115    69.0
116    69.0
117    69.7
118    69.5
119    69.0
12     74.0
121    69.0
122    69.0
123    69.5
124    69.0
125    69.0
126    69.0
127    69.0
       ...
71     70.0
72     70.0
73     70.0
74     70.0
75     70.0
76     70.0
77     70.0
78     70.0
79     70.5
8      74.0
80     70.5
81     70.0
82     70.0
83     70.0
85     70.5
86     70.0
87     70.0
88     70.0
89     70.5
9      74.5
90     70.3
91     70.5
92     70.0
93     70.0
94     70.0
95     70.0
96     70.0
97     69.0
98     69.0
99     69.0
Name: Father, Length: 197, dtype: float64

In [366]: gdf.groupby('Family').max()[['Father', 'Mother']]
Out[366]:
        Father  Mother
Family
1         78.5    67.0
10        74.0    65.5
100       69.0    66.0
101       69.0    66.7
102       69.0    66.0
103       69.0    66.5
104       69.5    66.5
105       69.0    66.5
106       69.5    66.0
107       69.0    66.0
108       69.0    65.0
109       69.5    64.5
11        74.0    62.0
110       69.2    64.0
112       69.0    63.0
113       69.0    63.0
114       69.0    63.0
115       69.0    63.5
116       69.0    63.5
117       69.7    62.0
118       69.5    62.0
119       69.0    62.0
12        74.0    61.0
121       69.0    62.5
122       69.0    62.0
123       69.5    61.0
124       69.0    61.0
125       69.0    60.0
126       69.0    60.0
127       69.0    60.5
...        ...     ...
71        70.0    65.0
72        70.0    65.0
73        70.0    65.0
74        70.0    65.0
75        70.0    64.7
76        70.0    64.0
77        70.0    64.0
78        70.0    64.2
79        70.5    64.0
8         74.0    66.5
80        70.5    64.5
81        70.0    64.0
82        70.0    64.0
83        70.0    63.7
85        70.5    63.0
86        70.0    63.5
87        70.0    63.0
88        70.0    63.0
89        70.5    62.0
9         74.5    66.0
90        70.3    62.7
91        70.5    62.0
92        70.0    61.0
93        70.0    60.0
94        70.0    60.0
95        70.0    58.5
96        70.0    58.0
97        69.0    68.5
98        69.0    67.0
99        69.0    66.0

[197 rows x 2 columns]

In [367]: gdf.groupby('Family').max()[['Father', 'Mother']].plot.scatter()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-367-35d06d579a19> in <module>
----> 1 gdf.groupby('Family').max()[['Father', 'Mother']].plot.scatter()

TypeError: scatter() missing 2 required positional arguments: 'x' and 'y'
> <ipython-input-367-35d06d579a19>(1)<module>()
----> 1 gdf.groupby('Family').max()[['Father', 'Mother']].plot.scatter()

ipdb> c

In [368]: gdf.groupby('Family').max()[['Father', 'Mother']].plot.scatter(x='Mother', y='Father')
Out[368]: <matplotlib.axes._subplots.AxesSubplot at 0x7fd251358518>

In [369]: gdf.groupby('Family').max()[['Father', 'Mother']]
Out[369]:
        Father  Mother
Family
1         78.5    67.0
10        74.0    65.5
100       69.0    66.0
101       69.0    66.7
102       69.0    66.0
103       69.0    66.5
104       69.5    66.5
105       69.0    66.5
106       69.5    66.0
107       69.0    66.0
108       69.0    65.0
109       69.5    64.5
11        74.0    62.0
110       69.2    64.0
112       69.0    63.0
113       69.0    63.0
114       69.0    63.0
115       69.0    63.5
116       69.0    63.5
117       69.7    62.0
118       69.5    62.0
119       69.0    62.0
12        74.0    61.0
121       69.0    62.5
122       69.0    62.0
123       69.5    61.0
124       69.0    61.0
125       69.0    60.0
126       69.0    60.0
127       69.0    60.5
...        ...     ...
71        70.0    65.0
72        70.0    65.0
73        70.0    65.0
74        70.0    65.0
75        70.0    64.7
76        70.0    64.0
77        70.0    64.0
78        70.0    64.2
79        70.5    64.0
8         74.0    66.5
80        70.5    64.5
81        70.0    64.0
82        70.0    64.0
83        70.0    63.7
85        70.5    63.0
86        70.0    63.5
87        70.0    63.0
88        70.0    63.0
89        70.5    62.0
9         74.5    66.0
90        70.3    62.7
91        70.5    62.0
92        70.0    61.0
93        70.0    60.0
94        70.0    60.0
95        70.0    58.5
96        70.0    58.0
97        69.0    68.5
98        69.0    67.0
99        69.0    66.0

[197 rows x 2 columns]

In [370]: gdf.groupby('Family').max()
Out[370]:
        Father  Mother Gender  Height  Kids
Family
1         78.5    67.0      M    73.2     4
10        74.0    65.5      F    65.5     1
100       69.0    66.0      M    71.2     3
101       69.0    66.7      M    75.0     6
102       69.0    66.0      M    70.0     6
103       69.0    66.5      M    73.0     5
104       69.5    66.5      M    70.5     4
105       69.0    66.5      M    71.0     6
106       69.5    66.0      M    71.0     7
107       69.0    66.0      M    73.0     9
108       69.0    65.0      M    70.0     7
109       69.5    64.5      M    69.7     7
11        74.0    62.0      M    74.0     8
110       69.2    64.0      M    71.7     4
112       69.0    63.0      M    69.0     3
113       69.0    63.0      M    72.0     1
114       69.0    63.0      M    73.0     6
115       69.0    63.5      M    70.5     7
116       69.0    63.5      M    70.5     3
117       69.7    62.0      F    62.5     1
118       69.5    62.0      M    73.0     3
119       69.0    62.0      M    73.0     5
12        74.0    61.0      F    65.0     1
121       69.0    62.5      M    71.0     8
122       69.0    62.0      M    72.0     4
123       69.5    61.0      M    70.0     5
124       69.0    61.0      M    68.0     9
125       69.0    60.0      M    70.5     3
126       69.0    60.0      M    69.0     4
127       69.0    60.5      M    69.5     1
...        ...     ...    ...     ...   ...
71        70.0    65.0      M    70.0     6
72        70.0    65.0      M    79.0     7
73        70.0    65.0      M    73.0     3
74        70.0    65.0      M    69.0     2
75        70.0    64.7      M    72.0     7
76        70.0    64.0      M    70.7     7
77        70.0    64.0      M    70.0     4
78        70.0    64.2      M    72.0     5
79        70.5    64.0      M    74.0     8
8         74.0    66.5      F    70.5     3
80        70.5    64.5      F    60.0     1
81        70.0    64.0      M    68.0     4
82        70.0    64.0      M    71.0     9
83        70.0    63.7      M    70.0     8
85        70.5    63.0      M    72.5     5
86        70.0    63.5      M    71.0     4
87        70.0    63.0      M    68.0     4
88        70.0    63.0      M    70.0     4
89        70.5    62.0      M    72.0     8
9         74.5    66.0      F    66.0     1
90        70.3    62.7      M    70.7     7
91        70.5    62.0      M    72.0     3
92        70.0    61.0      M    71.2     2
93        70.0    60.0      M    67.0     4
94        70.0    60.0      F    65.0     2
95        70.0    58.5      M    71.5     3
96        70.0    58.0      M    72.0     5
97        69.0    68.5      M    75.0    10
98        69.0    67.0      F    64.0     1
99        69.0    66.0      M    73.0     8

[197 rows x 5 columns]

In [371]: gdf.groupby('Family').max().plot.scatter(x='Mother', y='Father')
Out[371]: <matplotlib.axes._subplots.AxesSubplot at 0x7fd25137a978>

In [372]: gdf.groupby('Family').max()[['Father', 'Mother']]
Out[372]:
        Father  Mother
Family
1         78.5    67.0
10        74.0    65.5
100       69.0    66.0
101       69.0    66.7
102       69.0    66.0
103       69.0    66.5
104       69.5    66.5
105       69.0    66.5
106       69.5    66.0
107       69.0    66.0
108       69.0    65.0
109       69.5    64.5
11        74.0    62.0
110       69.2    64.0
112       69.0    63.0
113       69.0    63.0
114       69.0    63.0
115       69.0    63.5
116       69.0    63.5
117       69.7    62.0
118       69.5    62.0
119       69.0    62.0
12        74.0    61.0
121       69.0    62.5
122       69.0    62.0
123       69.5    61.0
124       69.0    61.0
125       69.0    60.0
126       69.0    60.0
127       69.0    60.5
...        ...     ...
71        70.0    65.0
72        70.0    65.0
73        70.0    65.0
74        70.0    65.0
75        70.0    64.7
76        70.0    64.0
77        70.0    64.0
78        70.0    64.2
79        70.5    64.0
8         74.0    66.5
80        70.5    64.5
81        70.0    64.0
82        70.0    64.0
83        70.0    63.7
85        70.5    63.0
86        70.0    63.5
87        70.0    63.0
88        70.0    63.0
89        70.5    62.0
9         74.5    66.0
90        70.3    62.7
91        70.5    62.0
92        70.0    61.0
93        70.0    60.0
94        70.0    60.0
95        70.0    58.5
96        70.0    58.0
97        69.0    68.5
98        69.0    67.0
99        69.0    66.0

[197 rows x 2 columns]

In [373]: gdf.groupby('Family').max()[['Father', 'Mother']].corr()
Out[373]:
          Father    Mother
Father  1.000000  0.100606
Mother  0.100606  1.000000

In [374]: gdf.groupby('Family').unique
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-374-ce517da61a52> in <module>
----> 1 gdf.groupby('Family').unique

/usr/local/lib/python3.6/dist-packages/pandas/core/groupby/groupby.py in __getattr__(self, attr)
    534
    535         raise AttributeError("%r object has no attribute %r" %
--> 536                              (type(self).__name__, attr))
    537
    538     @Substitution(klass='GroupBy',

AttributeError: 'DataFrameGroupBy' object has no attribute 'unique'
> /usr/local/lib/python3.6/dist-packages/pandas/core/groupby/groupby.py(536)__getattr__()
    534
    535         raise AttributeError("%r object has no attribute %r" %
--> 536                              (type(self).__name__, attr))
    537
    538     @Substitution(klass='GroupBy',

ipdb> c

In [375]: gb = gdf.groupby('Family')

In [376]: gb.nunique
Out[376]: <bound method DataFrameGroupBy.nunique of <pandas.core.groupby.generic.DataFrameGroupBy object at 0x7fd251343cc0>>

In [377]: gb.nunique()
Out[377]:
        Family  Father  Mother  Gender  Height  Kids
Family
1            1       1       1       2       3     1
10           1       1       1       1       1     1
100          1       1       1       1       3     1
101          1       1       1       1       6     1
102          1       1       1       2       6     1
103          1       1       1       2       4     1
104          1       1       1       2       4     1
105          1       1       1       2       5     1
106          1       1       1       2       5     1
107          1       1       1       2       7     1
108          1       1       1       2       7     1
109          1       1       1       2       6     1
11           1       1       1       2       7     1
110          1       1       1       2       4     1
112          1       1       1       2       3     1
113          1       1       1       1       1     1
114          1       1       1       2       5     1
115          1       1       1       2       7     1
116          1       1       1       2       3     1
117          1       1       1       1       1     1
118          1       1       1       1       3     1
119          1       1       1       2       4     1
12           1       1       1       1       1     1
121          1       1       1       2       6     1
122          1       1       1       2       3     1
123          1       1       1       2       5     1
124          1       1       1       2       6     1
125          1       1       1       2       3     1
126          1       1       1       2       4     1
127          1       1       1       1       1     1
...        ...     ...     ...     ...     ...   ...
71           1       1       1       2       4     1
72           1       1       1       2       7     1
73           1       1       1       2       3     1
74           1       1       1       1       1     1
75           1       1       1       2       7     1
76           1       1       1       2       6     1
77           1       1       1       2       4     1
78           1       1       1       2       5     1
79           1       1       1       2       6     1
8            1       1       1       1       3     1
80           1       1       1       1       1     1
81           1       1       1       2       4     1
82           1       1       1       2       7     1
83           1       1       1       2       8     1
85           1       1       1       2       5     1
86           1       1       1       2       3     1
87           1       1       1       2       4     1
88           1       1       1       2       4     1
89           1       1       1       2       7     1
9            1       1       1       1       1     1
90           1       1       1       2       7     1
91           1       1       1       2       2     1
92           1       1       1       1       2     1
93           1       1       1       2       4     1
94           1       1       1       1       1     1
95           1       1       1       2       3     1
96           1       1       1       2       4     1
97           1       1       1       2       7     1
98           1       1       1       1       1     1
99           1       1       1       2       8     1

[197 rows x 6 columns]

In [378]: gdf.groupby('Family').unique
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-378-ce517da61a52> in <module>
----> 1 gdf.groupby('Family').unique

/usr/local/lib/python3.6/dist-packages/pandas/core/groupby/groupby.py in __getattr__(self, attr)
    534
    535         raise AttributeError("%r object has no attribute %r" %
--> 536                              (type(self).__name__, attr))
    537
    538     @Substitution(klass='GroupBy',

AttributeError: 'DataFrameGroupBy' object has no attribute 'unique'
> /usr/local/lib/python3.6/dist-packages/pandas/core/groupby/groupby.py(536)__getattr__()
    534
    535         raise AttributeError("%r object has no attribute %r" %
--> 536                              (type(self).__name__, attr))
    537
    538     @Substitution(klass='GroupBy',

ipdb> c

In [379]: gdf.groupby('Family').nunique()
Out[379]:
        Family  Father  Mother  Gender  Height  Kids
Family
1            1       1       1       2       3     1
10           1       1       1       1       1     1
100          1       1       1       1       3     1
101          1       1       1       1       6     1
102          1       1       1       2       6     1
103          1       1       1       2       4     1
104          1       1       1       2       4     1
105          1       1       1       2       5     1
106          1       1       1       2       5     1
107          1       1       1       2       7     1
108          1       1       1       2       7     1
109          1       1       1       2       6     1
11           1       1       1       2       7     1
110          1       1       1       2       4     1
112          1       1       1       2       3     1
113          1       1       1       1       1     1
114          1       1       1       2       5     1
115          1       1       1       2       7     1
116          1       1       1       2       3     1
117          1       1       1       1       1     1
118          1       1       1       1       3     1
119          1       1       1       2       4     1
12           1       1       1       1       1     1
121          1       1       1       2       6     1
122          1       1       1       2       3     1
123          1       1       1       2       5     1
124          1       1       1       2       6     1
125          1       1       1       2       3     1
126          1       1       1       2       4     1
127          1       1       1       1       1     1
...        ...     ...     ...     ...     ...   ...
71           1       1       1       2       4     1
72           1       1       1       2       7     1
73           1       1       1       2       3     1
74           1       1       1       1       1     1
75           1       1       1       2       7     1
76           1       1       1       2       6     1
77           1       1       1       2       4     1
78           1       1       1       2       5     1
79           1       1       1       2       6     1
8            1       1       1       1       3     1
80           1       1       1       1       1     1
81           1       1       1       2       4     1
82           1       1       1       2       7     1
83           1       1       1       2       8     1
85           1       1       1       2       5     1
86           1       1       1       2       3     1
87           1       1       1       2       4     1
88           1       1       1       2       4     1
89           1       1       1       2       7     1
9            1       1       1       1       1     1
90           1       1       1       2       7     1
91           1       1       1       2       2     1
92           1       1       1       1       2     1
93           1       1       1       2       4     1
94           1       1       1       1       1     1
95           1       1       1       2       3     1
96           1       1       1       2       4     1
97           1       1       1       2       7     1
98           1       1       1       1       1     1
99           1       1       1       2       8     1

[197 rows x 6 columns]

In [380]: gdf.groupby('Family').max()
Out[380]:
        Father  Mother Gender  Height  Kids
Family
1         78.5    67.0      M    73.2     4
10        74.0    65.5      F    65.5     1
100       69.0    66.0      M    71.2     3
101       69.0    66.7      M    75.0     6
102       69.0    66.0      M    70.0     6
103       69.0    66.5      M    73.0     5
104       69.5    66.5      M    70.5     4
105       69.0    66.5      M    71.0     6
106       69.5    66.0      M    71.0     7
107       69.0    66.0      M    73.0     9
108       69.0    65.0      M    70.0     7
109       69.5    64.5      M    69.7     7
11        74.0    62.0      M    74.0     8
110       69.2    64.0      M    71.7     4
112       69.0    63.0      M    69.0     3
113       69.0    63.0      M    72.0     1
114       69.0    63.0      M    73.0     6
115       69.0    63.5      M    70.5     7
116       69.0    63.5      M    70.5     3
117       69.7    62.0      F    62.5     1
118       69.5    62.0      M    73.0     3
119       69.0    62.0      M    73.0     5
12        74.0    61.0      F    65.0     1
121       69.0    62.5      M    71.0     8
122       69.0    62.0      M    72.0     4
123       69.5    61.0      M    70.0     5
124       69.0    61.0      M    68.0     9
125       69.0    60.0      M    70.5     3
126       69.0    60.0      M    69.0     4
127       69.0    60.5      M    69.5     1
...        ...     ...    ...     ...   ...
71        70.0    65.0      M    70.0     6
72        70.0    65.0      M    79.0     7
73        70.0    65.0      M    73.0     3
74        70.0    65.0      M    69.0     2
75        70.0    64.7      M    72.0     7
76        70.0    64.0      M    70.7     7
77        70.0    64.0      M    70.0     4
78        70.0    64.2      M    72.0     5
79        70.5    64.0      M    74.0     8
8         74.0    66.5      F    70.5     3
80        70.5    64.5      F    60.0     1
81        70.0    64.0      M    68.0     4
82        70.0    64.0      M    71.0     9
83        70.0    63.7      M    70.0     8
85        70.5    63.0      M    72.5     5
86        70.0    63.5      M    71.0     4
87        70.0    63.0      M    68.0     4
88        70.0    63.0      M    70.0     4
89        70.5    62.0      M    72.0     8
9         74.5    66.0      F    66.0     1
90        70.3    62.7      M    70.7     7
91        70.5    62.0      M    72.0     3
92        70.0    61.0      M    71.2     2
93        70.0    60.0      M    67.0     4
94        70.0    60.0      F    65.0     2
95        70.0    58.5      M    71.5     3
96        70.0    58.0      M    72.0     5
97        69.0    68.5      M    75.0    10
98        69.0    67.0      F    64.0     1
99        69.0    66.0      M    73.0     8

[197 rows x 5 columns]

In [381]:
