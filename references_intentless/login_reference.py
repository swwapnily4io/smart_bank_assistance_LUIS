from botbuilder.core import (
    TurnContext,)
import requests
from requests.auth import HTTPBasicAuth
from config.config_reader import ConfigReader

def configReader():
    config_reader = ConfigReader()
    configuration = config_reader.read_config()
    auth_username = configuration['AUTH_USERNAME']
    auth_password = configuration['AUTH_PASSWORD']
    restServerURL = configuration['REST_SERVER_URL']
    return auth_username, auth_password, restServerURL

def login(turn_context: TurnContext):
    print("Printing customer id------", turn_context._activity.value["customerId"])
    print("Printing password------", turn_context._activity.value["password"])

    customerId = turn_context._activity.value["customerId"]
    password = turn_context._activity.value["password"]
    terms = turn_context._activity.value["terms"]
    isvalid = True
    if (customerId is None) or (str(customerId).strip() == ""):
        isvalid = False
        # return turn_context.send_activity("Please enter valid Customer ID")
        message = "Please enter valid Customer ID"
        return message

    if (password is None) or (str(password).strip() == ""):
        isvalid = False
        #return turn_context.send_activity("Please enter valid Password")
        message = "Please enter valid Password"
        return message
    if (terms is None or terms in ("false")):
        isvalid = False
        #return turn_context.send_activity("Please accept the terms and conditions.")
        message = "Please accept the terms and conditions."
        return message
    if (isvalid and turn_context._activity.value["type"] in ("Login")):
        auth_username, auth_password, restServerURL = configReader()
        #url = "http://localhost:8080/oauth/token?grant_type=password&username=swwapnil&password=swwapnilpass"
        url = restServerURL+"/oauth/token?grant_type=password&username=swwapnil&password=swwapnilpass"
        print(url)
        payload = {}
        files = {}
        response = requests.request("POST", url, auth=HTTPBasicAuth(auth_username, auth_password), data=payload,files=files)
        print(response.text.encode('utf8'))
        print(response.json()["access_token"])
        print("customer id - ",customerId)
        # defining a params dict for the parameters to be sent to the API
        PARAMS = {'userName': customerId, 'password': password}
        # sending get request and saving the response as response object
        #url = "http://localhost:8080/api/login"
        url = restServerURL+"/api/login"
        print(url)
        payload = {}
        headers = {'Authorization': 'Bearer ' + response.json()["access_token"]}
        loginResp = requests.request("GET", url, headers=headers, params=PARAMS)
        print(loginResp.text.encode('utf8'))
        data = loginResp.json()
        # extracting data in json format
        print("printing loginStatus ", data["loginStatus"])
        if (data["loginStatus"] is not None and data["loginStatus"] in ("success")):
            message = "Login Succeded. \n An OTP is sent to your registered mobile number xxxxxxxx90. \n Please enter the OTP."
        else:
            message = "User not found. Please check the username and password."
        return message
        #return turn_context.send_activity("Login Succeded. \n An OTP is sent to your registered mobile number xxxxxxxx90. \n Please enter the OTP.")
        # await turn_context.send_activity()
        # await turn_context.send_activity("Please enter the OTP.")
        # else:
        #    await turn_context.send_activity("Login Failed. Please try again")
    #            for key in turn_context._activity.value:
    #                print(turn_context._activity.value[key])

    # if (isvalid and turn_context._activity.value["type"] in ("Submit")):
    #     await turn_context.send_activity("Deposits Applied")