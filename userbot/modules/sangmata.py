from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot import bot, CMD_HELP
from userbot.events import register
from asyncio.exceptions import TimeoutError


@register(outgoing=True, pattern=r"^\.sa(?: |$)(.*)")
async def lastname(steal):
    if steal.fwd_from:
        return
    if not steal.reply_to_msg_id:
        await steal.edit("```Direplay Dulu Kontol!!!!!.```")
        return
    message = await steal.get_reply_message()
    chat = "@SangMataInfo_bot"
    user_id = message.sender.id
    id = f"/search_id {user_id}"
    if message.sender.bot:
        await steal.edit("```Balas Ke Pesan Pengguna Yang Sebenarnya.```")
        return
    await steal.edit("```Mampus. Ga Lama Lagi Gue Tau Nama Lo., Sabar Ye Anjing..```")
    try:
        async with bot.conversation(chat) as conv:
            try:
                msg = await conv.send_message(id)
                r = await conv.get_response()
                response = await conv.get_response()
            except YouBlockedUserError:
                await steal.reply(
                    "```Mohon Unblock @sangmatainfo_bot Dan Coba Lagi```"
                )
                return
            if r.text.startswith("Name"):
                respond = await conv.get_response()
                await steal.edit(f"`{r.message}`")
                await steal.client.delete_messages(
                    conv.chat_id, [msg.id, r.id, response.id, respond.id]
                )
                return
            if response.text.startswith("No records") or r.text.startswith(
                "No records"
            ):
                await steal.edit("```𝘠𝘌 𝘈𝘕𝘈𝘒 𝘈𝘕𝘑𝘐𝘕𝘎 𝘎𝘈 𝘗𝘌𝘙𝘕𝘈𝘏 𝘎𝘈𝘕𝘛𝘐 𝘕𝘈𝘔𝘈 . 𝘕𝘎𝘌𝘕𝘛𝘖𝘛 𝘓𝘖!```")
                await steal.client.delete_messages(
                    conv.chat_id, [msg.id, r.id, response.id]
                )
                return
            else:
                respond = await conv.get_response()
                await steal.edit(f"```{response.message}```")
            await steal.client.delete_messages(
                conv.chat_id, [msg.id, r.id, response.id, respond.id]
            )
    except TimeoutError:
        return await steal.edit("`Saya Sedang Sakit Mohon Maaf`")


CMD_HELP.update({
    "sangmata":
        "`.sa`\
          \nUsage: Mendapatkan Riwayat Nama Pengguna."
})
