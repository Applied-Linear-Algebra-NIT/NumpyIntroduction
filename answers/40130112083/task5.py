import numpy as np

a = np.array([5,9,4,11,3,9,4,4])
b = np.array([1,2,3,4,4,3,2,1])
print(f'''mean : {np.mean(a)}
median : {np.median(a)}
variance : {np.var(a)}
standard deviation : {np.std(a)}
correlation : 
{np.corrcoef(a,b)}''')