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
            "id": "1"
        },
        {
            "type": "Input.Number",
            "placeholder": "Loan Amount",
            "id": "6"
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
            "id": "5",
            "separator": True,
            "wrap": True
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