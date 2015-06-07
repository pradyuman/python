from collections import OrderedDict
import pprint

def cpuinfo():
	''' Return the information in /proc/cpuinfo
	as a dictionary in the following format:
	cpu['proc0']={...}
	cpu['proc1']={...}
	'''

	cpuinfo = OrderedDict()
	procinfo = OrderedDict()

	proc_num = 0
	with open('/proc/cpuinfo') as data:
		for line in data:
			if not line.strip():
				#end of info for one processor
				cpuinfo['proc%s' % proc_num] = procinfo
				proc_num = proc_num + 1

				#Clear the procinfo dictionary
				procinfo = OrderedDict()
			else:
				if len(line.split(":")) == 2:
					#Getting processor information
					procinfo[line.split(':')[0].strip()] = line.split(':')[1].strip()
				else:
					procinfo[line.split(':')[0].strip()] = ''

	return cpuinfo

#printing out model names of processor
if __name__=='__main__':
	cpuinfo = cpuinfo()
	for processor in cpuinfo.keys():
		print(cpuinfo[processor]['model name'])
