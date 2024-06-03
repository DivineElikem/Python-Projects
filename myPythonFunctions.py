from random import randint
from os import remove, rename

secret_number = randint(1, 100)

def getUserPoints(userName):
    try:
        userScores = open('userScores.txt', 'r')
        for line in userScores:
            content = line.split(', ')
            if userName == content[0]:
                userScores.close()
                return content[1]
            else:
                userScores.close()
                return '-1'
    except IOError:
        print('File not found')



def updateUserPoints(newUser, userName, score):
    if newUser:
        userScores = open('userScores.txt', 'a')
        userScores.write(f'\n{userName},{score}')
    else:
        userScores = open('userScores.txt', 'r')
        userScorestmp = open('userScores.tmp', 'w')
        for line in userScores:
            content = line.split(', ')
            if userName == content[0]:
                content[1] = score
                s = ', '
                line = s.join(content) + '\n'
            userScorestmp.write(line)
        userScores.close()
        userScorestmp.close()
        remove('userScores.txt')
        rename('userScores.tmp', 'userScores.txt')


operandList = [0, 0, 0, 0, 0]
operatorList = ['', '', '', '']
operatordict = {1:'+', 2:'-', 3:'/', 4:'*', 5:'**'}
for index, operand in enumerate(operandList):
    operandList[index] = randint(1,9)

for index, operand in enumerate(operatorList):
    if operatordict[randint(1,5)] not in operatorList:
        operatorList[index] = operatordict[randint(1,5)]