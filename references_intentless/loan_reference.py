from botbuilder.core import (
    TurnContext, )

def loan(turn_context: TurnContext):

    print("Printing type------", turn_context._activity.value["type"])
    print("Printing type------", turn_context._activity.value["name"])
    print("Printing account------", turn_context._activity.value["amount"])
    print("Printing loantype------", turn_context._activity.value["loan_type"])
    print("Printing account------", turn_context._activity.value["mobile_number"])
    print("Printing account------", turn_context._activity.value["email"])
    name = turn_context._activity.value["name"]
    amount = turn_context._activity.value["amount"]
    loan_type = turn_context._activity.value["loan_type"]
    mobile_number = turn_context._activity.value["mobile_number"]
    email = turn_context._activity.value["email"]
    isvalid = True
    if (name is None) or (str(name).strip() == ""):
        isvalid = False
        # return turn_context.send_activity("Please enter valid Customer ID")
        message = "Please enter valid Name"
        return message
    if (amount is None) or (str(amount).strip() == ""):
        isvalid = False
        #return turn_context.send_activity("Please enter valid Password")
        message = "Please enter valid Amount"
        return message
    if (loan_type is None) or (str(loan_type).strip() == ""):
        isvalid = False
        #return turn_context.send_activity("Please accept the terms and conditions.")
        message = "Please enter valid Loan Type"
        return message
    if (mobile_number is None) or (str(mobile_number).strip() == ""):
        isvalid = False
        #return turn_context.send_activity("Please accept the terms and conditions.")
        message = "Please enter valid Mobile Number"
        return message
    if (email is None) or (str(email).strip() == ""):
        isvalid = False
        #return turn_context.send_activity("Please accept the terms and conditions.")
        message = "Please enter valid EmailID"
        return message
    if (isvalid and turn_context._activity.value["type"] in ("Apply Loan")):
        message = "Application Succeded"

    return  message