import pandas as pd
import random

# Исходные данные
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Создаем столбцы для one-hot кодировки
data['robot'] = [1 if x == 'robot' else 0 for x in data['whoAmI']]
data['human'] = [1 if x == 'human' else 0 for x in data['whoAmI']]

# Удаляем оригинальный столбец
data = data.drop('whoAmI', axis=1)

# Смотрим результат
print(data.head())
