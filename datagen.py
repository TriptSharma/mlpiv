import numpy as np
import pandas as pd

pdf = pd.read_csv('datap.csv')
udf = pd.read_csv('datav.csv')

# print(pdf.head())

f =  open('C:/Users/Tript/Desktop/What!/asme/cavity/postProcessing/probes/0/probeloc.dat', 'r')

df = pd.DataFrame()
#time, x, y, ux, uy, pressure
data = []
count = 1

for x in f:
	
	x = x.split()
	
	arr1 = []
	for index, row in pdf.iterrows():
		arr1.append([float(row[1]), x[0], x[1], row[count+1]])	
	# print(arr1)
	
	arr2=[]
	for index, row in udf.iterrows():
		arr2.append([float(row[(count-1)+2].lstrip('(')), row[(count-1)+3]])
	# print(arr2)
	# print(len(dp1), len(dp2))
	
	dp = np.concatenate([(arr1),(arr2)], axis=1)
	# print(dp)
	if count==1:
		data=dp
	else:
		data = np.concatenate([data,dp], axis=0)

	count=+1

df = pd.DataFrame(data)
df.to_csv(r'data.csv')
