from adaptivecardbuilder import Column, ColumnSet,Image ,TextBlock,AdaptiveCard, InputText, ActionShowCard, ActionSubmit, ActionOpenUrl

def transaction_history_card(data):
    transactionHistoryCard = AdaptiveCard(
        backgroundImage="https://image.freepik.com/free-photo/wall-wallpaper-concrete-colored-painted-textured-concept_53876-31799.jpg")
    transactionHistoryCard.add(
        TextBlock(text="Savings Account xxxxxxxxx4567 - Balance is  "+str(data['account']['currencySymbol'])+str(data['account']['balance']), color="light", size="Medium",
                  weight="Bolder"))
    transactionHistoryCard.add(
        TextBlock(text="Last 10 transaction details:", color="light", size="Medium", weight="Bolder"))
    transactionHistoryCard.add(ColumnSet())
    if (data["statusMsg"] is not None and data["statusMsg"] in ("Success")):
        print("success response ", data)
        historyList = data["historyList"]
        transactionHistoryCard.add(Column(width=1))
        transactionHistoryCard.add(TextBlock(text="TRANSACTION DATE", color="light", weight="Bolder"))
        for lst in historyList:
            print(lst['transactionDate'])
            transactionHistoryCard.add(TextBlock(text=lst['transactionDate'], color="light"))
        transactionHistoryCard.up_one_level()
        transactionHistoryCard.add(Column(width=1))
        transactionHistoryCard.add(TextBlock(text="REF. NO", color="light", weight="Bolder"))
        for lst in historyList:
            print(lst['refNo'])
            transactionHistoryCard.add(TextBlock(text=str(lst['refNo']), color="light"))
        transactionHistoryCard.up_one_level()
        transactionHistoryCard.add(Column(width=1))
        transactionHistoryCard.add(TextBlock(text="TRANSACTION TYPE", color="light", weight="Bolder"))
        for lst in historyList:
            print(lst['transactionType'])
            transactionHistoryCard.add(TextBlock(text=lst['transactionType'], color="light"))
        transactionHistoryCard.up_one_level()
        transactionHistoryCard.add(Column(width=1))
        transactionHistoryCard.add(TextBlock(text="AMOUNT", color="light", weight="Bolder"))
        for lst in historyList:
            print(lst['amount'])
            transactionHistoryCard.add(TextBlock(text=str(lst['amount']), color="light"))
        transactionHistoryCard.up_one_level()
        transactionHistoryCard.add(Column(width=1))
        transactionHistoryCard.add(TextBlock(text="DESCRIPTION", color="light", weight="Bolder"))
        for lst in historyList:
            print(lst['description'])
            transactionHistoryCard.add(TextBlock(text=lst['description'], color="light"))

    return transactionHistoryCard