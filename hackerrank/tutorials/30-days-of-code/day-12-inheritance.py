# https://www.hackerrank.com/challenges/30-inheritance


class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    def __init__(self, firstName, lastName, id, scores):
        self.idNumber = id
        self.firstName = firstName
        self.lastName = lastName
        self.scores = scores

    def calculate(self):
        avg = sum(self.scores) / len(self.scores)
        if avg >= 90 and avg <= 100:
            letter = "O"
        elif avg >= 80 and avg < 90:
            letter = "E"
        elif avg >= 70 and avg < 80:
            letter = "A"
        elif avg >= 55 and avg < 70:
            letter = "P"
        elif avg >= 40 and avg < 55:
            letter = "D"
        else:
            letter = "T"
        return(letter)


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
