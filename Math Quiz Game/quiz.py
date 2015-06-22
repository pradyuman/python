import datetime
import random

from questions import Add
from questions import Subtract
from questions import Multiply
from questions import Divide

class Quiz:
	questions = []
	answers = []

	def __init(self):

	def take_quiz(self):

	def ask(self, questions):

	def total_correct(self):

	def summary(self):
		print("You got {} out of {} correct.".format(
			  self.total_correct(), len(self.questions)
		))

		print("It took you {} seconds total.".format(
			 (self.end_time-self.start_time).seconds
		))
