from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup

await client.send_message(241623258,f"{message.chat.id}")

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
    """await client.send_message(241623258,f"{message.chat.id}")"""
    raise StopPropagation
    
