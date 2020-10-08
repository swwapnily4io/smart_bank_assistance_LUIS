from botbuilder.core import (
    TurnContext, )

def deposit(turn_context: TurnContext):

    print("Printing type------", turn_context._activity.value["type"])
    print("Printing type------", turn_context._activity.value["name"])
    print("Printing deposit------", turn_context._activity.value["deposit_type"])
    print("Printing amount------", turn_context._activity.value["amount"])
    print("Printing period------", turn_context._activity.value["period"])
    print("Printing account------", turn_context._activity.value["account_number"])
    name = turn_context._activity.value["name"]
    deposit_type = turn_context._activity.value["deposit_type"]
    amount = turn_context._activity.value["amount"]
    period = turn_context._activity.value["period"]
    account_number = turn_context._activity.value["account_number"]
    isvalid = True
    if (name is None) or (str(name).strip() == ""):
        isvalid = False
        # return turn_context.send_activity("Please enter valid Customer ID")
        message = "Please enter valid Name"
        return message
    if (amount is None) or (str(amount).strip() == ""):
        isvalid = False
        # return turn_context.send_activity("Please enter valid Password")
        message = "Please enter valid Amount"
        return message
    if (deposit_type is None) or (str(deposit_type).strip() == ""):
        isvalid = False
        # return turn_context.send_activity("Please accept the terms and conditions.")
        message = "Please enter valid Deposit Type"
        return message
    if (period is None) or (str(period).strip() == ""):
        isvalid = False
        # return turn_context.send_activity("Please accept the terms and conditions.")
        message = "Please enter valid Period"
        return message
    if (account_number is None) or (str(account_number).strip() == ""):
        isvalid = False
        # return turn_context.send_activity("Please accept the terms and conditions.")
        message = "Please enter valid Account Number"
        return message
    if (isvalid and turn_context._activity.value["type"] in ("Apply Deposit")):
        message = "Application Succeded"

    return  message
