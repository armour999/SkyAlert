
#!/usr/bin/env python
import forecastio
import os
import piglow as PG
import piglow
import time
from time import sleep
piglow.auto_update = True

# API details
api_key = os.environ['DARKSKY_API']
lat = float(os.environ['LAT'])
lng = float(os.environ['LON'])

forecast = forecastio.load_forecast(api_key, lat, lng)

daily = forecast.daily()
sunrise = daily.data[0].sunriseTime
sunset = daily.data[0].sunsetTime

forecast = forecastio.load_forecast(api_key, lat, lng)

daily = forecast.daily()
sunrise = daily.data[0].sunriseTime
sunset = daily.data[0].sunsetTime

hourly = forecast.hourly()
for i in range(0, 8):
  hourlyData = hourly.data[i]
  print(i, hourlyData.icon)


  if hourlyData.icon == "wind":
   #while True:
    for x in range(100):
        piglow.leg_bar(0, x / 100.0)
        #piglow.leg_bar(1, x / 100.0)
        #piglow.leg_bar(2, x / 100.0)
        piglow.yellow(200)
        piglow.show()
        time.sleep(0.01)
    for x in reversed(range(100)):
        piglow.leg_bar(0, x / 100.0)
        #piglow.leg_bar(1, x / 100.0)
        #piglow.leg_bar(2, x / 100.0)
        piglow.yellow(200)
        piglow.show()
        time.sleep(0.01)

  elif hourlyData.icon == "rain":
    	 for x in range(100):
        piglow.leg_bar(0, x / 100.0)
        #piglow.leg_bar(1, x / 100.0)
        #piglow.leg_bar(2, x / 100.0)
        piglow.blue(200)
        piglow.show()
        time.sleep(0.01)
     for x in reversed(range(100)):
        piglow.leg_bar(0, x / 100.0)
        #piglow.leg_bar(1, x / 100.0)
        #piglow.leg_bar(2, x / 100.0)
        piglow.blue(200)
        piglow.show()
        time.sleep(0.01) 
  
  elif hourlyData.icon == "snow":
    for x in range(100):
        piglow.leg_bar(0, x / 100.0)
        #piglow.leg_bar(1, x / 100.0)
        #piglow.leg_bar(2, x / 100.0)
        piglow.white(200)
        piglow.show()
        time.sleep(0.01)
     for x in reversed(range(100)):
        piglow.leg_bar(0, x / 100.0)
        #piglow.leg_bar(1, x / 100.0)
        #piglow.leg_bar(2, x / 100.0)
        piglow.white(200)
        piglow.show()
        time.sleep(0.01) 
          
  elif hourlyData.icon == "sleet":
  for x in range(100):
        piglow.leg_bar(0, x / 100.0)
        #piglow.leg_bar(1, x / 100.0)
        #piglow.leg_bar(2, x / 100.0)
        piglow.red(200)
        piglow.show()
        time.sleep(0.01)
     for x in reversed(range(100)):
        piglow.leg_bar(0, x / 100.0)
        #piglow.leg_bar(1, x / 100.0)
        #piglow.leg_bar(2, x / 100.0)
        piglow.red(200)
        piglow.show()
        time.sleep(0.01) 
 
  
  elif hourlyData.icon == "fog":
 for x in range(100):
        piglow.leg_bar(0, x / 100.0)
        #piglow.leg_bar(1, x / 100.0)
        #piglow.leg_bar(2, x / 100.0)
        piglow.orange(200)
        piglow.show()
        time.sleep(0.01)
     for x in reversed(range(100)):
        piglow.leg_bar(0, x / 100.0)
        #piglow.leg_bar(1, x / 100.0)
        #piglow.leg_bar(2, x / 100.0)
        piglow.orange(200)
        piglow.show()
        time.sleep(0.01) 
      
  elif hourlyData.icon == "cloudy":
  for x in range(100):
        piglow.leg_bar(0, x / 100.0)
        #piglow.leg_bar(1, x / 100.0)
        #piglow.leg_bar(2, x / 100.0)
        piglow.green(200)
        piglow.show()
        time.sleep(0.01)
     for x in reversed(range(100)):
        piglow.leg_bar(0, x / 100.0)
        #piglow.leg_bar(1, x / 100.0)
        #piglow.leg_bar(2, x / 100.0)
        piglow.green(200)
        piglow.show()
        time.sleep(0.01) 
      
    
  elif hourlyData.icon == "clear-day":
 for x in range(100):
        #piglow.leg_bar(0, x / 100.0)
        #piglow.leg_bar(1, x / 100.0)
        #piglow.leg_bar(2, x / 100.0)
        piglow.blue(10)
        piglow.show()
        time.sleep(0.01)
     for x in reversed(range(100)):
        piglow.leg_bar(0, x / 100.0)
        #piglow.leg_bar(1, x / 100.0)
        #piglow.leg_bar(2, x / 100.0)
        piglow.blue(10)
        piglow.show()
        time.sleep(0.01) 

  elif hourlyData.icon == "partly-cloudy-night":
     for x in range(100):
        piglow.leg_bar(0, x / 100.0)
        #piglow.leg_bar(1, x / 100.0)
        #piglow.leg_bar(2, x / 100.0)
        piglow.blue(10)
        piglow.show()
        time.sleep(0.01)
     for x in reversed(range(100)):
        piglow.leg_bar(0, x / 100.0)
        #piglow.leg_bar(1, x / 100.0)
        #piglow.leg_bar(2, x / 100.0)
        piglow.blue(10)
        piglow.show()
        time.sleep(0.01) 
