import os

def process_list():
	pids = []
	for subdir in os.listdir('/proc'):
		if subdir.isdigit():
			pids.append(subdir)
	
	return pids

if __name__=='__main__':
	pids = process_list()
	print('Number of running processes: {0}'.format(len(pids)))
