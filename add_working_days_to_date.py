
from datetime import datetime, timedelta
import numpy as np
def add_days_to_date(start_date, days):
    if(days == 0):
        return start_date
    end_date = start_date + timedelta(days)
    
    while(True):
        business_days = np.busday_count(start_date + timedelta(1), end_date+timedelta(1))
        # print(start_date, end_date, business_days)
        weekends = int(days  - business_days)
        # print(weekends)
        if(weekends == 0):
            break
        start_date = end_date 
        end_date = end_date + timedelta(1) + timedelta(weekends-1)
        days = weekends 
    
    return end_date
#%%


## calling the above fun
start_date = datetime.strptime('13/12/2021','%d/%m/%Y').date() #2021-12-13
days = 5

res_date = add_days_to_date(start_date, days)
print(res_date)

print(type(res_date), type(start_date))
