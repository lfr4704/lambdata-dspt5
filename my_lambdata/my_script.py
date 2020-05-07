import pandas as pd
import numpy as np
from my_lambdata.my_mod import enlarge


df = pd.DataFrame(np.random.randint(0,100, size=(100,4)), columns=list('ABCD'))

print(df.head())

x = 11
print(enlarge(x))
