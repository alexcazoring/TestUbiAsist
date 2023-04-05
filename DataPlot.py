# Código para pltear los valores de un archivo de datos

# import pandas as pd
# import matplotlib.pyplot as plt

# tabla = pd.read_csv('datos.csv')
# print(tabla.head(1))
# tiempo = tabla['Times (s)']
# plt.plot(tabla['Time'])
# plt.show()

import pandas as pd
import matplotlib.pyplot as plt

tabla = pd.read_csv('datos.csv', decimal='.', sep=',')
plt.plot(tabla['Time'], tabla['AngleX'])
plt.xlabel('Time (s)')
plt.ylabel('AngleX (degrees)')
plt.title('Gráfica de Time vs AngleX')
plt.show()
