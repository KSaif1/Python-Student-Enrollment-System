# Text file intialization
import datetime
students = open("students.txt","a+")
enrollments = open("enrollments.txt","a+")
courses = open("courses.txt","a+")
# Function to display student information
def displayStudent():
    print("Displaying all registered students. (if its empty that means that there are no registered students)")
    with open("students.txt","r") as students:
        print("(Student Name,Student ID, Student Contact)")
        print(students.read())
    while True:
        try:
            desiredStudentID = int(input("Enter the ID of the desired student to see which courses they are enrolled in: "))
            break
        except:
            print("Enter a number.")
    desiredStudentID = "S"+str(desiredStudentID) #Add's S to the front of the student ID to prevent reading errors from other functions
    with open("enrollments.txt","r") as enrollments:
        lineEnrollments = enrollments.readlines() # Creates an array with everything that is inside the enrollments text file
    with open("enrollments.txt","r") as enrollments:
        lineEnrollmentsCheck = enrollments.readlines() # Creates an identical arry that is used for checking purpose
    indexes = [] # Intializing an array that will store the index values of the lineEnrollmentsCheck array so we can retrieve them later
    count = 0
    for i in lineEnrollments: # A for loop to run a small algorithim that matches values and returns the index values of where it found a matching value
        temp1 = lineEnrollmentsCheck.pop(0)
        temp2 = [] # creating a temporary array to hold the values from the first temporary array that holds the values from the lineEnrollmentsCheck array being popped.
        temp2 = temp1.split(",")
        studentIDCheck = temp2.pop(0)
        if desiredStudentID == studentIDCheck:
            indexes.append(count)
            count+=1
        else:
            count+=1
            continue
    if not indexes: # Checking if the indexes array is empty, if it is then the student ID doesnt exist or student is not registered in anything.
        print("No such student ID exists OR student is not registered in any courses.")
    else:
        length = len(indexes)
        print("Student is enrolled into the following courses:")
        for i in range(length): # small algorithim that uses indexes from the indexes array to pop specific values from the lineEnrollmentsCheck2 file and prints them in a presentable way.
            with open("enrollments.txt","r") as enrollments:
                lineEnrollmentsCheck2 = enrollments.readlines()
            temp = lineEnrollmentsCheck2.pop(int(indexes.pop(0)))
            studentIDNotUsed, courseIDUsed,timeUsed = temp.split(",") #spliting temp into 3 values 
            timeUsed = timeUsed.strip("\n") # removing \n from the last value
            print(courseIDUsed,timeUsed)
# Function for dropping subject
def dropping():
    courses = open("courses.txt","r+")
    enrollments = open("enrollments.txt","r+")
    while True: # While loop to check whether the user as entered a correct value or not.
        try:
             n = int(input("Enter the student ID: "))
             print("Student:")
             student = studentInfo(n).pop(0) 
             print(student)
             break
        except IndexError: # Error handling for if the ID is not found
             print("ID not found") 
        except:
             print("Invalid ID")
    while True: # While loop to check whether the user as entered a correct value or not.
        try:
             n = int(input("Enter the course ID: "))
             print("Course:")
             course = courseInfo(n).pop(0)
             print(course)
             break
        except IndexError:
             print("ID not found")
        except:
             print("Invalid ID")
    lineCourses = courses.readlines() # Saving the contents of courses.txt as an array
    lineEnrollments = enrollments.readlines() # Saving the contents of enrollments.txt as an array
    enrollments.close()
    enrollments = open("enrollments.txt","r")
    lineEnrollmentsCheck = enrollments.readlines() # Reads the enrollments file and stores it in a list for the purpose of checking
    enrollments.close()
    courses.close()
    courseID = course.pop(0) # Popping the course variable twice to extract all the important information out of it to store in other more useful variables
    courseSubDetails = course.pop(0)
    courseName = courseSubDetails.pop(0)
    space = courseSubDetails.pop(0)
    space = int(space)
    courseCheck = f"C{str(courseID)},{str(courseName)},{str(space)}\n" #saving a variable to check with the original
    space+=1
    course = f"C{str(courseID)},{str(courseName)},{str(space)}\n" # saving a variable to replace the original once the original check as gone through
    countCourse = 0
    courseID = f"C{courseID}" # Adding letters to ensure that student and course IDs stay unique and unable to be confused with any other values in the files.
    studentID = student.pop(0)
    studentID = f"S{studentID}"
    courseAndStudentIDs = [studentID,courseID] # storing studentID and courseID in the same array to match with courseAndStudentIDsCheck
    countEnroll = 0
    for i in lineEnrollments: # algorithim to check whether both values match and returns a boolean variable
        temp = lineEnrollmentsCheck.pop(0)
        courseAndStudentIDsCheck = []
        courseAndStudentIDsCheck = temp.split(",")
        time = courseAndStudentIDsCheck.pop(-1)
        if courseAndStudentIDs == courseAndStudentIDsCheck:
            existence = True
            break
        else:
            existence = False
        countEnroll+=1
    if existence == True: # if statement to check whether the boolean value from the previous for loop is true
        something2 = ""
        trash = lineEnrollments.pop(countEnroll) #creating a variable that will not be used (unnecessary value within the variable)
        lineEnrollments = something2.join(lineEnrollments) #converting line enrollments into a string by using the join() function
        enrollments = open("enrollments.txt","w")
        enrollments.write(lineEnrollments)
        for i in lineCourses: #for loop to find the index of where the courseCheck variable is in lineCourses
            if str(courseCheck) == lineCourses[countCourse]:
                break
            countCourse+=1
        lineCourses[countCourse] = course # Replacing the specific index found in the previous for loop with the course along with the space incremented
        something = ""
        lineCourses = something.join(lineCourses)
        courses = open("courses.txt","w")
        courses.write(lineCourses)
        courses.close()
        print("Course sucessfully dropped!")
    else:# if it couldnt match any student ID or course ID then it was unable to find matching IDs
        print("There is no student enrolled with the student ID and course ID that you have entered.")
student_details = []
# Function for retrieving student info
def studentInfo(n):
    students = open("students.txt","r+") # Text file initialization
    for line in students:
        student_name, student_id, student_number = line.split(",") # Splitting the line into the respective variables
        student_id = student_id.replace("S","") # Removes the S from the student ID so we can use it as an integer
        student_id = int(student_id)
        if student_id == n: # Checking for the student ID using information from the text file
            student_number = (student_number.strip("\n"))
            sub_details = [student_name, student_number]
            student_details.append([student_id, sub_details]) # Makes a list with the ID and then a sublist for that student
    students.close()
    if student_details[0] != "":
        return student_details
# Function to add students
def studentAdd():
    dupe = False # Bool value to track dupelicate existence 
    while dupe == False:
        name = input("Enter the name of the student: ")
        while True: # while loop to prevent user from doing anything that shoulldnt be done
            try:
                studentID = int(input("Enter the students ID: "))
                if studentID<0:
                    print("A students ID cannot be a negative number.")
                    continue
                break
            except:
                print("Enter a number for the ID.")
        contact = input("Enter the students email or phone number: ")
        with open("students.txt","r") as students:
            firstChar = students.read(1) # Reading the first char of the students.txt file to see whether its empty or not
        if firstChar: # If firstChar is not empty then it will proceed to check as normal
            studentID = str(studentID)
            studentID = "S"+studentID # adding an S again to ensure uniqueness 
            with open("students.txt","r") as students: 
                lineStudents = students.readlines() #creating variables to read all of students.txt into an array
            with open("students.txt","r") as studentsCheck:
                lineStudentsCheck = studentsCheck.readlines() # another identical variable for checks
            for i in lineStudents: # small algorithim used to match values, if it matches it then an error will be displayed and program will not proceed
                temp = lineStudentsCheck.pop(0)
                nameNotUsed, studentIDCheck,contactNotUsed = temp.split(",")
                studentIDCheck = studentIDCheck.strip(" ")
                studentID = studentID.strip(" ")
                if studentIDCheck == studentID:
                    dupe = False
                    print("A student is already registed with the same ID you have entered.")
                    break
                else: #in the case that it doesnt find a match, meaning there is no duplicate, program proceeds as normal
                    dupe = True
        else: # if firstChar is empty then it will move on as duplication is immpossible in an empty file
            studentID = str(studentID)
            studentID = "S"+studentID
            break
    print("Proceeding with registration of student.")
    students = open("students.txt","a+") # Opens the file in append mode once more incase the user restarts the program rather than closing it and opening it.
    students.write(f"{name},{studentID},{contact}\n") # Writes variables into text file
    students.close()
    print("Student added successfully!")
# function for checking for course
course_details = []
def courseInfo(n):
    courses = open("courses.txt","r+") # Text file initialization
    for line in courses:
        course_id, course_name, space = line.split(",") # Splitting the line into the respective variables
        course_id = course_id.replace("C","") # Replaces the C from the course id
        course_id = int(course_id)
        if course_id == n:
            space = (space.strip("\n"))
            sub_details = [course_name, space]
            course_details.append([course_id, sub_details]) # Makes a list with the ID and then a sublist for that course information
    courses.close()
    if course_details[0] != "":
        return course_details
def courseAdd():
    dupe = False #another boolean used to track the existence of a duplicate line
    while dupe == False: 
        while True: # While loop to prevent users from entering any data/info that is illegal or would cause the program to break
            try:
                course_id = int(input("Enter the course ID: "))
                if course_id<0: #Checks that the ID is less than 0
                    print("A course's ID cannot be a negative number.")
                    continue
                break
            except:
                print("Enter an ID that consists of numbers.")
        course_name = input("Enter the course name: ")
        while True: # While loop to prevent users from entering any data/info that is illegal or would cause the program to break
            try:
                max_seats = int(input("Enter the maximum seats: "))
                if max_seats<=0:
                    print("Cannot have the max seats of a course be a negative number or 0.")
                    continue
                break
            except:
                print("Enter a number.")
        with open("courses.txt","r") as courses:
            firstChar = courses.read(1) #creating a variable to see whether the first char of a file is empty or not
        if firstChar: #if first char does hold value, then it will proceed with duplicate checks as normal
            course_id = str(course_id)
            course_id = "C"+course_id
            with open("courses.txt","r") as courses:
                lineCourses = courses.readlines() #creating a variable to read all of courses into an array
            with open("courses.txt","r") as courses:
                lineCoursesCheck = courses.readlines() #identical variable 
            for i in lineCourses: # algorithim that matches 2 variables and checks whether they are the same, and returns a bool 
                temp = lineCoursesCheck.pop(0)
                course_id_check, course_name_not_used,max_seats_not_used = temp.split(",")
                course_id_check = course_id_check.strip(" ")
                course_id = course_id.strip(" ")
                if course_id_check == course_id:
                    dupe = False
                    print("A course is already registed with the same ID you have entered.")
                    break
                else:
                    dupe = True
        else: # if first char is empty then it will break the loop and proceed to adding as a dupe is impossible in an empty file.
            course_id = str(course_id)
            course_id = "C"+course_id
            break
    print("Proceeding with adding course.")
    courses = open("courses.txt","a+")
    courses.write(f"{course_id},{course_name},{max_seats}\n")
    courses.close()
    print("Course added successfully!")

def enrollment():
    students = open("students.txt","r") 
    courses = open("courses.txt","r")
    while True: # Checks to prevent the user from doing anything that could break the program
            try:
                n = int(input("Enter the student ID: "))
                print("Student:")
                student = studentInfo(n).pop(0)
                print(student)
                break
            except IndexError:
                print("ID not found")
            except ValueError:
                print("Invalid ID")
    while True: # checks to prevent the user from doing anything that could break the program
        try:
            n = int(input("Enter the course ID: "))
            print("Course:")
            course = courseInfo(n).pop(0)
            print(course)
            break
        except IndexError:
            print("ID not found")
        except ValueError:
            print("Invalid ID")
    courseID = course.pop(0) # popping information our of course variable to rearrange all the info present within into standalone variables
    subDetails = course.pop(0)
    courseName = subDetails.pop(0)
    max_seats = subDetails.pop(0)
    studentID = student.pop(0)
    subDetailsStudent = student.pop(0)
    studentName = subDetailsStudent.pop(0)
    contact = subDetailsStudent.pop(0)
    max_seats = int(max_seats)
    with open("enrollments.txt","r") as enrollments:
        lineEnrollments = enrollments.readlines() # creating a variable to read enrollments as an array
    with open("enrollments.txt","r") as enrollments:
        lineEnrollmentsCheck = enrollments.readlines() # creating a variable to read enrollments as an array
    studentID = "S"+str(studentID) # adding letters to IDs to maintain uniqueness
    courseID = "C"+str(courseID)
    courseAndStudentIDs = [studentID,courseID] # combining both IDs into one array to compare later on
    courseAndStudentIDsCheck = [] # creating an empty list to input IDs later on for checking purposes
    if courseAndStudentIDs == courseAndStudentIDsCheck:
        existence = True
    else:
        existence =False
    for i in lineEnrollments: # Algorithim to check if IDs match to stop double booking or double enrolling. (returns boolean value)
        temp = lineEnrollmentsCheck.pop(0)
        courseAndStudentIDsCheck = temp.split(",")
        temp1 = courseAndStudentIDsCheck.pop(-1)
        if courseAndStudentIDs == courseAndStudentIDsCheck:
            print("The student ID you have entered is already registed to the course you have entered.")
            existence = True
            break
        else:
            existence = False
    with open("enrollments.txt","r") as enrollments:
        firstChar = enrollments.read(0) # creating a variable that checks whether the beginning of the flie is empty or not (only works on first time using program or if files are empty)
    if firstChar or existence == False:
        if max_seats > 0: # Checks if there are any seats left in the course
            enrollments = open("enrollments.txt","a+")
            time = datetime.datetime.now() #creating a variable for time 
            a_time  = time.strftime("%Y-%m-%d %H:%M") #formatting the date and time
            final = str(studentID) + "," + str(courseID) + "," +str(a_time)
            enrollments.write(f"{final}\n")
            enrollments.close()
            print("Enrolled successfully!")
            max_seats -=1 # decrementing the max_seats to update the fact that a new stand has enrolled
            courseCheck = courseID+","+courseName
            with open("courses.txt","r") as courses:
                lineCourses = courses.readlines() #creating 2 variables to check 
            with open("courses.txt","r") as courses:
                lineCoursesCheck = courses.readlines()
            count = 0
            for i in lineCourses: #algorithim to check the 2 variables match and a count is incremented everytime 
                temp = lineCoursesCheck.pop(0)
                courseIDCheck,courseNameCheck,max_seats_not_used = temp.split(",")
                courseCheck2 = courseIDCheck+","+courseNameCheck
                if courseCheck == courseCheck2:
                    break
                else:
                    count+=1
            courseCheck = courseCheck +","+str(max_seats) +"\n"
            lineCourses[count] = courseCheck # replacing the coursecheck variable into the linecourses variable at the index that for loop ended at
            something3 = ""
            lineCourses = something3.join(lineCourses) # converting the array into a string
            with open("courses.txt","w") as courses:
                courses.write(lineCourses)
            print("Course information sucessfully updated.")
        else:
            print("Course is full, try another course.")
    else:
        print("As the student ID is already registered into the course ID, the program is unable to proceed.")
# Main while loop
while True:
    # Nested while loop for the selection of options
    while True:
        try:
            selection = int(input("enter a number:\n1 for adding a new student.\n2 for adding a new course.\n3 for enrolling in a course.\n4 for dropping a course.\n5 for checking course availability.\n6 for checking student information.\n7 for exiting the program.\n"))
            break
        except ValueError:
            print("Error, please enter a number.")
        # Match case for selected option operation
    match selection:
        case 1: # Case for adding students
            studentAdd()
        case 2: # Case for adding courses
            courseAdd()
        case 3:# Case for enrolling a student
            enrollment()
        case 4: # Case for dropping a course
            dropping()   
        case 5: # Case for checking for course avaliability
            with open("courses.txt","r") as courses:
                print("Here is a list of all courses\n(Course ID, Course Name, Space):")
                print(courses.read())
        case 6: # Case for displaying all registered students
            displayStudent()
        case 7: # Case for closing program completely 
            print("Closing the program.")
            break
        case _: # Case incase user inputs a number that is not within legal range
            print("Error, please enter a number that is between 1 and 7 (inclusive)")
    # Check for if user wants to continue using the program
    proceed = input("Do you want to continue using the program? (Y/y for yes, N/n for no): ")
    if proceed.upper() == "Y":
        print("Restarting (any changes done will be saved)")
    else:
        print("Closing.")
        break