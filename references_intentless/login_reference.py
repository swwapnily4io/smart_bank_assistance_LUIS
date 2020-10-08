from botbuilder.core import (
    TurnContext,)


def login(turn_context: TurnContext):
    print("Printing type------", turn_context._activity.value["type"])
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
        message = "Login Succeded. \n An OTP is sent to your registered mobile number xxxxxxxx90. \n Please enter the OTP."
        return message
        # defining a params dict for the parameters to be sent to the API
        # PARAMS = {'userName': customerId, 'password': password}
        # sending get request and saving the response as response object
        # r = requests.get(url="http://localhost:8080/login", params=PARAMS)
        # extracting data in json format
        # data = r.json()
        # print("printing response ", data["loginStatus"])
        # if (data["loginStatus"] is not None and data["loginStatus"] in ("success")):
        #return turn_context.send_activity("Login Succeded. \n An OTP is sent to your registered mobile number xxxxxxxx90. \n Please enter the OTP.")
        # await turn_context.send_activity()
        # await turn_context.send_activity("Please enter the OTP.")
        # else:
        #    await turn_context.send_activity("Login Failed. Please try again")
    #            for key in turn_context._activity.value:
    #                print(turn_context._activity.value[key])

    # if (isvalid and turn_context._activity.value["type"] in ("Submit")):
    #     await turn_context.send_activity("Deposits Applied")