import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Создаем столбцы для каждого уникального значения в 'whoAmI'
for value in data['whoAmI'].unique():
    data[value] = (data['whoAmI'] == value).astype(int)

# Удаляем исходный столбец 'whoAmI'
data = data.drop('whoAmI', axis=1)

print(data.head())