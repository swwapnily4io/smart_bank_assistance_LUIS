LOAN_APPLICATION_CARD = {
    "type": "AdaptiveCard",
    "body": [
        {
            "type": "TextBlock",
            "size": "Medium",
            "weight": "Bolder",
            "text": "Apply Loan"
        },
        {
            "type": "TextBlock",
            "text": "Please enter the below details for applying loan.",
            "wrap": True
        },
        {
            "type": "Input.Text",
            "placeholder": "Full Name",
            "id": "name"
        },
        {
            "type": "Input.Number",
            "placeholder": "Loan Amount",
            "id": "amount"
        },
        {
            "type": "Input.ChoiceSet",
            "choices": [
                {
                    "title": "Car Loan",
                    "value": "Car Loan"
                },
                {
                    "title": "House Loan",
                    "value": "House Loan"
                },
                {
                    "title": "Personal Loan",
                    "value": "Personal Loan"
                },
                {
                    "title": "Education Loan",
                    "value": "Education Loan"
                }
            ],
            "placeholder": "Select Loan Type",
            "id": "loan_type",
            "separator": True,
            "wrap": True
        },
        {
            "type": "Input.Text",
            "placeholder": "Debiting Account Number",
            "id": "account_number"
        },
        {
            "type": "ActionSet",
            "actions": [
                {
                    "type": "Action.Submit",
                    "data": {
                        "type": "Apply Loan"
                    },
                    "title": "Apply",
                }
            ]
        }
    ],
    "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
    "version": "1.2"
}