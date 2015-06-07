#all cpu info
with open('/proc/cpuinfo') as data:
  for line in data:
    print(line.rstrip('\n'))

#just cpu models
with open('/proc/cpuinfo') as data:
  for line in data:
     if line.strip('\n').startswith('model name'):
        model_name = line.rstrip('\n').split(':')[1]
        print(model_name)

#find real bit architecture by looking for lm flag (long mode)
with open('/proc/cpuinfo') as data:
  for line in data:
    if line.strip('\n').startswith('flags'):# or line.strip('\n').startswith('Features'):
      if 'lm' in line.strip('\n').split():
        print('64-bit')
      else:
        print('32-bit')
        
