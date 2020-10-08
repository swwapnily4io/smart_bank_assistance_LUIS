from botbuilder.ai.luis import LuisApplication,LuisPredictionOptions,LuisRecognizer
import json
#from config.config_reader import ConfigReader
from config.config_reader import ConfigReader
from logger.logger import Log
from botbuilder.core import (
    ActivityHandler,
    TurnContext,
    UserState,
    CardFactory,
    MessageFactory,
)
from botbuilder.schema import (
    Attachment,
    SigninCard,
)
from botbuilder.schema import (
    ChannelAccount,
    CardAction,
    ActionTypes,
)

from adaptive_cards.congratulations_adaptive_card import CONGRATULATIONS_ADAPTIVE_CARD
from adaptive_cards.into_adaptive_card import INTRO_ADAPTIVE_CARD_CONTENT
from adaptive_cards.login_otp_page import LOGIN_OTP_CARD_CONTENT
from adaptive_cards.invoice_adaptive_card import INVOICE_ADAPTIVE_CARD
from adaptive_cards.transaction_list_adaptive_card import ADAPTIVE_CARD_CONTENT
from adaptive_cards.loan_application_card import LOAN_APPLICATION_CARD
from adaptive_cards.deposits_application_card import DEPOSITS_APPLICATION_CARD

from cards.send_intro_card import intro_card
from cards.mobile_billPaymentConfirmation_card import billPaymentConfirmation_card
from cards.mobile_billDue_card import mobile_billDue_card
from cards.mobile_confirmation_card import mobile_confirmation_card
from cards.send_accountbalance_card import accountbalance_card
from cards.show_selectAccountForBill_card import account_SelectionForBill_card

from references_intentless.login_reference import login
from references_intentless.deposit_reference import deposit
from references_intentless.loan_reference import loan

class LuisConnect(ActivityHandler):
    def __init__(self, user_state: UserState):
        self.config_reader = ConfigReader()
        self.configuration = self.config_reader.read_config()
        self.luis_app_id = self.configuration['LUIS_APP_ID']
        self.luis_endpoint_key = self.configuration['LUIS_ENDPOINT_KEY']
        self.luis_endpoint = self.configuration['LUIS_ENDPOINT']
        self.luis_app = LuisApplication(self.luis_app_id, self.luis_endpoint_key, self.luis_endpoint)
        self.luis_options = LuisPredictionOptions(include_all_intents=True, include_instance_data=True)
        self.luis_recognizer = LuisRecognizer(application=self.luis_app, prediction_options=self.luis_options,
                                              include_api_results=True)
        self.log = Log()

        self._user_state = user_state

        self.user_state_accessor = self._user_state.create_property("WelcomeUserState")

        self.WELCOME_MESSAGE = """Welcome to Modern bank. I am your smart assistant. You can type 'menu' to start. """

        self.INFO_MESSAGE = """You are seeing this message because the bot received at least one
                                'ConversationUpdate' event, indicating you (and possibly others)
                                joined the conversation. If you are using the emulator, pressing
                                the 'Start Over' button to trigger this event again. The specifics
                                of the 'ConversationUpdate' event depends on the channel. You can
                                read more information at: https://aka.ms/about-botframework-welcome-user"""

        self.LOCALE_MESSAGE = """"You can use the 'activity.locale' property to welcome the
                                user using the locale received from the channel. If you are using the 
                                Emulator, you can set this value in Settings."""

        self.PATTERN_MESSAGE = """It is a good pattern to use this event to send general greeting
                                to user, explaining what your bot can do. In this example, the bot
                                handles 'hello', 'hi', 'help' and 'intro'. Try it now, type 'hi'"""

    async def on_turn(self, turn_context: TurnContext):
        await super().on_turn(turn_context)

        # save changes to WelcomeUserState after each turn
        await self._user_state.save_changes(turn_context)

    async def on_members_added_activity(self, members_added: [ChannelAccount], turn_context: TurnContext):
        """
        Greet when users are added to the conversation.
        Note that all channels do not send the conversation update activity.
        If you find that this bot works in the emulator, but does not in
        another channel the reason is most likely that the channel does not
        send this activity.
        """
        for member in members_added:
            if member.id != turn_context.activity.recipient.id:
                await turn_context.send_activity(
                    f"Hi there. " + self.WELCOME_MESSAGE
                )

    def create_signin_card(self) -> Attachment:
        card = SigninCard(
            text="ModernBank - Login",
            buttons=[
                CardAction(
                    type=ActionTypes.im_back,
                    title="Sign-In",
                    value="Sign-In",
                )
            ],
        )
        return CardFactory.signin_card(card)

    async def on_message_activity(self, turn_context: TurnContext):
        # weather_info=WeatherInformation()
        luis_result = await self.luis_recognizer.recognize(turn_context)
        text = luis_result.text
        isvalid = False
        if luis_result.properties == {}:
            print("unrecognized intent --> adaptive")
            if turn_context._activity.value["type"] in ("Login"):
                message =  login(turn_context)
                await turn_context.send_activity(message)
            elif turn_context._activity.value["type"] in ("Apply Deposit"):
                #print("Printing fd_rd------", turn_context._activity.value["deposit_type"])
                message = deposit(turn_context)
                await turn_context.send_activity(message)
            elif turn_context._activity.value["type"] in ("Apply Loan"):
                #print("Printing fd_rd------", turn_context._activity.value["deposit_type"])
                message = loan(turn_context)
                await turn_context.send_activity(message)

        else:

            result = luis_result.properties["luisResult"]
            reply = MessageFactory.list([])
            query = result.query
            #print(query)
            intent = json.loads((str(result.intents[0])).replace("'", "\""))['intent']
            #print(intent)

            if intent == 'WelcomeUser' and query not in ("1234", "369"):
                reply.attachments.append(self.create_signin_card())
                await turn_context.send_activity(reply)
                # await turn_context.send_activity(f"Echo: \n\n Intent: {intent}")
                # await self.__send_intro_card(turn_context)
            elif intent == 'UserLogin':
                await self.__login_otp_card_card(turn_context)
            elif intent == 'Accounts':
                # entity = json.loads((str(result.entities[0])).replace("'", "\""))['entity']
                # entity_type = json.loads((str(result.entities[0])).replace("'", "\""))['type']
                await self.__send_accountbalance_card(turn_context)
                await turn_context.send_activity(
                    "Also, your deposit xxxxxxxxx9243 is closed pre-maturely as per your request and amount is credited to your third party account.")
            elif intent == 'CreditCard':
                await turn_context.send_activity(
                    "Credit card xxxxxxxxxxxx7653 \n\n Current outstanding is $0.00 \n\n Card closed on 09/01/2020 \n\n Balance reward points are 514")
            elif intent == 'ServiceRequest':
                await turn_context.send_activity("Currently there are no open service requests.")
            elif query in ('xxxxxxxxx4567', 'xxxxxxxxx4566'):
                await self.__list_accountTransaction_card(turn_context)
                await self.__mobile_billDue_card(turn_context)
            elif intent == 'Billing':
                await self.__show_invoice_card(turn_context)
                await self.__show_selectAccountForBill_card(turn_context)
            elif intent == "Debit_From" and query in ("Debit from xxxxxxxxx4567"):
                await turn_context.send_activity("An OTP is sent to your registered mobile number xxxxxxxx90.")
                await turn_context.send_activity("Please enter the OTP.")
            elif query == "1234":
                await turn_context.send_activity(
                    "Transaction Successful !! Mobile bill paid for $100 from your account number xxxxxxxxx4567")
                await turn_context.send_activity(
                    "As a loyal customer, we are happy to offer you one year free VISA card which comes with $25 movie voucher.\n\n Also your balance reward points 514 from card xxxxxxxxxxxx7653 will be added to the new card.")
                await self.__show_congratulations_card(turn_context)
            elif query in ("xxxxxxxxx4566"):
                await turn_context.send_activity(
                    "Your current account xxxxxxxxx4566 is Active, but there are no transactions on it.")
            elif intent == "Debit_From" and query in ("Debit from xxxxxxxxx4566"):
                await turn_context.send_activity("Insufficient account balance. Please choose another account")
                await self.__show_selectAccountForBill_card(turn_context)
            elif intent == 'Loan':
                # entity = json.loads((str(result.entities[0])).replace("'", "\""))['entity']
                # entity_type = json.loads((str(result.entities[0])).replace("'", "\""))['type']
                await self.__loan_application_card(turn_context)
            elif intent == 'Deposits':
                # entity = json.loads((str(result.entities[0])).replace("'", "\""))['entity']
                # entity_type = json.loads((str(result.entities[0])).replace("'", "\""))['type']
                await self.__deposits_application_card(turn_context)
            elif query in ("369"):
                await self.__send_intro_card(turn_context)

    async def __send_intro_card(self, turn_context: TurnContext):

        return await turn_context.send_activity(
            MessageFactory.attachment(CardFactory.hero_card(intro_card()))
        )

    async def __login_otp_card_card(self, turn_context: TurnContext):

        return await turn_context.send_activity(
            MessageFactory.attachment(CardFactory.adaptive_card(LOGIN_OTP_CARD_CONTENT))
        )

    async def __send_accountbalance_card(self, turn_context: TurnContext):

        return await turn_context.send_activity(
            MessageFactory.attachment(CardFactory.thumbnail_card(accountbalance_card()))
        )

    async def __show_selectAccountForBill_card(self, turn_context: TurnContext):

        return await turn_context.send_activity(
            MessageFactory.attachment(CardFactory.thumbnail_card(account_SelectionForBill_card()))
        )

    async def __list_accountTransaction_card(self, turn_context: TurnContext):

        return await turn_context.send_activity(
            MessageFactory.attachment(CardFactory.adaptive_card(ADAPTIVE_CARD_CONTENT))
        )

    async def __show_congratulations_card(self, turn_context: TurnContext):

        return await turn_context.send_activity(
            MessageFactory.attachment(CardFactory.adaptive_card(CONGRATULATIONS_ADAPTIVE_CARD))
        )

    async def __show_menu_card(self, turn_context: TurnContext):

        return await turn_context.send_activity(
            MessageFactory.attachment(CardFactory.adaptive_card(INTRO_ADAPTIVE_CARD_CONTENT))
        )

    async def __show_invoice_card(self, turn_context: TurnContext):

        return await turn_context.send_activity(
            MessageFactory.attachment(CardFactory.adaptive_card(INVOICE_ADAPTIVE_CARD))
        )

    async def __mobile_billDue_card(self, turn_context: TurnContext):

        return await turn_context.send_activity(
            MessageFactory.attachment(CardFactory.thumbnail_card(mobile_billDue_card()))
        )

    async def __mobile_billPaymentConfirmation_card(self, turn_context: TurnContext):

        return await turn_context.send_activity(
            MessageFactory.attachment(CardFactory.thumbnail_card(billPaymentConfirmation_card()))
        )

    async def __mobile_confirmation_card(self, turn_context: TurnContext):

        return await turn_context.send_activity(
            MessageFactory.attachment(CardFactory.thumbnail_card(mobile_confirmation_card()))
        )

    async def __loan_application_card(self, turn_context: TurnContext):

        return await turn_context.send_activity(
            MessageFactory.attachment(CardFactory.adaptive_card(LOAN_APPLICATION_CARD))
        )

    async def __deposits_application_card(self, turn_context: TurnContext):

        return await turn_context.send_activity(
            MessageFactory.attachment(CardFactory.adaptive_card(DEPOSITS_APPLICATION_CARD))
        )
