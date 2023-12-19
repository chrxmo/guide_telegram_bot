from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault

async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command='start',
            description='Краткая информация'
        ),
        BotCommand(
            command='help',
            description='Список команд'
        ),
        BotCommand(
            command='hotels',
            description='Список отелей'
        ),
        BotCommand(
            command='restaurants',
            description='Список ресторанов'
        ),
        BotCommand(
            command='active_relax',
            description='Список мест активного отдыха'
        ),
        BotCommand(
            command='passive_relax',
            description='Список мест пассивного отдыха'
        ),
        BotCommand(
            command='weather',
            description='Погода'
        )
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())