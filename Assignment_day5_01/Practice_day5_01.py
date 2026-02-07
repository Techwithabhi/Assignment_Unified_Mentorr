# LIST'S ###########################################################################################################

# Create empty list, name it 'a'
a = []                      

# Print the value of a
print(a)                    

# Print the type of a 
print(type(a))              

l = ['R', 'Python', 'SAS', 'Scala', 42]
# Print the number of element in the list
print(len(l))               

# Using for loop iterate and print all the elements in the list
for item in l:
    print(item)   

# Select the second item, 'Python' and store it in a new variable named 'temp'
temp = l[-4]                
print(temp)    
# Print the value of temp and type(temp)     
print(type(temp))           

ab = ['R', 'Python', 'SAS', 'Scala', 42]
# Append the element 'Java' in the list
ab.append('Java')
print(ab)                   

# Remove the element 42 from the list and print the list
ab.remove(42)               
print(ab)

colors = ['Red', 'Blue', 'White']
#  the element 'Black' to colors
colors.append('Black')
# Append the color 'Orange' to second position (index=1) and print the list      
colors.insert(1, 'Orange')  
print(colors)

colors2 = ['Gray','Sky Blue']
# Add the elements of colors2 to colors using extend function in the list
colors.extend(colors2)      
print(len(colors))      
print(colors)

# Sort the list and print it.
colors.sort()
print(colors)               

sent = "Coronavirus Caused Lockdowns Around The World."
# Use split function to convert the string into a list of words and save it in variable words and print the same
words = sent.split()        
print(words)

# Convert each word in the list to lower case and store it in variable words_lower. 
words_lower = [word.lower() for word in words]
print(words_lower)

# Check whether ‘country’ is in the list
if 'country' in words_lower:
    print("Yes, 'country' is present in the list")
else:
    print("No, 'country' is not present in the list")

# Remove the element ‘the’ from the list and print the list.
words_lower.remove('the')   
print(words_lower)

# Select the first 4 words from the list words_lower using slicing and store them in a new variable x4
x4 = words_lower[0:4]       
print(x4)

# Convert the list of elements to single string using join function and print it
result = " ".join(x4)       
print(result)

# SET'S ############################################################################################################

stud_gread = ['A', 'A', 'B', 'C', 'C', 'F']
# Print the len of stud_grades
print(len(stud_gread))      

# Create a new variable, stud_grades_set = set(stud_grades) & Print it
stud_gread_set = set(stud_gread)
print(stud_gread_set)          

# Print the type of stud_grades and stud_grades_set and print their corresponding elements. Try to understand the difference between them.
'''
Basically List(stud_gread) have power to store all type of element and it would be mutable so a list alawys gives new list but in other side set(stud_gread_set) is store all values but it only return unordered unique values what it make diffarent from list and sets are immutable so we cannot change the existing set component.
'''

# Add a new element ‘G’ to stud_grades_set
stud_gread_set.add('G')

# Add element 'F' to stud_grades_set. and print it.
stud_gread_set.add('F')     
print(stud_gread_set)
#!!Did you notice? set doesn't add an element if it's already present in it, unlike lists.
#Yes, beacause sets are always return unique values thats whay 'F' element show only 1 time

# Remove ‘F’ from stud_grades_set
stud_gread_set.remove('F')

# Print the elements and the length of stud_grades_set
print(stud_gread_set)
print(len(stud_gread_set))

colorsS = ['red','blue','orange']
fruitsS = ['orange','grapes','apples'] 

# Print color and fruits
print(colorsS, fruitsS)

# Create colors_set, and fruits_set. (using set() ) and print them
colorsS_set = set(colorsS)
fruitsS_set = set(fruitsS)
print(colorsS_set, fruitsS_set)

# Find the union of both the sets.
union_set = colorsS_set.union(fruitsS_set)

# Find the intersection of both the sets 
intsec_set = colorsS_set.intersection(fruitsS_set)

print(union_set, intsec_set)

# Find the elements which are Fruits but not colors (using set.difference() )
fruits_not_colors = fruitsS_set.difference(colorsS_set)
print(fruits_not_colors)

# TUPEL'S ##########################################################################################################

temP = [17, 'Virat', 50.0]

# Iterate through temp and print all the items in temp
for item in temP:
    print(item)

# Replace first element with 11 in temp
temP[0] = 11

# Set temp1 = tuple(temp)
temp1 = tuple(temP)

# Iterate through temp1 and print all the items in temp1. 
for item in temp1:
    print(item)

# Replace first element with 17 in temp1
# temp1[0] = 17
# print(temp1)
# I will do it by following the instraction but it give us an error because we use 'Tuple' so we can't change the value of an tuple as a List

city = ('Bangalore', 28.9949521, 72)
# Print first element of city
print(city[0])

city2 = ('Chennai', 30.01, 74)
# Create cities which consist of city and city2 & print cities
cities = city + city2
print(cities)

# Print type of first element in cities
print(type(cities[0]))

# print the type of cities
print(type(cities))

# Dictionary #######################################################################################################

d = {"actor":"amir","animal":"cat","earth":2,"list":[23,32,12]}

# Print the value of d[0]
# print(d[0])
# It's a dictionary and a dict create with pair of 'Key' & 'values' so we can't call them by indexing

# Store the value of d[‘actor’] to a new variable actor.
actor = {"actor":"amir"}

# Print the type of actor
print(type(actor))

# Store the value of d[‘list’] in new variable List. 
list = {"list":[23,32,12]}

# Print the type of List. 
print(type(list))

d1 = { 'singer' : 'Kr$na' , 'album': 'Still here', 'genre' : 'hip-hop'}

# Merge d1 into d. & print d
d.update(d1)
print(d)

# Print all the keys in d
for key in d.keys():
    print(key)

# Print all the values in d
for values in d.values():
    print(values)

# Iterate over d, and print each key, value pair as this - (actor ----> amir)
for key, value in d.items():
    print(f"{key} ----> {value}")

# count the number of occurences of charachters in string named "sent" using dictionary and print the same.
a = str(input("Type, what you want to write in words: "))
sent = a.lower()

char_count = {}

for ch in sent:
    char_count[ch] = char_count.get(ch, 0) + 1

# Print character occurrences
for char, count in char_count.items():
    print(f"{char} : {count}")

############################################ END OF THE ASSIGNMENT ############################################