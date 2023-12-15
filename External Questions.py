#!/usr/bin/env python
# coding: utf-8

# 
# # Eternal Questions :LeetCode

# 

# In[1]:


import numpy as np
from collections import *
import functools, math
from decimal import Decimal
import sys
from sortedcontainers import SortedList
from bisect import *
import copy


# # Easy:

# # 1) 118. Pascal's Triangle
# Given an integer numRows, return the first numRows of Pascal's triangle. 
# In Pascal's triangle, each number is the sum of the two numbers directly above it
# 
# 

# In[2]:


def  pascalTriangle(numRows):
    """
    1)we always start with 1 at the top
    2)in the next row add 1 to the left
    3)calculate the value of the middle elemnts by add the 2 on the row above
    4)add 1 to the end of the row
    """
    arr=[[1]]
    if numRows>=2:
        arr.append([1,1])
    for j in range(2,numRows,1):
        temp=[1]
        for i in range(1,j,1):
            temp.append(arr[j-1][i-1]+arr[j-1][i])
        temp.append(1)
        arr.append(temp)
    return arr

numOfRows=input("Enter Number Of Rows: ")
print("pascsl's Triangle for %d rows is:"%int(numOfRows))
for row in (pascalTriangle(int(numOfRows))):
    print("\n%s" %(row))


# # 2) 202. Happy Number
# Write an algorithm to determine if a number n is happy. A happy number is a number defined by the following process:
# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.

# In[3]:


"""
it caught my attention that any digit except 0 and will get sum of digits in an endless loop,
all we have to do is to check if we ever get to one of those digit to end the loop and return False
"""

def happynumber(num):
    
    nums={2,3,4,5,6,8,9}
    if num in nums:
        return False
    if num ==1:
        return True
    
    sum_digits=0
    while (num//10 !=0):
        sum_digits+=((num%10)**2)
        num=num//10
    sum_digits+=(num%10)**2
    return happynumber(sum_digits)
    

d=[4526184,423615,213121,2,7]
for num in d:
    print("\nChecking if %d is a Happy Number: %s"%(num,happynumber(num)))


# In[ ]:





# # 3) 2591. Distribute Money to Maximum Children
# You are given an integer money denoting the amount of money (in dollars) that you have and another integer children denoting the number of children that you must distribute the money to.
# 
# You have to distribute the money according to the following rules:
# 
# All money must be distributed.
# Everyone must receive at least 1 dollar.
# Nobody receives 4 dollars.
# Return the maximum number of children who may receive exactly 8 dollars if you distribute the money according to the aforementioned rules. If there is no way to distribute the money, return -1.
# 

# In[4]:


"""since the minimum for each child should be 1, we distribute that to all the kids, 
now we get greed by checking if we can give 7 more to all the kids, incase we have 4 given to one of the children->
remove that option and lower the number of 8 that can be distribute to the kids
"""
def distMoney( money: int, children: int) -> int:
   
    if money-children < 0:
          return -1
    money-=children
    if (money // 7) == children and  (money % 7) == 0:
          return (money // 7)

    if (money // 7) == children - 1 and (money % 7) == 3:
          return (money // 7) - 1


    return min(children - 1, money // 7)
options=[(20,3),(16,2),(1,2)]
for money,children in options:
    print("\nFor the amount of money %d and number of children %d: " %(money,children) ,"Maximun amount of children who can recive 8 Dollar are:",distMoney(money,children))


# In[ ]:





# In[ ]:





# # 4) 914. X of a Kind in a Deck of Cards
# You are given an integer array deck where deck[i] represents the number written on the ith card.
# 
# Partition the cards into one or more groups such that:
# 
# Each group has exactly x cards where x > 1, and
# All the cards in one group have the same integer written on them.
# Return true if such partition is possible, or false otherwise.

# In[5]:


def hasGroupsSizeX(deck) -> bool:
    """1) first we use counter to get the pair value for each card
    2) we send all the values to a function 
    3)The functions finds the greats commomn factor
    4)and then finds the smalles prime that is divisable by all the numbers
    """    
    
    def primFactors(NotPrime):
        n = functools.reduce(math.gcd, NotPrime)
        list_prime={}
        i=1
        while(i<=n):
            k=0
            if(n%i==0):
                j=1
                while(j<=i):
                    if(i%j==0):
                        k+=1
                    j+=1
                if(k==2):
                    return i
            i+=1


    c=Counter(deck) 
    factors=primFactors(list(c.values()))
    if factors==None:
        return False
    else:
        return True
    
decks = [[1,1,1,2,2,2,3,3,3],
[1,1,2,2,2,2,2,2,3,4,5,6,7,8,9,0],
[1,1,2,2,2,2,3,3,3,3,3,3],
[1,1,1,1,3,3,3,3,3,3],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18]
        ]
for deck in decks:
    
    print("\nThe Deck of Card:%s" %(deck))
    if(hasGroupsSizeX(deck)):
        print("\nPartitioning according to the Guidlines is Possible")
    else:
        print("\nPartitioning according to the Guidlines is Not Possible")


# In[ ]:





# In[ ]:





# # 5) 1979. Find Greatest Common Divisor of Array
# Given an integer array nums, return the greatest common divisor of the smallest number and largest number in nums.
# The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.
# 

# In[6]:


def findGCD(nums) -> int:
    
    """
    we keep looking for the smallest moduls that we can get, we eventually can get 1 if all else fails
    """        
    def hcv(a,b):

        if(b == 0):
            return abs(a)
        else:
            return hcv(b, a % b)



    return hcv(max(nums),min(nums))
    
    
a=[{2,5,6,9,10},
    {7,5,6,8,3}]
for li in a:
    print("The Greates Common Divisor for the list: %s is ->" %li ,findGCD(li))



# # 6) 1037. Valid Boomerang
# Given an array points where points[i] = [xi, yi] represents a point on the X-Y plane, return true if these points are a boomerang.
# 
# A boomerang is a set of three points that are all distinct and not in a straight line.
# 

# In[10]:


def isBoomerang( points) -> bool:
    """
    1)check if the first points ar identical
    2)checking if both x coordinats are the same if not
    3) calculate the line and check if the third point is on it
    4)if x coordinats are the same check the third point if it shares the same x 
    
    """

    
    x1=points[0][0]
    y1=points[0][1]
    x2=points[1][0]
    y2=points[1][1]
    
    if(x1==x2 and y1==y2):
        return False
   
    x=points[2][0]
    y=points[2][1]
    
    if abs(x1-x2)!=0:
        m=(y1-y2)/(x1-x2)
        b=y1-m*x1
        return float(y) != round(Decimal(m*x+b),2)
    else:
        return x!=x1


points = [[[1,1],[1,1],[3,2]],
        [[1,1],[2,2],[3,3]],
        [[0,0],[1,0],[2,1]],
        [[1,0],[1,1],[1,0]],
        [[22,33],[37,27],[67,15]],
        [[2,0],[0,1],[1,0]]]
for point in points:
    print("\nChecking if All Points in: \n%s make a Boomerang: "%(np.matrix(point)), isBoomerang( point))


# In[ ]:





# In[ ]:





# In[ ]:





# # 7) 2423. Remove Letter To Equalize Frequency
# You are given a 0-indexed string word, consisting of lowercase English letters. You need to select one index and remove the letter at that index from word so that the frequency of every letter present in word is equal.
# 
# Return true if it is possible to remove one letter so that the frequency of all letters in word are equal, and false otherwise.
# 

# In[11]:


def equalFrequency(word) -> bool:
    c=Counter(list(word))

    for char in c.keys():
        sum_frq=0
        c[char]-=1
        c=+c
        min_freq=c.most_common()[len(c)-1][1]

        for char2 in c.keys():
            if(c[char2]==0): 
                continue
                
            sum_frq+=abs(c[char2]-min_freq)

        if sum_frq ==0:
            return True
        else:
            c[char]+=1
            
    return False

    

strings=["abcc",
         "aazz",
         "bac",
        "abbcc"]

for s in strings:
    print("\nRemove  One Letter To Equalize Frequency in %s: "%(s),end="")
    if(equalFrequency( s)):
        print("Possible")
    else:
        print("Not Possible")


# # 8) 605. Can Place Flowers
# 
# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.
# 
# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.
# 

# In[12]:


def canPlaceFlowers(flowerbed, n) -> bool:
    """
    first we check the right edge for possible planting spot
    and then we keep checking as long as we have more plants that need planting
    then we check the left edge for one more spot
    if we have negative n -> more than enough
    """    

    if flowerbed[0]==0:
        if len(flowerbed)>1 and flowerbed[1]==0:
            flowerbed[0]=1
            n-=1
        elif len(flowerbed)==1:
            flowerbed[0]=1
            n-=1

    if(n!=0):
        for i in range(1,len(flowerbed)-1):
            if flowerbed[i-1]==0 and flowerbed[i+1]==0 and flowerbed[i]!=1:
                n-=1
                flowerbed[i]=1

    if flowerbed[-1]==0 and flowerbed[-2]==0:
            flowerbed[-1]=1
            n-=1
                
    
    if n<=0:
        return True
    else:
        return False
    
            
    
flowerbed= [[1,0,0,0,1]
            ,[0,0,1,0,1,0,0]
            ,[0]
            ,[0,0,1,0,0]]
n= [2,2,1,1]
   
for flower,s in zip(flowerbed,n):
    print("\n Checking available %d spots for planting in pot %s: "%(s,flower),end=""  )
    if(canPlaceFlowers(flower,s)):
        print("Possible")
    else:
        print("Not Possible")


# In[ ]:





# In[ ]:





# In[ ]:





# # 9) 2525. Categorize Box According to Criteria
# Given four integers length, width, height, and mass, representing the dimensions and mass of a box, respectively, return a string representing the category of the box.
# 
# The box is "Bulky" if:
# Any of the dimensions of the box is greater or equal to 104.
# Or, the volume of the box is greater or equal to 109.
# If the mass of the box is greater or equal to 100, it is "Heavy".
# If the box is both "Bulky" and "Heavy", then its category is "Both".
# If the box is neither "Bulky" nor "Heavy", then its category is "Neither".
# If the box is "Bulky" but not "Heavy", then its category is "Bulky".
# If the box is "Heavy" but not "Bulky", then its category is "Heavy".

# In[13]:


def categorizeBox(length: int, width: int, height: int, mass: int) -> str:
    """
    setting all the conditions from the question"""
    
    param=[length, width, height]
    size=""
    mas=""
    if any(par>=10**4 for par in param):
            size= "Bulky"
        
    if((height*width*length) >= 10**9):
        size= "Bulky"
        
    if mass>=100:
        mas= "Heavy"
        
        
    if  size== "Bulky" and mas== "Heavy":
        return "Both"
    
    if size== "Bulky":
        return "Bulky"
    
    elif mas=="Heavy":
        return "Heavy"

    else:
        return "Neither"
    
    
    
height=int(input("Enter Height "))
width=int(input("Enter Width "))
length=int(input("Enter Length "))
mass=int(input("Enter Mass "))

print("Box with Dimensions %d and %d, %d and a Mass of %d is Catagorized: %s" %(height,width,length,mass,categorizeBox(length, width, height, mass)))


# In[ ]:





# # 10) 2099. Find Subsequence of Length K With the Largest Sum
# 
# You are given an integer array nums and an integer k. You want to find a subsequence of nums of length k that has the largest sum.
# Return any such subsequence as an integer array of length k.
# A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
# 

# In[14]:


def maxSubsequence( nums,k) :
    #sorting the list while keeping track of the indxes
        l = sorted(enumerate(nums), key=lambda i: i[1])
        subseq=[]
        for i in range(len(l)-1,len(l)-1-k,-1):
            #taking the indexes of the highes k elemnts
            subseq.append(l[i][0]) 
            
        s=sorted(subseq) #in order to get the elemnt in the original order

        for j in range(len(s)):
            #getting  the values of the highes elemnts
            s[j]=nums[s[j]]
        return s




nums = [[-1,-2,3,4]
,[3,5,3,4]
,[2,1,3,3]
,[50,-75]
,[-1,-2,3,4]
,[3,4,3,3]
,[6, 3, 4, 1, 1, 8,3, 7, -4, 2]]
k=[3,3,2,2,3,3,5]



for num,ln in zip(nums,k):
    
    print("\nThe Greates Subsequence with %d elements from %s is: %s" %(ln,num,maxSubsequence(num,ln)) )


# In[ ]:





# In[ ]:





# # 11) 482. License Key Formatting
# 
# You are given a license key represented as a string s that consists of only alphanumeric characters and dashes. The string is separated into n + 1 groups by n dashes. You are also given an integer k.
# We want to reformat the string s such that each group contains exactly k characters, except for the first group, which could be shorter than k but still must contain at least one character. Furthermore, there must be a dash inserted between two groups, and you should convert all lowercase letters to uppercase.
# Return the reformatted license key

# In[15]:


def licenseKeyFormatting( s, k) -> str:
    """
    first we put together all the letters
    and find the modulos of number of charcters by the number of elements in a group-> this will be in the first group
    and then add every k elements to the next group with seperation
    eventually we capitlize every letter
    """
    list_string=s.split("-")
    x=''.join(list_string)
    result=''
    char_Group1=(len(x)%k)
    num_groups=(len(x)//k)
    
    for i in range(char_Group1):
        result+=x[i]
    
    next_char=char_Group1    
    for j in range(num_groups):
        
        result+='-'
        result+=x[next_char:next_char+k]
        next_char+=k
        
    return result.upper().strip('-')

s=["5fdfdsf-sf45ds-s32s5ds",
   "5F3Z-2e-9-w" ,
   "2-5g-3-J"]
k=[3,4,2]

for lic,gr in zip(s,k):
    print("\n License Key Formatting From '"'%s'"' to '"'%s'"' ,Grouping each %d letters together" %(lic,licenseKeyFormatting(lic,gr),gr))


# In[ ]:





# # 12) 1009. Complement of Base 10 Integer
# The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in its binary representation.
# For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.
# Given an integer n, return its complement.

# In[16]:


def bitwiseComplement( n: int) -> int:
    digit=0;
    i=0
    result=0
    if(n==0): #base case for dealing with input zero
        result=1
    #checking if the number is divisable by two to get the left bit in its repersntation
    # we add the counterpart to the result( if 0 in first bit we add 1, if 0 in secoend bit we add 2)
    
    while(n>0):
        if(n%2==0):
            digit=1
        else:
            digit=0
            
        result+=(2**i)*digit
        n//=2
        i+=1
    
    return result
num=int(input("Enter Number: "))
print("\nThe Counterpart for The Number %d is: %d" %(num,bitwiseComplement(num)))


# In[ ]:





# # 13) 268. Missing Number
# Given an array nums containing n distinct numbers in the range [0, n],
# return the only number in the range that is missing from the array.

# In[17]:


def missingNumber( nums) -> int:
    """Since the sum of the numbers follows the rule of sum for mathamatical series
    we use that for our advantage and looke for the missing number from the total of the original series"""
    size=(len(nums)*(len(nums)+1))/2
    for elem in nums:
        size-=elem
    return int(size)
nums = [[3,0,1],
        [0,1,2,3,4,8,7,5],
        [0,1],
        [9,6,4,2,3,5,7,0,1],
        [1,2,3,4]]

for num  in nums:
    print("\nMissing Number From thr Series %s is: %d" %(num,missingNumber(num)))
    


# In[ ]:





# # 14) 2022. Convert 1D Array Into 2D Array
# 
# You are given a 0-indexed 1-dimensional (1D) integer array original, and two integers, m and n. You are tasked with creating a 2-dimensional (2D) array with m rows and n columns using all the elements from original.
# 
# The elements from indices 0 to n - 1 (inclusive) of original should form the first row of the constructed 2D array, the elements from indices n to 2 * n - 1 (inclusive) should form the second row of the constructed 2D array, and so on.
# 
# Return an m x n 2D array constructed according to the above procedure, or an empty 2D array if it is impossible.
# 

# In[19]:


def construct2DArray( original, m: int, n: int) :
    """
    simply move the first n elements to the first row
    and so on
    """
    array_2d=[ []*n for i in range(m)]

    if len(original)!=(m*n):
        return []
    
    for i in  range(m):
        array_2d[i][:]=original[n*i:n*(i+1)]
    return array_2d





values=[([1,2,3],1,3),
        ([1,2,3,4],2,2),
        ([1,2],1,1),
        ([1,2,3,4,5,6,7,8],4,2)]

for arr,m,n in values:
    print("\n Th Original array is: %s, The 2D Array with Dimosion %d by %d is:\n%s" %(arr,m,n,np.matrix(construct2DArray(arr,m,n))   ))
     


# In[ ]:





# In[ ]:





# # 15) 2293. Min Max Game
# You are given a 0-indexed integer array nums whose length is a power of 2.
# Apply the following algorithm on nums:
# 
# Let n be the length of nums. If n == 1, end the process. Otherwise, create a new 0-indexed integer array newNums of length n / 2.
# For every even index i where 0 <= i < n / 2, assign the value of newNums[i] as min(nums[2 * i], nums[2 * i + 1]).
# For every odd index i where 0 <= i < n / 2, assign the value of newNums[i] as max(nums[2 * i], nums[2 * i + 1]).
# Replace the array nums with newNums.
# Repeat the entire process starting from step 1.
# Return the last number that remains in nums after applying the algorithm

# In[20]:


def minMaxGame( nums) -> int:
    def  mini_Game(nums):
            if (len(nums)==1):
                return nums[0]
    
            newNums=[0]*(len(nums)//2)


            for i in range(len(newNums)):
                if(i%2==1):
                    newNums[i]=max(nums[2*i],nums[2*i+1])
                else:
                    newNums[i]=min(nums[2*i],nums[2*i+1])

            return mini_Game(newNums)
            
    return mini_Game(nums)


nums = [[5,3,7,8,9,7,6,4],
        [1,3,5,2,4,8,2,2],
        [3],
        [1,1,2,2,3,3,4,4]]

for i in nums:
    print("\nThe Mini Max Game Result for %s is: %s" %(i,minMaxGame(i)))


# In[ ]:





# # Medeium

# # 1) 2304. Minimum Path Cost in a Grid
# You are given a 0-indexed m x n integer matrix grid consisting of distinct integers from 0 to m * n - 1. You can move in this matrix from a cell to any other cell in the next row. That is, if you are in cell (x, y) such that x < m - 1, you can move to any of the cells (x + 1, 0), (x + 1, 1), ..., (x + 1, n - 1). Note that it is not possible to move from cells in the last row.
# 
# Each possible move has a cost given by a 0-indexed 2D array moveCost of size (m * n) x n, where moveCost[i][j] is the cost of moving from a cell with value i to a cell in column j of the next row. The cost of moving from cells in the last row of grid can be ignored.
# 
# The cost of a path in grid is the sum of all values of cells visited plus the sum of costs of all the moves made. Return the minimum cost of a path that starts from any cell in the first row and ends at any cell in the last row.

# In[23]:


def minPathCost(grid, moveCost) -> int:
    m=len(grid)
    n=len(grid[0])
    d=grid[0][:]

    for j in range(1,m): #row index
        cost=grid[j][:]
        for k in range(n): #coloum index
            cost[k]+=min(d[l]+moveCost[grid[j-1][l]][k] for l in range(n))
        d=cost
            
    return(min(d))
    

grid = [[[5,3],[4,0],[2,1]],
        [[5,1,2],[4,0,3]]]
moveCost = [[[9,8],[1,5],[10,12],[18,6],[2,4],[14,3]],
            [[12,10,15],[20,23,8],[21,7,1],[8,1,13],[9,10,25],[5,3,2]]]

for g,move in zip(grid,moveCost):
    print("\nMinimum Path Cost for the Grid \n%s is: %d" %(np.matrix(g),minPathCost(g, move)))


# In[ ]:





# In[ ]:





# # 2) 669. Trim a Binary Search Tree
# 
# Given the root of a binary search tree and the lowest and highest boundaries as low and high, trim the tree so that all its elements lies in [low, high]. Trimming the tree should not change the relative structure of the elements that will remain in the tree (i.e., any node's descendant should remain a descendant). It can be proven that there is a unique answer.
# 
# Return the root of the trimmed binary search tree. Note that the root may change depending on the given bounds.
# 
#  

# In[24]:


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
          self.val = val
          self.left = left
          self.right = right

def trimBST(root, low, high) :
    if not root:
        return None
    if root.val>high:
        return trimBST(root.left,low, high)
        
    if root.val<low:
        return trimBST(root.right,low, high)
    root.left=trimBST(root.left,low, high)
    root.right=trimBST(root.right,low, high)
    return root 

        


# In[ ]:





# ## 3) 337. House Robber III
# The thief has found himself a new place for his thievery again. There is only one entrance to this area, called root.
# 
# Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that all houses in this place form a binary tree. It will automatically contact the police if two directly-linked houses were broken into on the same night.
# 
# Given the root of the binary tree, return the maximum amount of money the thief can rob without alerting the police.

# In[25]:


def rob(root) -> int:
    def depthSearch(root):
        if not root:
            return [0,0]

        leftside=depthSearch(root.left)
        rightside=depthSearch(root.right)

        withRoot=root.val+leftside[1]+rightside[1]
        withoutRoot=max(leftside)+max(rightside)

        return [withRoot,withoutRoot]
    return max(depthSearch(root))
        


# In[ ]:





# In[ ]:





# ## 4) 152. Maximum Product Subarray
# Given an integer array nums, find a subarray that has the largest product, and return the product.
# 
# The test cases are generated so that the answer will fit in a 32-bit integer.

# In[26]:


'''
The idea is to keep track of minimum and maximum of the subarray just in case the next elemnt is 
negative which can swich between the min and max, since we are dealing with multiplication each 
time we run into zero we set the value back to 1
'''
def maxProduct( nums) -> int:
    maxVal=max(nums)
    tempMin,tempMax=1,1
    
    for num in nums:
        if num==0:
            tempMin,tempMax=1,1
            continue
        temp=num*tempMax #saving the product between the new element and the previous maximum
        tempMax=max(num*tempMax,num*tempMin,num)
        tempMin=min(temp,num*tempMin,num)
        maxVal=max(maxVal,tempMax)
    return maxVal

nums = [[2,3,-2,4],
        [-2,0,-1],
        [1,10,0,1,2,2,0,4,5,0,1,2,4]]
for num in nums:
    print("\nMaximum Product Subbarray for  array %s is: %d"%(num,maxProduct( num)))


# In[ ]:





# ## 5) 55. Jump Game
# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
# 
# Return true if you can reach the last index, or false otherwise.

# In[27]:


'''
we start from the end and check if we can get to the end from the previous element( if(i+nums[i]>=endTarget) ) 
if not we go one step back to chack if we can get from that point to the end,
at some point if we could reach the end from a certin previous point we rename that point as the new target 
and check if we can get to the new target from any other previous elemnts
'''
def canJump(nums) -> bool:
    
    endTarget=len(nums)-1
    for i in range(len(nums)-1,-1,-1):
        if i+nums[i]>=endTarget:
            endTarget=i
        
    return (endTarget==0)

    
nums=[[2,0,1,1,4,3],
      [2,3,1,1,4],
      [3,2,1,0,4],
      [2,1,0,0]]      

for num in nums:
    if canJump(num):
        print("\n for Array %s it is Possible to Reach The End" %(num))
    else:
        print("\n for Array %s it is Not Possible to Reach The End"%(num))
    


# In[ ]:





# ## 6) 36. Valid Sudoku
# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
# 
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

# In[31]:


"""
The idea is to create 3 unique hash sets (columns, rows, squares)
for the columns and rows set the keys are the values (0-9)
for squares the key is a tuple of indexes from (0-2), for each square we give indexes(Exmaple: top left square is (0,0))  
if the value was already found in one of the three sets -> return False
for the squares we  transform the indexes[i,j] to corresponding indexes in the set
"""

def isValidSudoku(board) :
    cols=defaultdict(set)
    rows=defaultdict(set)
    squares=defaultdict(set)
    
    for j in range(9):
        for i in range(9):
            if board[j][i]==".":
                continue
            if (board[j][i] in rows[j] or
                board[j][i] in  cols[i] or
                #since each 3 elements fall in the same square , we can use div to calculate the right square for each elemnt
                board[j][i] in squares[(j//3,i//3)]):
                
                    return False
            cols[i].add(board[j][i])
            rows[j].add(board[j][i])
            squares[(j//3,i//3)].add(board[j][i])       
    return True
     
boards= [[["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]],
         [["8","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]]


for board in boards:    
    if(isValidSudoku(board)):
        print("\nThe Board: \n%s is a valid Sudoku" %(np.matrix(board)))
    else:
        print("\nThe Board: \n%s is Not a valid Sudoku"%(np.matrix(board)))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ## 7) 1472. Design Browser History
# You have a browser of one tab where you start on the homepage and you can visit another url, get back in the history number of steps or move forward in the history number of steps.
# 
# Implement the BrowserHistory class:
# 
# BrowserHistory(string homepage) Initializes the object with the homepage of the browser.
# void visit(string url) Visits url from the current page. It clears up all the forward history.
# string back(int steps) Move steps back in history. If you can only return x steps in the history and steps > x, you will return only x steps. Return the current url after moving back in history at most steps.
# string forward(int steps) Move steps forward in history. If you can only forward x steps in the history and steps > x, you will forward only x steps. Return the current url after forwarding in history at most steps.

# In[32]:


"""
creating Nodes with double connections to represent back and forward from the url
initialy only homepage
visiting next page will create a new node and connect it to the current url and restting the cuurent to the new visited url
that way we can delete any forwars nodes that represnt pages in the forward history
back/forward update according to step number if not possible get to the first/last page
"""
class Node:
    def __init__(self,val,prev=None,next=None):
        self.val=val
        self.prev=prev
        self.next=next
        
class BrowserHistory:

    def __init__(self, homepage):
         self.curr=Node(homepage)

    def visit(self, url) :
        self.curr.next=Node(url,self.curr)
        self.curr=self.curr.next
            

    def back(self, steps) :
        while self.curr.prev and steps >0:
            self.curr=self.curr.prev
            steps-=1
        return self.curr.val
        

    def forward(self, steps) :
        while self.curr.next and steps >0:
            self.curr=self.curr.next
            steps-=1
        return self.curr.val
        
browserHistory = BrowserHistory("leetcode.com");
print("\nHome Page is:",browserHistory.curr.val)
browserHistory.visit("google.com");
print("\nVist page:",browserHistory.curr.val)
browserHistory.visit("facebook.com");
print("\nVist page:",browserHistory.curr.val)
browserHistory.visit("youtube.com");
print("\nVist page:",browserHistory.curr.val)
d=1
browserHistory.back(d);
print("\nGo Back %d pages:"%d,browserHistory.curr.val)
browserHistory.back(d);
print("\nGo Back %d pages:"%d,browserHistory.curr.val)
browserHistory.forward(d);
print("\nGo Forward %d pages:"%d,browserHistory.curr.val)
browserHistory.visit("linkedin.com");
print("\nVist page:",browserHistory.curr.val)
d=2
browserHistory.forward(2);
print("\nGo Forward %d pages:"%d,browserHistory.curr.val)
d=2
browserHistory.back(2); 
print("\nGo Back %d pages:"%d,browserHistory.curr.val)
d=7
browserHistory.back(7);
print("\nGo Back %d pages:"%d,browserHistory.curr.val)


# In[ ]:





# ## 8) 473. Matchsticks to Square
# 
# You are given an integer array matchsticks where matchsticks[i] is the length of the ith matchstick. You want to use all the matchsticks to make one square. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.
# 
# Return true if you can make this square and false otherwise.

# In[33]:


def makesquare(matchsticks):
    n=len(matchsticks)
    
    per=sum(matchsticks)
    if per%4 !=0:
        return False
    else:
        side=per//4
    
    matchsticks.sort(reverse=True)
    def dfs(a,b,c,d,k):
        if k==n:
            if a==b==c==d:
                return True
            return False
        m=matchsticks[k]
        if a+m<=side and dfs(a+m,b,c,d,k+1):
            return True
        if b+m<=side and dfs(a,b+m,c,d,k+1):
            return True
        if c+m<=side and dfs(a,b,c+m,d,k+1):
            return True
        if d+m<=side and dfs(a,b,c,d+m,k+1):
            return True
        return False
    return dfs(0,0,0,0,0)

matchsticks=[[1,1,2,2,2],
             [3,3,3,3,4],
             [2,3,5,4,1,2,3],
             [2,2,3,4]]
for matchstick in matchsticks:
    
    if makesquare(matchstick):
        print("\n Match Sticks with measurments of %s: It is Possible to create a Square"%matchstick)
    else:
         print("\n Match Sticks with measurments of %s: It is  Not Possible to create a Square"%matchstick)   


# In[ ]:





# ## 9) 825. Friends Of Appropriate Ages
# There are n persons on a social media website. You are given an integer array ages where ages[i] is the age of the ith person.
# 
# A Person x will not send a friend request to a person y (x != y) if any of the following conditions is true:
# 
# age[y] <= 0.5 * age[x] + 7
# age[y] > age[x]
# age[y] > 100 && age[x] < 100
# Otherwise, x will send a friend request to y.
# 
# Note that if x sends a request to y, y will not necessarily send a request to x. Also, a person will not send a friend request to themself.
# 
# Return the total number of friend requests made.

# In[34]:


"""
using counter, we find the number of repition for each age
then we find out if a request is made by checking all the requirments
we add the product of both  ages's number of occurances
special case: checking the same age with it self -> we subtract the people with themself from the product
"""

def numFriendRequests(ages) -> int:
    def friendRequest(a,b):                
        if b<=(0.5*a +7):
            return False
        if b>a:
            return False
        if b>100 and a<100:
            return False 
        return True
    
    age_groups=Counter(ages)
    total_requests=0
    for j,num_j in age_groups.items():
        for i,num_i in age_groups.items():
            if friendRequest(j,i):
                total_requests+=num_i*num_j
                if i==j:
                    total_requests-=num_i

    return total_requests



ages=[[16,16],
      [16,17,18],
      [20,30,100,110,120]]
for age in ages:
    print("\nTHe number of Friends Requests for the Group %s is: %d" %(age,numFriendRequests(age)))


# In[ ]:





# ## 10) 2034. Stock Price Fluctuation
# You are given a stream of records about a particular stock. Each record contains a timestamp and the corresponding price of the stock at that timestamp.
# 
# Unfortunately due to the volatile nature of the stock market, the records do not come in order. Even worse, some records may be incorrect. Another record with the same timestamp may appear later in the stream correcting the price of the previous wrong record.
# 
# Design an algorithm that:
# 
# Updates the price of the stock at a particular timestamp, correcting the price from any previous records at the timestamp.
# Finds the latest price of the stock based on the current records. The latest price is the price at the latest timestamp recorded.
# Finds the maximum price the stock has been based on the current records.
# Finds the minimum price the stock has been based on the current records.
# Implement the StockPrice class:
# 
# StockPrice() Initializes the object with no price records.
# void update(int timestamp, int price) Updates the price of the stock at the given timestamp.
# int current() Returns the latest price of the stock.
# int maximum() Returns the maximum price of the stock.
# int minimum() Returns the minimum price of the stock.

# In[36]:


class StockPrice:

    def __init__(self):
        self.prices = {}
        self.latest = (None,None)
        self.sl=SortedList()

    def update(self, timestamp: int, price: int) -> None:
        
        if timestamp in self.prices:
            self.sl.remove(self.prices[timestamp])
        if self.latest[0] is None or timestamp >= self.latest[0]:
            self.latest=(timestamp,price)
        self.sl.add(price)
        self.prices[timestamp]=price
        
    def current(self) -> int:
        return self.latest[1]


    def maximum(self) -> int:
        return self.sl[-1]
            

    def minimum(self) -> int:
        return self.sl[0]
    
obj = StockPrice()
stock_updates={(1,10),(2,5),(1,3),(4,2)}
for (timestamp,price) in stock_updates:
    obj.update(timestamp,price)
    param_2 = obj.current()
    param_3 = obj.maximum()
    param_4 = obj.minimum()
    print("Current stak price is:",param_2," ,Maximum stack price so far:",param_3," Minimum Stack price so far is:",param_4)
print("\nStack prices Up tp Date: ",obj.prices)


# In[ ]:





# In[ ]:





# # Hard

# ## 1) 2296. Design a Text Editor
# Design a text editor with a cursor that can do the following:
# 
# Add text to where the cursor is.
# Delete text from where the cursor is (simulating the backspace key).
# Move the cursor either left or right.
# When deleting text, only characters to the left of the cursor will be deleted. The cursor will also remain within the actual text and cannot be moved beyond it. More formally, we have that 0 <= cursor.position <= currentText.length always holds.
# 
# Implement the TextEditor class:
# 
# TextEditor() Initializes the object with empty text.
# void addText(string text) Appends text to where the cursor is. The cursor ends to the right of text.
# int deleteText(int k) Deletes k characters to the left of the cursor. Returns the number of characters actually deleted.
# string cursorLeft(int k) Moves the cursor to the left k times. Returns the last min(10, len) characters to the left of the cursor, where len is the number of characters to the left of the cursor.
# string cursorRight(int k) Moves the cursor to the right k times. Returns the last min(10, len) characters to the left of the cursor, where len is the number of characters to the left of the cursor.

# In[37]:


class TextEditor:
    
    #initializing empty text, and stack to help
    def __init__(self):
        self.txt=[]
        self.stack=[]
    
    #adding text to the last character in text
    def addText(self, text: str) -> None:
        for ch in text:
            self.txt.append(ch)
    
    #deleting from the last character k letters       
    def deleteText(self, k: int) -> int:
        del_num=min(k,len(self.txt))
        for c in range(del_num):
            self.txt.pop()
        return del_num
    
    #pointing to the kth letter from the left of the last character
    def cursorLeft(self, k: int) -> str:
        while self.txt and k>0:
            self.stack.append(self.txt.pop())
            k-=1
        return self.getStr()
    
    #pointing to the kth letter from the right of the last character
    def cursorRight(self, k: int) -> str:
        while self.stack and k>0:
            self.txt.append(self.stack.pop())
            k-=1
        return self.getStr()
    
    #returns either the text or all but 10 last letters from the text
    def getStr(self):
        if len(self.txt)<10:
            return ''.join(self.txt)
        return ''.join(self.txt[-10:])
    

obj = TextEditor()
obj.addText("leetcode")
param_2 = obj.deleteText(4)
obj.addText("practice")
obj.cursorRight(3)
obj.cursorLeft(8)
obj.deleteText(10)
obj.cursorLeft(2)
print(obj.cursorRight(6))




# In[ ]:





# ## 2) 1755. Closest Subsequence Sum
# You are given an integer array nums and an integer goal.
# 
# You want to choose a subsequence of nums such that the sum of its elements is the closest possible to goal. That is, if the sum of the subsequence's elements is sum, then you want to minimize the absolute difference abs(sum - goal).
# 
# Return the minimum possible value of abs(sum - goal).
# 
# Note that a subsequence of an array is an array formed by removing some elements (possibly all or none) of the original array.

# In[41]:


"""
First we create a list of sub sum for each half of the original array
next we check if we can insert the sums from the first subarray in the seconed subarray
we try y=to minimize the diffrence between the elemnet from the first subarray and the goal the 
and the element which we where suppose to insert our new element
"""



def minAbsDifference(nums, goal: int) -> int:
    n=len(nums) //2
    result=math.inf
    subarray1=[]
    subarray2=[]
    
    
    def dfb(arr,i,p,sums):
        if i==len(arr):
            sums.append(p)
            return 
        dfb(arr,i+1,p+arr[i],sums)
        dfb(arr,i+1,p,sums)
    
    dfb(nums[:n],0,0,subarray1)
    dfb(nums[n:],0,0,subarray2)
    subarray2.sort()
    
    for Sum1 in subarray1:
        i=bisect_left(subarray2,goal-Sum1)
        if i<len(subarray2):
            result=min(result,abs(goal-Sum1-subarray2[i]))
        if i>0:
            result=min(result,abs(goal-Sum1-subarray2[i-1]))
    return result





numsList = [[5,-7,3,5],
        [7,-9,15,-2],
        [1,2,3]]
goalsForList = [6,-5,-7]

for nl,g in zip(numsList,goalsForList):
    print("Closest Subsequence Sum for Array %s and Goal %d is:"%(nl,g),minAbsDifference(nl, g) )


# In[ ]:





# In[ ]:





# In[ ]:





# ## 3) 127. Word Ladder
# A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:
# 
# Every adjacent pair of words differs by a single letter.
# Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
# sk == endWord
# Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

# In[42]:


"""
start with the first word and figure out what combinaitions with inly 1 letter different can we have, we add thos as a key to a dictionary
next: find out combinations to the words in the list and the word as a value to to the key(combination)
we start by adding the first word to a queue and we check what other word have the same combination
we take out the word and add the next until we reach the end
visit: so we dont use the same word twice
we keep checking until we reach the end word
"""
def ladderLength(beginWord, endWord, wordList) -> int:
    if endWord not in wordList:
            return 0
    #creating dict with combinations as key anw words that make the combination as values    
    newdic=defaultdict(list)
    wordList.append(beginWord)
    for word in wordList:
         for j in range(len(word)):
                pattern = word[:j]+ "*"+ word[j+1:]
                newdic[pattern].append(word)
                
    visit=set([beginWord])
    q=deque([beginWord])
    result=1
    while q:
        for i in range(len(q)):
            word=q.popleft()
            #reaching the end word stops the algorithem 
            if word== endWord:
                return result
            
            for j in range(len(word)):
                pattern = word[:j]+ "*"+ word[j+1:]
                #checking in the list of values for the key pattern
                for neiword in newdic[pattern]:
                    if neiword not in visit:
                        visit.add(neiword)
                        q.append(neiword)
                    
                    
        result+=1
        
        
    return 0
        
        
beginWord = ["hit","hit","hot"]
endWord = ["cog","cog","dog"]
wordList = [["hot","dot","dog","lot","log","cog"],
            ["hot","dot","dog","lot","log"],
            ["hot","dog"]]

for b,e,w in zip(beginWord,endWord,wordList):
    print("\nThe Shortest transformation Sequence for word Beginning with '"'%s'"' and Ending with '"'%s'"' from the List is: %d Long" %(b,e,ladderLength(b, e, w)))


# In[ ]:





# ## 4) 1284. Minimum Number of Flips to Convert Binary Matrix to Zero Matrix
# Given a m x n binary matrix mat. In one step, you can choose one cell and flip it and all the four neighbors of it if they exist (Flip is changing 1 to 0 and 0 to 1). A pair of cells are called neighbors if they share one edge.
# 
# Return the minimum number of steps required to convert mat to a zero matrix or -1 if you cannot.
# 
# A binary matrix is a matrix with all cells equal to 0 or 1 only.
# 
# A zero matrix is a matrix with all cells equal to 0.

# In[46]:


"""
if the metrix is zero matrix -> stop
transverse through each node in the matrix flip its value together with its neighbors using flip function
check if we have visited the new matrix befor if not add it to the queue and work with that
until zero matrix
"""
def minFlips(mat) -> int:
        m,n=len(mat),len(mat[0])
        queue=deque()
        queue.append(mat)
        visitied =set()
        step=0
        
        
        while queue:
            size=len(queue)
            for _ in range(size):
                node=queue.popleft()
                if sum(map(sum,node))==0: #if already zero matrix stop
                    return step
                
                for i in range(m):
                    for j in range(n):
                        newNode=flip(node,i,j)
                        hashNode=tuple(map(tuple,newNode))
                        #checking  if we have the new matrix 
                        if hashNode in visitied:
                            continue
                        
                        #now we work with the transformed matrix
                        queue.append(newNode)
                        visitied.add(hashNode)
            step+=1
        return -1
        
def flip(mat,i,j):
        m,n=len(mat),len(mat[0])
        result=copy.deepcopy(mat)
        result[i][j]^=1 #fliping using XOR
        for dx, dy in [(-1,0),(1,0),(0,1),(0,-1)]:
            x=i+dx
            y=j+dy
            if(x<0 or x>=m or y<0 or y>=n):
                continue
            result[x][y]^=1
        return result
                

mats=[[[0,0],[0,1]],
    [[0]],
    [[1,0,0],[1,0,0]]]
for mat in mats:
    print("\n For The Marix \n%s Minimum flips are: %d" %(np.matrix(mat),minFlips( mat)))


# In[ ]:





# In[ ]:





# ## 5) 834. Sum of Distances in Tree
# There is an undirected connected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.
# 
# You are given the integer n and the array edges where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.
# 
# Return an array answer of length n where answer[i] is the sum of the distances between the ith node in the tree and all other nodes.

# In[47]:


"""
first we create a dict that writes the relationship between one node to the others
second: we calculat how many childs for each Node and add 1 to count the node itself
third: for each node we use the previous calculation but add (n-2count[node]) which is the shift for each node from the root
"""
class Solution:
    def sumOfDistancesInTree(self, n, edges) :
        graph =defaultdict(list)
        for s,t in edges:
            graph[s].append(t)   
            graph[t].append(s)  
            
            
        out=[0]*n
        count=[1]*n
        self.root=0   

        def dfs_tree(cur,parent,depth):
            output=1
            for child in graph[cur]:
                if child!=parent:
                    output+=dfs_tree(child,cur,depth+1)
                    self.root+=(depth+1)
            count[cur]=output
            return output

        dfs_tree(0,-1,0)
        def dfs_tree2(cur,parent,depth):
            out[cur]=depth
            for child in graph[cur]:
                if child !=parent:
                    dfs_tree2(child,cur,depth+(n-count[child]-count[child]))

        dfs_tree2(0,-1,self.root)

        return out
        
    
edges=[[[0,1],[0,2],[2,3],[2,4],[2,5]],
      [],
      [[1,0]],
      [[0,1],[0,2],[2,3],[2,4],[2,5],[3,6],[3,7],[3,8]]]
n=[6,1,2,9]
sol=Solution()
for ed,no in zip(edges,n):
    print("\nSum of Distances for the Tree %s is:\n%s" %(ed,sol.sumOfDistancesInTree(no,ed)))

