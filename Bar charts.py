"""Weekly expenditures:"""

import matplotlib.pyplot as plt

def draw_bar_graph(data, labels):
	
	num_bars = len(data)

	positions = range(1, num_bars + 1)
	plt.barh(positions, data, align = 'center')
	
	plt.yticks(positions, labels)
	plt.xlabel('Amount')
	plt.ylabel('Catagories')
	plt.title('Weekly Expenditures')
	plt.grid()
	plt.show()


if __name__ == '__main__':
	costs = []
	catagories = []
	
	catagory = int(raw_input("Enter number of catagories:>> "))
	while True:
		try:
			for i in range(catagory):
				cat = str(raw_input("Enter catagory:>> "))
				catagories.append(cat)
				cost = float(raw_input("Enter expenditure:>> "))
				costs.append(cost)
		except ValueError: print "**Error, invalid entry."
		
		draw_bar_graph(costs, catagories)
	
		query = str(rae_input("Are you ready to quit?(Y/N):>> ").upper())		
		if query == "Y": break