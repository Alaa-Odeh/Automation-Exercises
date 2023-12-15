#!/usr/bin/env python
# coding: utf-8

# # Python Basic Exercises

# In[50]:


import numpy as np
import igraph
from igraph import Graph, EdgeSeq


# ## Arrays and Strings:

# ### Write a program to reverse a string in place

# In[3]:


s_string=input("Enter Text:");
print("Original Text: "+s_string)
s_string= s_string[::-1]
print("Reversed Text: "+s_string)


# In[ ]:





# ### Write a program to find the maximum and minimum elements in an array.

# In[6]:


num=input("Enter array size:")
arr=[]
for i in range(int(num)):
    arr.append(input("Enter Element:"))
print("Minimum: " ,arr[0] ,"\nMaximum: " ,arr[-1])


# ### Write a program to remove duplicates from a sorted array

# In[8]:


#creating a temporary array that will only take unique values,

def delete_duplicates(arr):   
    arr_temp=[]
    for i in range(len(arr)-1):
        if(arr[i]!=arr[i+1]):
            arr_temp.append(arr[i])
    arr_temp.append(arr[-1]) #adding the last element
    return(arr_temp)



num=input("Enter array size:")
arr=[]
for i in range(int(num)):
    arr.append(input("Enter Element in sorted order:"))
print("Unique values: ",delete_duplicates(arr))


# In[ ]:





# 

# ## Linked Lists:
#   Write a program to reverse a linked list
#   Write a program to find the middle element of a linked list.
#   Write a program to detect if a linked list has a cycle.
# 
# 

# In[11]:


class Node:
    #create a node object
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    #initialize the head
    def __init__(self):
        self.head = None
        
    #reversing the LinkedList
    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next ##temp 
            current.next = prev ## updating the pointer
            prev = current      ## updating the current
            current = next
        self.head = prev
        
    #insert a new node at the beginning   
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    #length of linkedlist
    def getLen(self, head):
        temp = head
        len = 0
        while (temp != None):
            len += 1
            temp = temp.next
        return len
    
    #print the LinkedList
    def printList(self):
        temp = self.head
        while(temp):
            print (temp.data)
            temp = temp.next
            

    #find the middle element
    def getMiddle(self):
        if self.head != None:
            # find length
            len = self.getLen(self.head)
            temp = self.head
 
            middle = len // 2  # move till we reached half of length
            while middle != 0:
                temp = temp.next
                middle -= 1
            return(temp.data)  # temp stores middle element
            
    
    #Detect a Cycle
    def cycleDetect(self):
        hashTbl=set() 
        temp=self.head
        while(temp):
            if temp in hashTbl:
                return True
            hashTbl.add(temp)
            temp=temp.next
        return False
    
            


# In[12]:


#reversing the list by changing the links bewtween the nodes (fliping the links) and pointing the head to be the
# tail of the list
linklist=LinkedList()  #creating a linkedkist
# adding nodes to thr list
linklist.push(5)
linklist.push(46)
linklist.push(73)
linklist.push(29)
linklist.push(86)
print("Original LinkedList")
linklist.printList()
#reverse the list
linklist.reverse()
print("Reversed LinkedList")
linklist.printList()


# In[ ]:





# In[13]:


# Write a program to find the middle element of a linked list
print("The middle element of the Linked List is: %d" %(linklist.getMiddle()))


# In[ ]:





# In[14]:


#Write a program to detect if a linked list has a cycle.
# Create a loop
linklist.head.next.next.next=linklist.head

# the idea is to build a hash table that can only containg unique values,
#once we find the same value again it means that we have a loop

if (linklist.cycleDetect()):
    print("Loop was Found")
else:
    print("Loop was Not Found")


# In[ ]:





# ## Stacks and Queues

# In[15]:


#creat stack classe
from _collections import deque

class Stack:
 
    def __init__(self):
        # Two inbuilt queues
        self.q1 = deque()
        self.q2 = deque()
        

    def push(self, x):
        # Push x first in empty q2
        self.q2.append(x)
    ##remove all elemnts except the last one added, 
    ##take the last element as temp and swap the queues    
    def pop(self): 
        if not self.q2:
            return -1
        while(len(self.q2)!=1):
            temp=self.q2.popleft()
            self.q1.append(temp)
        stack_top=self.q2.pop()
        self.q1,self.q2=self.q2,self.q1
        
        
        return stack_top
    
        
    
        


# In[16]:


#Implement a stack using two queues
s = Stack()  #creating a stack
s.push(1)    #adding elements
s.push(2)
s.push(3)
s.push(4)    
s.push(5)
s.push(6)

print(s.pop()) #poping elements LIFO
print(s.pop())
print(s.pop())



# In[17]:


class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []
    
    def push(self,x):
        #move everything to s2 and push x to s1
        while len(self.s1) != 0: 
            self.s2.append(self.s1[-1]) 
            self.s1.pop()
        self.s1.append(x) 
 
        # Push everything back to s1 
        while len(self.s2) != 0: 
            self.s1.append(self.s2[-1]) 
            self.s2.pop()    
    def pop(self):
         
            # if first stack is empty 
        if len(self.s1) == 0: 
            return -1;
     
        # Return top of s1 
        x = self.s1[-1] 
        self.s1.pop() 
        return x


# In[18]:


q = Queue()
q.push(1) 
q.push(2) 
q.push(3) 
q.push(4) 
q.push(5) 
print(q.pop())
print(q.pop())
q.push(6) 
print(q.pop())


# In[20]:


# Write a program to check if a given string of parentheses is balanced.
# the idea is to create a stack an fill it up with openining parentheses 
# and then we compare the last parentheses in the stack with coresponding 
#closing parenthese if match was not found return false
def isBalanced(text):
    s_stack=[] 
    for char in text:
        if char in['(','{','[']:
            s_stack.append(char)
        else :
            if not s_stack:
                return False
            current_char=s_stack.pop()

            if current_char=='(':
                if char!=')':
                    return False

            if current_char=='{':
                if char!='}':
                    return False


            if current_char=='[':
                if char!=']':
                    return False
            
    if s_stack:
        return False
    return True
            
            
            


# In[21]:


text=["()",
   "[(1(2(3(4(5(6))))))+(1(2(3(4(5))))}])", ## Num of opening paren = Num of closing paren
    "([{1(234(5(6))))))+(1(2(3(4(5)]}))", ## Num of opening paren < Num of closing paren
    "(1(234(5(6))}}{{}}))+(1(2(3(4(5))))"] ## Num of opening paren > Num of closing paren
for t in text:
    
    print("Checking if the parentheses in the Text "+t+ " is balanced:" ,isBalanced(t))


# In[ ]:





# 
# # Trees and Graphs

# In[23]:


#Write a program to find the lowest common ancestor of two nodes in a binary tree
#create a tree node
class Node:
    # Constructor to create a new binary node
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

#function to find the path from the root to the node         
def pathToNode(root,path,val):
   #return false if root is null
    if root is None:
        return False
    
    #push root val to the list
    path.append(root.val)
    
    #if we found the deired node return true
    if root.val==val:
        return True
    
    if((root.left != None and pathToNode(root.left,path,val)) or (root.right != None and pathToNode(root.right,path,val))):
           #if we find the note on the left or right subtree return true
            return True
    
    path.pop() #backtracking by removing the last element
    return False

        
def findLCA(root,n1,n2):
    #lists to store the paths from the root to node
    path1=[]
    path2=[]
    
    
    if (not pathToNode(root,path1,n1) or not pathToNode(root,path2,n2)):
        return -1 #if LCA not found return -1
    i=0
    
    #checking the first Not common ancestor 
    while (i<len(path1) and i<len(path2)):
        if path1[i] != path2[i]:
            break
        i+=1
    return path1[i-1] #returning the last common ancestor


# In[24]:


#application by creating A 3-Layerd TREE
root = Node(3)
root.left = Node(5)
root.right = Node(1)
root.left.left = Node(6)
root.left.right = Node(2)
root.right.left = Node(0)
root.right.right = Node(8)
root.left.right.left = Node(7)
root.left.right.right = Node(4)

print("Last Common Ancestor for %d and %d is: "%(4,5),findLCA(root,4,5))
print("Last Common Ancestor for %d and %d is: "%(1,8),findLCA(root,1,8))
print("Last Common Ancestor for %d and %d is: "%(3,4),findLCA(root,3,4))
print("Last Common Ancestor for %d and %d is: "%(2,4),findLCA(root,2,4))
print("Last Common Ancestor for %d and %d is: "%(6,7),findLCA(root,6,7))
print("Last Common Ancestor for %d and %d is: "%(7,8),findLCA(root,7,8))


# In[25]:


#Write a program to find the shortest path between two nodes in a graph.
def shortest_path(graph, node1, node2):
    path_list = [[node1]]
    path_index = 0
    # To keep track of previously visited nodes
    previous_nodes = {node1}
    if node1 == node2:
        return path_list[0]
        
    while path_index < len(path_list):
        current_path = path_list[path_index]
        last_node = current_path[-1]
        next_nodes = graph[last_node]
        # Search goal node
        if node2 in next_nodes:
            current_path.append(node2)
            return current_path
        # Add new paths
        for next_node in next_nodes:
            if not next_node in previous_nodes:
                new_path = current_path[:]
                new_path.append(next_node)
                path_list.append(new_path)
                # To avoid backtracking
                previous_nodes.add(next_node)
        # Continue to next path in list
        path_index += 1
    # No path is found
    return []


# In[26]:


graph = {}
graph[1] = {2, 5}
graph[2] = {1, 3, 5}
graph[3] = {2, 4}
graph[4] = {3, 5, 6}
graph[5] = {1, 2, 4}
graph[6] = {4}
shortest_path(graph, 5, 3)


# In[ ]:





# In[27]:


#Implement a binary search tree and write functions to insert, delete and search  for elements

class BinarySearchTree:
    # Constructor to create a new binary tree
    def __init__(self,val=None):
        self.val = val
        self.left = None
        self.right = None
        
         
    
    #using the informaition that the nodes on the left of the root are smaller \
    #we recurcivly search for the matching node within the right subtree
    
    #we keep searching for the right position for the node all the way until
    #we reach a null node in the right side of the tree
    def insert(self,val):
        if not self.val:
            self.val=val
            return
        if self.val==val:
            return
        if val<self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left=BinarySearchTree(val)

        if val>self.val:
            if self.right:
                self.right.insert(val)
                return
            self.right=BinarySearchTree(val)
            
def inOrder(node):
    current=node
    while (current.left is not None):
        current=current.left
    return current


def nodeDeletion(tree,val):
        if tree is None:
            return tree


        if val < tree.val:
            tree.left=nodeDeletion(tree.left,val)

        elif val > tree.val:
            tree.right=nodeDeletion(tree.right,val)

        else:
            if tree.left is None:
                temp=tree.right
                tree=None
                return temp

            elif tree.right is None:
                temp=tree.left
                tree=None
                return temp

            temp=inOrder(tree.right)
            tree.val=temp.val
            tree.right=nodeDeletion(tree.right,temp.val)

        return tree

def searchinTree(tree,x):
    node = tree
    depth = 0

    while True:
        depth += 1
        if node.val == x:
            break
        elif x < node.val:
            node = node.left
        elif x > node.val:
            node = node.right
    return depth

    #before we delete a node, we hold on to the subtree that connects to the node and then,
    #reattach it to the parent node of the node thats being deleted

    



# In[30]:


tree = BinarySearchTree()
for i in range(20,100,10):
    tree.insert(i)
for i in range(0,100,5):
    tree.insert(i)

tree=nodeDeletion(tree,20)
print(searchinTree(tree,55))



# In[ ]:





# ## Sorting Algorithms

# ## Bubble Sort Algorithem
# Worse case scinario is having to go through the entire pairs of the array
# each iteration results in the biggest number moving to the end of the array
# thus each iteration actually goes through n-1 elements than the prevoius iteration
# councluding the time comlixity: O(n^2)

# In[31]:


#Implement the bubble sort algorithm.
#we keep swiching between two adjecent elements and keep reapeting the process till fully sorted
def bubbleSort(arr):
    n = len(arr)
    # if the array is already sorted, it doesn't need to go through the entire process
    flag = False
    # walkthrough through all array elements
    for i in range(len(arr)-1):

        for j in range(0, len(arr)-i-1):
             
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                flag = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
         
        if not flag:
            #if we didnt need to swap any elemnts in the inner loop -> array is sorted
            return
 
 


# In[33]:


arr = [1,62,43,85,29,0,76,102,5000]

print("Original array:" ,arr) 

bubbleSort(arr)
 
print("\nSorted array using Bubble sort Algorithem is:",arr)


# In[ ]:





# ## Merge Sort Algorethim
# in the algorethim, we chose to sort the right half and the left half of the array so we take that operation in consideration when we calculate the time complexity, their's also the mergeing of the two half as well
# each time we cut the array in half we have to add the time complixety until we reach one element in each side (n elements)
# T(n)=n+nlogn -> O(nlogn)
# 

# In[34]:


#Implement the merge sort algorithm.
#we recursively divide the array to 2 subarrays untill we get to the smalles subarray
#and then we performe merging in the right order
def merge(arr,i,m,n):
    len_subarray1=m-i+1
    len_subarray2=n-m
    #temperary arrays
    subarray1=[0]*len_subarray1
    subarray2=[0]*len_subarray2
    
    
    #move data to the right array
    for j in range(0,len_subarray1):
        subarray1[j]=arr[i+j]
    for k in range(0,len_subarray2):
        subarray2[k]=arr[m+1+k]
        
    #merging the two subarrays into one
    j,k,l=0,0,i #initial indexes for subarray1, subarray2,mergerd array
    
    #inserting the right element in the right oder
    while(j<len_subarray1) and (k<len_subarray2):
        if subarray1[j]<=subarray2[k]:
            arr[l]=subarray1[j]
            j+=1
        else:
            arr[l]=subarray2[k]
            k+=1
        l+=1
    
    
    #since one of the subarrays is doomed to finish first we need to add
    #the rest of the elements to the array
    while j<len_subarray1:
        arr[l]=subarray1[j]
        j+=1
        l+=1
    while k<len_subarray2:
        arr[l]=subarray2[k]
        k+=1
        l+=1

        
def mergeSort(arr,i,n):
    if  i < n:
        
        m=i+(n-i)//2
        mergeSort(arr,i,m)
        mergeSort(arr,m+1,n)
        merge(arr,i,m,n)
        


# In[35]:


arr = [1,62,43,85,29,0,76,102,5000]

n = len(arr)
print("Original array is: ",arr)

mergeSort(arr, 0, n-1)
print("\nSorted array using merge-sort algorithem is: ",arr)

 


# In[ ]:





# ## Quick Sort Algorethim
# the same as in the merge sort algorethim but this time we chose a pivot to work around it
# but, at each level we still work with n elemnts and we have log(n)layers or leves to partition the array until 1 element is lef, thus the time complexity is (nlogn)

# In[36]:


#Implement the quicksort algorithm.

#we recursively divid the array to 2 subarrays around a specific pivote untill we get one 
#element array and then we start swiching the elements such that the smaller than the pivot is on its left side


def partition(array,left,right):
    #let us choose the the last right element as pivot
    pivot=array[right]
    
    
    #pointer for the left element, going to be the biggest element
    i=left-1
    
    #copmare each element with pivot
    for j in range(left,right):
        if array[j]<= pivot:
            #if element is smaller than pivot swap it with the pointer of the left element
            i+=1
            #swapping
            array[i],array[j]=array[j],array[i]
            
            
    #swap the pivot with the biggest element
    array[i+1],array[right]=array[right],array[i+1]
    
    
    return i+1 #the position from where the partition is done





def quickSort(array,left, right):
    if left<right:
        
        #find pivot 
        pivot=partition(array,left,right)
        #perfom quick sort on each subarray from the pivot element
        quickSort(array,left, pivot-1)
        quickSort(array, pivot+1,right)

    
    
    


# In[37]:


arr = [1,62,43,85,29,0,76,102,5000]
print("Original Array is: ",arr)


size = len(arr)

quickSort(arr, 0, size - 1)

print('\nSorted Array using Quick sort algorithem is: ',arr)


# In[38]:


#Implement the linear search algorithm.
#moving through the array untill we find the target
def search (array,target):
    n=len(array)
    for i in range(0,n):
        if(arr[i]==target):
            return i
    return -1


# In[40]:


arr = [1,62,43,85,29,0,76,102,5000]
print("Array is: ",arr)
elem =search (arr,102)
if(elem==-1):
        print("\nElement Not Found")
else:
        print('\nElement fount at index %d using Linear Search Algorithem '%elem)


# In[ ]:





# In[41]:


#Implement the binary search algorithm
#assuming sorted array we start the search at the middle of the array if not found ->
# we move to the corresponding half depending on the reletavness of the target to the middle element
def binarySearch(array,i,n,target):
   while i<=n:
       mid=i+(n-i)//2
       
       if array[mid]==target: #checking if the target is right at the middle
           return mid
       elif array[mid]<target: #checking the reltavness of the target to the middle
           i=mid+1
       else:
           n=mid-1
   return -1 #   if not found return -1


# In[43]:


arr = [1,62,43,85,29,0,76,102,5000]
print("Original Array is: ",arr)
quickSort(arr,0,len(arr)-1)

print("\nSorted Array is: ",arr)

elem =binarySearch (arr,0,len(arr),85)
if(elem==-1):
        print("\nElement Not Found")
else:
        print('\nElement fount at index %d using Binary Search Algorithem '%elem)


# ##  Recursion

# ## Factorial of a number
# The space complexity for this function is O(1) since we only used one variable and recursively changed it throghout the algorethim

# In[53]:


#Write a program to calculate the factorial of a number using recursion.

def factorial(x):
    if x==0:
        return 1
    return x*factorial(x-1)

num=10
print("Factorial of %d is: %d" %(num,factorial(num)))


# ## Permutations
# There are n! permutations, each of the length n. Hence the space complexity is O(n*n!)

# In[150]:


#Write a program to generate all permutations of a string using recursion

#we keep one part fixed and swap the rest
def permutation(s_string,i,n):
    s=list(s_string)
    if i==n:
        print(''.join(s))
    else:
        for j in range(i,n):
            s[i],s[j]=s[j],s[i]
            permutation(s,i+1,n)
            s[i],s[j]=s[j],s[i] #BackTracking


s="ABCD"
print("All the Possible premutations from the string "+s)
permutation(s,0,len(s))


# ## HASH Table

# In[45]:


#Implement a hash table and write functions to insert, delete, and search for elements.
#chose an array of 500 elemnts to be my container
# the hash function= (index(char)+length(string))^(order(char))%capacity  -> this is to ensure randomizaition

INITIAL_CAPACITY=500
class HashTable:
    #creating a constructor
    def __init__(self):
        self.capacity=INITIAL_CAPACITY
        self.array=[None]*self.capacity
        
    #creating the hash table using the function described above
    def getHash(self,key):  
        hashsum=0
        
        for i,c in enumerate(key):
            hashsum+=(i + len(key)+1)**ord(c)
            hashsum=hashsum%self.capacity
        return hashsum
    
    # this is the insert function, since python uses dictionaries for hash map
    def __setitem__ (self,key,value): 
        #first we get the index for the key by hashing the key
        index=self.getHash(key)
        #and then add the value to the corresponding index
        self.array[index]=value
    
    #this is the search function that retrives the value by hashing the key and ,
    #getting the value in the corresponding index
    def __getitem__(self,key):
        h=self.getHash(key)
        return self.array[h]
    
    
    #delete function simply clears out the value in the arrays[index] ->where index is optained by hashing the key
    def __delitem__(self,key):
        h=self.getHash(key)
        self.array[h]=None

        

        
    




# In[46]:


#implementation
hash_table=HashTable() #create a hash table
hash_table['afdg']=10     # inserting values to the hash table
hash_table['bfdb']=11
hash_table['sfgfc']=12
hash_table['d']=13
hash_table['edfv']=14
hash_table['f']=15
hash_table['gdg']=16
hash_table['hgbd']=17
hash_table['gdf']=20
print("The Hash Table after inserting values: " ,hash_table.array[:50]) 

#Searching for the value of a certin key
print("\nThe Value for Key %s is: %d"%('gdf',hash_table['gdf']))
print("\nThe Value for Key %s is: %d"%('sfgfc',hash_table['sfgfc']))
print("\nThe Value for Key %s is: %d"%('f',hash_table['f']))

#Deleting Value
del hash_table['f']
print("\nThe Hash Table after Deleting value : " ,hash_table.array[:50]) 


# In[ ]:





# ## Bit Manipulation

# In[47]:


# Write a program to check if a given number is even or odd using bit manipulation.
# using And operand with 1
# Even numbers return 1 and odd numbers retun 0
def isEven(x):
    return(not(x & 1))



# Write a program to find the number of set bits in a given integer using bit manipulation
def numOfSetBits(x):
    if(x==0):
        return 0
    else:
        # check first bit on the right
        return (x & 1) + numOfSetBits(x>>1) #shift right 1 bit and check again
    
    
# Implementation:
n=43
if isEven(n):
    print("Number %d is Even" %n)
else:
    print("Number %d is Odd" %n)

    
print("\nNumber of set bits for %d is: " %n,numOfSetBits(n))


# 

# ### ## Question 11
# Suppose you have a grid of n x m cells, where each cell is either empty or contains a rock. You're given a starting position in the grid (x,y), and you want to reach a target  position (tx,ty), but you can only move in four directions (up, down, left, right) and you can only move through empty cells.You're also given a limited number of moves k that you can make. Write a program to determine if it's possible to reach the target position from the starting position within k moves.
# 
# 
# 
# 
# 
# 

# In[48]:


# we transverse through the grid recursively, each time we run into a rock or we move outside the grid-> False is returned
# to avoid going back to cells we already visted, we change the value in that cell to -1, that way we can cut off redundant checks
# if we reach the target with steps left ( at least 0) -> return True


def roadToTarget(grid,x,y,xt,yt,k):
    flag=False
    
    if k < 0 or x==len(grid) or y==len(grid[0]) or grid[x][y]==1 or x==-1 or y==-1:
        return False
    elif (x==xt and y==yt):
        
        return True
    
    elif(grid[x][y]==-1):
        return
    
    else:
        grid[x][y]=-1
        flag=(roadToTarget(grid,x,y+1,xt,yt,k-1) or
        roadToTarget(grid,x,y-1,xt,yt,k-1) or
        roadToTarget(grid,x+1,y,xt,yt,k-1) or
        roadToTarget(grid,x-1,y,xt,yt,k-1) )
    return flag
    
    
    
    


# In[51]:


grid= [[0, 0, 0], [1, 1, 0], [0, 0, 0]]
x,y= 0,0
xt,yt=2,2
k=4
print("The Grid: \n", np.matrix(grid))
print("\nStarting point (%d,%d)\nEnding Point (%d,%d)" %(x,y,xt,yt))
print("Number of steps Required: %d" %k)
if(roadToTarget(grid,x,y,xt,yt,k)):
    print("It is possible to reach the target with %d steps\n" %k)
else:
    print("It is Not possible to reach the target with %d steps\n" %k)

print("___________________________________________________________")
# only one rout is availabe and it takes 10 steps
grid=[[0,0,0,0],[0,0,1,0],[0,1,0,0],[0,1,0,0]] 
x,y= 3,0
xt,yt=3,2
k=10
print("The Grid: \n", np.matrix(grid))
print("\nStarting point (%d,%d)\nEnding Point (%d,%d)" %(x,y,xt,yt))
print("Number of steps Required: %d" %k)
if(roadToTarget(grid,x,y,xt,yt,k)):
    print("It is possible to reach the target with %d steps\n" %k)
else:
    print("It is Not possible to reach the target with %d steps\n" %k)

print("___________________________________________________________")
#this is an impossible situation
grid=[[0,0,0,0],[1,0,0,0],[0,1,0,0],[0,0,1,0]] 
x,y=(3,0)
xt,yt=(3,2)
k=10
print("The Grid: \n", np.matrix(grid))
print("\nStarting point (%d,%d)\nEnding Point (%d,%d)" %(x,y,xt,yt))
print("Number of steps Required: %d" %k)
if(roadToTarget(grid,x,y,xt,yt,k)):
    print("It is possible to reach the target with %d steps\n" %k)
else:
    print("It is Not possible to reach the target with %d steps\n" %k)
    
    
print("___________________________________________________________")
#more than one rout is available the shortest is 3 steps long

grid= [[0, 0, 0], [0, 1, 0], [0, 0, 0]] 
x,y= 0,0
xt,yt=2,1
k=3
print("The Grid: \n", np.matrix(grid))
print("\nStarting point (%d,%d)\nEnding Point (%d,%d)" %(x,y,xt,yt))
print("Number of steps Required: %d" %k)
if(roadToTarget(grid,x,y,xt,yt,k)):
    print("It is possible to reach the target with %d steps\n" %k)
else:
    print("It is Not possible to reach the target with %d steps\n" %k)




# In[ ]:





# In[ ]:





# ## Singleton Design Pattern for Web Logging 

# In[52]:


import logging
class MyLogger:
    #instantiate the logger for the first time
    _logger = None

    ## this dunder method __new__ calls the __init__ method and instantiat a logger
    def __new__(cls, *args, **kwargs):
        if cls._logger is None:

            cls._logger = super().__new__(cls ,*args, **kwargs)
            cls._logger = logging.getLogger("ABC")
            
        
        #returning the logger whether its new or old but not changed     
        return cls._logger
    
    
print("Constructing 2 Loggers From the same Class" )
logger = MyLogger()
logger2 = MyLogger()
print("\nchecking if the Objects are the same one: ",logger is logger2)

logger.info="Hello Logger"
logger2.debug="bug occured"

print("\nChanging info for one Logger object: ", logger2.info)
print("\nChanging debug for one logger object: ", logger.debug)

