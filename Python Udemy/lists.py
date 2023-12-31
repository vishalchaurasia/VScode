t = ["apple",1, "cherry"]
print(t)

list1 = ["apple", "banana", "cherry"]                #string
list2 = [1, 5, 7, 9, 3]                            #int
list3 = [True, False, False]                            #boolean
print(list1)
print(list2)
print(list3)

list4 = ["abc", 34, True, 40, "male"]
print(list4)

#SLICING
floats = [0.98, 8.76, 6.54, 4.32]
print(floats[1:])
print(floats[1:3])
print(floats[:2])

list5 = ["apple", "banana", "cherry","orange","kiwi"] 
print(list5)
del list5[0]
print(list5)

arctic_animals = ["penguin", "elephant", "polar bear", "walrus", "tiger", "reindeer"]
del arctic_animals[4]
arctic_animals.remove("elephant")
arctic_animals.append("arctic fox")
arctic_animals.insert(2, "snowy owl")  
arctic_animals.sort()  
print(arctic_animals)
print(arctic_animals.index("reindeer"))
print(arctic_animals.pop())