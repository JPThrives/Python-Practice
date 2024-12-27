def contains_even_number(a):
    for no in a:
        if no % 2 == 0:
            print("list contains even number")
        else:
            print("doesnot contain even number")

print("List1:")
contains_even_number([1,9,8])
print("List2:")
contains_even_number([1,3,5])

count = 0 

while (count < 1):
    count = count + 1
    print(count)
    break
else:
    print("No Break")