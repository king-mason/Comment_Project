# Comment creation

# Creating each comment as a list of strings then join them at the end


def list_grammar(words):	
	if len(words) > 2:
		words[-1] = 'and ' + words[-1]
		combined = ', '.join(words)
	elif len(words) == 2:
		words.insert(1, 'and')
		combined = ' '.join(words)
	else:
		combined = words[0]

	return combined

def class_desc(class_info):
	comment = ["It has been a pleasure getting to know you."]

	# Overview of topics
	if class_info[1]:
		comment.append('This year we have covered the topics of')
		topics = [x for x in class_info[1].split('/')]
		if len(topics) == 1:
			comment[-1] = comment[-1][:-4] + comment[-1][-3:]
		comment.append(list_grammar(topics) + '.')

	return ' '.join(comment)


def strengths(class_info, stu_info):
	comment = []
	strengths = stu_info[6].split(' ')
	indicators = class_info[0].split('/')
	work_ethic = int(stu_info[3])
	collab = int(stu_info[4])
	persv = int(stu_info[5])
	tests = [float(x) for x in stu_info[0].split(' ') if x]

	comment.append('So far, you have shown strength in the following learning objectives:\n\n')
		
	for ind in strengths:
		comment.append(' * ' + indicators[int(ind) - 1] + '\n')

	# Details about work ethic, collaboration, and perseverance
	if work_ethic + collab + persv == 12:
		comment.append('\nOutstanding job this year!')
	elif work_ethic + collab + persv >= 9:
		comment.append('\nGreat job this year!')
	else:
		comment.append('\nI hope you have enjoyed learning in this class.')
	
	if work_ethic >= 3:
		comment.append('Overall, your work ethic has been')
		if work_ethic == 3:
			comment.append('good.')
		else:
			comment.append('great!')
	if collab >= 3:
		comment.append("You've done a")
		if collab == 4:
			comment.append('super')
		comment.append('nice job of collaborating and working with your classmates.')
	if persv >= 3:
		comment.append('You have done')
		if persv == 4:
			comment.append('extremely')
		comment.append('well at persevering through challenges and working hard to stay on top of everything, keep it up!')

	if tests:
		avg = sum(tests)/len(tests)
		if avg > 95:
			comment.append('\n\nYou are an excellent and thourough test taker, and consistantly demonstrated your proficiency on exams. Moving forward, I hope to see you maintain your stellar performance!')
		elif avg <= 95 and avg >= 85:
			comment.append("\n\nAs for in class exams, you were able to grasp the concepts, but made a couple errors or slip ups here and there, and weren't able to fully demonstrate proficiency. Hopefully you can remove some of your weaknessess moving forward and start acing some tests!")
		elif avg < 85:
			comment.append("\n\nAs for in class exams, this is one area you definitely need to work on, as you didn't quite appear to fully understand the content, and averaged relatively low on tests and quizzes. Moving forward, I hope you can work on studying more, and feel free to contact me if you need help.")


	return ' '.join(comment)

	
def weaknesses(class_info, stu_info):
	comment = []
	growth = stu_info[7].split(' ')[0]
	indicators = class_info[0].split('/')
	work_ethic = int(stu_info[3])
	collab = int(stu_info[4])
	persv = int(stu_info[5])

	
	comment.append('As you continue, focus on improving in the following category:\n\n')

	comment.append(' * ' + indicators[int(growth) - 1] + '\n')

	comment.append('\nWorking on this area in particular will result in the best growth in the future and help you improve the most in this subject.')

	if work_ethic < 3:
		comment.append('In addition, you could definitely work on participating more in the work and trying your best to show what you can do.')
	if collab < 3:
		comment.append('It would also be good for you to engage more wholeheartedly in participating in class and collaborating with your fellow students.')
	if persv < 3:
		comment.append('It would be wise to also work on persevering through projects, and making sure you are throurough in your investigations.')

	return ' '.join(comment)


def summary(stu_info):
	work_ethic = int(stu_info[3])
	collab = int(stu_info[4])
	persv = int(stu_info[5])
	tests = [float(x) for x in stu_info[0].split(' ') if x]
	homework = [float(x) for x in stu_info[1].split(' ') if x]
	projects = [float(x) for x in stu_info[2].split(' ') if x]


	# General summary of strengths and areas of growth
	strengths = []
	growths = []

	if work_ethic >= 3:
		strengths.append('work ethic')
	else:
		growths.append('work ethic')

	if collab >= 3:
		strengths.append('collaboration')
	else:
		growths.append('collaboration')

	if persv >= 3:
		strengths.append('perseverance')
	else:
		growths.append('perseverance')

	if tests:
		if sum(tests)/len(tests) >= 90:
			strengths.append('testing skills')
		else:
			growths.append('testing skills')

	if homework:
		if sum(homework)/len(homework) >= 90:
			strengths.append('homework')
		else:
			growths.append('homework')

	if projects:
		if sum(projects)/len(projects) >= 90:
			strengths.append('project work')
		else:
			growths.append('project work')


	comment = []
	
	if strengths:
		comment.append('\n\nAltogether, your')
		comment.append(list_grammar(strengths))
		comment.append('have all been great!')

	if growths:
		comment.append('As you go continue to learn, you can work on improving your')
		comment.append(list_grammar(growths) + '.')
	

	return ' '.join(comment)




# Putting everything together
def student_comment(class_info, info, student):
	comment = [student.title(), '—']
	stu_info = info.get(student)

	comment.append(class_desc(class_info))
	comment.append('\n\n' + strengths(class_info, stu_info))
	comment.append('\n\n\n' + weaknesses(class_info, stu_info))
	comment.append('\n' + summary(stu_info))

	return ' '.join(comment)

