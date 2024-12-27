#My First Python program
print("Hello, World!")
a = 3
A = 7
c = 2+4j
string1 = "This is a string"
print(A)
print(a)
B = a+A
print(B)
print(a*A)

if a == A :
    print("Nice")
else :
    print("Oops!")

print("Type of A : ",type(A))
print("Type of c : ",type(c))
print(string1)
print(type(string1))
print(string1[-1])
print(string1[0])

List = ["This is a list","Another one",["list"]]
print(List)
print(List[0])
print(List[-1])

Tuple1 = ('I','am','JP')
print(Tuple1)
print(type(True))
set1 = set([1,2,3,4,5])
print(set1)
for i in set1:
    print(i)

x = 111
y = 100
z = x%y
print(z)

p = True
q = False

print(p and q)
print(p or q)
print(not q)

print(x is y)
print(p is not q)
