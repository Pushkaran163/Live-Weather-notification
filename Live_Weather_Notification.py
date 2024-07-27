import requests
from bs4 import BeautifulSoup
from win10toast import ToastNotifier

# Create an object to ToastNotifier class
n = ToastNotifier()

# Define a function to get HTML data from a URL
def getdata(url):
    r = requests.get(url)
    return r.text

try:
    # Fetch the weather data
    htmldata = getdata("https://weather.com/en-IN/weather/today/l/25.59,85.14?par=google&temp=c/")
    soup = BeautifulSoup(htmldata, 'html.parser')

    # Extract current temperature
    current_temp = soup.find("span", class_="CurrentConditions--tempValue--MHmYY")
    if current_temp:
        current_temp = current_temp.text
    else:
        current_temp = "N/A"

    # Extract chances of rain
    chances_rain = soup.find("div", class_="CurrentConditions--precipValue--2aJSf")
    if chances_rain:
        chances_rain = chances_rain.text
    else:
        chances_rain = "N/A"

    # Create the result string
    result = f"Current Temperature: {current_temp} in Patna, Bihar\nChances of Rain: {chances_rain}"

    # Show the toast notification
    n.show_toast("Live Weather Update", result, duration=10)

except Exception as e:
    print(f"An error occurred: {e}")