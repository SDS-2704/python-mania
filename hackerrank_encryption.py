#MAINCODE
import math
import numpy as np
import itertools
s = 'feed the dog'
s_witoutspcs = s.replace(" ","")
s_witoutspcs
len_ = len(s_witoutspcs)
row_ =  math.floor(math.sqrt(len_))
col_ = math.ceil(math.sqrt(len_))
# Time complexity: O(row_*column_), where len_ is length of given string s and row_ = math.floor(math.sqrt(len_)), col_ = math.ceil(math.sqrt(len_))
# Auxiliary space: O(row_*column_)
# print(row_,col_)
assert(row_*col_>=len_)
lst_ = []
for i in range(len_):
    
    if i % col_ == 0:
      sub = s_witoutspcs[i:i+col_]
      lst = []
      for j in sub:
        lst.append(j)
      lst_.append(lst)
      print(''.join(lst))
lst_t = list(map(list, itertools.zip_longest(*lst_)))
# for itr_ in lst_t:
#     # print(itr_)
#     # str_ = ''
#     # for itr__ in itr_:
#     #     str_ += itr__
#     # print(str_,end=" ")
str_final = ''
for itr_ in lst_t:
    # print(itr_)
    str_ = ''
    for itr__ in itr_:
        if itr__ == None:
           str_ += ""
        else:
           str_ += itr__
    str_final += str_ + " "
print(str_final)  
