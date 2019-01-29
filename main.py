names = []
test1 = []
test2 = []
test3 = []
totals = []
test1max = 20
test2max = 25
test3max = 35
students = 2

for i in range(students):
    print('Enter the next student\'s name')
    name = input()
    print('Enter the student\'s score for test 1 out of ' + str(test1max))
    score1 = 0
    problem = False
    try:
        score1 = int(input())
    except ValueError:
        problem = True
    while problem | (score1 > test1max) | (score1 < 0):
        print('The max score for that test is ' + str(
            test1max) + ' please re-enter the mark and the score but be above 0. Also ensure you only enter an integer.')
        try:
            score1 = int(input())
            problem = False
        except ValueError:
            problem = True

    print('Enter the student\'s score for test 2 out of ' + str(test2max))
    score2 = 0
    problem = False
    try:
        score2 = int(input())
    except ValueError:
        problem = True
    while problem | (score2 > test2max) | (score2 < 0):
        print('The max score for that test is ' + str(
            test2max) + ' please re-enter the mark and the score but be above 0. Also ensure you only enter an integer.')
        try:
            score2 = int(input())
            problem = False
        except ValueError:
            problem = True

    print('Enter the student\'s score for test 3 out of ' + str(test3max))
    score3 = 0
    problem = False
    try:
        score3 = int(input())
    except ValueError:
        problem = True
    while problem | (score3 > test3max) | (score3 < 0):
        print('The max score for that test is ' + str(
            test3max) + ' please re-enter the mark and the score but be above 0. Also ensure you only enter an integer.')
        try:
            score3 = int(input())
            problem = False
        except ValueError:
            problem = True
    names.append(name)
    test1.append(score1)
    test2.append(score2)
    test3.append(score3)
    totals.append(score1 + score2 + score3)
    print('\n')
for i in range(students):
    print(names[i] + ' scored a total of ' + str(totals[i]) + ' marks out of ' + str(test1max + test2max + test3max))
print('Class average total mark: ' + str(sum(totals) / len(totals)) + ' out of ' + str(test1max + test2max + test3max))
maxIndex = totals.index(max(totals))
print(names[maxIndex] + ' scored the highest in the class with ' + str(totals[maxIndex]) + ' out of ' + str(test1max + test2max + test3max))