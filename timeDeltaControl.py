import os
import glob
import requests
from time import sleep
import datetime
from datetime import timedelta as td
from datetime import datetime as dt
from datetime import timezone as tz

# Set up destination from where to read timestamp files
dest = "/dev/shm/utc_timestamps/*"

# Connection to Influx/Grafana
db_url = "http://130.92.128.162"
db_port = 8086
db_name = "slowcontrol"


while True:
    files = glob.glob(dest)
    # Time of the next pulse
    file_now = float(files[-1].split('/')[-1])
    # Current UTC time
    utc_now = dt.now(tz.utc).timestamp()
    # file_now should be ahead of utc_not by a second or less
    timeDelta = file_now - utc_now

    # Send information to influx/grafana
    fullUrl = f"{db_url}:{db_port}/write?db={db_name}"
    post = f'timedelta value={timeDelta}'
    r = requests.post(fullUrl, data=post)

    sleep(0.8)
