from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
digits = load_digits()

print(digits.data.shape)
    
import matplotlib.pyplot as plt
plt.gray()
plt.matshow(digits.images[5])
  
plt.show()