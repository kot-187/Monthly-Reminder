#Importing modules
import os
from dotenv import load_dotenv , dotenv_values
import requests
import time

#fetching variables from the token file .env
load_dotenv()
apiUrl = os.getenv("apiUrl")
idInstance = os.getenv("idInstance")
apiTokenInstance = os.getenv("apiTokenInstance")

#predefined variables
month = [0]

#The message sending code for whatsapp 
def whatsappMsg():
    url = f"{apiUrl}/waInstance{idInstance}/sendMessage/{apiTokenInstance}"

    payload = "{\r\n\t\"chatId\": \"PHONE-NUMBER-GOES-HERE@c.us\" , \r\n\t\"message\" : \"This is a monthly reminder to send my pocket money.\"\r\n}"
    headers = {
        'Content-Type' : 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data = payload)

    print(response.text.encode('utf8'))
    month.pop(0)

#Code for automatic message sending on the first of every month
def main():
    currentTime= time.localtime()
    if currentTime[2] == 1:
        if currentTime[1] != month[0]:
            month.append(currentTime[1])
            whatsappMsg()        

while True:
    main()