import sklearn
from sklearn import tree

features = [[140, 1], [130, 1], [150, 0], [170, 0]]
labels = [0, 0, 1, 1, ]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print(clf.predict([[150, 0]]))


import numpy as np
input_vector = np.array([2, 4, 11])
print(input_vector)

[2, 4, 11]
