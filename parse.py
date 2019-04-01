import pandas as pd
import numpy as np
import re

#PATH = 'queen2_exp_00001.dat'

# def parse(path):
# 	arr = []
# 	data = []
# 	with open(path, 'r') as f:
# 		for dpt in f:
# 			for d in dpt.split(','):
# 				d=d.strip()
# 				arr.append(d)
# 			data.append(arr)
# 			arr=[]

# 	df = pd.DataFrame(data)
# 	#print(df)

# 	# df.to_csv(r'data.csv')
# 	return df

def parse(path):
	arr = []
	f = open(path, 'r')
	for dp in f:
		
		arr.append(dp.split())
		# print(arr)
		# exit(0)
	f.close()

	df = pd.DataFrame(arr)
	df = df[1:]
	print(df.head())
	# new_df = df[0].str.split(expand=True)
	# print(new_df.head())

	# df.to_csv(r'data.csv')
	return df

if __name__ == '__main__':
	path = 'C:/Users/Tript/Desktop/What!/asme/cavity/postProcessing/probes/0'

	#get press data
	ppath = path+'/p.dat'

	#get vel data
	vpath = path+'/U.dat'
	pass

	pdf = parse(ppath)
	pdf.to_csv(r'datap.csv', index=False)

	vdf = parse(vpath)
	vdf.to_csv(r'datav.csv', index=False)
