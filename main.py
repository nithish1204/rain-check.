import requests
import os
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/weather"
api_key = os.environ.get("OMW_API_KEY")
account_sid = "ACd6c72e835b565e8cc5e487f8b7376366"
auth_token = os.environ.get("AUTH_TOKEN")
TO = os.environ.get("TO")

weather_params = {
    "lat": 8.587364,
    "lon": 81.215210,
    "appid": api_key,
}
response = requests.get(OWM_Endpoint, params=weather_params)
# print(response.json())
response.raise_for_status()
weather_data = response.json()
condition_code = weather_data["weather"][0]["id"]
if int(condition_code) < 700:
    # proxy_client = TwilioHttpClient()
    # proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today, bring an umbrella☔️",
        from_="+19804145881",
        to=TO
    )
    print(message.status)












