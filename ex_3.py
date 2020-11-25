#Известно, что рост футболистов в сборной распределен нормально
#с дисперсией генеральной совокупности, равной 25 кв.см. Объем выборки равен 27,
#среднее выборочное составляет 174.2. Найдите доверительный интервал для математического
#ожидания с надежностью 0.95.
import numpy as np
import pandas as pd
import sys
import statistics
M_X= 174.2
std_X = np.sqrt(25)
M_std_X = std_X / np.sqrt(27)
M_std_X =M_X - std_X / (np.sqrt(10))
M_std_X2 = M_X + std_X/(np.sqrt(10))
print(M_std_X, M_std_X2)