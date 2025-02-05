courses = ["MIT","CYBERSECURITY","Datascience"]
print(courses)
print()

#acessing an element
print(courses[2])

#looping through an array
for x in courses :
    print("course is",x)

#adding a new element into an array
courses.append("laravel")
print(courses)

#removing an element
courses.remove("CYBERSECURITY")
print(courses)