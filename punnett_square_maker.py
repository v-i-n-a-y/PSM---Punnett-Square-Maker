# Punnet Square Maker
#
# Written by Vinay Williams
#
# Written 07/08/21
#
# Copyright (C) 2021 Vinay Williams (see license file)
# 
#

# Imports
import matplotlib.patches as patches
import matplotlib.pyplot as plt

# Prints the program header
def header():
	print("PSM - Punnet Square Maker\n")
	print("Copyright (C) 2021 Vinay Williams")
	print("Please include the reference found on the GitHub repository if you use this in your project")
	print("Use '/' to separate the alleles\n")
	print("Example of how to enter the genotype: A/a B/b C/c D/d\n")

# This functions find all combinations of alleles from a parental genetic sequence
def combinations(p):
	if len(p) == 1:
		p = str(p[0]).split("/")
		# print(parent)
		return p
	else:
		c = []
		for x in combinations(p[1:]):
			temp = str(p[0]).split("/")
			c.append(temp[0] + x)
			c.append(temp[1] + x)
		return c

# This function creates a tabular data structure for all possible genotypes
def make_table(p1, p2):
	table = []
	for a in p1:
		row = []
		for b in p2:
			row.append(b + a)
		table.append(row)
	return table
	
# Formats and prints the table to the terminal window
def print_table(table, c1, c2, style = 1, label = "PunnettSquare"):
	latextable = []
	divlength = (len(c1[0])*2+4)*2**(len(c1[0]))
	print('')
	print('', end=' ')
	for a in c2:
		print(' '*(len(c1[0])+3) + a + '', end=' ')
		latextable.append('& ' + a + ' ')
	print('\n' + ' '*(len(c1[0])+1) + '-'*(divlength))
	latextable.append('\\\ \n\\hline\n')
	
	for i, row in enumerate(table):
		print(c1[table.index(row)], end=' ')
		latextable.append(c1[table.index(row)] + ' & ')
		print('|', end=' ')
		for j, cell in enumerate(row):
			print(cell + ' | ', end=' ')
			if j != len(row)-1:
				latextable.append(cell + ' & ')
			else:
				latextable.append(cell + ' ')
		print('\n' + ' '*(len(c1[0])+1) + '-'*(divlength))
		if i != len(table)-1:
			latextable.append('\\\ \n')	
	return latextable	

	latextable = []
	header = '\\begin{table}[]\n\\centering\n\\caption{'+title+'}\n\\label{'+label+'}\n'
	width = '\\begin{tabular}{l|' + 'l'*max(len(c1), len(c2)) + '}\n\\hline\n'

# This function accepts the possible combinations of the parental genotypes and returns a punnet square
def plot_punnett_square(c1, c2, show = False, save = True):

	font_size = 8
	length = 10^23
	print(str(length))
	fig = plt.figure()
	ax = fig.add_subplot()

	for w in range(1,len(c1)+1):
		for h in range(1,len(c2)+1):
			ax.add_patch(plt.Rectangle((w*length,h*length), length, length, edgecolor = 'black',facecolor = 'none'))
			ax.text((w*length)+(length/2), (h*length)+(length/2), c1[w-1]+c2[h-1], horizontalalignment="center", verticalalignment="center",size = font_size)

			if h == len(c2):
				ax.text((w*length)+(length/2), (h*length)+(length*1.5), c1[w-1], horizontalalignment="center", verticalalignment="center",size = font_size)

	for w in range(1,len(c1)+1):
		ax.text(0, (w*length)+(length/2.5), c2[w-1], horizontalalignment="center", verticalalignment="center",size = font_size)

	ax.set_aspect(1)
	plt.axis("off")
	# ax.relim()
	# update ax.viewLim using the new dataLim
	plt.xlim(length/2, (length*len(c1))+length)
	plt.ylim(length/2, (length*len(c1))+length)

	if show == True:
		plt.show()

	if save == True:
		plt.savefig("test.png")

# Main Runtime
if __name__ == '__main__':
	while True:
		p1 = input("Enter genetic sequence of 1st parent: ").split(' ')
		c1 = combinations(p1)
		print(c1)
		p2 = input("Enter genetic sequence of 2nd parent: ").split(' ')
		c2 = combinations(p2)
		plot_punnett_square(c1, c2, show = True, save = False)
		quit()
