import array as arr
from xml.dom.minidom import ProcessingInstruction

Score1 = int(input("Enter your first exam score: "))
Score2 = int(input("Enter your second exam score: "))
Score3 = int(input("Enter your third exam score: "))

ScoreArray = arr.array('i', [Score1, Score2, Score3])

AverageScore = float(sum(ScoreArray)/len(ScoreArray))
HighestScore = max(ScoreArray)
LowestScore = min(ScoreArray)
Grade = ""
PassOrFail = ""

if AverageScore >= 90:
    Grade = "A"
    PassOrFail = "Pass"
elif AverageScore >= 80:
    Grade = "B"
    PassOrFail = "Pass"
elif AverageScore >= 70:
    Grade = "C"
    PassOrFail = "Pass"
elif AverageScore >= 60:
    Grade= "D"
    PassOrFail = "Pass"
elif AverageScore < 60:
    Grade = "F"
    PassOrFail = "Fail"

print("Student Report")
print("----------")
print("Scores: " )
print(ScoreArray)
print("Average score: " + str(AverageScore))
print("Highest score: " + str(HighestScore))
print("Lowest score: " + str(LowestScore))
print("Average Grad: " + str(PassOrFail))