# a=int(input("enter the number"))
# rev=0
# while a>0:
#     rev=(rev*10)+a%10
#     a=a//10
# print(rev)




# a=int(input("enter no:-"))
# b=int(input("enter no:-"))
# c=int(input("enter no:-"))
# if a>b and a>c:
#     print(a,"oldest")
# elif b>a and b>c:
#     print(b,"oldest")
# elif c>a and c>b:
#     print(c,"oldest")
# elif a<b and a<c:
#     print(a,"is youngest")
# elif b<a and b<c:
#     print(b,"is youngest")
# elif c<a and c<b:
#     print(c,"is youngest")
# else:
#     print("no")


# num=int(input("enter age:-"))
# if num*5:
#     print("hello")
# else:
#     print("bye")


# num=int(input("enter the no."))
# print(num//10)

# alpha=input("enter the name :-")
# if alpha>"a" and alpha<"z":
#     print(alpha)
# else:
#     print("its a number not alpha")

a=int(input("enter the number:"))
rev=0
while a>0:
    rev=(rev*10)+a%10
    a=a//10
print(rev)





a=int(input("enter the number:"))
rev=0
while a>0:
    rev=(rev*10)+a%10
    a=a//rev
print(rev)