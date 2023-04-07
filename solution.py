import pandas as pd
import numpy as np


chat_id = 390760498 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    return (np.log(x-243)).mean() 
