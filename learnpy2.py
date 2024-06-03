'''
from os import remove, rename


def updateUserPoints(newUser, userName, score):
    if newUser:
        userScores = open('user.txt', 'a')
        userScores.write(f'\n{userName},{score}')
    else:
        userScores = open('user.txt', 'r')
        userScorestmp = open('user.tmp', 'w')
        for line in userScores:
            content = line.split(', ')
            if userName == content[0]:
                content[1] = str(score)
                s = ', '
                line = s.join(content) + '\n'
            userScorestmp.write(line)
        userScores.close()
        userScorestmp.close()
        remove('user.txt')
        rename('user.tmp', 'user.txt')


updateUserPoints(False, 'Fred', 201)
f = open('user.txt', 'r')
for line in f:
    print(line)
f.close()
'''
from random import randint
operandList = [0, 0, 0, 0, 0]
operatorList = ['', '', '', '']
operatordict = {1:'+', 2:'-', 3:'/', 4:'*'}
for index, operand in enumerate(operandList):
    operandList[index] = randint(1,9)
for index, operand in enumerate(operatorList):
    if operatordict[randint(1, 4)] not in operatorList:
        operatorList[index] = operatordict[randint(1, 4)]
print(operandList)
print(operatorList)