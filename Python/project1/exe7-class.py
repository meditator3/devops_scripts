#Given the names and grades for each student in a class of  N students,
# store them in a nested list and print the name(s)
# of any student(s) having the second lowest grade.

#example: records = [["chi", 20.0], ["beta", 50.0], ["alpha",50.0]]
#the ordered list of scores is [20.0,50.0] so the second lowest is 50.0.
# there are two students with that score:["beta", "alpha"].
# ordered alphabetically, the names are printed as:
# alpha
# beta
# input this data into the array of students/grades:
#
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39
records = [["Harry", 37.21], ["Berry", 37.21], ["Tina", 37.2], ["Akriti", 41], ["Harsh", 39]]
lowest_grade = records[0][1]
second_lowest_names = []

for grade in records:
    if grade[1] < lowest_grade:
        temp = lowest_grade
        lowest_grade = grade[1]
        second_lowest_grade = temp

for grade in records:
    if grade[1]==second_lowest_grade:
        print(grade[0])

