import random

class Student:

    def __init__(self, fname, lname, gender, score, major):
        self.fname = fname
        self.lname = lname
        self.gender = gender
        self.score = score
        self.major = major

    def info(self):
        return self.fname, self.lname, self.gender, self.score, self. major

    def __repr__(self):
        return 'Student: {} {}, {}, {}, {}'.format(self.fname, self.lname, self.gender, self.score, self.major)

    def getgender(self):
        return self.gender

def makeStudent(infoStr):
    fname, lname, gender, socre, major = infoStr.split()
    return Student(fname, lname, gender, score, major)

def main():
    infile = open("UserNames.prn","r")
    outfile = open("PIGroups.prn", "w")
    header = infile.readline()
    students = []
    for line in infile.readlines():
        fname, lname, gender, score, major = line.split()
        student = Student(fname, lname, gender, score, major)
        students.append(student)
        #print(student.getgender())

    total = len(students)
    members = 4
    groups = round(total/members)

    parameter = []
    for i in range(groups):
        parameter.append([])

    random.shuffle(students)
    while len(students) != 0:
        x = random.randrange(groups)
        if len(parameter[x]) < members and student.gender.count("f") > student.gender.count("m"):
            parameter[x].append(students.pop())
        else:
            pass

    for i in range(groups):
        print("Group", i+1 ,parameter[i],"\n")
    
    for i in range(groups):
        print("Group", i+1 ,parameter[i],"\n", file = outfile)

    infile.close()
    outfile.close()

    print("PI Groups have been written to PIGroups.prn")
    
if __name__ == "__main__":
    main()
