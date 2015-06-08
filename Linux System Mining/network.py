from collections import namedtuple

def netinfo():
	'''RX and TX bytes for each of the network devices '''
	with open('/proc/net/dev') as data:
		net_dump = data.readlines()

		device_data = {}
		data = namedtuple('data',['rx', 'tx'])
		for line in net_dump[2:]:
			line = line.split(':')
			if line[0].strip() != 'lo':
				device_data[line[0].strip()] = data(float(line[1].split()[0])/(1024.0**2),
													float(line[1].split()[8])/(1024.0**2))
	
	return device_data

if __name__=='__main__':
	netinfo = netinfo()
	for info in netinfo.keys():
		print('{0}: Recieved {1} MiB | Transmitted {2} MiB'.format(info, netinfo[info].rx, netinfo[info].tx))
