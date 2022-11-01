import operator
def readStudentDetails():
    print("enter number of students")
    noOfStudents=int(input())
    studentsRecord={}
    for i in range (0,noOfStudents):
        print("enter student name:")
        name=input()
        print("enter marks:")
        marks=int(input())
        studentsRecord[name]=marks
    return studentsRecord
def rankStudents(studentsRecord):
    try:
        sortedStudentsRecord=sorted(studentsRecord.items(), key=operator.itemgetter(1), reverse= True)
        print()
        print("{} has secured first rank with marks {}".format(sortedStudentsRecord[0][0],sortedStudentsRecord[0][1]))
        print("{} has secured second rank with marks {}".format(sortedStudentsRecord[1][0],sortedStudentsRecord[1][1]))
        print("{} has secured third rank with marks {}".format(sortedStudentsRecord[2][0],sortedStudentsRecord[2][1]))
        print()
        return sortedStudentsRecord
    except IndexError:
        print("enter a minimum of 3 students")
        quit()
def rewardStudents(sortedStudentsRecord,reward):
    print()
    print("{} has been rewarded with cash prize {}".format(sortedStudentsRecord[0][0],reward[0]))
    print("{} has been rewarded with cash prize {}".format(sortedStudentsRecord[1][0],reward[1]))
    print("{} has been rewarded with cash prize {}".format(sortedStudentsRecord[2][0],reward[2]))
    print()
   
def appreciateStudents(sortedStudentsRecord):
    for record in sortedStudentsRecord:
        if record[1]>=950:
            print("congratulations {}, for scoring {}".format(record[0],record[1]))
        else:
            break
studentsRecord =readStudentDetails()
sortedStudentsRecord=rankStudents(studentsRecord)
reward=(500,300,100)
rewardStudents(sortedStudentsRecord,reward)
appreciateStudents(sortedStudentsRecord)