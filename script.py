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
        print(data)
        try:
            size.append(data[0].split(':')[1])
            Mflops.append(data[1].split(':')[1])
            percentage.append(data[2].split(':')[1])
        # the last line of the file will not have two entires, so except it
        except IndexError:
            pass
 
    my_dict['size'] = size
    my_dict['Mflops'] = Mflops
    my_dict['percentage'] = percentage
    print(my_dict['Mflops'])
