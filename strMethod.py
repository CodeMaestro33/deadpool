Greeting="GOOD MORNING"
Name=" Steve"
print(type(Name))
# print(Greeting+Name)
c=Greeting+Name
print(c)
print(Name[-5:4])#[1:5]this is indexing and this one is [-5:2] negative indexing 
Story="lost in the labyrinth of my own mind i grapple with unsolved problems yearning for a glimpse of a Brighter future amidst the shadows of the past"
print(Story[0:17])
#String Functions
print(len(Story))
print(Story.endswith("past"))#it says end word is true or false
print(Story.replace("past","Memory"))
print(Story.capitalize())
# print(Story.Find("Brighter"))
