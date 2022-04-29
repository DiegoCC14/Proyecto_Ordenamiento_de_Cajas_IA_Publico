from numpy.random import seed , randn
import matplotlib.pyplot as plt
import numpy as np
seed(1)

lista_result = [ [3,4,1,5,5,6,3] ,[3,4,1,5,5,5,5] , [3,4,1,5,5,2,41] ]
plt.boxplot( lista_result )
plt.ylabel('Porcentaje de area sin uso')

values = ['AG-22', 'AG+PSO-22', 'AG-101' , 'AG+PSO-101' , 'AG-200' , 'AG+PSO-200'] 
plt.xticks( [1,2,3,4,5,6] , values )
plt.show()