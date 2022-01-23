#2.0
#1-Dictionary methods
D = {1:"Good",2:"Bad",3:"Happy",4:"Sad"}
X = D.copy()
print(X)

A = (1,2,3,4)
B = ("Hello")
Da = dict.fromkeys(A,B)
print(Da)

X = D.get(3)
print(X)

I = D.items()
print(I)

K = D.keys()
print(K)

D.pop(2)
print(D)

D.popitem()
print(D)

X = D.setdefault(3,"Very Good")
print(X)

D.update({5:"Nice"})
print(D)

X = D.values()
print(X)

D.clear()
print(D)



#2-Creating a set
S = set(("a",1,"b",2))
print(S)
       #OR
SS = {"a",1,"b",2}
print(SS)
       #OR
Ss = set(["a",1,"b",2])
print(Ss)



#3-Sorted function
A = ("12","22","18","24")
X = sorted(A,reverse=True)
print(X)



#4-filename extension
fn = input("input the filename:")
fn_extn = fn.split(".")[-1]
print ("The extension of the file is: ",fn_extn)



#5-calculator
print("Calculator")
print("1-Add")
print("2-Substract")
print("3-Multiply")
print("4-Divide")

n=int(input("Enter Choice(1-4): "))

if n==1:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    S=a+b
    print("Sum = ",S)
elif n==2:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    D=a-b
    print("Difference = ",D)
elif n==3:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    P=a*b
    print("Product = ",P)
elif n==4:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    Q=a/b
    print("Quotient = ",Q)
else:
    print("Invalid Choice")

