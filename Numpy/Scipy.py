import numpy as np
from scipy.sparse import csr_matrix

# We can create CSR matrix by passing an arrray into function scipy.sparse.csr_matrix()
# Create a CSR matrix from an array:
arr = np.array([1,2,3,4,5])

print(csr_matrix(arr))