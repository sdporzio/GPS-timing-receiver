screen -dmS get_utc_timestamp bash -c "python /home/daq/UTC_receiver/receiver.py"
screen -dmS monitor_time_delta bash -c "python /home/daq/UTC_receiver/timeDeltaControl.py"