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
            "id": "name"
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
            "id": "deposit_type"
        },
        {
            "type": "Input.Number",
            "placeholder": "Amount",
            "id": "amount"
        },
        {
            "type": "Input.Number",
            "placeholder": "Period (Months)",
            "id": "period"
        },
        {
            "type": "Input.Text",
            "placeholder": "Mobile Number",
            "id": "mobile_number"
        },
        {
            "type": "Input.Text",
            "placeholder": "Email ID",
            "id": "email"
        },
{
            "type": "ActionSet",
            "actions": [
                {
                    "type": "Action.Submit",
                    "data": {
                            "type": "Apply Deposit"
                    },
                    "title": "Apply",
                }
            ]
        }
    ],
    "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
    "version": "1.2"
}