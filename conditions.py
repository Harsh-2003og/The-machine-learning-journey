#if-elif-else.
"""marks = int(input("Enter your marks\n"))

if marks >= 80:
    print("You will be a part of A0 batch")
elif marks >= 60 and marks < 80:
    print("you will be the part of A1 batch")
elif marks >=40 and marks <60:
    print("you will be a part of A2 batch")
else:
    print("You will be a part of A3 batch")
     
#nested if
price = int(input("Enter the price"))     
if price > 1000:
    print("I will not purchase")
    if price > 5000:
        print("omg it's too much")
    elif price < 2000:
        print("But it's ok")
elif price < 1000:
    print("I will purchase")
else:
    print("Not interested")"""


l = [1,2,3,4,5,6,7,8]
l1 = []
s = 1
for i in l:
    s= i + 1
    l1.append(s)
print(l1)

l2 = [1,2,3,4,5,"harshu", 34,432,"guru"]
l_num = []
l_str = []

for i in l2:
    if type(i) == int or type(i) == float:
        l_num.append(i)
        print(l_num)
    else:
        l_str.append(i)
        print(l_str)