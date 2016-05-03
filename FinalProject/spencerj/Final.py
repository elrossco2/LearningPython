class Student:
    def __init__(self,name1,name2,gender,score,major):
        self.name1 = name1
        self.name2 = name2
        self.gender = gender
        self.score = score
        self.major = major
    def getName(self):
        print(self.name1, self.name2)
    def getGender(self):
        print(self.gender)
    def getScore(self):
        print(self.score)
    def getMajor(self):
        print(self.major)
def main():
    #with open("UserNames.prn") as infile:
    #    mylist = list(infile)
    #print(mylist[1])
    #std = mylist[1].split()
    #print(std)
    infile = open("UserNames.prn")
    header = infile.readline()
    #print(header)
    fnames = []
    lnames = []
    genders = []
    scores = []
    majors = []
    students = []
    for i in range(19):
        students.append(i)
    print(students)
    for line in infile:
        line = line.split()
        name1 = line[0]
        name2 = line[1]
        gender = line[2]
        score = line[3]
        major = line[4]
        fnames.append(name1)
        lnames.append(name2)
        genders.append(gender)
        scores.append(score)
        majors.append(major)
    #print(fnames[0],lnames[0],genders[0],scores[0],majors[0])
    #std1 = Student(fnames[0],lnames[0],genders[0],scores[0],majors[0])
    #std1.getName()
    #std1.getGender()
    #std1.getScore()
    #std1.getMajor()
    for i in range(19):
        students[i] = Student(fnames[i],lnames[i],genders[i],scores[i],majors[i])

    #students[0].getName()
    #students[0].getGender()
    #students[18].getName()
    group1 = []
    group2 = []
    group3 = []
    group4 = []
    group5 = []
    students = sorted(students, key=lambda students: students.score)
    #for i in range(19):
    #     print(students[i].getScore(),students[i].getName(),students[i].getGender())
    group1.append(students[0])
    group2.append(students[-1])
    group3.append(students[-2])
    group4.append(students[-3])
    group5.append(students[-4])
    print(group1[0].getName())
    
    
main()
