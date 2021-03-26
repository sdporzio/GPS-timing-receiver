screen -dmS get_utc_timestamp bash -c "python /home/daq/UTC_receiver/Receiver/receiver.py"
screen -dmS monitor_time_delta bash -c "python /home/daq/UTC_receiver/Receiver/timeDeltaControl.py"
screen -ls