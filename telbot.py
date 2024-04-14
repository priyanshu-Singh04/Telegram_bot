from typing import Final
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)

TOKEN: Final = "Token"

BOT_USERNAME: Final = "@botname"


#Commands

async def start_command(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello thanks for chatting with me")

async def help_command(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome to the help section")

async def some_command(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("work in progress")
    

#Responses

def handle_response(text: str)-> str:

    ptext : str= text.lower()
    if 'hello' in ptext:
        return "hey"
    
    if 'how are you' in ptext:
        return "fine"
    
    if 'i love python' in ptext:
        return "mee tooo"
    
    return "Unknown Command"
    
async def handle_message(update:Update,context:ContextTypes.DEFAULT_TYPE):
    message_type : str = update.message.chat.type
    text : str = update.message.text

    print(f'user({update.message.chat.id})in {message_type}:"{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text:str = text.replace(BOT_USERNAME,"").strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response:str = handle_response(text)

    print("Bot: ",response)
    await update.message.reply_text(response)

async def error(update:Update,context:ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} Error {context.error}')

if __name__ == '__main__':
    print("Starting Bot.....")
    app = Application.builder().token(TOKEN).build()


    app.add_handler(CommandHandler('start',start_command))
    app.add_handler(CommandHandler('help',help_command))
    app.add_handler(CommandHandler('some',some_command))


    app.add_handler(MessageHandler(filters.TEXT,handle_message))


    app.add_error_handler(error)

    print("Polling.......")
    app.run_polling(poll_interval=3)
