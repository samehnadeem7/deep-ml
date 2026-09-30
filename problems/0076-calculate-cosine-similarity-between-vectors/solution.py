import numpy as np

def cosine_similarity(v1, v2):
	"""
	Calculate the cosine_similarity of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The cosine_similarity of the two vectors.
	"""
	# Implement your code here
	dot=0
	m,m2=0,0
	for i in range(len(v1)):
		dot+=v1[i]*v2[i]
		m +=v1[i]*v1[i]
		m2 +=v2[i]*v2[i]
    
	den=np.sqrt(m)*np.sqrt(m2)
	
	return dot/den