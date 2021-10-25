for count in range(0,151):
    print(count)

for count in range(5,1001,5):
    print(count)

for count in range(1,101):
    if count % 10 == 0:
        print("coding dojo")
    elif count % 5 == 0:
        print("coding")
    else:
        print(count)


total = 0

for count in range(0,500001):
    if count % 2 == 1:
        total += count
print(total)

for count in range(2018,0,-4 ):
    print(count)

lowNum = 2
highNum = 11
mult = 2

for count in range(lowNum, highNum, mult):
    print(count)