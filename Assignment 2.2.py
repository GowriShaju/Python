#2.2
#1-Step Function
for i in range(10,40,2):
    print(i)



#2-To make a for loop infinite.
L = [0]
for i in L:
    L.append(i+1)
    print(i)



#3-Adding values in a tuple.
#      Since tuples are unchangeable, we can add values by first converting
# them to lists, then addding the values and then converting them back to 
# the tuple.

T = (2,4,6,8)
print("T:",T)

L = list(T)
print("L:",L)
L.append(10)  #adding 10 n the last position.
print("L:",L)
L.insert(0,0) #adding 0 in the first position
print("L:",L)

Tt = tuple(L)
print("New Tuple:",Tt)




