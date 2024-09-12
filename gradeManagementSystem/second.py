
import root
#from gradeManagementSystem.root import studentNum


class Calc:
    def __init__(self):
        self.avg_list = []
        self.new_list=[]
        self.student_averages = {}
        self.student_with_max_avg=[]
        self.mark=[]

    def fun1(self):
        for name in root.dic.keys():
            grades = root.dic[name]
            all_grade=grades['grade']
            avg = sum(all_grade) // len(all_grade)
            self.student_averages[name] = avg
            self.avg_list.append(avg)
            self.mark.append(all_grade)

    def pass_fail(self):
        for b in self.avg_list:
            if b>=60:
                self.new_list.append(b)



    def print_max_average(self):
        max_avg = max(self.avg_list)
        max_index=self.avg_list.index(max_avg)
        self.student_with_max_avg = list(self.student_averages.keys())
        key_word=self.student_with_max_avg[max_index]
        length = len(self.new_list)
        failed=root.studentNum-length
        print(f'Student with the highest average: {key_word}')
        print(f'Highest average: {max_avg:.2f}')
        print(f'Total number of students:{root.studentNum}')
        print(f'Number of students who passed the exam:{length}')
        print(f'Number of failed students:{failed}')

# Create an instance of Calc and use it
calculator = Calc()
#calculator.fun1()
#print(calculator.mark)
#calculator.pass_fail()
#calculator.print_max_average()
