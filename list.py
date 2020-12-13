placesToVisit= ["Rajasthan", "Goa", "Himachal", "Kerala", "Jammu and kashmir", "Punjab"]
print(placesToVisit)


#For sppecific terms
print(placesToVisit[0])
print(placesToVisit[3])
print(placesToVisit[-2])


#For specific range
print(placesToVisit[1:3])


#From fixed to last
print(placesToVisit[2:])


#From last to fixed
print(placesToVisit[:-1])


#for replacing a viariable
placesToVisit[2]= "Ladakh"
print(placesToVisit)


#Adding a new item using append
placesToVisit.append("West Bengal") #Append adds at the last
print(placesToVisit)


#Adding new item using insert 
placesToVisit.insert(2, "Uttar Pradesh")
print(placesToVisit)


#Adding 2 list using extend function
thingsToDo= ["Scuba Diving", "Horse riding", "Trekking", "Mountain-climbing", "Hitchhiking", "Paragliding"]
placesToVisit.extend(thingsToDo)
print(placesToVisit)


#Removing an element from list
thingsToDo.remove("Trekking")
print(thingsToDo)


#Clearing or deleting an entire list
placesToVisit.clear()
placesToVisit.extend(thingsToDo)
print(placesToVisit)


#removing using pop
thingsToDo.pop() #pop removes last element
print(thingsToDo)


#Checking if a value is in the list
print(thingsToDo.index("Horse riding"))


#For sorting elements in the list
thingsToDo.sort()
print(thingsToDo)


#For reversing a list
thingsToDo.reverse()
print(thingsToDo)


#for copying a list
MyDreams= thingsToDo.copy()
print(MyDreams)


#Output using f" function
interest= ["Purnima", "Urmi"]
mine= f"I love {interest[0]}"
for girls in interest:
    print(girls)

    
favFood= ['chinese', "burger", 'biryani', "Eggs"]
for food in favFood:
    print(f"my fav diet is , {food}")
    print("I also like ", food.title())


landAnimals= ["Cow", "Goat", "Tiger", "Lion", "Hyena"]
for animal in landAnimals:
    print(f"Is  {animal} carnivore?")
    print(f" Is  {animal} harbivore?")


#making a numeric range
for value in range(2, 20):
    print(value)

    
#using square
squares= []
for Value in range(2, 20):
    square= Value ** 2
    squares.append(square)
print(squares)


squares= []
for value in range(1, 13):
    print(squares.append(value**2))


square= [value**2 for value in range(1, 10)]
print(square)
