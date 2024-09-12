print('THIS IS THE DATA BASE OF WEBSTER UNIVERSITY FOR STUDENTS GRADE')
print('If the average of total grades is more than 60,Students finish the semester successfully')
subjects=['Math','Physics','English','Marketing']
dic={}
studentNum=int(input("How many students' data you are going to enter: "))
begin = 1

for name in range(0,studentNum):

    grade_list = []
    info=input(f'{begin}.Student name:')
    begin=begin+1
    print('Enter grades for four subjects')
    for a in subjects:
            assign=int(input(f'{a}:'))
            grade_list.append(assign)

    dic[info]={
     'grade':grade_list
            }







