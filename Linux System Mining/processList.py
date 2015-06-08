#!/usr/bin/env python3
from subprocess import Popen
from subprocess import PIPE
from re import split

class Process(object):
	'''Data structure for a process. The class properties are process attributes. '''
	def __init__(self, proc_info):
		self.user = proc_info[0]
		self.pid = proc_info[1]
		self.cpu = proc_info[2]
		self.cpu = proc_info[3]
		self.mem = proc_info[4]
		self.vsz = proc_info[5]
		self.rss = proc_info[6]
		self.stat = proc_info[7]
		self.start = proc_info[8]
		self.time = proc_info[9]
		self.cmd = proc_info[10]
	
	def info_str(self):
		'''Returns a string containg information about the process'''
		return '%s %s %s' % (self.user, self.pid, self.cmd)
	
def process_list():
	'''Return a list of active processes (Process objects)'''
	proc_list = []
	psaux = Popen(['ps', 'aux'], stdout=PIPE, universal_newlines=True)
	#Discard the ps aux header
	psaux.stdout.readline()
	for line in psaux.stdout:
		#delimeter is variable number of spaces
		proc_info = split(" *", line.strip())
		proc_list.append(Process(proc_info))
	
	return proc_list

if __name__ == '__main__':
	process_list = process_list()

	print('Process list:\n')
	for process in process_list:
		print('\t%s' % process.info_str())
	
	root_process_list = [ x for x in process_list if x.user == 'root']

	print('Owned by root:\n')
	for process in root_process_list:
		print('\t%s' % process.info_str())
	
	
		

