#!/usr/bin/env python
import fitbit
import ConfigParser
import json
  
#Load Settings
parser = ConfigParser.SafeConfigParser()
 
parser.read('config.ini')
 
CI_id              = parser.get('Login Parameters', 'CLIENT_ID')
CI_client_secret   = parser.get('Login Parameters', 'CLIENT_SECRET')

with open ('token.json') as data_file:
   data = json.load(data_file)
 
authd_client = fitbit.Fitbit(CI_id, CI_client_secret, oauth2=True, access_token=data["ACCESS_TOKEN"], refresh_token=data["REFRESH_TOKEN"])
 
intradayS = authd_client.intraday_time_series('activities/steps', base_date    = 'today', detail_level = '1min', start_time   = None, end_time     = None)
 
f = open('datadumpSteps.json', 'w')
json.dump(intradayS, f)
 
intradayH = authd_client.intraday_time_series('activities/heart', base_date    = 'today', detail_level = '1sec', start_time   = None, end_time     = None)
 
f = open('datadumpHeart.json', 'w')
json.dump(intradayH, f)

alarmsH = authd_client.get_alarms (218802607)
f=open('datadumpAlarms.json', 'w')
json.dump(alarmsH, f)
