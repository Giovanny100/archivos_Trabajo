import numpy as np
import matplotlib.pyplot as plt

#Tupla (fig, ax)
fig, ax = plt.subplots(2,2)

#Seis funciones
x1 = [0,1,2,3,4,5]
y1 = [70,30,30,70,70,70]

x2 = np.arange(0,5, 0.15)
y2 = -30 * np.ones(len(x2))

x3 = np.arange(0,5/3.14*np.pi, 0.25)
y3 = 10*np.cos(2*x3)

x4 = np.linspace(0,5, 20, endpoint = True)
y4 = x4**2 + 100


#Función y1
ax[0,0].plot(x1, y1, 'r--o', label = "$y_1 -> Tab1$")
ax[0,0].set_xlabel('x', color = 'red',fontsize=12)
ax[0,0].set_ylabel('y', color = 'red',fontsize=12)
ax[0,0].legend(loc=1)
ax[0,0].set_title('y1')
ax[0,0].grid(color='powderblue', linestyle='--')

#Función y2
ax[0,1].plot(x2, y2, 'b-v', label = "$y_2 = -30$")
ax[0,1].set_xlabel('x', color = 'blue',fontsize=12)
ax[0,1].set_ylabel('y', color = 'blue',fontsize=12)
ax[0,1].legend(loc=1)
ax[0,1].set_title('y2')
ax[0,1].grid(color='powderblue', linestyle='--')

#Función y3
ax[1,0].plot(x3, y3, ':p', color = 'orange', label = "$y_3 = cos(x)$")
ax[1,0].set_xlabel('x', color = 'orange',fontsize=12)
ax[1,0].set_ylabel('y', color = 'orange',fontsize=12)
ax[1,0].legend(loc=1)
ax[1,0].set_title('y3')
ax[1,0].grid(color='powderblue', linestyle='--')

#Función y4
ax[1,1].plot(x4, y4, 'c-',  label = "$y_4 = x^2 +100$")
ax[1,1].set_xlabel('x', color = 'cyan',fontsize=12)
ax[1,1].set_ylabel('y', color = 'cyan',fontsize=12)
ax[1,1].legend(loc=1)
ax[1,1].set_title('y4')
ax[1,1].grid(color='powderblue', linestyle='--')

#Título de toda la figura
fig.suptitle('Ejemplo de funciones en un mismo gráfico Python - Matplotlib', fontsize=15)

#Nombres de ejes comunes
fig.text(0.5, 0.03, 'Eje común X', va='center', ha='center', fontsize=16)
fig.text(0.03, 0.5, 'Eje común Y', va='center', ha='center', fontsize=16, rotation='vertical')

#Evita solapamiento de textos
fig.tight_layout()

#Mostrar imagen
plt.show()