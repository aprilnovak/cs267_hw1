import sys

filename = sys.argv[1]
description = sys.argv[2]

with open(filename, 'r') as f:
    size = []
    Mflops = []
    percentage = []
    my_dict = {'description': description}

    for line in f:
	data = line.split('\t')
	try:
	    size.append(data[0].split(':')[1].strip())
	    Mflops.append(data[1].split(':')[1].strip())
	    percentage.append(data[2].split(':')[1].strip())
	# the last line of the file will not have two entires, so except it
	except IndexError:
	    pass
	 
    my_dict['size'] = size[1:]
    my_dict['Mflops'] = Mflops
    my_dict['percentage'] = percentage
