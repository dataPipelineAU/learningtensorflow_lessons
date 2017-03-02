from sklearn.datasets import load_digits
from matplotlib import pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split

digits = load_digits()

#fig = plt.figure(figsize=(3, 3))

#plt.imshow(digits['images'][66], cmap="gray", interpolation='none')

#plt.show()

from sklearn import svm

classifier = svm.SVC(gamma=0.001)
classifier.fit(digits.data, digits.target)
predicted = classifier.predict(digits.data)


print(np.mean(digits.target == predicted))

X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target)



from tensorflow.contrib import learn
n_classes = len(set(y_train))
classifier = learn.LinearClassifier(n_classes=n_classes)
classifier.fit(X_train, y_train, steps=10)

y_pred = classifier.predict(X_test)


from sklearn import metrics
print(metrics.classification_report(y_true=y_test, y_pred=y_pred))

