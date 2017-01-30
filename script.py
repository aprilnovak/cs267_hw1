import sys # For: command line arguments
import matplotlib # For: plotting
matplotlib.use("Agg") # For: showing figures
from matplotlib import pyplot as plt

# get the filenames and descriptions for comparison
num_files = (len(sys.argv) - 1)/2

filenames = []
descriptions = []
for i in range(0, num_files + 1, 2):
    filenames.append(sys.argv[i + 1])
    descriptions.append(sys.argv[i + 2])

my_dict = dict()
for index, filename in enumerate(filenames):
    with open(filename, 'r') as f:
        size = []
	Mflops = []
	percentage = []
        description = descriptions[index]
    
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
print(my_dict)

for description in descriptions:
    plt.plot(my_dict[description]['size'], my_dict[description]['Mflops'], label=description)
    plt.ylabel('Mflop/s')
    plt.xlabel('Size')
plt.legend()
plt.savefig(description + '.png')
