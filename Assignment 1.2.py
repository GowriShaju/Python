#1.2
#1-List methods
print("List Methods")
L=[1,2,3,4,5,6]
L.append(7)
print(L)

L.clear()
print(L)

List = ["a","b","c","d"]
X = List.copy()
print(X)

C = List.count("b")
print(C)

L2 = ["e","f","g","h"]
List.extend(L2)
print(List)

I = List.index("e")
print(I)

List.insert(1,2)
print(List)

List.pop(1)
print(List)

List.remove("h")
print(List)

List.reverse()
print(List)

List.sort()
print(List)



#2-String Methods
print("String Methods")
S = "i love Maths"
X = S.capitalize()
print(X)

Sa = "Hello It's Me"
X = Sa.casefold()
print(X)

X = Sa.center(20)
print(X)

C = Sa.count("Me")
print(C)

X = Sa.encode()
print(X)

Sb = "Enjoy every moment."
X = Sb.endswith(".")
print(X)

Sc = "H\te\tl\tl\to"
X = Sc.expandtabs(2)
print(X)

X = Sb.find("every")
print(X)

Sd = "I am working on {x:}"
print(Sd.format(x = "python"))

Se = "Good Good very Good"
I = Sb.index("very")
print(I)

X = Se.isalnum()
print(X)

X = Se.isalpha()
print(X)

Sf = "\u0030" 
X = Sf.isdecimal()
print(X)

Sg = "141305"
X = Sg.isdigit()
print(X)

Sh = "Demo"
X = Sh.isidentifier()
print(X)

Si = "it's raining"
X = Si.islower()
print(X)

Sj = "24242424"
X = Si.isnumeric()
print(X)

Sk = "Hello::Hi"
X = Sk.isprintable()
print(X)

Sl = "   "
X = Sl.isspace()
print(X)

Sm = "Hello, And Welcome To My World!"
X = Sm.istitle()
print(X)

Sn = "HELLO"
X = Sn.isupper()
print(X)

So =  ("John", "Peter", "Vicky")
X = "#".join(So)
print(X)

Sp = "banana"
X = Sp.ljust(10)
print(X, "is my favorite fruit.")

Sq = "THERE it is"
X = Sq.lower()
print(X)

Sr = "     banana     "
X = Sr.lstrip()
print("Yeah,", X, "is sweet")

Ss = "Hello Jennie"
X = Ss.maketrans("J", "G")
print(Ss.translate(X))

St = "I could eat chocos all day"
X = St.partition("chocos")
print(X)

Su = "I like apples"
X = Su.replace("apples", "oranges")
print(X)

Sv = "Hello World"
X = Sv.rfind("World")
print(X)

X = Sv.rindex("World")
print(X)

Sw = "I could eat oranges all day, oranges are my favorite fruit"
X = Sw.rpartition("oranges")
print(X)

Sx = "Dairy Milk, Ferrero, Lindt"
X = Sx.rsplit(", ")
print(X)

Sy = "     oranges     "
X = Sy.rstrip()
print("of all fruits", X, "are my favorite")

Sz = "Home sweet Home"
X = Sz.split()
print(X)

T = "Thank you for the music\nWelcome to the jungle"
X = T.splitlines()
print(X)

Ta = "Hello, welcome to my world."
X = Ta.startswith("Hello")
print(X)

Tb = "     dairy milk     "
X = Tb.strip()
print("The chocolate", X, "is my favorite")

Tc = "Wow, It's HERE"
X = Tc.swapcase()
print(X)

Td = "Hello Everyone"
X = Td.title()
print(X)

dict = {83:  80}
Te = "Hello Sam!"
print(Te.translate(dict))

Tf = "It's nice"
X = Tf.upper()
print(X)

Tg = "22"
X = Tg.zfill(10)
print(X)



#3-Usage of negative numbers as index
#    Negative ndexing allows to access data from the end of the list.
L = [1,2,3,4]
l = L[-2]
print(l)


