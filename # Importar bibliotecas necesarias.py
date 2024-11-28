# Importar bibliotecas necesarias
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import matplotlib.pyplot as plt
import numpy as np

# 1. Cargar el conjunto de datos Iris completo
iris = datasets.load_iris()

# Usaremos las dos primeras características para poder visualizar
X = iris.data[:, :2]  # Tomamos las dos primeras características
y = iris.target       # Tres clases: 0, 1 y 2

# 2. Dividir los datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Crear e inicializar el modelo SVM (con kernel no lineal: RBF)
svm = SVC(kernel='rbf', C=1.0, gamma=0.5)

# 4. Entrenar el modelo
svm.fit(X_train, y_train)

# 5. Evaluar el modelo
accuracy = svm.score(X_test, y_test)
print(f"Precisión del modelo: {accuracy:.2f}")

# 6. Visualizar las fronteras de decisión
# Crear una malla de puntos para graficar la frontera de decisión
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.01), np.arange(y_min, y_max, 0.01))

# Predecir para cada punto de la malla
Z = svm.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# Graficar la frontera de decisión
plt.contourf(xx, yy, Z, alpha=0.8, cmap=plt.cm.Paired)
plt.scatter(X[:, 0], X[:, 1], c=y, edgecolors='k', cmap=plt.cm.Paired)
plt.title("SVM con tres clases: Frontera de decisión")
plt.xlabel("Característica 1")
plt.ylabel("Característica 2")
plt.show()