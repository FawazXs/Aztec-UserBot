from time import sleep
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern='^.kontol(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("`1.Kontol kamu bengkok`")
    sleep(2)
    await typew.edit("`2.Kontol Kamu Patah`")
    sleep(1)
    await typew.edit("`3.Kontol Kamu Kecil`")
    sleep(2)
    await typew.edit("`Jadi Jangan Sosoan Buat Ngentotin ANAK ORANG YE BANGSAT!`")


CMD_HELP.update({
    "kontol":
    "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.kontol`\
    \n↳ : Biasalah sadboy hikss"
    }
)
