# Machine Learning Foundations: Ep #1
# Exercise
# from https://www.youtube.com/watch?v=_Z9TRANg4c0
# runs on https://colab.research.google.com/github/lmoroney/dlaicourse/blob/master/Exercises/Exercise%201%20-%20House%20Prices/Exercise_1_House_Prices_Question.ipynb#scrollTo=PUNO2E6SeURH
# setup local environment https://medium.com/@stephenjoel2k/how-to-set-up-tensorflow-and-keras-on-your-local-system-using-pip-84b4d9f4475a

import tensorflow as tf
import numpy as np
from tensorflow import keras

# define algorhitms
optimizers = ['adadelta', 'adagrad', 'adam', 'adamax',
              'ftrl', 'nadam', 'rmsprop', 'sgd']
losses = ['mean_squared_error']

# define arrya of prediction
xs = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0,
               8.0, 9.0, 10.0], dtype=float)
ys = np.array([100000.0, 150000.0, 200000.0, 250000.0, 300000.0,
               350000.0, 450000.0, 500000.0, 550000.0], dtype=float)

# define spected results
expectedResults = [400000.0, 600000.0]


def runAI(optimizer, loss):
    model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
    model.compile(optimizer=optimizer, loss=loss)
    model.fit(xs, ys, epochs=500)
    res[f"{optimizer}-{loss}"] = model.predict([7.0, 11.0])


res = dict()
for opt in optimizers:
    for los in losses:
        runAI(opt, los)

for key in res:
    print(
        f"{key} => {res[key][0]},{res[key][1]} => diff: {res[key][0]-expectedResults[0]},{res[key][1]-expectedResults[1]}")
