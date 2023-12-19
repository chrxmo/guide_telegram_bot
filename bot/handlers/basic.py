from aiogram.types import Message


async def start(message: Message):
    await message.answer('Здравствуйте, вас приветствует навигатор по Екатеринбургу. Я могу помочь вам открыть для себя новые места. Расскажите, куда бы вы хотели.')


async def commands_list(message: Message):
    await message.answer('Конечно! Вот список команд:\n/restaurants - если вы хотите посетить ресторан;\n/hotels - если вы хотите посетить отель;\n'
                              '/active_relax - если вы хотите посетить место для активного отдыха;\n/passive_relax - если вы хотите посетить место для пассивного отдыха;\n'
                         '/weather - если вам интересна погода в Екатеринбурге на сегодня;\n/help - если вам снова понадобится помощь.')