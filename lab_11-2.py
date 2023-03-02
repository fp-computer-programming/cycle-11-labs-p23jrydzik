# author: JHR 2/27/23

# creating dictionary of my grades
grades = {'Midyear Project Presention':100,'Midyear Project Proposal':100,'Midyear Project Code':94,'Mid Year Project Reflection':86}

# printing all of my grades
print(grades.values()) 

# printing all of the assignment names
for values in grades: 
    print(values)   

# printing all scores above 70
print('Scores above 70:')
for keys,values in grades.items(): 
    if values >= 70:
        print(keys,values)

# printing all scores below 50
print('Scores below 50: ')
for keys,values in grades.items():     
    if values <=50:
        print(keys,values)