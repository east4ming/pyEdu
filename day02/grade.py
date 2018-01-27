"""Judge Your Grade.

根据你的成绩判断你的等级.
"""


def judge_grade(grade) :
    """输入grade, 输出级别."""
    if grade >= 90:
        print('优秀')
    elif grade >= 80:
        print('good')
    elif grade >= 70:
        print('nice')
    elif grade >= 60:
        print('OK')
    else:
        print('你要努力了')

while True:
    grade = int(input('Please input your grade:'))
    judge_grade(grade)
