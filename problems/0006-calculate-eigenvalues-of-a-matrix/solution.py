import numpy as np
def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	a,b,c,d=matrix[0][0],matrix[0][1],matrix[1][0],matrix[1][1]
	tr=a+d
	det=a*d-c*b
	x1=(tr+np.sqrt(tr*tr-4 *1*det))/2
	x2=(tr-np.sqrt(tr*tr-4 *1*det))/2
	eigenvalues=[]
	eigenvalues.append(x1)
	eigenvalues.append(x2)
	return eigenvalues