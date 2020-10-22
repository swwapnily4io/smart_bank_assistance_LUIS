from adaptivecardbuilder import Column, ColumnSet,Image ,TextBlock,AdaptiveCard, InputText, ActionShowCard, ActionSubmit, ActionOpenUrl

def serviceRequestsList_card(data):
    serviceRequestCard = AdaptiveCard(
        backgroundImage="https://image.freepik.com/free-photo/wall-wallpaper-concrete-colored-painted-textured-concept_53876-31799.jpg")
    serviceRequestCard.add(
        TextBlock(text="Service request details:", color="light", size="Medium", weight="Bolder"))
    serviceRequestCard.add(ColumnSet())
    if (data["statusMsg"] is not None and data["statusMsg"] in ("Success")):
        print("success response ", data)
        serviceRequestList = data["serviceRequest"]
        serviceRequestCard.add(Column(width=1))
        serviceRequestCard.add(TextBlock(text="REQUEST ID", color="light", weight="Bolder"))
        for lst in serviceRequestList:
            print(str(lst['requestId']))
            serviceRequestCard.add(TextBlock(text=str(lst['requestId']), color="light"))
        serviceRequestCard.up_one_level()
        serviceRequestCard.add(Column(width=1))
        serviceRequestCard.add(TextBlock(text="DESCRIPTION", color="light", weight="Bolder"))
        for lst in serviceRequestList:
            print(lst['description'])
            serviceRequestCard.add(TextBlock(text=str(lst['description']), color="light"))
        serviceRequestCard.up_one_level()
        serviceRequestCard.add(Column(width=1))
        serviceRequestCard.add(TextBlock(text="CREATED ON", color="light", weight="Bolder"))
        for lst in serviceRequestList:
            print(lst['createdOn'])
            serviceRequestCard.add(TextBlock(text=lst['createdOn'], color="light"))
        serviceRequestCard.up_one_level()
        serviceRequestCard.add(Column(width=1))
        serviceRequestCard.add(TextBlock(text="STATUS", color="light", weight="Bolder"))
        for lst in serviceRequestList:
            print(lst['status'])
            serviceRequestCard.add(TextBlock(text=str(lst['status']), color="light"))
        serviceRequestCard.up_one_level()
        serviceRequestCard.add(Column(width=1))
        serviceRequestCard.add(TextBlock(text="COMMENTS", color="light", weight="Bolder"))
        for lst in serviceRequestList:
            print(lst['comments'])
            serviceRequestCard.add(TextBlock(text=lst['comments'], color="light"))

    return serviceRequestCard