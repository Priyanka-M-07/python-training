n=int(input("How many students ?"))
students={}
for i in range(2):
    name=input(f"Enter the name of student {i+1}:")
    mark1=int(input(f"enter the mark1 {name}:"))
    mark2=int(input(f"enter the mark2 {name}:"))
    marks=(mark1,mark2)
    c=sum(marks)
    students[name]=c
    print(f"mark of students{name}:",c)
topper=max(students,key=students.get)
print("topper:",topper,"with",students[topper],"marks")





        





        





    





  

    
   

    