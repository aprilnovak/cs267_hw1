import sys # For: command line arguments
import matplotlib # For: plotting
matplotlib.use("Agg") # For: showing figures
from matplotlib import pyplot as plt

filename = sys.argv[1]
description = sys.argv[2]

my_dict = dict()
with open(filename, 'r') as f:
    size = []
    Mflops = []
    percentage = []
    
    my_dict[description] = {}
    for line in f:
	data = line.split('\t')
	try:
	    size.append(data[0].split(':')[1].strip())
	    Mflops.append(data[1].split(':')[1].strip())
	    percentage.append(data[2].split(':')[1].strip())
	# the last line of the file will not have two entires, so except it
	except IndexError:
	    pass
    my_dict[description] = {'size':size[1:], 'Mflops':Mflops, 'percentage':percentage}
    #my_dict = {description:{'size':size[1:], 'Mflops':Mflops, 'percentage':percentage}}
print(my_dict)
plt.plot(my_dict[description]['size'], my_dict[description]['Mflops'])
plt.ylabel('Mflop/s')
plt.xlabel('Size')
plt.legend(description)
plt.savefig(description + '.png')
