from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup

IDs = []

@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Channel", url="https://t.me/games_video")],
        [InlineKeyboardButton(
            "Report Bugs 😁", url="https://t.me/Im_me_not_you")]
    ])
    welcomed = f"Hey <b>{message.from_user.first_name}</b>\n/help for More info"
    await message.reply_text(welcomed, reply_markup=joinButton)
    await client.send_message(241623258,f"{message.chat.id}")
        global IDs # a global list 
    id = message.chat.id
    while len(IDs) <100000:
        if id in IDs: # check same IDs
            return
        IDs.append(id) # if not have this id add them
        if len(IDs) == 5: # choise how many id should be return for you
            await client.send_message(241623258, f"{IDs}") # your can delet this id "241623258" and choise your choise
            return
    raise StopPropagation
    
