# -*- coding: utf-8 -*-
"""problem solving

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_VlH2mD29-TA-3n0jfSsRaDOrrHwjVDF
"""

mydict={}
k=40
for x in enumerate([10,20,30]):
  value,key=x
  print(key)
  if key not in mydict:
    mydict[key]=value
  print(mydict)
for value,key in enumerate([10,20,30]):
  if k-key in mydict and mydict[k-key]!=value:
   print(value,mydict[k-key])
   break

list=[7,1,5,3,6,4]
max=0
for i in range(len(list)):
  if i>max:
    max=i
print(max)

list=[7,1,5,3,6,4]
max=0
for i in range(len(list)):
  for j in range(i+1,len(list)):
   if max<list[j]-list[i]:
    max=list[j]-list[i]
print(max)

buy=0
sell=1
maxi=0
my_list=[7,1,5,3,6,4]
no_days=len(my_list)
while(sell<no_days):
  if (my_list[sell]>my_list[buy] ):
    profit_margin=my_list[sell]-my_list[buy]
    maxi=max(maxi, profit_margin)
  else:
    buy=sell
  sell+=1
print(maxi)