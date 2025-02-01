import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

# Datos como array de pares x(Concentración de ácido acetilsalicílico), y(Absorbancia)
datos = np.array([[0.000, 0.000],
                  [0.055, 0.160],
                  [0.111, 0.383],
                  [0.166, 0.640],
                  [0.222, 0.836],
                  [0.277, 1.087], 
                  [0.332, 1.340]])

# Separar los datos en  x(Concentración de ácido acetilsalicílico en mg/L), y(Absorbancia)
concentracion = datos[:,0].reshape(-1, 1) 
absorbancia = datos[:,1]

# Crear y ajustar el modelo de regresión lineal
modelo = LinearRegression()
modelo.fit(concentracion, absorbancia)
    
# Predicciones del modelo
absorbancia_pred = modelo.predict(concentracion)

# Obtener la pendiente (m) y la intersección (b) de la regresión lineal
pendiente = modelo.coef_[0]
interseccion = modelo.intercept_

# Calcular el R^2
r2 = modelo.score(concentracion, absorbancia)

# Crear figura y ejes
fig, ax = plt.subplots()

# Graficar los puntos originales y la línea de regresión
ax.scatter(concentracion, absorbancia, color='blue', label='Datos experimentales')  # Puntos originales
ax.plot(concentracion, absorbancia_pred, color='red', label='Línea de calibrado')  # Línea ajustada

# Etiquetas y título
ax.set_xlabel('Concentración de ácido acetilsalicílico [mg/L]')
ax.set_ylabel('Absorbancia')
ax.set_title('Curva de Calibrado: Ácido Acetilsalicílico')

# Agregar la ecuación de la recta en el gráfico dentro de los datos
ecuacion_texto = f'Y = {pendiente:.3f}X + {interseccion:.3f}'
r2_texto = f'R² = {r2:.3f}'

ax.text(0.15, 1.2, ecuacion_texto, color='green', fontsize=12)  # Ajusta las coordenadas para que se vea bien
ax.text(0.15, 1.1, r2_texto, color='purple', fontsize=12)  # Mostrar R² en el gráfico

# Agregar leyenda
ax.legend()

# Mostrar la gráfica
plt.show()
