import numpy as np
import random
from math import exp

train = np.loadtxt("train.csv", delimiter=",")
test = np.loadtxt("test.csv", delimiter=",")

def normalize(X):
    return X / np.max(np.abs(X), axis=0)

X = normalize(train[:,:5])  # columns 0..4
y = normalize(train[:,5])   # column 5  (classification, 0 or 1)


def sse_loss(w, X, y):
    yhat = w[0] + (w[1:] * X).sum(axis=1)
    err = y - yhat
    return np.square(err).sum()

def predict(row, coefficients):
    yhat = coefficients[0]
    for i in range(len(row)):

        yhat += coefficients[i + 1] * row[i]
    return yhat

def fit_sgd(X, y, niter=100000, alpha=0.01):
    # initialize weights vector w

    # loop niter times
        # select random sample from X
        #    (and corresponding value in y)
        # let's say X[n], y[n]

        # calculate the estimate yhat from X[n] and weights

        # calculate error y[n]-yhat

        # update w_0
        # for each weight w_i in w_1, ...
            # update w_i

    w = [random.uniform(0, 1) for i in range(len(X[0]) + 1)]

    prev_loss = 100
    for epoch in range(niter):
        if (epoch % 10 == 0):
            loss = sse_loss(w, X, y)

            if abs(loss - prev_loss) < 0.001:
                break
            prev_loss = loss
        n = random.randint(0, len(X) - 1)


        yhat = predict(X[n], w)

        error = y[n] - yhat

        w[0] = w[0] + alpha * error
        for i in range(len(X[n])):
            w[i + 1] = w[i + 1] + alpha * error * X[n][i]

    return w    # weights vector




def test_model(w, X, y, threshold=0.5):
    yhat = w[0] + (w[1:] * X).sum(axis=1)      # value from linear model
    ypred = (yhat > threshold).astype(int)     # prediction (is somebody in the room?)
    ytrue = (ypred == y).astype(int)           # compare to true value
    return ytrue.sum() / y.shape[0]            # true count / total count






w = fit_sgd(X, y)

X_test = normalize(test[:,:5])
y_test = normalize(test[:,5])

X_test = X_test
y_test = y_test
print("X test: ", X_test)
print("y test: ", y_test)
print(test_model(w, X_test, y_test) * 100)
