from collections import OrderedDict

def meminfo():
	''' Return the information in /proc/meminfo
	as a dictionary in the following format:
	meminfo['mem_attribute'] = 'attribute value'
	'''
	meminfo = OrderedDict()

	with open('/proc/meminfo') as data:
		for line in data:
			meminfo[line.split(':')[0]] = line.split(':')[1].strip()
	
	return meminfo

if __name__ == '__main__':
	meminfo = meminfo()
	print('Total memory: {0}'.format(meminfo['MemTotal']))
	print('Free memory: {0}'.format(meminfo['MemFree']))


