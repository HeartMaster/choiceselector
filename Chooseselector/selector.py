import docx
import re
import mysql


def get_question(line):
    line = line.replace(' ','')
    line = line.replace('(','（')
    line = line.replace(')','）')
    try:
        reg = '.*[（](.*?)[）].*。'
        item = re.findall(reg, line)
        result = para.text.replace(item[0], '')
        return result
    except:
        pass


def get_key(line):
    line = line.replace(' ', '')
    line = line.replace('(', '（')
    line = line.replace(')', '）')
    try:
        reg = '.*[（](.*?)[）].*。'
        item = re.findall(reg, line)[0]
        return item
    except:
        pass


def get_A(line):
    try:
        try:
            regA = 'A[.](.*?) '
            itemA = re.findall(regA, line)
            return 'A.'+itemA[0]
        except:
            regA = 'A[.](.*)'
            itemA = re.findall(regA, line)
            return 'A.' + itemA[0]
    except:
        pass


def get_B(line):
    try:
        try:
            regB = 'B[.](.*?) '
            itemB = re.findall(regB, line)
            return 'B.'+itemB[0]
        except:
            regB = 'B[.](.*)'
            itemB = re.findall(regB, line)
            return 'B.' + itemB[0]
    except:
        pass


def get_C(line):
    try:
        try:
            regC = 'C[.](.*?) '
            itemC = re.findall(regC, line)
            return 'C.'+itemC[0]
        except:
            regC = 'C[.](.*)'
            itemC = re.findall(regC, line)
            return 'C.' + itemC[0]
    except:
        pass


def get_D(line):
    regD = '(D[.].*)'
    try:
        result = re.findall(regD, line)[0]
        return result
    except:
        pass


def print_list(list):
    count = 0
    for i in list:
        if i is not None:
            count = count + 1
            print(count,i)


def RemoveNone(list):
    list_result = []
    for i in list:
        if i is not None:
            list_result = list_result + [i]
    return list_result


def deal_key(list):
    list_result = []
    for i in list:
        i = i.replace('',' ').replace('，',',').replace('，','、')
        list_result = list_result + [i]
    return list_result


if __name__ == '__main__':
    # 打开docx文件路径
    file = docx.Document('选择题自动录入.docx')
    questions = []
    keys = []
    choice_A = []
    choice_B = []
    choice_C = []
    choice_D = []
    questions_result = []
    for para in file.paragraphs:
        line = para.text
        questions = questions + [get_question(line)]
        keys = keys + [get_key(line)]
        choice_A = choice_A + [get_A(line)]
        choice_B = choice_B + [get_B(line)]
        choice_C = choice_C + [get_C(line)]
        choice_D = choice_D + [get_D(line)]
    questions = RemoveNone(questions)
    choice_A = RemoveNone(choice_A)
    choice_B = RemoveNone(choice_B)
    choice_C = RemoveNone(choice_C)
    choice_D = RemoveNone(choice_D)
    keys = deal_key(RemoveNone(keys))
    for i in zip(questions,choice_A,choice_B,choice_C,choice_D,keys):
        print(i)
        mysql.savetopice(i)








