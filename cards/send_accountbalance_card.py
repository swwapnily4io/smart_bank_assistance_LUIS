from botbuilder.schema import (
    ChannelAccount,
    HeroCard,
    CardImage,
    CardAction,
    ThumbnailCard,
    ActionTypes,
)

from adaptivecardbuilder import Column, ColumnSet, Image, TextBlock, AdaptiveCard, InputText, ActionShowCard, ActionSubmit, ActionOpenUrl


def buildAccountBalance_card(data):
    accountsCard = AdaptiveCard(
        backgroundImage=
        "https://image.freepik.com/free-photo/wall-wallpaper-concrete-colored-painted-textured-concept_53876-31799.jpg"
    )
    accountsCard.add(
        TextBlock(
            text=
            "Account Details \n\n Please select an account to see last 10 transaction details",
            color="light",
            size="Medium",
            weight="Bolder"))
    if (data["statusMsg"] is not None and data["statusMsg"] in ("Success")):
        print("success response ", data)
        accountsList = data["accountList"]

        for lst in accountsList:
            print(lst['accountType'])
            accountsCard.add(
                ActionSubmit(title="" + str(lst['accountType']) +
                             "\n Account No. " + str(lst['accountNo']) +
                             "\n Opened date: " + str(lst['createdOn']) +
                             "\n Balance is:" + str(lst["currencySymbol"]) +
                             str(lst["balance"]),
                             data=str(lst['accountNo'])))
    return accountsCard


def accountbalance_card():
    card = ThumbnailCard(
        title="Account Details",
        text="Please select an account to see last 10 transaction details",

        # images=[CardImage(url="https://www.iconfinder.com/data/icons/infographic-bar-16/512/17-512.png")],
        buttons=[
            CardAction(
                type=ActionTypes.im_back,
                title=
                "Savings Account No. xxxxxxxxx4567 \n Opened date: 05/10/2010 \n Balance is $112.02",
                text="Balance is $112.02",
                display_text="Balance is $112.02",
                value="xxxxxxxxx4567",
            ),
            CardAction(
                type=ActionTypes.im_back,
                title=
                "Current Account xxxxxxxxx4566 \n Opened date: 05/10/2012 \n Balance is $0.00",
                text="Balance is $0.00",
                display_text="Balance is $0.00",
                value="xxxxxxxxx4566",
            ),
        ],
    )

    return card