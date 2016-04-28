import numpy as np

def sigmoid(x,deriv=False):
	if(deriv==True):
	    return x*(1-x)

	return 1/(1+np.exp(-x))

X = np.array([[0,0,1],
            [0,1,1],
            [1,0,1],
            [1,1,1]])

y = np.array([[0],
			[1],
			[1],
			[0]])

np.random.seed(1)

# randomly initialize our weights with mean 0
syn0 = 2*np.random.random(X.shape[::-1]) - 1
syn1 = 2*np.random.random(y.shape) - 1

for j in range(10001):

	# Feed forward through layers 0, 1, and 2
    l0 = X
    l1 = sigmoid(np.dot(l0,syn0))
    l2 = sigmoid(np.dot(l1,syn1))

    # how much did we miss the target value?
    l2_error = y - l2

    if (j% 1000) == 0:
		erro = np.mean(np.abs(l2_error))
		print("Erro: %.2e" % erro)
		if erro < 1e-2: break

    # in what direction is  the target value?
    # were we really sure? rif so, don't change too much.
    l2_delta = l2_error * sigmoid(l2, deriv=True)

    # how much did each l1 value contribute to the l2 error (according to the weights)?
    l1_error = l2_delta.dot(syn1.T)

    # in what direction is the target l1?
    # were we really sure? if so, don't change too much.
    l1_delta = l1_error * sigmoid(l1, deriv=True)

    syn1 += l1.T.dot(l2_delta)
    syn0 += l0.T.dot(l1_delta)
