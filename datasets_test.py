from sklearn.datasets import load_boston
from sklearn.datasets import load_digits
import matplotlib.pyplot as plt

data, target = load_boston(return_X_y=True)
print(data.shape)
print(target.shape)

digits = load_digits()
plt.matshow(digits.images[3])
plt.show()