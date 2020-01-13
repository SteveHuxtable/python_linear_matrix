
def firstMethod():
    import numpy as np  
    a = np.array([1, 2, 3, 4])

    print(a)

    A = np.array([1, 2, 3, 4])
    A_t = A[:, np.newaxis]
    print(A_t)
    print(A_t.shape)

    A = np.array([[1, 2, 3, 4]])
    print(A)
    print(A.T)

    print("Hello EuroPython!")
