import csv
from comment_functions import student_comment


# Reading the information

def read_class_desc():
	with open('classes.csv') as csvfile:
		info = csv.reader(csvfile)
		next(info)

		class_info = {}
		for line in info:
			class_info[line[0]] = line[1:]
	return class_info


def read_student_info(teacher):
	with open(teacher + '.csv') as csvfile:
		info = csv.reader(csvfile)
		next(info)
	
		stu_info = {}
		for line in info:
			stu_info[line[0]] = line[1:]
	return stu_info



if __name__ == '__main__':
	TEACHER = input('Enter teacher name: ')
	STUDENT = input('Enter student name: ')
	print('-------------------')
	CLASS_INFO = read_class_desc()
	STUDENT_INFO = read_student_info(TEACHER)
	try:
		print(student_comment(CLASS_INFO.get(TEACHER), STUDENT_INFO, STUDENT))
		with open('comment.txt', 'w') as f:
			f.write(student_comment(CLASS_INFO.get(TEACHER), STUDENT_INFO, STUDENT))

	except TypeError as e:
		print('Something went wrong. Make sure to check that the names entered match the ones in the files.')
		print()
		print('Error:', e)

