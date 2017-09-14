import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(color_codes=True)

data = pd.read_csv('pokemon.csv')
types = ['Normal', 'Fire', 'Fighting', 'Water', 'Flying', 'Grass', 'Poison', 'Electric', 'Ground', 'Psychic', 'Rock', 'Ice', 'Bug', 'Dragon', 'Ghost', 'Dark', 'Steel', 'Fairy']

sns.jointplot("height", "weight", data, kind="kde")
plt.show()

# for type in types:
# 	type_data = data[data.type.str.contains(type)]
# 	plt.title(type)
# 	x = type_data.height
# 	y = type_data.weight
#
# 	plt.xlabel('Height')
# 	plt.ylabel('Weight')
# 	plt.scatter(x, y)
# 	m, b = np.polyfit(x, y, 1)
# 	plt.plot(x, m*x + b, '-')
#  	plt.savefig('{}.png'.format(type))
# 	plt.clf()
