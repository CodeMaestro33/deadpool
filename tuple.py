#Creating a tuple using
t=(1,2,3,4)
#t1=()#Empty tuple
#t1=(1)#Wrong way to declare a tuple with a single element
t1=(1)#Tuple with single element
print(t1)
#Elementing the Element of a tuple
# print[t(0)]
#Cannot update the value of a tuple
#Creating a tuple using()
t=(1,2,3,4,5,6,7,5,4,3,2,1)
print(t.count(1))# it counts the value inside brace
print(t.index(5))# it tells value in indexing method

#Tuple is a collection which is ordered & unchangeable
#Create Tuple
fruits2=('Watermelon','Cherry')
#If u write a code in this manner ("Watermelon") it's type will be Str
#If u write a code in this manner ("Watermelon",) it's type will be Tuple
print(fruits2,type(fruits2))
#Single value Need Trailing Comma
#Get Value
print(fruits2[0])
#Can't change value
fruits2[0]="pears"#Gives an Error
#Delete tuple
del fruits2
print(fruits2)
#output no defined
#Get length
print(len(fruits2))