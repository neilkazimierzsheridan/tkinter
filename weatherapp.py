from tkinter import *
from PIL import ImageTk, Image
import requests
import json

# APIs with tkinter! Part 1


root = Tk()
root.title("Air Quality App")
root.geometry("600x100")
root.configure(background="")

#zip code lookup function
def zipLookup():
	zip.get()
	zipLabel = Label(root, text=zip.get())
	zipLabel.pack()



#URL https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=90210&distance=25&API_KEY=6E809401-62C6-45AC-A316-CACB4CC8FF06

#api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=90210&distance=25&API_KEY=6E809401-62C6-45AC-A316-CACB4CC8FF06")

#api = json.loads(api_request.content) #pass the content we got with requests.get()

try:
	api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=10013&distance=25&API_KEY=6E809401-62C6-45AC-A316-CACB4CC8FF06")
	api = json.loads(api_request.content) #pass the content we got with requests.get()
	city = api[0]['ReportingArea'] #select the parts of list we want
	quality = api[0]['AQI']
	category = api[0]['Category']['Name'] #and the dictionary part of list, see bottom for raw data from api
	# now set background colors for the category e.g. green for good
	if category == "Good": 
		weather_color = "#0C0"
	elif category == "Moderate":
		weather_color = "#FFFF00"
	elif category == "Unhealthy for Sensitive Groups":
		weather_color = "#ff9900"
	elif category == "Unhealthy":
		weather_color ="#FF0000"
	elif category == "Very Unhealthy":
		weather_color ="#990066"
	elif category == "Hazardous":
		weather_color ="#660000"

	root.configure(background=weather_color) #set background for window
	myLabel = Label(root, text=city + " Air Quality AQI " + str(quality) + " " + category, font=("Helvetica", 20), background=weather_color)
	myLabel.pack()
except Exception as e:
	api = "Error"

#myLabel = Label(root, text=city + " Air Quality AQI " + str(quality) + " " + category, font=("Helvetica", 20), background="green")
#myLabel.pack()

zip = Entry(root)
zip.pack()

zipBtn = Button(root, text="Lookup ZipCode", command=zipLookup)
zipBtn.pack()


root.mainloop()


## Data from api e.g.

# 0 item from the list api gives
#[{"DateObserved":"2021-06-07 ","HourObserved":7,"LocalTimeZone":"PST","ReportingArea":"NW Coastal LA",
#"StateCode":"CA","Latitude":34.0505,"Longitude":-118.4566,"ParameterName":"O3","AQI":30,
#"Category":{"Number":1,"Name":"Good"}}

#whats's wanted above? The ReportingArea and AQI and Catergory which returns dictionary which we need name
#from so e.g. api[0]['Category']['Name']

#,{"DateObserved":"2021-06-07 ","HourObserved":7,"LocalTimeZone":"PST",
#"ReportingArea":"NW Coastal LA","StateCode":"CA","Latitude":34.0505,"Longitude":-118.4566,"ParameterName":"PM2.5",
#"AQI":15,"Category":{"Number":1,"Name":"Good"}}]