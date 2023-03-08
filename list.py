"""List = [1, 34, "harsh", True, 5+7j, 45.91]
print(List)
print(type(List))
#list is a data type.
print(List[2])
print(List[0:3]) #Slicing.
print(List[-1]) #Reverse indexing.
print(List[::-1])
print(List[::2]) #jump.
s = "harshu"
List.append("Jagdish") #adding items to the list.
#append adds at the end of the list.
print(List)
print(List[2][0:3]) #Slicing the items of the list.
print(len(List))
List.append(s)
print(List) # Nesting of list.
# Extend vs Append (V.imp)
List.insert(2, [2,4,5])
print(List)
#Insert helps to add data with the index chosen by us.
List.insert(0, 23)
print(List)
print(List.pop(3))
print(List)
#pop used to remove any item from index.
List.remove("harsh")
#remove directly remove the elements of the list.
print(List)"""

l = [7,8,3,2,9,0,1]
l.sort() #sorting is only for one data type.
print(l)
print(l.index(3))

print(l.count(1))

l[2] = 30
print(l)