import requests
from datetime import datetime

api_key = '6e06abc0bb444ce7720cc1fbe34663b3'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print ("-------------------------------------------------------------")
print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
print ("-------------------------------------------------------------")

print ("Current temperature is: {:.2f} deg C".format(temp_city))
print ("Current weather desc  :",weather_desc)
print ("Current Humidity      :",hmdt, '%')
print ("Current wind speed    :",wind_spd ,'kmph')

# To store the fetched report in the form of .txt file
x=open("Weather_report.txt","a") # Here 'a' is used so as to add(append) the data and store it  
print ("-------------------------------------------------------------",file=x)
print ("Weather Stats for - {}  || {}".format(location.upper(), date_time),file=x)
print ("-------------------------------------------------------------",file=x)

print ("Current temperature is: {:.2f} deg C".format(temp_city),file=x)
print ("Current weather desc  :",weather_desc,file=x)
print ("Current Humidity      :",hmdt, '%',file=x)
print ("Current wind speed    :",wind_spd ,'kmph',file=x)
x.close()