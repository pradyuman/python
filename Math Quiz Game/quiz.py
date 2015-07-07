import datetime
import random

from questions import Add
from questions import Subtract
from questions import Multiply
from questions import Divide

class Quiz:
	questions = []
	answers = []

	def __init__(self):
		question_types = (Add, Subtract, Multiply, Divide)
		
		for _ in range(10):
			num1 = random.randint(1,10)
			num2 = random.randint(1,10)
			question = random.choice(question_types)(num1, num2)
			self.questions.append(question)

	def take_quiz(self):
		#start time
		self.start_time = datetime.datetime.now()
		
		#ask questions
		for q in self.questions:
			self.answers.append(self.ask(q))
		else:
			self.end_time = datetime.datetime.now()
		
		return self.summary()

	def ask(self, question):
		correct = False
		
		#start time
		start = datetime.datetime.now()
		
		#get user input
		answer = input(question.text + ' = ')
		
		#check answer
		if answer == str(question.answer):
			correct = True
		
		#log end time
		end = datetime.datetime.now()
		
		return correct, end - start

	def total_correct(self):
		total = 0
		for answer in self.answers:
			if answer[0]:
				total += 1
		
		return total

	def summary(self):
		print("You got {} out of {} correct.".format(
			  self.total_correct(), len(self.questions)
		))

		print("It took you {} seconds total.".format(
			 (self.end_time-self.start_time).seconds
		))

if __name__ == '__main__':
	Quiz().take_quiz()
