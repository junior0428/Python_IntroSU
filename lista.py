#Listas "[]"
mylist=["maria", "pepe", "Marta","Antonio", "carlos", "Carmen"]
"""
mylist.append("sandra") #Add at the end
mylist.pop() #delete the end value that was adding recently
mylist.insert(2, "juan") #add any position at the mylist
mylist.extend(["carla", "jacki", "jose"]) #add more of one values
mylist.remove("maria") #delete one o more values
print(mylist[:])
print(mylist.index("carlos")) #to know the position of one value
print("pepe" in mylist) #to know if the value is inside in mylist
"""
mylist2=["Sandra", "lucia"]*3 # if you put "* 3" you obtened three time of mylist2 for example
mylist3=mylist+mylist2
print(mylist3)