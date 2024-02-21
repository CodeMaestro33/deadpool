#LIST AND TUPLE
a=[1,3,5,7,2,4,6,8]
#PRINT THE LIST USING PRINT() FUNCTION
print(a)
#Access using index using a[0],a[1],a[2]
print(a[5])
#Changes the value of the list using 
a[3]=9
print(a)
#We can Create a list with items of the difffrent types 
c=[45, "Marry",False,6.9]
print(c)
#Sort 
l1=[2,12,4,6,16,23,43]
l1.sort()
print(l1)
#Reverse
l1=[2,12,4,6,16,23,43]
l1.reverse()
print(l1)
#Appends adds at the end of the list
l1=[2,12,4,6,16,23,43]
l1.append(47)
print(l1)
#Insert
l1=[2,12,4,6,16,23,43]
l1.insert(2,5)
print(l1)
#pop remove element at index
l1=[2,12,4,6,16,23,43]
l1.pop(5)
print(l1)
#Remove [remove of the list]
l1=[2,12,4,6,16,23,43]
l1.remove(12)
print(l1)

#CREATING LIST IN A DIFFRENT METHODS
fruits=['Apples','orange','grapes','pears']
#Get Value a single value with indexing
print(fruits[1]) 
#Get length
print(len(fruits))
#Get Append to List
fruits.append('Mangoes')
print(fruits)
#Remove from list
fruits.remove('grapes')
print(fruits)
#Insert into position 
fruits.insert(2,'kiwi')
print(fruits)
#POP remove element form list
fruits.pop(4)
print(fruits)
#Sort list it set by an alphabetic order
fruits.sort()
print(fruits)
#Reverse Sort
fruits.sort(reverse=True)
print(fruits)
#Change Value
fruits[0]="Blueberries"
print(fruits)