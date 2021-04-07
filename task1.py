#! python3
"""
(10 points) 
Create a class object for a student.
It should have the following properties
str name
str studentNumber
int grade
list courses - to corresepond with course names
list grades - to correspond with grades

It should have the following methods:
average()       - determines the mathematical average of all course grades
getHonorRoll()  - determines the average of the top 5 courses if there are at least 5 courses.
                  returns True if the average is 86 or higher (on the honor roll)
                  returns False if not on the honor roll
showCourses()   - prints a list of all courses
showGrade(int)  - takes 1 parameter, the index of the list
                - displays the course name and grade
getCourses(list)- Receives a list of courses and stores that in the class property
getGrades(list) - Receives a list of grades and stores that in the class property
constructor     - should require the student name, studentNumber and grade (in that order)
"""

class student:

    # properties should be listed first
    name=''
    number=''
    grade=0


    def __init__(self,name,number,grade):
        # You will need to create your own input parameters for all methods
        self.name=name
        self.number=number
        self.grade=str(grade)

        print('Student name is '+ self.name)
        print('His/her student number is '+self.number)
        print("He/She is in grade "+ self.grade)

    def inputCourses(self):

        print("enter your course grade")
        print("================================================")
        
        course=[]

        while True:
            a=input("course = ")
            if a != "0":
                course.append(a)
            if a == '0':
                break

            return course

        def getCourses(self,course):
            self.course=course

        def inputGrades(self,course):
            num=len(course)
            i=0
            print("enter your course grades")
            print("============================================")
            grades=[]
            while i<num:
                a=input("course grade= ")
                a=int(a)
                grades.append(a)
                i += 1

            return grades

        def getGrades(self,grades):
            self.grades=grades

        def avarage(self):
            num=len(self)
            num=int(num)
            i=0
            a=0
            while i<num:
                a += self.grades[i]
                i += 1
            average=a/num
            return average

        def showGrades(self,index):
            print(self.course[index])
            print(self.grades[index])

        def showCourses(self):
            print(self.course)

        def getHonorRoll(self):
            self.grades.sort()
            ave5=(self.grades[-1]+self.grades[-2]+self.grades[-3]+self.grades[-4]+self.grade[-5])/5
            if ave5 >= 86:
                print("Honor Roll")
                return True
            else:
                return False

        def __del__(self):
            print("END")



def main():
    # This contains test data that will be used by the autograder.
    # do not modify this function

    st1 = student("Anita Bath","91334",11)
    st1.getCourses( ["English","Math","PE","Computers","History","Biology","Japanese"] )
    st1.getGrades( [91, 94, 87, 99, 82, 100, 73])
    st1.average()
    st1.showCourses()
    st1.showGrades(3)
    st1.HonorRoll()

    

    st2 = student("Joe Lunchbox","12346", 11)
    st2.getCourses( ["English","Math","Physics","Computers","Geography","Chemistry","French"] )
    st2.getGrades( [71, 98, 93, 95, 68, 81, 71])
    st2.average()
    st2.showCourses()
    st2.showGrades(3)
    st2.HonorRoll()


main()