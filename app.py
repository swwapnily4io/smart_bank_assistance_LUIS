from flask import Flask, request, Response
from botbuilder.core import BotFrameworkAdapter, BotFrameworkAdapterSettings, ConversationState,MemoryStorage
from botbuilder.schema import Activity
import asyncio
from luis.luisApp import LuisConnect
import os
from logger.logger import Log
from botbuilder.core import (
    BotFrameworkAdapter,
    BotFrameworkAdapterSettings,
    MemoryStorage,
    TurnContext,
    UserState,
)

import sys
import traceback
from datetime import datetime
from aiohttp import web
from aiohttp.web import Request, Response, json_response
from http import HTTPStatus
from botbuilder.core.integration import aiohttp_error_middleware
from botbuilder.schema import Activity, ActivityTypes

APP = Flask(__name__)
loop = asyncio.get_event_loop()

#added change
# async def fetch(url):
#     async with aiohttp.ClientSession() as session, async_timeout.timeout(10):
#         async with session.get(url) as response:
#             return await response.text()

# bot_settings = BotFrameworkAdapterSettings("", "")
# bot_adapter = BotFrameworkAdapter(bot_settings)

#CON_MEMORY = ConversationState(MemoryStorage())
# MEMORY = MemoryStorage()
# USER_STATE = UserState(MEMORY)
# luis_bot_dialog = LuisConnect(USER_STATE)

# bot_settings = BotFrameworkAdapterSettings("", "")
# bot_adapter = BotFrameworkAdapter(bot_settings)


# @app.route("/api/messages", methods=["POST"])
# def messages():
#     if "application/json" in request.headers["content-type"]:
#         log=Log()
#         request_body = request.json
#         user_says = Activity().deserialize(request_body)
#         log.write_log(sessionID='session1',log_message="user says: "+str(user_says))
#         authorization_header = (request.headers["Authorization"] if "Authorization" in request.headers else "")
#
#         async def call_user_fun(turncontext):
#             await luis_bot_dialog.on_turn(turncontext)
#
#         task = loop.create_task(
#             bot_adapter.process_activity(user_says, authorization_header, call_user_fun)
#         )
#         loop.run_until_complete(task)
#         return ""
#     else:
#         return Response(status=406)  # status for Not Acceptable


SETTINGS = BotFrameworkAdapterSettings("9c7fe1a9-6dff-4a18-bb7f-7c8acc78b57c", "111112222233333444445555566666")
ADAPTER = BotFrameworkAdapter(SETTINGS)


async def on_error(context: TurnContext, error: Exception):
    # This check writes out errors to console log .vs. app insights.
    # NOTE: In production environment, you should consider logging this to Azure
    #       application insights.
    print(f"\n [on_turn_error] unhandled error: {error}", file=sys.stderr)
    traceback.print_exc()

    # Send a message to the user
    await context.send_activity("The bot encountered an error or bug.")
    await context.send_activity(
        "To continue to run this bot, please fix the bot source code."
    )
    # Send a trace activity if we're talking to the Bot Framework Emulator
    if context.activity.channel_id == "emulator":
        # Create a trace activity that contains the error object
        trace_activity = Activity(
            label="TurnError",
            name="on_turn_error Trace",
            timestamp=datetime.utcnow(),
            type=ActivityTypes.trace,
            value=f"{error}",
            value_type="https://www.botframework.com/schemas/error",
        )
        # Send a trace activity, which will be displayed in Bot Framework Emulator
        await context.send_activity(trace_activity)

ADAPTER.on_turn_error = on_error
MEMORY = MemoryStorage()
USER_STATE = UserState(MEMORY)
luis_bot_dialog = LuisConnect(USER_STATE)

async def messages(req: Request) -> Response:
    # Main bot message handler.
    if "application/json" in req.headers["Content-Type"]:
        body = await req.json()
    else:
        return Response(status=HTTPStatus.UNSUPPORTED_MEDIA_TYPE)

    activity = Activity().deserialize(body)
    auth_header = req.headers["Authorization"] if "Authorization" in req.headers else ""

    response = await ADAPTER.process_activity(activity, auth_header, luis_bot_dialog.on_turn)
    if response:
        return json_response(data=response.body, status=response.status)
    return Response(status=HTTPStatus.OK)

APP = web.Application(middlewares=[aiohttp_error_middleware])
APP.router.add_post("/api/messages", messages)


if __name__ == '__main__':
    #app.run(port= 3978)
    #app.run()
    web.run_app(APP,  host="localhost", port=5000)
