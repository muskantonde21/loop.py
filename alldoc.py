# 1.
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# 1
# 44
# 999
# 16 16 16 16 
# 25 25 25 25 25

# i=1
# while i<=5:
#     j=1
#     while j<=i:
#         print(i,end=" ")
#         j+=1
#     print()
#     i+=1

# 2.
# 5
# 4 4
# 3 3 3
# 2 2 2 2
# 1 1 1 1 1


# i=5
# while i>=1:
#     j=5
#     while j>=i:
#         print(i,end=" ")
#         j=j-1
#     print()
#     i=i-1

# 3.
# 5 4 3 2 1
# 5 4 3 2
# 5 4 3
# 5 4
# 5

# i=1
# while i<=5:
#     j=5
#     while j>=i:
#         print(j,end="")
#         j=j-1
#     print()
#     i=i+1

# 4.
# 5
# 54
# 543
# 5432
# 54321

# i=5
# while i>=1:
#     j=5
#     while j>=i:
#         print(j,end="")
#         j=j-1
#     print()
#     i=i-1

# 5.
# 5 5 5 5 5
# 4 4 4 4
# 3 3 3
# 2 2
# 1

# i=5
# while i>=1:
#     j=1
#     while j<=i:
#         print(i,end="")
#         j=j+1
#     print()
#     i=i-1

# 6.
# 12345
# 1234
# 123
# 12
# 1

# i=5
# while i>=1:
#     j=1
#     while j<=i:
#         print(j,end=" ")
#         j=j+1
#     print()
#     i=i-1

# 7.
#     *
#    * *
#   * * *
#  * * * *
# * * * * *

# num=int(input("enter"))
# row=0
# while row<=num:
#     space=num-row-1
#     while space>=0:
#         print(end=" ")
#         space=space-1
#     star=row+1
#     while star>1:
#         print("*",end=" ")
#         star=star-1
#     row=row+1
#     print()

# 8.
# 12345
# 12345
# 12345
# 12345

# i=1
# while i<=5:
#     print(i)
#     j=1
#     while j<=i:
#         print(j,end="")
#         j=j+1
#     i=i+1




from typing import Coroutine


9.
#        1
#      2 2
#    3 3 3
#  4 4 4 4
# 5 5 5 5 5

# i=1
# while i<=5:
#     b=1
#     while b<=5-i:
#         print(' ',end=" ")
#         b=b+1
#     r=1
#     while r<=i:
#         print(i,end=" ")
#         r=r+1
#     print()
#     i=i+1

# 0
# 0 1
# 0 1 4
# 0 1 4 9
# 0 1 4 9 16


# i=0
# while i<5:
#     print(0,end="")
#     j=1
#     while j<=i:
#         print(j*j,end="")
#         j+=1
#     print()
#     i+=1


# *
# **
# ***
# ****
# *****

# i=1
# while i<=5:
#     j=1
#     while j<=i:
#         print("*",end=" ")
#         j=j+1
#     print()
#     i=i+1

# * * * * *
# * * * *
# * * *
# * *
# *

# i=5
# while i>=1:
#     j=1
#     while j<=i:
#         print("*",end=" ")
#         j=j+1
#     print()
#     i=i-1


# A
# B B
# C C C
# D D D D
# E E E E E

# A
# A B 
# A B C
# A B C D
# A B C D E

# i=65
# while i<70:
#     j=65
#     while j<=i:
#         print(chr(j),end=" ")
#         j=j+1
#     print()
#     i=i+1

# p
# p y 
# p y t
# p y t h
# p y t h o
# p y t h o n 

# a="python"
# i=0
# while i<len(a):
#     j=0
#     while j<=i:
#         print(a[j],end=" ")
#         j=j+1
#     print()
#     i=i+1


# Cross

# i=1
# while i<=5:
#     b=1
#     while b<=5-i:
#         print(' ',end=" ")
#         b=b+1
#     r=1
#     while r<=i:
#         print("*",end=" ")
#         r=r+1
#     print()
#     i=i+1
# i=5
# while i>=1:
#     b=5
#     while i>b:
#         print(' ',end=" ")
#         b=b+1
#     r=1
#     while i>=r:
#         print("*",end=" ")
#         r=r+1
#     print()
#     i=i-1


# halfdiamond
# i=1
# while i<=5:
#     j=1
#     while j<=i:
#         print("*",end=" ")
#         j=j+1
#     print()
#     i=i+1
# while i>=1:
#     j=1
#     while j<=i:
#         print("*",end=" ")
#         j=j+1
#     print()
#     i=i-1

# deciaml into binary

# m letter patern
# for row in range (7):
#     for col in range(7):
#         if col==0 or col==6 or ((row==col) and (col>0 and col<4)) or (row==1 and col==5) or (row==2 and col==5):
#            print("*",end="")
#         else:
#             print(end=" ")
#     print()

# n leeter pattern
# for row in range (7):
#     for col in range(7):
#         if col==0 or col==6 or ((row==col) and (col>0 or col<2)) or (col==0 and col==5):
#            print("*",end="")
#         else:
#             print(end=" ")
#     print()
        
# a="12 hours"
# a=12 
# print(a+a,"hours")



# 5 5 5 5 5 
# 4 4 4 4 4 
# 3 3 3 3 3
# 2 2 2 2 2
# 1 1 1 1 1 
# i=5
# while i>=1:
#     j=1
#     while j<=5:
#         print(i,end="")
#         j=j+1
#     print()
#     i=i-1




# i=1
# while i<=50:
#     if i%2:
#        print(i)
#     i=i+1


# i=70
# while i>=65:
#     j=65
#     while j<=i:
#         print(chr(i),end="")
#         j=j+1
#     print()
#     i=i-1

#  G
#  G F
#  G F E
#  G F E D
#  G F E D C
#  G F E D C B
#  G F E D C B A 

# i=71
# while i>=65:
#     j=71
#     while j>=i:
#         print(chr(j),end=" ")
#         j=j-1
#     print()
#     i=i-1

# name=input("enter the name:-")
# i=0
# while i<(len(name)):
#     j=0
#     while j<i+1:
#         print(name[i],end="")
#         j+=1
#     print("_",end="")
#     i+=1

# 1234
# 5678
# 9 10 11 12
# 13 14 15 16

# i=1
# while i<=16:
#     j=1
#     while j<=4:
#         print(i,end="")
#         j=j+1
#         i=i+1
#     print()


# num=int(input("enter"))
# i=0
# while i<=num:
#     print(i)
#     i=i+2

# avg of sum 
# num=int(input("enter"))
# i=0
# sum=0
# while i<=num:
#     sum=sum+num
#     if i%2==0:
#         print(i,"even")
#     else:
#         print(i,"odd")
#     i=i+1
# print(sum/2)


#  0 4 8 12 
#  4 8 12 16
#  8 12 16 20
#  12 16 20 24

# i=0
# while i<20:
#     c=i
#     while c<=i+12:
#         print(c,end=" ")
#         if c==24:
#             break
#         c=c+4
#     i=i+4
#     print( )


    




    


