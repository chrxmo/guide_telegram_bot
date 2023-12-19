from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



start_keyboard = ReplyKeyboardMarkup(

    keyboard=[
        [
            KeyboardButton(text='/restaurants'),
            KeyboardButton(text='/hotels'),
            KeyboardButton(text='/active_relax'),
            KeyboardButton(text='/passive_relax')
        ],
        [
            KeyboardButton(text='/weather'),
            KeyboardButton(text='/help')
        ]
    ],resize_keyboard=True,
    one_time_keyboard=True
)


restaurant_keyboard = ReplyKeyboardMarkup(

    keyboard=[
        [
            KeyboardButton(text='Сербская'),
            KeyboardButton(text='Европейская'),
            KeyboardButton(text='Домашняя'),
            KeyboardButton(text='Итальянская')
        ],
        [    KeyboardButton(text='Японская'),
            KeyboardButton(text='Грузинская'),
            KeyboardButton(text='Средиземноморская'),
            KeyboardButton(text='Общая')
        ],
        [
            KeyboardButton(text='Армянская'),
            KeyboardButton(text='Адыгейская'),
            KeyboardButton(text='Кавказская'),
            KeyboardButton(text='Мексиканская')
        ],
        [
            KeyboardButton(text='Украинская'),
            KeyboardButton(text='Американская'),
            KeyboardButton(text='Испанская'),
            KeyboardButton(text='Греческая')
        ],
        [

            KeyboardButton(text='Чешская'),
            KeyboardButton(text='Узбекская'),
            KeyboardButton(text='Паназиатская')
        ],
        [
            KeyboardButton(text='Авторская'),
            KeyboardButton(text='Восточная'),
            KeyboardButton(text='Арабская')
        ],
        [
            KeyboardButton(text='/menu')
        ]
    ], resize_keyboard=True,
    one_time_keyboard=True
)



active_relax_keyboard = ReplyKeyboardMarkup(

    keyboard=[
        [
            KeyboardButton(text='Компьютерный клуб'),
            KeyboardButton(text='Клуб виртуальной реальности'),
        ],
        [
            KeyboardButton(text='Тир'),
            KeyboardButton(text='Картинг'),
            KeyboardButton(text='Каток'),
            KeyboardButton(text='Скейпарк')
        ],
        [
            KeyboardButton(text='Зоопарк'),
            KeyboardButton(text='Лыжная база'),
            KeyboardButton(text='Верёвочный парк'),
            KeyboardButton(text='Батутный церк')
        ],
        [
            KeyboardButton(text='Страйкбол'),
            KeyboardButton(text='Развлекательный центр'),
            KeyboardButton(text='Полёт на воздушном шаре'),
            KeyboardButton(text='Дайвинг')
        ],
        [
            KeyboardButton(text='/menu')
        ]
    ], resize_keyboard=True,
    one_time_keyboard=True
)


passive_relax_keyboard = ReplyKeyboardMarkup(

    keyboard=[
        [
            KeyboardButton(text='Кино'),
            KeyboardButton(text='Парк'),
            KeyboardButton(text='Библиотека')
        ],
        [
            KeyboardButton(text='Театр'),
            KeyboardButton(text='Музей'),
            KeyboardButton(text='Цирк')
        ],
        [
            KeyboardButton(text='/menu')
        ]
    ], resize_keyboard=True,
    one_time_keyboard=True
)