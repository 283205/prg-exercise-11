class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores

    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)

    def get_grade(self, index):
        pocet = self.scores[index]
        if pocet >= 90:
            results = "A"
        elif pocet < 90 and pocet >= 80:
            results = "B"
        elif pocet < 80 and pocet >= 70:
            results = "C"
        elif pocet < 70 and pocet >= 60:
            results = "D"
        elif pocet < 60 and pocet >= 50:
            results = "E"
        else:
            results = "F"
        return results

    def find(self, pocet):
        vysledky = []
        scores = self.scores
        for i in range(len(self.scores)):
            if scores[i] == pocet:
                vysledky.append(i)
        return vysledky

    def get_sorted(self):
        scores = list(self.scores)
        for i in range(len(scores)):  # říká nám jak dlouho budeme dělat
            for j in range(0, len(scores) - 1):  # porovnáva dva prvky vedle sebe

                if scores[j] > scores[j + 1]:
                    scores[j], scores[j + 1] = scores[j + 1], scores[j]
        return scores





#print(results.count())          # 9
#print(results.get_by_index(2))  # 91
#print(results.scores)           # [85, 42, 91, 67, 50, 73, 100, 38, 58]
#print(results.get_grade(0))
#print(results.get_grade(6))
#print(results.get_grade(7))

#print(results.find(100))  # [6]
#print(results.find(50))   # [4]
#print(results.find(77))   # []
#print(results.get_sorted())   # [38, 42, 50, 58, 67, 73, 85, 91, 100]
#print(results.scores)         # [85, 42, 91, 67, 50, 73, 100, 38, 58]

if __name__ == "__main__":
    results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])
    print(results.count())
    for i in range(results.count()):
        print(f"Sutent {i}: {results.get_by_index(i)} points - {results.get_grade(i)}")

    print(results.find(100))
    print(results.get_sorted())

    from sorting import random_numbers

    random_results = StudentsGrades(random_numbers(30, 0, 100))
    print(random_results.count())
    print(random_results.get_sorted())
