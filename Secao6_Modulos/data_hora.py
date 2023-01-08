from datetime import datetime

data_str = '2023-01-08 17:30:00'
data_str_fmt = '%Y-%m-%d %H:%M:%S'

# data = datetime(2023, 1, 8, 17, 20, 00)
data = datetime.strptime(data_str, data_str_fmt)
print(data)
