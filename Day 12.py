class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores = scores
        
    def calculate(self):
        wynik2 = sum(self.scores) / len(self.scores)
        
        if 90 <= wynik2 and wynik2 <= 100:
            return "O"
        elif 80 <= wynik2 and wynik2 < 90:
            return "E"
        elif 70 <= wynik2 and wynik2 < 80:
            return "A"
        elif 55 <= wynik2 and wynik2 < 70:
            return "P"
        elif 40 <= wynik2 and wynik2 < 55:
            return "D"
        elif wynik2 < 40:
            return "T"
