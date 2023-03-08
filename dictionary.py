#Set
s1 = {}
print(type(s1))
s2 = {1, 3, 56, 67}
print(type(s2))
s3 = {35,345,56.67,"harshu",45+65j,True}
#set remove all the duplicates.
s4 = {1,2,3,4,5,6,3,4,2,1,4,5,6,3,4,2,1,4}
print(s4)
s5 = [1,2,3,4,6,5,3,2,1,5,4,6,3,4,2,1,"Harsh","harsh"]
s6 = list(set(s5)) #List to set and viceversa.
print(s6)
# Set only presents the unordered collection of unique elements.
# Indexing and slicing will not gona work.
s4.add(9)
print(s4)

# Dictionary
d = {}
print(type(d))

d1 = {"car": "volvo" , "name": "harsh" , "dog": "husky" , "email": "harshvardhanbansode78@gmail.com"}
print(d1)
print(d1['name'])

d2 = {'name': "harshu" , 'mail_id': "harshu@gmail.com", 'name': "changez khan"}
print(d2['name'])
d3 = {'company': "pwskills", 'courses': ["web dev", "data science", "java with dsa system design"]}
print(d3)
print(d3['courses'][2])

d4 = {"number": [2,3,34,54,21], 'assignment': (1,3,24,5,6), 'launch_date': {24,45,12}, "class_time":{"web_dev": 7, "data_science": 4, "dsa with java and system design": 8} }
print(d4)
print(d4["class_time"]["web_dev"])  
d4['mentor'] = ['harshu', 'sudhanshu', 'anurag', 'hayder'] #insertion in dictionary.
print(d4)

del d4['number'] #Deletion.
print(d4)
print(list(d4.keys()))
#indexing is not there but keys can work well.
 