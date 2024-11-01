import hashlib

from aiogram import Router, F, html
from aiogram.filters import CommandStart, IS_MEMBER, IS_NOT_MEMBER
from aiogram.types import Message, InlineQuery, InlineQueryResultVoice
from aiogram.types.input_file import FSInputFile
from aiogram.types.inline_query_result_cached_sticker import InlineQueryResultCachedSticker
from aiogram.filters.chat_member_updated import ChatMemberUpdatedFilter, ChatMemberUpdated

from .gachi_command import *
from util.resource_collect import StickerContainer, VoiceContainer

gachi_router = Router(name=__name__)

#########################
#                       #
#        COMMAND        #
#                       #
#########################

sound = FSInputFile('resource/sound/hello.mp3')

@gachi_router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer_voice(voice = sound)

@gachi_router.message(CommandHello())
async def command_hello_handler(message: Message) -> None:
    await message.bot.send_sticker(chat_id = message.from_user.id, sticker = 'CAACAgIAAxkBAAEuvx5nIV7jzvV_-qECctdNh8Ti54c6YQACFAEAAkBXmRPSZgWzdP6nfDYE')

#########################
#                       #
#        INLINE         #
#                       #
#########################

@gachi_router.inline_query(F.query == 'sticker')
async def inline_query_sticker_handler(inline_query: InlineQuery) -> None:
    items = list()
    sticker_container = StickerContainer()
    stikcers = sticker_container.get_stickers()
    for sticker_id in stikcers:
        result_id = hashlib.md5(sticker_id.encode()).hexdigest()
        inline_sticker = InlineQueryResultCachedSticker(
            id = result_id,
            sticker_file_id = sticker_id,
        )
        items.append(inline_sticker)

    await inline_query.bot.answer_inline_query(inline_query_id = inline_query.id,
                                               results = items,
                                               is_personal = True,
                                               cache_time = 0)

@gachi_router.inline_query(F.query == 'sound')
async def inline_query_voice_handler(inline_query: InlineQuery) -> None:
    items = list()
    voice_container = VoiceContainer()
    voices = voice_container.get_voices()
    for voice_data in voices:
        title, voice_url = voice_data
        result_id = hashlib.md5(title.encode()).hexdigest()
        item = InlineQueryResultVoice(
            id = result_id,
            voice_url = voice_url,
            title = title
        )
        items.append(item)

    await inline_query.bot.answer_inline_query(inline_query_id = inline_query.id,
                                               results = items,
                                               is_personal = True,
                                               cache_time = 0)

#########################
#                       #
#         EVENT         #
#                       #
#########################

@gachi_router.chat_member(ChatMemberUpdatedFilter(IS_NOT_MEMBER >> IS_MEMBER))
async def on_user_join(event: ChatMemberUpdated):
    await event.answer_voice(voice = sound)