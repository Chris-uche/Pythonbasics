for x in range(0,10,2): #start,stop,step
    print(x)

#The While Loop section

uche = True 
while uche:
    name = input("insert something here: ")
    if name == "stop":
        uche = False
        break 


Fredschoolname = True
while Fredschoolname:
    nameOfschool =input("insert Fred's schoool name: ")
    if nameOfschool == "FUTO":
        break


MastersProgram = True
while MastersProgram:
    classOfDegree = input("What class of Degree: ")
    if classOfDegree == "Distinction":
        break



school = ["FUTO","Uniport","EmbryRiddle","Caltech"]
for college in school:
    if college != "Caltech":
        print(college)
    else:
        print("Caltech")