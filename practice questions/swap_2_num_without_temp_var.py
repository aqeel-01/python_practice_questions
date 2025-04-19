

# q1 => first using temp var

a = 5
b = 10
print("Before swapping a= ", a ,"b = ", b)

#using temp var
temp = a
a = b
b = temp

print("After swapping: a =  ", a , "b =", b)


# q2 => now without using temp var

a = 2
b = 4
print("Before swapping a =" , a , "b =", b)

a,b = b,a # python tuple unpacking does the swap in one line

print("After swapping : a= ",a ,"b = ",b)
