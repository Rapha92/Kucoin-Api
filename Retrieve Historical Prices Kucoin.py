# =================================================================================
# Description     : Retrieve Historic Price Data from Kucoin
# Input           : Kucoin API
# Output          : Trading Dataset
# Review status   : DEV
# V1 - 20180430 - RMA
# =================================================================================
# Data Retrieval
import pandas as pd
import numpy as np
import dateparser
import pytz
import json
import os
import threading
from kucoin.client import Client
import time
import datetime
import math
import os
#############################
#Start-Up Kucoin API
key = "Insert your Key"
secret = "Insert your Key"
client = client = Client(key, secret)
################################################################################
cwd = os.getcwd()
### Set Time Frame for Data Retrieval
from_time = 1507479171
to_time = 1510278278
klines = client.get_kline_data_tv(
    'KCS-BTC',
    Client.RESOLUTION_15MINUTES,
    from_time,
    to_time
)
################################################################################
# Define Functions
def change_time(x):
    return(time.strftime("%D %H:%M", time.localtime(int(str(x)))))
from_time = 1507479300
to_time = 1507479300 + 10000
#### Set Time Interval ####
s = "01/01/2018"
#t = "30/04/2018"
to_time = int(round(time.time(),0))
from_time = int(time.mktime(datetime.strptime(s, "%d/%m/%Y").timetuple()))
#to_time = int(time.mktime(datetime.strptime(t, "%d/%m/%Y").timetuple()))

# Load Data & Transform
klines = client.get_kline_data_tv('ETH-BTC', Client.RESOLUTION_15MINUTES, int(from_time), int(to_time))
klines.pop('s', None)
KCS = pd.DataFrame(klines)
KCS.columns = ["Close", "High", "Low", "Open",  "Time", "Volume"]   
KCS['Time_Date'] = KCS['Time'].apply(lambda x: change_time(x))
##############################################################################
# Plotting Data
KCS['Time_Date'] = pd.to_datetime(KCS['Time_Date'])
KCS = KCS.set_index('Time_Date')
KCS['High'].plot(grid= True, lw = 2, title = "KCS-BTC Price")
KCS.to_pickle(cwd +"\KCS-Data.pkl")
























