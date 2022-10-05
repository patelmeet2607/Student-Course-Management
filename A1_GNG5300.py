print("-------------------------------------")
print("Student and Course management program")
print("-------------------------------------")
print("Hello, please choose below options")
print("-------------------------------------")

class Student():
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.student_details=[]
        
    def __repr__(self):
        return f"{self.name},{self.email}"

    def add (self,name, email):
        self.sDict = {"name": name, "email" : email, "course" : []}
        self.student_details.append(self.sDict)
    
    def remove (self,name,email):
        self.sDict = {"name": name, "email" : email, "course" : []}
        self.student_details.remove(self.sDict)
        
    def modify (self,index1,value):
        ind = self.name.index(2)
        self.name[ind] = 1

    def dis(self):
        return self.student_details[:]

class Course():
    def __init__(self,course_name, courseID):
        self.course_name = course_name
        self.courseID = courseID
        self.course_details=[]

    def __repr__(self):
        return f"{self.course_name},{self.courseID}"

    def addCourse (self,course_name,courseID):
        self.cDict = {"course_name" : course_name, "courseID":courseID}
        self.course_details.append(self.cDict)

    def removeCourse (self, course_name,courseID):
        self.cDict = {"course_name" : course_name, "courseID":courseID}
        self.course_details.remove(self.cDict)
        
    def modifyCourse(self,index1,value2):
        ind3 = self.course_name.index(4)
        self.course_name[ind3] = 3
        
    def dis (self):
        return self.course_details[:]
        
obj = Student("","")
obj1 = Course("","")

while (True):
# Student Class management
    option = input(
    "Enter [A] to Add, Modify or Delet Students details\n"
    "Enter [B] to Enroll or Unenroll in course\n"
    "Enter [G] to Enter grade\n"
    "Enter[Admin Password] to access Course details\n")
    
    print("\n")
    
    # add = Name, Email

    if option == "A":
        option2 = input("Enter [X] to Add a new student: \n""Enter [Y] to Modify a student list: \n""Enter [Z] to Delete a student from list: \n")
        print("\n")

        if option2 =="X":
            name = str(input("Enter Name: \n"))
            email = str(input("Enter Email: \n"))
            print("\n")
            # student_details = Student(name,email)
            obj.add(name,email)
            
            print("Student list", obj.dis())
            print("\n")

        # Modify = Name, Email

        elif option2 == "Y":
            email = input("Enter your registered email for modify details:\n")
            print("\n")
            j = 0

            for i in obj.student_details:

                if i["email"] == email:
                    option9 = (input("Enter[G] for modify name:\nEnter[H] for modify email\n"))
                    print("\n")

                    if option9 == "G":
                        name = input("Enter new name which you want to modify: ")
                        print("\n") 
                        obj.student_details[j]["name"] = name

                    elif option9 == "H":
                        email = str(input("Enter the Email: "))
                        print("\n")
                        obj.student_details[j]["email"] = email

                    else:
                        print("INVALID INPUT")

                j += 1
            print("List: ", obj.dis())

        # Delete: Name and Email

        elif option2 == "Z":
            option4 = input("Are you sure? you want to delete student details, Enter [N]\n")
            print("\n")

            if option4 == "N":
                print("Student list", obj.dis())
                print("\n")
                name1 = input("Enter the name which want to be delete from the student list: \n")
                print("\n")
                email1 = str(input("Please confirm the email to delete student details \n"))
                print("\n")
                obj.remove(name1,email1)
                print("After Delet ", obj.dis())
            
            else:
                print("studentlist : ", obj.dis())
    
# Course Class management

    elif option == "admin":

        option5 = input("Enter [J] to Add a new course: \n""Enter [K] to Modify course list: \n""Enter [L] to Delete a course from list: \n")
        print("\n")

        # Add : Course name, Course ID

        if option5 =="J":
            course_name = str(input("Enter course Name: \n"))
            print("\n")
            courseID = str(input("Enter course course ID: \n"))
            print("\n")
            
           
            obj1.addCourse(course_name,courseID)
            
            print("list", obj1.dis())
            print("\n")

        # Modify: Course name, Course ID

        elif option5 == "K":
            print("list", obj1.dis())
            print("\n")
            courseID = input("Enter your register course ID for modification of course details: \n")
            print("\n")
            
            j = 0

            for i in obj1.course_details:
                if i ["courseID"] == courseID:
                    option10 = input("Enter [J] for modify course name:\nEnter[K] for modify course ID: \n")
                    print("\n")
                    if option10 == "J":
                        course_name = input("Enter new course name: \n")
                        print("\n")
                        obj1.course_details[j]["course_name"] = course_name
                    elif option10 == "K":
                        courseID = input("Which course ID do you want to change for this course? \n")
                        print("\n")
                        obj1.course_details[j]["courseID"] = courseID

                    else:
                        print("INVALID INPUT")
                        print("\n")
                
                j += 1
            print("List of course", obj1.dis())

        # Delete : Course name, Course ID
            
        elif option5 == "L":
            option6 = input("Are you sure? you want to delete course details, Enter [C]\n")
            print("\n")
            if option6 == "C":
                print("List of course", obj1.dis())
                print("\n")
                course_name1 = str(input("Enter the course name which want to be delete from the course list: \n"))
                print("\n")
                courseID1 = str(input("Please confirm correct course id for deleteing the course: \n"))
                obj1.removeCourse(course_name1,courseID1)
                print("\n")
                print("After Delet ", obj1.dis())
            
            else:
                print("studentlist : ", obj1.dis())
                
            
    # Course Enrollment and Unenrollment

    elif option == "B":
        option13 = input("Enter [D] to Enroll Course: \nEnter [U] to Unenroll Course: \n" )
        print("\n")
        if option13 == "D":
            print("student details: ", obj.dis())
            print("\n")
            print("course details: ", obj1.dis())
            print("\n")
            nameOfStudent = input("Enter your name: ")
            print("\n")
            nameOfCourse = input("Which Course do you want to Enroll: ")
            print("\n")
            gr = "Not IN LIST"
            dict = {"courses":nameOfCourse, "Grade":gr}

            q = 0
            for i in obj.student_details:
                if i["name"] == nameOfStudent:
                    i["course"].append(dict)
                q += 1
            
            print("list", obj.dis())
            print("\n")

        elif option13 == "U":
            print("student details: ",obj.dis())
            print("course details: ", obj1.dis())
            nameOfStudent = input("Enter your name: ")
            print("\n")
            nameOfCourse = input("Which Course do you want to Unenroll: ")
            print("\n")

            q = 0
            for i in obj.student_details:
                if i ["name"] == nameOfStudent:
                    i["course"].remove(dict)
                q += 1
            
            print("list", obj.dis())
            print("\n")

    # Grade 

    elif option == "G":
        print("student details: ",obj.dis())
        print("\n")
        print("course details: ", obj1.dis())
        print("\n")
        nameOfStudent = input("Enter your Name: ")
        print("\n")
        grade1 = str(input("Which Course Grade do you Want to enter: "))
        
        q=0
        for i in obj.student_details:
            if i["name"] == nameOfStudent:
                v = 0
                for p in i["course"]:
                    
                    if p["courses"] == grade1:
                        gr = input("Enter the Grades: ")
                        p["Grade"] = gr
                    else:
                        print("Course is not register")
                    v += 1
                                    
                q += 1
        print("student details: ",obj.dis())

    else:
        print("Invalid Password")

