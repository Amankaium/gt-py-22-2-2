# import datetime
from datetime import datetime, timedelta


c = datetime.now()
print(c)
usa_time = c - timedelta(hours=11)
japan_time = c + timedelta(hours=6)
print(japan_time)
