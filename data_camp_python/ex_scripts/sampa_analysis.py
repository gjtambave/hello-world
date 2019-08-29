#to Run the code: in shell 
#-> ipython ->%run sampa_analysis.py
#->%edit codename.py

import matplotlib.pyplot as plt
import pandas as pd

file = 'tp.dat'

data = pd.read_csv(file, sep = '  ')

print(data.head())

#plot one of the column in histo
pd.DataFrame.hist(data[[3]])
plt.xlabel('Basline(ADC values)')
plt.ylabel('counts')
plt.show()
