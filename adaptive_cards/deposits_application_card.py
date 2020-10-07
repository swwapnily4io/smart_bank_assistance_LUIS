DEPOSITS_APPLICATION_CARD = {
    "type": "AdaptiveCard",
    "body": [
        {
            "type": "TextBlock",
            "size": "Medium",
            "weight": "Bolder",
            "text": "Apply Deposits"
        },
        {
            "type": "TextBlock",
            "text": "Please enter the below details for applying.",
            "wrap": True
        },
        {
            "type": "Input.Text",
            "placeholder": "Full Name",
            "id": "1"
        },
        {
            "type": "Input.ChoiceSet",
            "choices": [
                {
                    "title": "Fixed Deposit",
                    "value": "FD"
                },
                {
                    "title": "Recurring Deposit",
                    "value": "RD"
                }
            ],
            "placeholder": "Select Deposit Type",
            "id": "8"
        },
        {
            "type": "Input.Number",
            "placeholder": "Amount",
            "id": "6"
        },
        {
            "type": "Input.Number",
            "placeholder": "Period (Months)",
            "id": "7"
        },
        {
            "type": "Input.Text",
            "placeholder": "Debiting Account Number",
            "id": "4"
        },
{
            "type": "ActionSet",
            "actions": [
                {
                    "type": "Action.Submit",
                    "data": {
                            "type": "Submit"
                    },
                    "title": "Submit",
                }
            ]
        }
    ],
    "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
    "version": "1.2"
}