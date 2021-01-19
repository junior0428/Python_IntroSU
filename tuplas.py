#Tuplas "()"

valores=("Python", True, "zone", 5)
milista=list(valores)#convert tupla to list
mitupla=tuple(milista) #convert list to tupla

print(valores)
print(milista)
print(mitupla.count(5))
print(len(mitupla)) # "len" give you all the elements of list o tuple

#Tuple packing in python 
# there are two way to add parameters or values in tuples, this is the second way

SwayTuple= "juan", 13, 1, 1995
print(len(SwayTuple))

#now we are going tu unpacking in python
#we have the variable "Swaytuple"
nombre, dia, mes, agno=SwayTuple #assign "nombre=juan"
print(nombre,dia,mes, agno)