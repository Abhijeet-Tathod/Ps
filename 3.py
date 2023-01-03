import math
import numpy as np 

price_data = [12, 30, 54, 48, 54, 71, 87, 46, 32, 35, 18]
range = max(price_data) - min(price_data)
print("Range is : " , range)


n = len(price_data)
mean = sum(price_data)/n
deviation = [(x-mean)**2 for x in price_data]
varience = sum(deviation)/n
print("Varience : " , varience)
print("Deviation : " , math.sqrt(varience))

q1 = np.median(price_data[:10])
q3 = np.median(price_data[10:])
IQR = q3 - q1


from scipy import stats
IQR1 = stats.iqr(price_data.)
