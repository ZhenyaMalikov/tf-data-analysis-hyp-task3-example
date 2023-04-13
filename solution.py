import pandas as pd
import numpy as np
from scipy import 

chat_id = 516575251 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    sgn_lvl = 0.01
    
    test = stats.ttest_ind(x, y, alternative = 'less')
    p_value = test[1]
    return p_value < sgn_lvl
