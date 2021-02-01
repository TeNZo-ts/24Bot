# -*- coding: utf8 -*-
# Импорт модулей
import config
import logging
import asyncio
from datetime import datetime
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import Bot, Dispatcher, executor, types

# Уровень логов
logging.basicConfig(level=logging.INFO)
# Токен бота
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

# Основное меню  
button_back = KeyboardButton('Назад')
# Main KeyBoards
button_daryn = KeyboardButton('Daryn Online')
button_lyceum = KeyboardButton('Lyceum')
button_info = KeyboardButton('Info')
# Classes
button_10a = KeyboardButton('10(a)')
button_10ae = KeyboardButton('10(ae)')
button_10b = KeyboardButton('10(b)')
button_10v = KeyboardButton('10(v)')
# Timetable 10(a)
button_timetable_10a = KeyboardButton('Расписание 10(a)')
# Week 10(a)
button_monday_10a = KeyboardButton('Понедельник 10(a)')
button_tuesday_10a = KeyboardButton('Вторник 10(a)')
button_wednesday_10a = KeyboardButton('Среда 10(a)')
button_thursday_10a = KeyboardButton('Четверг 10(a)')
button_friday_10a = KeyboardButton('Пятница 10(a)')
# Timetable 10(ae)
button_timetable_10ae = KeyboardButton('Расписание 10(ae)')
# Week 10(ae)
button_monday_10ae = KeyboardButton('Понедельник 10(ae)')
button_tuesday_10ae = KeyboardButton('Вторник 10(ae)')
button_wednesday_10ae = KeyboardButton('Среда 10(ae)')
button_thursday_10ae = KeyboardButton('Четверг 10(ae)')
button_friday_10ae = KeyboardButton('Пятница 10(ae)')
# Lessons
infor = KeyboardButton('Информатика')
physEng = KeyboardButton('Физика (English)')
phystrain = KeyboardButton('Физкультура')
geo_phys = KeyboardButton('География/Физика')
kz = KeyboardButton('Казахский язык')
bio = KeyboardButton('Биология')
law_bas1 = KeyboardButton('Основы права (1Г)')
kz_lit = KeyboardButton('Казахская литература')
voen = KeyboardButton('Военная подготовка')
class_hour = KeyboardButton('Классный час')
algebra = KeyboardButton('Алгебра')
mir_ist = KeyboardButton('Всемирная история')
phys_geo = KeyboardButton('Физика/География')
geom = KeyboardButton('Геометерия')
eng = KeyboardButton('English')
eco = KeyboardButton('Экономика')
chem = KeyboardButton('Химия')
rus_lit = KeyboardButton('Русский язык и Литература')
ling = KeyboardButton('Лингвистика')
abai = KeyboardButton('Абайтану')
law_bas2 = KeyboardButton('Основы права (2Г)')
audarma = KeyboardButton('Аударма')
samo_pozn = KeyboardButton('Самопознание')
ist_kz = KeyboardButton('История Казахстана')
chem_bio = KeyboardButton('Химия/Биология')
mir_ist1 = KeyboardButton('Всемирная история (1Г)')
geo = KeyboardButton('География')
law_bas = KeyboardButton('Основы права')
chemEng = KeyboardButton('Химия (English)')
phys = KeyboardButton('Физика')
mir_ist2 = KeyboardButton('Всемирная история (2Г)')
# Teachers 
Aizada_A = KeyboardButton('Айзада Адильханкызы')
Gulmira_A = KeyboardButton('Гульмира Апарбаева')
Aigerim_E = KeyboardButton('Айгерим Еркинбекова')
Maulet_K = KeyboardButton('Маулет Кисса')
Bakhyt_N = KeyboardButton('Бакыт Нуркожаева')
Murat_B = KeyboardButton('Мурат Буланов')
Asem_B = KeyboardButton('Асем Буланова')
Asel_M = KeyboardButton('Асель Муханова')
Kyrmyzy_N = KeyboardButton('Кырмызы Нурахметова')
Gulbarshin_D = KeyboardButton('Гульбаршын Долаева')
Zhanna_B = KeyboardButton('Жанна Баелова')
Zhanna_Z = KeyboardButton('Жанна Жунисбекова')
Zhadyra_B = KeyboardButton('Жадыра Бекбаева')
Gulzhat_D = KeyboardButton('Гульшат Д.')
Zharkyn = KeyboardButton('Жаркын Сансызбай')
Nurlan_T = KeyboardButton('Нурлан Токтарбекулы')
Zialy_A = KeyboardButton('Зиалы Алтаевна')
Kamida_T = KeyboardButton('Камида Тулеметова')
Tuganai_A = KeyboardButton('Туганай Аяпова')
# Предметы для Daryn (English letters: a,e,o,c,x)
button_daryn_1 = KeyboardButton('Гeoмeтрия')
button_daryn_2 = KeyboardButton('Физикa')
button_daryn_3 = KeyboardButton('Вceмирнaя иcтoрия')
button_daryn_4 = KeyboardButton('Иcтoрия Кaзaxcтaнa')
button_daryn_5 = KeyboardButton('Кaзaxcкий язык')
button_daryn_6 = KeyboardButton('Кaзaxcкaя литeрaтурa')
button_daryn_7 = KeyboardButton('Xимия')
button_daryn_8 = KeyboardButton('Инфoрмaтикa')
button_daryn_9 = KeyboardButton('Руccкий язык')
button_daryn_10 = KeyboardButton('Руcкaя литeрaтурa')
button_daryn_11 = KeyboardButton('Ocнoвы прaвa')
button_daryn_12 = KeyboardButton('Гeoгрaфия')
# История Казахстана
answer_ist_kz_1 = KeyboardButton('1. Орталық Азия: ұғымының тарихи')
answer_ist_kz_2 = KeyboardButton('2. Орталық Азияның дәстүрлі')
answer_ist_kz_3 = KeyboardButton('3. Орталық Азия өркениеттерінің ежелгі ошақтары')
answer_ist_kz_4 = KeyboardButton('4. Ұлы Дала: тарихи-географиялық сипаттамасы')
answer_ist_kz_5 = KeyboardButton('5. Ұлы дала өркениетінің қайнар көзі ')
answer_ist_kz_6 = KeyboardButton('6. Ерте көшпенділер дәуіріндегі')
answer_ist_kz_7 = KeyboardButton('7. Әлемдік мәдениеттің дамуына')
answer_ist_kz_8 = KeyboardButton('8. Қазақстандағы этногенез')
answer_ist_kz_9 = KeyboardButton('9. Қазақтардың ру-тайпалық құрылымы қалыптасуы')
answer_ist_kz_10 = KeyboardButton('10. Қазақтардың ру-тайпалық құрылымының')
answer_ist_kz_11 = KeyboardButton('11. Дәстүрлі қазақ қоғамының әлеуметтік жіктелуінің ерекшеліктері')
answer_ist_kz_12 = KeyboardButton('12. Қазақстан аумағындағы ерте мемлекеттердің')
# Основы права
answer_law_bas_10 = KeyboardButton('10. Қазақстан Республикасы Конститутциялық кұқығының институттары')
answer_law_bas_11 = KeyboardButton('11. Қазақстан Республикасындағы мемлекеттік басқарудың құқықтық реттелуі')
answer_law_bas_12 = KeyboardButton('12. Экологиялық құқықтың құқықтық реттелу түсінігі мен нысаны')
answer_law_bas_13 = KeyboardButton('13. Қылмыстық кодекс қылмыстық құқықтың негізгі қайнар көзі ретінде')
answer_law_bas_14 = KeyboardButton('14. Қылмыстық құқық бұзушылық және қылмыстық жауапкершілікке тартылатын тұлғалар')
answer_law_bas_15 = KeyboardButton('15. Қылмыстық жаза түсінігі және одан босату шарттары')
answer_law_bas_16 = KeyboardButton('16. Қазақстан Республикасындағы сыбайлас жемқорлыққа қарсы күреске бағытталған құқықтық және саяси актілер')
answer_law_bas_17 = KeyboardButton('17. Қазақстан Республикасындағы сыбайлас жемқорлыққа қарсы іс-шаралар жүйесі.Сыбайлас Жемқорлыққа қарсы мәдениет.')
answer_law_bas_18 = KeyboardButton('18. Азаматтық құқықтың принциптері мен субъектілері. Азаматтық құқықтың объектілері')
answer_law_bas_19 = KeyboardButton('19. Мәміле түсінігі және оның түрлері')
answer_law_bas_20 = KeyboardButton('20. Меншік құқығы түсінігі және оның қорғалуы')
answer_law_bas_21 = KeyboardButton('21. Міндеттемелік құқық')
answer_law_bas_22 = KeyboardButton('22. Қазақстан Республикасында тұтынушылар құқықтарының заңды түрде бекітілуі')
answer_law_bas_23 = KeyboardButton('23. Қазақстан Республикасындағы отбасы құқығының қайнар көздері. Қазақстан Республикасында отбасылық қарым-қатынастардың құқықтық реттелуі')

# Main
markup_back = ReplyKeyboardMarkup(resize_keyboard=True).add(button_back)
markup_menu = ReplyKeyboardMarkup(resize_keyboard=True).row(button_lyceum, button_daryn).add(button_info)
markup_DOsub = ReplyKeyboardMarkup(resize_keyboard=True).add(button_back)
# Classes
markup_classes = ReplyKeyboardMarkup(resize_keyboard=True).add(button_back).row(button_10a, button_10ae).row(button_10b, button_10v)
# Class 10a
markup_week_10a = ReplyKeyboardMarkup(resize_keyboard=True).row(button_monday_10a, button_tuesday_10a).row(button_wednesday_10a, button_thursday_10a, button_friday_10a).row(button_timetable_10a, button_back)
markup_mon_10a = ReplyKeyboardMarkup(resize_keyboard=True).row(eng, ist_kz).add(abai).row(phystrain, chem_bio, mir_ist1).row(button_timetable_10a, button_back)
markup_tue_10a = ReplyKeyboardMarkup(resize_keyboard=True).row(geo, kz_lit).add(voen).row(law_bas, chemEng, audarma).row(button_timetable_10a, button_back)
markup_wed_10a =ReplyKeyboardMarkup(resize_keyboard=True).row(algebra, infor, phys).add(chemEng).row(button_timetable_10a, button_back)
markup_thu_10a = ReplyKeyboardMarkup(resize_keyboard=True).row(rus_lit, kz).row(geom, ling, chem_bio).row(button_timetable_10a, button_back)
markup_fri_10a = ReplyKeyboardMarkup(resize_keyboard=True).row(algebra, phystrain).add(class_hour).row(samo_pozn, eco, mir_ist2).row(button_timetable_10a, button_back)
# Class 10ae
markup_week_10ae = ReplyKeyboardMarkup(resize_keyboard=True).row(button_monday_10ae, button_tuesday_10ae).row(button_wednesday_10ae, button_thursday_10ae, button_friday_10ae).row(button_timetable_10ae, button_back)
markup_mon_10ae = ReplyKeyboardMarkup(resize_keyboard=True).row(infor, physEng, phystrain).row(geo_phys).row(kz, bio, law_bas1).row(button_timetable_10ae, button_back)
markup_tue_10ae = ReplyKeyboardMarkup(resize_keyboard=True).row(kz_lit, voen, class_hour).row(algebra, mir_ist).row(button_timetable_10ae, button_back)
markup_wed_10ae =ReplyKeyboardMarkup(resize_keyboard=True).row(phys_geo, geom, eng).add(eco).row(button_timetable_10ae, button_back)
markup_thu_10ae = ReplyKeyboardMarkup(resize_keyboard=True).row(chem, rus_lit).add(ling).row(abai, phystrain, law_bas2).row(button_timetable_10ae, button_back)
markup_fri_10ae = ReplyKeyboardMarkup(resize_keyboard=True).row(physEng, audarma, geo_phys).row(phys_geo, samo_pozn, ist_kz).add(algebra).row(button_timetable_10ae, button_back)
# Groups 
markup_infor = ReplyKeyboardMarkup(resize_keyboard=True).row(Aizada_A, Gulmira_A)
markup_geo_phys = ReplyKeyboardMarkup(resize_keyboard=True).row(Aigerim_E, Maulet_K)
markup_algebra = ReplyKeyboardMarkup(resize_keyboard=True).row(Murat_B, Asem_B)
markup_phys_geo = ReplyKeyboardMarkup(resize_keyboard=True).row(Maulet_K, Aigerim_E)
markup_geom = ReplyKeyboardMarkup(resize_keyboard=True).row(Murat_B, Asem_B)
markup_english = ReplyKeyboardMarkup(resize_keyboard=True).row(Nurlan_T, Gulzhat_D).row(Asel_M, Kyrmyzy_N)
markup_rus_lit = ReplyKeyboardMarkup(resize_keyboard=True).row(Zhanna_B, Zhanna_Z)
markup_ling = ReplyKeyboardMarkup(resize_keyboard=True).row(Zhadyra_B, Kyrmyzy_N)
markup_audarma = ReplyKeyboardMarkup(resize_keyboard=True).row(Gulzhat_D, Zharkyn)
markup_kz = ReplyKeyboardMarkup(resize_keyboard=True).add(Tuganai_A).add(Bakhyt_N)
# Daryn Online
markup_DO = ReplyKeyboardMarkup(resize_keyboard=True).add(button_back).row(button_daryn_1, button_daryn_2).row(button_daryn_3, button_daryn_4, button_daryn_5).row(button_daryn_6, button_daryn_7).row(button_daryn_8, button_daryn_9, button_daryn_10).row(button_daryn_11, button_daryn_12)
markup_ist_kz = ReplyKeyboardMarkup(resize_keyboard=True).add(answer_ist_kz_1).add(answer_ist_kz_2).add(answer_ist_kz_3).add(answer_ist_kz_4).add(answer_ist_kz_5).add(answer_ist_kz_6).add(answer_ist_kz_7).add(answer_ist_kz_8).add(answer_ist_kz_9).add(answer_ist_kz_10).add(answer_ist_kz_11).add(answer_ist_kz_12)
markup_prava = ReplyKeyboardMarkup(resize_keyboard=True).add(answer_law_bas_10).add(answer_law_bas_11).add(answer_law_bas_12).add(answer_law_bas_13).add(answer_law_bas_14).add(answer_law_bas_15).add(answer_law_bas_16).add(answer_law_bas_17).add(answer_law_bas_18).add(answer_law_bas_19).add(answer_law_bas_20).add(answer_law_bas_21).add(answer_law_bas_22).add(answer_law_bas_23)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
	# Welcome!:)
	start = open('symbol.jpg', "rb")
	await bot.send_photo(message.chat.id, start, '🔔Добро пожаловать!🔔\nЯ бот🤖, выполняю команды моих разработчиков.\nМоя задача сэкономить Ваше время и оказать незаменимую помощь!\n\nПриятного пользования!💫', reply_markup=markup_menu)

@dp.message_handler(content_types=['text'])
async def menu(message: types.Message):
	# Commands
	if message.text == '/open':
		await message.reply('Menu opened\n\nКоманды:\n/start - Запустить бота\n/open - Открыть меню\n/close - Закрыть меню', reply_markup=markup_menu)
	elif message.text == '/close':
		await message.reply('Menu closed\n\nКоманды:\n/start - Запустить бота\n/open - Открыть меню\n/close - Закрыть меню', reply_markup=ReplyKeyboardRemove())
	# Назад
	elif message.text == 'Назад':
		await message.reply('🔙', reply_markup=markup_menu)
	# Daryn Online
	elif message.text == 'Daryn Online': 
		await message.reply('Введите код доступа:\n\nЕсли у вас нет кода доступа, обратитесь к основателям либо покиньте раздел.', reply_markup=markup_DOsub)
	# Info
	elif message.text == 'Info': 
		await message.reply('Привет👋 Я бот🤖\nМои разработчики усердно развивают проект с двух сторон и на достигнутом останавливаться не собираються👌\nМы будем рады принять любую помощь в развитии проекта.\nВ случаи отсутствия Вашего класса, наберитесь терпения и вскоре мы его добавим.\n\nОснователи - @TeNZo_ts, @Kezuh\n\nКоманды:\n/start - Запустить бота\n/open - Открыть меню\n/close - Закрыть меню\n\nНа данный момент доступно:⤵️\n10(a) класс: Понедельник, Вторник\n10(ае) класс: FULL\nDaryn Online\n\nОбновления:\nПодключили бота на хостинг✅\nБот работает стабильно и доступен 24/7✅\nРаботаем над 10(a) классом👍\nРаботаем над Daryn Online👍\n\nОбнаружили ошибку либо имеются пожелания и идеи по развитию проекта? Будем рады выслушать Ваше предложение/критику - @TeNZo_ts\n\nБот обновляется ежедневно и становиться лучше каждым днем!🤟', reply_markup=markup_back)
	# Lyceum
	elif message.text == 'Lyceum':
		await message.reply('➡️', reply_markup=markup_classes)
	# CLASS 10a
	elif message.text == '10(a)':
		tt10a_1 = open('tt10a.png', "rb")
		await bot.send_photo(message.chat.id, tt10a_1, '⚡️Ниже, выберите день недели, для получения идентификатора Zoom⤵️', reply_markup=markup_week_10a)
	elif message.text == 'Расписание 10(a)':
		tt10a_2 = open('tt10a.png', "rb")
		await bot.send_photo(message.chat.id, tt10a_2, '➡️', reply_markup=markup_week_10a)
	# Monday
	elif message.text == 'Понедельник 10(a)':
		await message.reply('➡️', reply_markup=markup_mon_10a)
	# Tuesday
	elif message.text == 'Вторник 10(a)':
		await message.reply('➡️', reply_markup=markup_tue_10a)
	elif message.text == 'География':
		await message.answer('География\nАйгерим Еркинбекова -\nПодключиться:\nhttps://us04web.zoom.us/j/6281342021?pwd=S3lZdERoT3lmVVJKeDJpN1djbE9oQT09\nИдентификатор: 628 134 2021\nКод:897756', reply_markup=markup_classes)
	elif message.text == 'Основы права':
		await message.answer('Основы права\nРысхан Байшыгашова -\nПодключиться:\nhttps://us04web.zoom.us/j/4182789875?pwd=S3Z2UG9taUlaajRVV05IUktHblMzdz09\nИдентификатор: 418 278 9875\nКод: 029958', reply_markup=markup_classes)
	elif message.text == 'Химия (English)':
		await message.answer('Химия\nЖаркын -\nПодключиться:\nnone\nИдентификатор: none\nКод: none', reply_markup=markup_classes)
	# Class 10ae
	elif message.text == '10(ae)':
		tt10ae_1 = open('tt10ae.jpg', "rb")
		await bot.send_photo(message.chat.id, tt10ae_1, '⚡️Ниже, выберите день недели, для получения идентификатора Zoom⤵️', reply_markup=markup_week_10ae)
	elif message.text == 'Расписание 10(ae)':
		tt10ae_2 = open('tt10ae.jpg', "rb")
		await bot.send_photo(message.chat.id, tt10ae_2, '➡️', reply_markup=markup_week_10ae)
	# Monday
	elif message.text == 'Понедельник 10(ae)':
		await message.reply('➡️', reply_markup=markup_mon_10ae)
	elif message.text == 'Информатика':
		await message.reply('Выберите своего учителя➡️', reply_markup=markup_infor)
	elif message.text == 'Физика (English)':
		await message.answer('Физика\nКуаныш Жакпаев -\nПодключиться:\nhttps://us04web.zoom.us/j/5883286704?pwd=dG9sUkVkazFTNUEvTDJCcUNKNEUrQT09\nИдентификатор: 588 328 6704\nКод: 24', reply_markup=markup_classes)
	elif message.text == 'Физкультура':
		await message.answer('Физкультура\nАзат Жақияұлы -\nПодключиться:https://us05web.zoom.us/j/9940612911?pwd=djNmdktPY0oyc2Iva2w0aXFBOXc2UT09\nИдентификатор: 994 061 2911\nКод: 24', reply_markup=markup_classes)
	elif message.text == 'География/Физика':
		await message.reply('Выберите своего учителя➡️', reply_markup=markup_geo_phys)
	elif message.text == 'Казахский язык':
		await message.reply('Выберите своего учителя➡️', reply_markup=markup_kz)
	elif message.text == 'Биология':
		await message.answer('Биология\nДаулен Муталиев -\nПодключиться:\nhttps://us04web.zoom.us/j/5953647658?pwd=SFlWOU9YVXlnc1h4MXFYcUt3K3JyUT09\nИдентификатор: 595 364 7658\nКод: 434547', reply_markup=markup_classes)
	elif message.text == 'Основы права (1Г)':
		await message.answer('Основы права\nРысхан Байшыгашова -\nПодключиться:\nhttps://us04web.zoom.us/j/4182789875?pwd=S3Z2UG9taUlaajRVV05IUktHblMzdz09\nИдентификатор: 418 278 9875\nКод: 029958', reply_markup=markup_classes)
	# Tuesday
	elif message.text == 'Вторник 10(ae)':
		await message.reply('➡️', reply_markup=markup_tue_10ae)
	elif message.text == 'Казахская литература':
		await message.reply('Выберите своего учителя➡️', reply_markup=markup_kz)
	elif message.text == 'Военная подготовка':
		await message.answer('Военная подготовка\nАзат Жакиянов -\nПодключиться:\nhttps://us04web.zoom.us/j/4620412083?pwd=amV6eExyYUEzOXVUaGhYYURVcnVMQT09\nИдентификатор: 462 041 2083\nКод: 24', reply_markup=markup_classes)
	elif message.text == 'Классный час':
		await message.answer('Классный час\nЖанна Баелова -\nПодключиться:\nhttps://us04web.zoom.us/j/9712435106?pwd=UlIwQ1B0b0M4MTJmVVFhSnMyNzBZQT09\nИдентификатор: 971 243 5106\nКод: 046044', reply_markup=markup_classes)	
	elif message.text == 'Алгебра':
		await message.reply('Выберите своего учителя➡️', reply_markup=markup_algebra)
	elif message.text == 'Всемирная история':
		await message.answer('Всемирная история\nРысхан Байшыгашова\nПодключиться:\nhttps://us04web.zoom.us/j/4182789875?pwd=S3Z2UG9taUlaajRVV05IUktHblMzdz09\nИдентификатор: 418 278 9875\nКод: 029958', reply_markup=markup_classes)
	# Wednesday 
	elif message.text == 'Среда 10(ae)':
		await message.reply('➡️', reply_markup=markup_wed_10ae)
	elif message.text == 'Физика/География':
		await message.reply('Выберите своего учителя➡️', reply_markup=markup_phys_geo)
	elif message.text == 'Геометерия':
		await message.reply('Выберите своего учителя➡️', reply_markup=markup_geom)
	elif message.text == 'English':
		await message.reply('Выберите своего учителя➡️', reply_markup=markup_english)
	elif message.text == 'Экономика':
		await message.answer('Экономика\nГульбаршын Долаева -\nПодключиться:\nhttps://us04web.zoom.us/j/6659425539?pwd=ak9PdEJqZnlhYkp0cTc5VkxRQW13UT09\nИдентификатор: 665 942 5539\nКод: 99999', reply_markup=markup_classes)
	# Thursday
	elif message.text == 'Четверг 10(ae)':
		await message.reply('➡️', reply_markup=markup_thu_10ae)
	elif message.text == 'Химия':
		await message.answer('Химия\nСаулетхан Амир -\nПодключиться:\nnone\nИдентификатор: none\nКод: none', reply_markup=markup_classes)
	elif message.text == 'Русский язык и Литература':
		await message.reply('Выберите своего учителя➡️', reply_markup=markup_rus_lit)
	elif message.text == 'Лингвистика':	
		await message.reply('Выберите своего учителя➡️', reply_markup=markup_ling)
	elif message.text == 'Абайтану':
		await message.reply('Выберите своего учителя➡️', reply_markup=markup_kz)
	elif message.text == 'Основы права (2Г)':
		await message.answer('Основы права\nРысхан Байшыгашова -\nПодключиться:\nhttps://us04web.zoom.us/j/4182789875?pwd=S3Z2UG9taUlaajRVV05IUktHblMzdz09\nИдентификатор: 418 278 9875\nКод: 029958', reply_markup=markup_classes)
	# Friday
	elif message.text == 'Пятница 10(ae)':
		await message.reply('➡️', reply_markup=markup_fri_10ae)
	elif message.text == 'Аударма':
		await message.reply('Выберите своего учителя➡️', reply_markup=markup_audarma)
	elif message.text == 'Самопознание':
		await message.answer('Самопознание\nСымбат Майкен -\nПодключиться:\nhttps://us04web.zoom.us/j/7661181251?pwd=RnpKN2RtUS9GSmw1VUNiMWZBUC9jUT09\nИдентификатор: 766 118 1251\nКод: FT6KE5', reply_markup=markup_classes)
	elif message.text == 'История Казахстана':
		await message.answer('История Казахстана\nРысхан Байшыгашова -\nПодключиться:\nhttps://us04web.zoom.us/j/4182789875?pwd=S3Z2UG9taUlaajRVV05IUktHblMzdz09\nИдентификатор: 418 278 9875\nКод: 029958', reply_markup=markup_classes)
	# CLASS b
	elif message.text == '10(b)':
		await message.reply('На данный момент доступны классы "10(a)" и "10(ae)". Разработка уже в процессе, ждите обновлений!➡️', reply_markup=markup_menu)
	# CLASS v
	elif message.text == '10(v)':
		await message.reply('На данный момент доступны классы "10(a)" и "10(ae)". Разработка уже в процессе, ждите обновлений!➡️', reply_markup=markup_menu)
	# Teachers
	elif message.text == 'Айзада Адильханкызы':
		await message.answer('Информатика\nАйазада Адилханова -\nПодключиться:\nhttps://us04web.zoom.us/j/6739738314?pwd=UlQzc2hxcVR4QWlnMFQ3YTVnSjcxQT09\nИдентификатор: 673 973 8314\nКод: 112076', reply_markup=markup_classes)
	elif message.text == 'Гульмира Апарбаева':
		await message.answer('Информатика\nГульмира Апарбаева -\nПодключиться:\nhttps://us04web.zoom.us/j/6671115307?pwd=K1JsQ3ZPczJVRHRNVGgrTlF6VVhiUT09\nИдентификатор: 667 111 5307\nКод: 551171', reply_markup=markup_classes)
	elif message.text == 'Айгерим Еркинбекова':
		await message.answer('География\nАйгерим Еркинбекова -\nПодключиться:\nhttps://us04web.zoom.us/j/6281342021?pwd=S3lZdERoT3lmVVJKeDJpN1djbE9oQT09\nИдентификатор: 628 134 2021\nКод:897756', reply_markup=markup_classes)
	elif message.text == 'Маулет Кисса':
		await message.answer('Физика\nМаулет Кисса -\nПодключиться:\nhttps://us04web.zoom.us/j/5261561075?pwd=SUdYcXZoalFEVkhDV0RFN0U0NjZ1QT09\nИдентификатор: 526 156 1075\nКод: 172522', reply_markup=markup_classes)
	elif message.text == 'Бакыт Нуркожаева':
		await message.answer('Казахский язык\nБакыт Нуркожаева -\nПодключиться:\nhttps://us04web.zoom.us/j/4865772347?pwd=SWhwNHNjRWE1TTlwRjJvZjFpNnphQT09\nИдентификатор: 486 577 2347\nКод: jBdv6e', reply_markup=markup_classes)
	elif message.text == 'Мурат Буланов':	
		await message.answer('Алгебра\nМурат Буланов -\nПодключиться:\nhttps://us04web.zoom.us/j/5803259738?pwd=QUphOEhPNlgzSmxMajkxV3VrbkhrZz09\nИдентификатор: 580 325 9738\nКод: 123456', reply_markup=markup_classes)
	elif message.text == 'Асем Буланова':
		await message.answer('Алгебра\nАсем Буланова -\nПодключиться:\nhttps://us02web.zoom.us/j/2147576084?pwd=c3A0WjJqMHA5UjdlbjRYcVJ5ZGtqUT09\nИдентификатор: 214 757 6084\nКод: 24', reply_markup=markup_classes)
	elif message.text == 'Асель Муханова':	
		await message.answer('English\nАсель Муханова -\nПодключиться:\nhttps://us04web.zoom.us/j/3705039375?pwd=dnl3SUpDTGVBR0NSYWhUVXl4dEtsZz09\nИдентификатор: 370 503 9375\nКод: 464196', reply_markup=markup_classes)
	elif message.text == 'Кырмызы Нурахметова':	
		await message.answer('English\nКырмызы Нурахметова -\nПодключиться:\nhttps://us04web.zoom.us/j/3705039375?pwd=dnl3SUpDTGVBR0NSYWhUVXl4dEtsZz09\nИдентификатор: 370 503 9375\nКод: 464196', reply_markup=markup_classes)
	elif message.text == 'Жанна Баелова':
		await message.answer('Русский язык и Литература\nЖанна Баелова -\nПодключиться:\nhttps://us04web.zoom.us/j/9712435106?pwd=UlIwQ1B0b0M4MTJmVVFhSnMyNzBZQT09\nИдентификатор: 971 243 5106\nКод: 046044', reply_markup=markup_classes)
	elif message.text == 'Жанна Жунисбекова':
		await message.answer('Русский язык и Литература\nЖанна Жунисбекова -\nПодключиться:\nhttps://us04web.zoom.us/j/3494752418?pwd=ZVZwYm5paUxoS3ZrNytUc3d5RWhYdz09\nИдентификатор: 349 475 2418\nКод: 453743', reply_markup=markup_classes)
	elif message.text == 'Жадыра Бекбаева':	
		await message.answer('Лингвистика\nЖадыра Бекбаева -\nПодключиться:\nhttps://us04web.zoom.us/j/8288810097?pwd=ellzVFpzVlFLT0JPU3ZOZ3A4WTE0QT09\nИдентификатор: 828 881 0097\nКод: 12345', reply_markup=markup_classes)
	elif message.text == 'Гульшат Д.':
		await message.answer('Аударма\nГульшат Д. -\nПодключиться:\nhttps://us04web.zoom.us/j/6776997623?pwd=eWhSSUE5TlFGc2hmWXpsU0poSDFsZz09\nИдентификатор: 677 699 7623\nКод: 192105', reply_markup=markup_classes)
	elif message.text == 'Жаркын Сансызбай':
		await message.answer('Аударма\nЖаркын -\nПодключиться:\nnone\nИдентификатор: none\nКод: none', reply_markup=markup_classes)
	elif message.text == 'Нурлан Токтарбекулы':
		await message.answer('English\nНурлан Токтарбекулы -\nПодключиться:\nhttps://us04web.zoom.us/j/7461456484?pwd=NW9Ob1VPNkw1ZzdUaTgzUXFjeWZtQT09\nИдентификатор: 746 145 6484\nКод: 1995', reply_markup=markup_classes)
	elif message.text == 'Зиалы Алтаевна':
		await message.answer('Алгебра\nЗиалы Алтаевна -\nПодключиться:\nhttps://us04web.zoom.us/j/5919934745?pwd=TmVnTnNyRUxuUVVjcTBhZHFXWFUyZz09\nИдентификатор: 591 993 4745\nКод: 2020', reply_markup=markup_classes)
	elif message.text == 'Камида Тулеметова':
		await message.answer('Алгебра\nКамида Тулеметова -\nПодключиться:\nhttps://us04web.zoom.us/j/7461456484?pwd=NW9Ob1VPNkw1ZzdUaTgzUXFjeWZtQT09\nИдентификатор: 268 124 4460\nКод: 144475', reply_markup=markup_classes)
	elif message.text == 'Туганай Аяпова':
		await message.answer('Казахский язык\nТуганай Аяпова -\nПодключиться:\nhttps://us04web.zoom.us/j/9203579917?pwd=LzhINlRCbEk5eGs2NVFNYlVaQjlUQT09\nИдентификатор: 920 357 9917\nКод: 158354', reply_markup=markup_classes)
	# Daryn
	elif message.text == '2San':
		await message.reply('Доступ получен✅\n\nВ наличии -\nИстория Казахстана: 1-12 тем\nОсновы права: 10-23 тем \n\nВыберите предмет:', reply_markup=markup_DO)
	# ist_kz
	elif message.text == 'Иcтoрия Кaзaxcтaнa:':
		await message.reply('Выберите тему', reply_markup=markup_ist_kz)
	elif message.text == '1. Орталық Азия: ұғымының тарихи':
		await message.reply('1) Орталық Азияда орналасқан мемлекетті көрсетіңіз: \n Ответ: Қырғызстан \n\n 2) Алтайдан оңтүстікке және Памирден шығысқа қарайғы аумақты Орталық Азия деп қарастырған ғалым: \n Ответ: А.Гумбольдт \n\n 3) Орталық Азияда орналасқан ірі құмды шөл: \n Ответ: Қызылқұм \n\n 4) Физикалық географияда Орталық Азия ұғымын қалай қолданады? \n Ответ: ішкі өзен алабына байланысты \n\n 5) Орталық Азияны Еуразияның ""ішкі биік аудандары"" деп қарастырған неміс ғалымы: \n Ответ: Карл Риттер \n\n 6) Еуразияның ішкі ағынды алабына жататын өзен: \n Ответ: Әмудария \n\n 7) ХІХ ғасырда Орталық Азия ұғымын кеңінен қолданған қай елдің ғалымдары? \n Ответ: неміс \n\n 8) Орталық Азиядағы ірі өзен: \n Ответ: Сырдария \n\n 9) Ресей империясы кезінде Орта Азия ұғымымен қатар қолданылған ұғым: \n Ответ: Түркістан \n\n 10) 1991 жылы ыдыраған мемлекет: \n Ответ:КСРО', reply_markup=markup_DO)
	elif message.text == '2. Орталық Азияның дәстүрлі':
		await message.reply('1) Қазақстанда археологиялық қазба жұмыстары басталды: \n Ответ: 1826 жылы \n\n 2) Ежелгі түркі жазуының алғашқы аудармасын жасаған: \n Ответ: В.Радлов \n\n 3) Бүгінгі таңда белгілі руна жазбаларының саны: \n Ответ: 255 \n\n 4) ""Жаратылыстану тарихы"" атты еңбектің авторы: \n Ответ: Үлкен Плини \n\n 5) ""Бехистун жазбаларын"" қалдырған патша: \n Ответ: І Дарий \n\n 6) Зороастризмнің қасиетті кітабы: \n Ответ: Авеста \n\n 7) Дәстүрлі өркениетке тән белгі: \n Ответ: дін және мифтік сана \n\n 8) Ғұндардың Еуропаға жасаған жорығы туралы баяндаған тарихшы: \n Ответ: Марцеллин \n\n 9) Орталық Азия туралы нақты мәлімет беретін деректер: \n Ответ: қытай деректері \n\n 10) Кирдің Орталық Азияға жасаған жорығы туралы жазған грек тарихшысы: \n Ответ: Геродот', reply_markup=markup_DO)
	elif message.text == '3. Орталық Азия өркениеттерінің ежелгі ошақтары':
		await message.reply('1) Орталық Азияның таулы аймағында орналасқан ойпат: \n Ответ: Ферғана \n\n 2) Тас өңдеу техникасының жетілген кезеңі: \n Ответ: неолит \n\n 3) Б.з.б ІІ мыңжылдықта Маргуштың астанасы болған қала: \n Ответ: Гонур \n\n 4) Балқаш көлі мен Ыстықкөл арасындағы тарихи-мәдени аймақ: \n Ответ: Жетісу \n\n 5) Неолиттік төңкерістің маңызды жетістіктерінің бірі: \n Ответ: егіншілік \n\n 6) Каналдар жүйесі жетілген, Әмударияның төменгі сағасында орналасқан мәдениет: \n Ответ: Хорезм \n\n 7) Төл жазуы болған, сауда және қолөнермен айналысқан мәдениет: \n Ответ: Соғды \n\n 8) Орталық Азияның оңтүстігіндегі Мургаб жазирасында пайда болған мәдениет: \n Ответ: Маргуш \n\n 9) Орталық Азияда алғаш болып жер өңдеп, дәнді дақылдар өсіре бастаған халық: \n Ответ: жейтундықтар \n\n 10) Ташкент пен Шымкент қалалары орналасқан аймақ: \n Ответ: Шаш ', reply_markup=markup_DO)
	elif message.text == '4. Ұлы Дала: тарихи-географиялық сипаттамасы':
		await message.reply('1) Ұлы Далада қалыптасқан өркениет: \n Ответ: көшпелі \n\n 2) ХІІІ ғасырда Еуразия даласында құрылған империя:  \n Ответ: Моңғол \n\n 3) Ұлы Дала халқының ауа-райы, жыл мезгіліне байланысты бір қоныстан, екінші қонысқа көшуі:  \n Ответ: көш \n\n 4) ""Шығыс Дешті Қыпшақ"" деп қай елдің даласын атады? \n Ответ: қазақ \n\n 5) Ұлы Даланың экологиялық, табиғи-климаттық жағдайы қандай шаруашылықтың дамуына қолайлы болды?  \n Ответ: көшпелі мал шаруашылығы \n\n 6) Дунайдан Алтайға, одан Маньчжурияға дейінгі жерді алып жатқан тарихи-мәдени аймақтың атауы: \n Ответ: Ұлы Дала \n\n 7) Ұлы Даланың географиялық атауы: \n Ответ: Еуразия даласы \n\n 8) Х-ХVІІ ғасырларда Қара теңіз бен Каспий теңізінің аралығын қалай атады?  \n Ответ: Батыс Дешті Қыпшақ \n\n 9) Орта ғасырлардағы мұсылман деректеріндегі Ұлы Даланың атауы:  \n Ответ: Дешті Қыпшақ \n\n 10) Ұлы Дала оңтүстігінде қай тауларға барып тіреледі?  \n Ответ: Тянь-Шань', reply_markup=markup_DO)
	elif message.text == '5. Ұлы дала өркениетінің қайнар көзі':
		await message.reply('1) Б.з.б ХVІІІ - VІІІ ғасырлар аралығын қамтитын дәуір: \n Ответ: қола \n\n 2) Қола дәуірінде далалық малшылар мәдениетін құраушылар:  \n Ответ: андрондықтар \n\n 3) Б.з.б ІІ мыңжылдықтың басында Дала тұрғындары қорытуды игерген металл:  \n Ответ: қола \n\n 4) Адамдар тұрмыста алғаш қолданған металл: \n Ответ: мыс \n\n 5) Тас дәуірі мен қола дәуірінің арасындағы өтпелі кезең:  \n Ответ: энеолит \n\n 6) Ботайлықтар қолға үйреткен жануар:  \n Ответ: жылқы \n\n 7) Б.з.б ІІІ-ІІ мыңжылдық аралығын қамтыған дәуір: \n Ответ: энеолит \n\n 8) Б.з.б 3700-3100 жылдар аралығында өмір сүрген Солтүстік Қазақстандағы мәдениет:  \n Ответ: Ботай \n\n 9) Мәйіттерді тізесін бүгіп, арқасымен жатқызып қорған астына жерлеген мәдениет:  \n Ответ: Көнешұңқыр \n\n 10) Қазақстан аумағындағы қола дәуірі:  \n Ответ: Андрон мәдениеті ', reply_markup=markup_DO)
	elif message.text == '6. Ерте көшпенділер дәуіріндегі':
		await message.reply('1) Қазақстанның Оңтүстік және Оңтүстік-Шығысында көшіп жүрген сақтар: \n Ответ: Тиграхауда \n\n 2) Орталық Қазақстанда кең тарыған сақ мәдениеті:  \n Ответ: Тасмола \n\n 3) Андрондық мәдениет түрінің орнына келген тарихи-мәдени қауымдастық:  \n Ответ: сақ-скиф \n\n 4) Көшпелі өмірге көшуге мәжбүрлеген жағдай: \n Ответ: құрғақшылық \n\n 5) Б.з.б І мыңжылдықтың ортасында Даладағы негізгі шаруашылық:  \n Ответ: көшпелілік \n\n 6) Орталық Қазақстанда оқшауланып тіршілік еткен сақ тайпасы:  \n Ответ: Исседондар \n\n 7) Дала халқы көшпелі өмірге қай кезде көшті? \n Ответ: Б.з.б І мыңжылдық \n\n 8) Көшпелі мал шаруашылығына өтудің барлық алғышарттары қалыптасты:  \n Ответ: Б.з.б ІІ мыңжылдықтың ортасы \n\n 9) Сақтар туралы ең алғаш дерек қалдырған ел:  \n Ответ: Парсы \n\n 10) Сақ-скиф тайпалары байланыста болған ежелгі дүниедегі мемлекет:  \n Ответ: Парсы ', reply_markup=markup_DO)
	elif message.text == '7. Әлемдік мәдениеттің дамуына':
		await message.reply('1) Б.з.б 331-327 жылдар аралығында Орталық Азияға шабуыл жасаған патша: \n Ответ: А.Македонский \n\n 2) ІІ ғасырдың ортасында Шығыс Қазақстан мен Жетісу жерінде құрылған мемлекет:  \n Ответ: Юэбань \n\n 3) Б.з.б 670 жылы ассириялықтармен болған шайқаста қаза тапқан скиф патшасы:  \n Ответ: Ишпакай \n\n 4) Ғұн мемлекетінің негізін салушы: \n Ответ: Мөде \n\n 5) Б.з.б 518 жылы сақ жеріне жасаған жорығы сәтсіз аяқталған парсы патшасы:  \n Ответ: І Дарий \n\n 6) Б.з.б 530 жылы массагеттерге жорық жасаған парсы патшасы:  \n Ответ: Кир \n\n 7) Ғұндардың оңтүстігіндегі басты қарсыласы: \n Ответ: Қытай \n\n 8) V ғасырда Шығыс Еуропа жерінде ғұндардың мемлекетін құрған тұлға:  \n Ответ: Аттила \n\n 9) Ғұндар юэчжи тайпасын толықтай жеңді:  \n Ответ: Б.з.б 165 жылы \n\n 10) А. Македонский шабуылына тойтарыс беріп, тәуелсіздігін сақтап қалған ел:  \n Ответ: Сақтар', reply_markup=markup_DO)
	elif message.text == '8. Қазақстандағы этногенез':
		await message.reply('1) Этностың шығу тегі, этникалық тарихы: \n Ответ: Этногенез \n\n 2) Түр ретінде адамның шығу тегі:  \n Ответ: антропогенез \n\n 3) Адам мен оның нәсілдерінің биологиялық табиғаты, шығу тегі мен эволюциясы туралы ғылым:  \n Ответ: Антропология \n\n 4) Этникалық үдерістерді зерттейтін ғылым: \n Ответ: Этнология \n\n 5) Әртекті бөліктердің біртіндеп жақындасуынан және қосылуынан жаңа этностың пайда болуы:  \n Ответ: интеграция \n\n 6) Өз этносы шегінде ғана неке құру қалай аталады?  \n Ответ: эндогамия \n\n 7) Дүниежүзінің әртүрлі аймақтарындағы генетикалық белгілердің таралуын зерттейтін ғылым: \n Ответ: гендік география \n\n 8) Қазақтардың этногенезі қандай өркениетпен тығыз байланысты?  \n Ответ: көшпелілер \n\n 9) Этнос сөзінің қарапайым мағынасы:  \n Ответ: халық \n\n 10) Белгілі бір аймақты ежелден бері мекен еткен жергілікті халық:  \n Ответ: автохтон', reply_markup=markup_DO)	
	elif message.text == '9. Қазақтардың ру-тайпалық құрылымы қалыптасуы':
		await message.reply('1) Туыс адамдардың үйленуіне салынған тыйым: \n Ответ: экзогамия \n\n 2) Қазақ жүздері туралы алғашқы деректер қай ғасырға жатады?  \n Ответ: XVII ғ. басы \n\n 3) Ер адам жағынан ата тегі ортақ топтар:  \n Ответ: патронимиялар \n\n 4) Қазақтардың тайпалық бірлестігі: \n Ответ: жүз \n\n 5) Шежіренің ең қысқа бөлігі:  \n Ответ: жеті ата \n\n 6) Қазақ хандығында ұлыстарды басқарды:  \n Ответ: сұлтан \n\n 7) Рудың көшіп-қону аймағы: \n Ответ: атажұрт \n\n 8) Ер адам жағынан ата-бабаларын ауызша немесе жазбаша санамалайтын туыстық қатынастар тізбегі:  \n Ответ: шежіре \n\n 9) Қазақ хандығында мемлекетті басқарды:  \n Ответ: хан \n\n 10) Қазақтардың шежіресі қатар жүреді:  \n Ответ: аңызбен', reply_markup=markup_DO)	
	elif message.text == '10. Қазақтардың ру-тайпалық құрылымының':
		await message.reply('1) Жүзге кірмейтін руды көрсетіңіз: \n Ответ: қожа \n\n 2) Кіші жүз қазақтарының мекен еткен аумағы:  \n Ответ: Батыс Қазақстан \n\n 3) Ұлы жүз құрамына кірмейтін ру:  \n Ответ: байбақты \n\n 4) Жетісу жері мен одан батысқа қарайғы жерді мекендеген қазақ жүзі: \n Ответ: ұлы жүз \n\n 5) Ұлы жүз құрамына кіретін тайпа:  \n Ответ: дулат \n\n 6) Кіші жүз құрамына кіретін ру:  \n Ответ: адай \n\n 7) Орта жүз құрамына кіретін ру: \n Ответ: арғын \n\n 8) Қыпшақ тайпасы кіреді:  \n Ответ: орта жүз \n\n 9) Солтүстік, Орталық және Шығыс Қазақстанды мекендеген қазақ жүзі:  \n Ответ: орта жүз \n\n 10) Ұлы жүздің қысқы жайылымдары болды:  \n Ответ: Алатауда', reply_markup=markup_DO)
	elif message.text == '11. Дәстүрлі қазақ қоғамының әлеуметтік жіктелуінің ерекшеліктері':
		await message.reply('1) Орталық Азияға ислам дінін таратушылардың ұрпақтары: \n Ответ: қожалар \n\n 2) Дәстүрлі қазақ қоғамы қанша әлеуметтік топтан тұрды?  \n Ответ: 2 \n\n 3) Хандық билікке үміткер Шыңғыс ұрпақтары:  \n Ответ: сұлтандар \n\n 4) Қазақ қоғамындағы кәсіпқой әскери адамдар: \n Ответ: батырлар \n\n 5) Қазақ қоғамында көп мал мен мүлікке ие болған дәулетті адамдар:  \n Ответ: байлар \n\n 6) Қазақ даласындағы барлық Шыңғыс ұрпақтарының ортақ таңбасы мен ұраны:  \n Ответ: арқар \n\n 7) Рулар мен тайпалардың басшылары: \n Ответ: билер \n\n 8) Әлеуметтік сатының жоғарғы сатысында орналасып, өздерін тән артықшылық жағдайды пайдаланған топ:  \n Ответ: ақсүйектер \n\n 9) Орта жүздің биі:  \n Ответ: Қазыбек \n\n 10) Құрметті және беделді жағдайға қол жеткізген қарт адам:  \n Ответ: Ақсақал', reply_markup=markup_DO)
	elif message.text == '12. Қазақстан аумағындағы ерте мемлекеттердің':	
		await message.reply('1) Көшпелі мемлекеттер өмірінде маңызды рөл атқарған жиналыс: \n Ответ: халық жиналысы \n\n 2) Туыстыққа негізделген, мұрагерлік билігі бар көсем басқаратын саяси құрылым:  \n Ответ: көсемдік \n\n 3) Қазақстан жеріндегі алғашқы мемлекеттік бірлестік:  \n Ответ: сақ \n\n 4) Қаңлылар солтүстігінде тәуелді болды: \n Ответ: ғұндарға \n\n 5) Көшпелілер мемлекетінде мемлекеттіліктің қанша үлгісі болды?  \n Ответ: 3 \n\n 6) Қаңлы мемлекетінің астанасы:  \n Ответ: Битянь \n\n 7) Көшпелі мемлекеттерде бір мезгілде басшы, әскербасы кейде абыз рөлін атқарған тұлға: \n Ответ: тайпа көсемі \n\n 8) Сақтардан кейін Жетісу жерін мекендеген тайпа:  \n Ответ: үйсін \n\n 9) Ерте көшпелі мемлекеттердің саяси құрылымы:  \n Ответ: әскери демократия \n\n 10) Үйсіндердегі жоғарғы билеуші:  \n Ответ: Күнби (гуньмо)', reply_markup=markup_DO)
	#Kykik
	elif message.text == 'Ocнoвы прaвa':
		await message.reply('Выберите тему:', reply_markup=markup_prava)
	elif message.text == '10. Қазақстан Республикасы Конститутциялық кұқығының институттары':
		await message.reply("1) Конституциялық құқық қызметтерін көрсет.  \n Ответ: Конституциялық құқық нормасымен реттелетін қоғамдық қатынастар мемлекеттік қызметтің маңызды жақтары; \n\n 2) Конституциялық құқық институттарын көрсет.  \n Ответ: ҚР Конституциялық құрылым негізгі институттары; \n\n 3) Конституция қандай түрлерге бөлінеді?  \n Ответ:Жазылған және жазылмаған;Қатаң және икемді;Кодификацияланған және кодификатцияланбаған \n\n 4) Конституцияның заңдық қасиеттеріне қандай қасиеттер жатады?  \n Ответ: Легитимділік;Құрылтайшылық;Конститутцияның үстемдігі; \n\n 5) Конституция қағидаттары қалай бөлінеді?  \n Ответ: Экономикалық;Саяси;Әлеуметтік \n\n 6) Конституцияның функциялары қалай бөлінеді?  \n Ответ: Құрылтайшылық;Ұйымдастырушылық;Құқықтық;Сыртқы саяси; \n\n 7) ҚР Конституциясына қанша толықтырулар мен өзгертулер енгізіліген?  \n Ответ: 5 \n\n 8) Конституциялық құқық қайнар көзін тап.  \n Ответ: ҚР министрлері мен басқа да орталық мемлекеттік орган басшыларының нормативтік-құқықтық бұйрықтары; \n\n 9) Конституциялық құқық әдістерін көрсет  \n Ответ: Міндеттеу әдісі \n\n 10) Конституциялық құқықтық нормалар қалай бөлінеді?  \n Ответ: Басқару;Тиым салу;Міндеттеу;", reply_markup=markup_DO)
	elif message.text == '11. Қазақстан Республикасындағы мемлекеттік басқарудың құқықтық реттелуі':
		await message.reply("1) Салалық басқару бойынша басқару тәртібі қандай?  \n Ответ: вертикалды \n\n 2) Қоғамдық тәртіпті қорғау және қоғамдық тәртіпті қамтамасыз ету қандай органдардың функциясы?  \n Ответ: Атқарушы биліктің \n\n 3) Мемлекеттік басқарудың қанша түрі бар?  \n Ответ: 2 \n\n 4) ҚР орталық атқарушы органдары қалай аталады?  \n Ответ: министрліктер, агенттіктер, комиттер. \n\n 5) Дәстүрлі әкімшілік құқық қалай бөлінеді?  \n Ответ: Жылпы, ерекше \n\n 6) ҚР жоғары атқарушы және басқарушы орган қалай аталады?  \n Ответ: Үкімет \n\n 7) Атқарушы биліктің алғашқы функциясы қандай?  \n Ответ: Мемлекеттік басқару \n\n 8) ҚР қанша облыс пен республикалық маңызы бар қала бар?  \n Ответ: 14 облыс, 3 қала \n\n 9) Әкімшілік құқық әдістері қаншаға бөлінеді?  \n Ответ: 3 \n\n 10) Үкімет құрамына кірмейтін атқарушы орган қалай аталады?  \n Ответ: құнды қағаздар бойынша ұлттық комиссия.", reply_markup=markup_DO)
	elif message.text == '12. Экологиялық құқықтың құқықтық реттелу түсінігі мен нысаны':
		await message.reply("1) Су кодексі қашан қабылданды?  \n Ответ: 2003 жылы 9 шілде \n\n 2) Орман кодексі қашан қабылданды?  \n Ответ: 2003 жылы 8 шілде \n\n 3) Адамның негізгі экологиялық міндеттері?  \n Ответ: Қоршаған орта мен табиғатты қорғау \n\n 4) Экологиялық құқықбұзушлыққа жауаптылық қанша жастан басталады?  \n Ответ: 16 жас  \n\n 5) Адамның негізгі экологиялық құқықтарына не жатады?  \n Ответ: Қоршаған орта жағдайы туралы шынайы ақпарат алу; \n\n 6) Экологиялық құқықбұзушылықты тап  \n Ответ: Қоршаған ортаның және табиғи нысандардың ластануы; \n\n 7) Экологиялық құқықтың негізгі объектілеріне не жатады?  \n Ответ: Жер, жер қойнауы, жерүсті, жерасты сулары \n\n 8) Жер кодексі қашан қабылданды?  \n Ответ: 2003 жылы 20 маусым  \n\n 9) ҚР- ның Экологиялық кодексі экологиялық құқықтық қатынстарды реттеп отыратын заң қашан қабылданды?  \n Ответ: 2007 жыл 9 қаңтар \n\n 10) Денсаулығына немсе мүлкіне экологиялық құқықбұзушылық арқылы залалы тисе, оның өтемін талап ету құқығы қандай құқық саласына жатады?  \n Ответ: экологиялық құқықтары", reply_markup=markup_DO)
	elif message.text == '13. Қылмыстық кодекс қылмыстық құқықтың негізгі қайнар көзі ретінде':
		await message.reply("1) Жеке тұлға жасаған қылмыс жазасын өтей алмаса басқа тұлғаға жазасын ауыстыруға болады ма?  \n Ответ: Жоқ тек өзі ғана жауап береді \n\n 2) Егер жекетұлғаның қоғам мен мемлекеттің аса маңызды мүддесі қозғалса құқықтың қандай функциясы орындалу керек?  \n Ответ: Қылмыстық құқықтың қорғау функциясы; \n\n 3) Қылмыстық құқық нормаларының құрылымы:  \n Ответ: Гипотеза, Диспозиция, Санкция \n\n 4) Диспозицияның төрт түрі бар қандай?  \n Ответ: Қарапайым;Сипаттау;Бланкетті;Сілтемелік; \n\n 5) Қылмыстық құқық жүйесі қалай бөлінеді?  \n Ответ: Жалпы, ерекше \n\n 6) Қылмыстық заң Қылмыстық кодекс түрінде болады. Ол қанша бөлімнен тұрады?  \n Ответ: 2 \n\n 7) Қазақстан Республикасындағы қолданыстағы Қылмыстық Кодекс қашан қабылданды?  \n Ответ: 2015ж \n\n 8) Қылмыстық құқықтың заңдылық қағидатын табыңыз?  \n Ответ: Заң аясында шешім шығару \n\n 9) Қылмыстық құқықтың негізгі бірінші функциясы қалай аталады?  \n Ответ: Алдын ала ескерту \n\n 10) Қылмыстық құқық міндеттері қаншаға бөлінеді:  \n Ответ: 3", reply_markup=markup_DO)		
	elif message.text == '14. Қылмыстық құқық бұзушылық және қылмыстық жауапкершілікке тартылатын тұлғалар':
		await message.reply("1) Кәмілетке толмағандар дегеніміз өанша жас аралығындағы жеткіншектер?  \n Ответ: 14 жастан асқан 18 жасқа толмаған \n\n 2) Кәмілетке толмағандар үшін ең ауыр қандай жаза қолданылады?  \n Ответ: 10 жыл бас бостандығынан айыру \n\n 3) Кәмілетке толмағандарды мәжбүрлі түрде тәрбиелеу шаралары қалай аталады?  \n Ответ: Ескерту;Пробауиялық бақылау орнату; \n\n 4) Қылмыстық құқықбұзушылық құрамы қанша элементтен тұрады?  \n Ответ: 4 \n\n 5) Қылмыстық жауаптылықтың шарты ҚР ҚК-нің қай бабында анықталып жазылады?  \n Ответ: 15-бап \n\n 6) Қылмыс категориялары қаншаға бөлінеді?  \n Ответ: 4 \n\n 7) Онша ауыр емес қылмыс бойынша қасақана жасаған әрекеті үшін қанша жыл бас бостандығынан айыру жазасы қолданылады?  \n Ответ: 2 жыл аспайтын \n\n 8) Аса ауыр қылмыстап үшін қандай жаза қолданылады?  \n Ответ: 12 жылдан аса бас бостандығана айыру \n\n 9) ҚР-ның Қылмыстық кодексі қашан қабылданды?  \n Ответ: 2014ж 3 шілде \n\n 10) Қылмыстық құқықбұзушылықтар қалай бөлінеді:  \n Ответ: Қылмыс, қылмыстық теріс қылық", reply_markup=markup_DO)
	elif message.text == '15. Қылмыстық жаза түсінігі және одан босату шарттары':
		await message.reply("1) ҚР Қылмыстық кодекстің қай бабында төмендегі бап баяндалған «Қоғамға қауіпті қолсұғушылықтан туындаған үрейлену, қорқу немесе сасқалақтау салдарынан қажетті қорғаныс шегінен шыққан адам қылмыстық жауаптылықтан босатылуы мүмкін»  \n Ответ: 66-бап \n\n 2) Сот арқылы алынатын ақшалай жаза түрі қалай аталады?  \n Ответ: Айыппұл \n\n 3) Қылмыстық жауаптылықтан босату түрлері ҚР Қылмыстық кодексінің қай бөлімі мен баптарында баяндалған:  \n Ответ: 5- бөлім, 65-78 бб \n\n 4) Татуласуға байланысты төмендегі нұсқаның қандай түрі келеді:  \n Ответ: Медиаторлық жолмен келісімге келу; \n\n 5) Қылмыс жасау құралдарын көрсету, қылмыстық жолмен табылған заттарды беру құқықта қалай аталады?  \n Ответ: Қылмысты ашуға көмектесу \n\n 6) ҚР Қылмыстық заңында қылмыстық жауаптылықпен қатар қандай жағдайлар қарастырылған?  \n Ответ: Жазаны ауырлау, жеңілдету \n\n 7) Қылмыстық құқықта қандай ережелер бар:  \n Ответ: Қорғау, реттеу, ынталандыру; \n\n 8) ҚР Қылмыстық кодексінің 65- бабында не турлы айтылады:  \n Ответ: ҚР Қылмыстық кодексінің 65- бабында не турлы айтылады: \n\n 9) Татуласуға байланысты ҚР ҚК қай бабында айтылады?  \n Ответ: 68- бап \n\n 10) Процестік келісімдер дегеніміз не?  \n Ответ: Кінәні мойындау және ынтымақтастық келісіммен жұмыс істеу түрінде жүргізіледі.", reply_markup=markup_DO)	
	elif message.text == '16. Қазақстан Республикасындағы сыбайлас жемқорлыққа қарсы күреске бағытталған құқықтық және саяси актілер':
		await message.reply('1)Биліктің жоғары эшалонындағы жемқорлық қалай аталады?\nОтвет: Саяси\n\n2) Ұзақ уақыт әрекет еткен жемқорлық қоғам дамуын әрі қарай не істейді?\nОтвет: Тежейді\n\n3)Сыбайлас жемқорлық түрлері қаншаға бөлінеді:\nОтвет: 3\n\n4) Мемлекеттің сатып алу саласындағы сыбайлас жемқорлыққа қарсы ҚР мемлекетті бағдарлама қалай аталады?\n Ответ: Сандық Қазақстан\n\n5)Мектеп ортасында жемқорлыққа қарсы мәдениет қалыптастыратын клуб:\nОтвет: Адал ұрпақ\n\n6)Сыбайлас жемқорлық субъектілері:\nОтвет: Жауапты мемлекеттік қызмет орнындағы тұлғалар\n\n 7) Билік пен ьизнестің өзара әрекеттестігі нәтижесінде туындайтын жемқорлық қалай аталады?\n Ответ: Іскерлік\n\n8)Сыбайлас жемқорлыққа қарсы және қоғамда оның кез келген түрінің пайда болуына төзбеушілікті қалыптастыруға байланысты қабылданған мемлекеттік бағдарлама:\nОтвет: 100 нақты қадам\n\n9)Қатардағы азаматтар мен шенеуліктердің өзара әрекеттігі нәтижесінде туындаған жемқорлық қалай аталады?\nОтвет: Тұрмыстық \n\n10) Білім саласындағы сыбайлас жемқорлыққа қарсы құралға жататындар:\nОтвет: Тәрбиенің тұжырымдамалық негіздері', reply_markup=markup_DO)
	elif message.text == '17. Қазақстан Республикасындағы сыбайлас жемқорлыққа қарсы іс-шаралар жүйесі.Сыбайлас Жемқорлыққа қарсы мәдениет.':
		await message.reply('1) ҚР сыбайлас жемқорлыққа қарсы іс- қимыл туралы заңның негізгі мақсаты:  \n Ответ: Сыбайлас жемқорлық деңгейін төмендету \n\n 2) Сыбайлас жемқорлыққа қарсы мәдениет барлық адамдарға......  \n Ответ: тән \n\n 3) Сыбайлас жемқорлыққа қарсы әрекеттер қанша бөліктен тұрады:  \n Ответ: 8 \n\n 4) Заңсыз алынған мүлікті және заңсыз көрсетілген қызмет түрін қайтару қалай аталады:  \n Ответ: Құқықбұзушылық салдарын жою \n\n 5) Өкілетті тұлғалар жазбаша түрде тікелей басшыға немес өздері жұмыс жасап отырған мекеме басшысына туындап отырған мүдделер шиеленісін хабарлау қалай аталады:  \n Ответ: Шиеленіс болдырмау және шешімін табу \n\n 6) Сыбайлас жемқорлыққа қарсы мәдениет туралы әрбір адам білуге міндетті:  \n Ответ: Заң ережесін біліп, түсініп, қолдануды \n\n 7) Сыбайлас жемқорлыққа қарсы мәдениет құқықтық үдесітерді не істеп отыратын арнайы жүйе?  \n Ответ: Реттеп \n\n 8) Жауапты мемлекеттік қызметтегі және мемлекеттік функцияларды орындауға өкілетті адамдардың міндеті:  \n Ответ: Сыбайлас жемқорлыққа қарсы шектеулер \n\n 9) Жемқорлық деңгейін қоғамның қабылдауы мен бағалуы сияқты ақпараттарды жинау, зерделеу, қорытындылау, сараптау және бағалау қызметі қалай аталды:  \n Ответ: Сыбайлас жемқорлыққа қарсы мониторинг \n\n 10) Сыбайлас жемқорлыққа қарсы мәдениет қанша деңгейден тұрады:  \n Ответ: 3', reply_markup=markup_DO)
	elif message.text == '18. Азаматтық құқықтың принциптері мен субъектілері. Азаматтық құқықтың объектілері':
		await message.reply('1) Құқық субъектілері дегеніміз не?  \n Ответ: құқықтар мен міндеттердің иелері. \n\n 2) Мүліктік емес қатынастар дегеніміз не?  \n Ответ: Адамның жеке қасиеттерінің нәтижесі. \n\n 3) Азаматтық құқық қайнар көзі:  \n Ответ: ҚР Конститутциясы \n\n 4) Азаматтық құқық қағидаттары:  \n Ответ: Құқықтық теңдік; \n\n 5) Кәмілетке толмағандар- азаматтық құқық субъектілеріне не жатады:  \n Ответ: Жазбаша келісіммен ғана жасай алады \n\n 6) Азаматтық құқық жүйесі қандай бөлімдерден тұрады:  \n Ответ: Жалпы, ерекше \n\n 7) Өз меншігі бар, өз меншігіне өз міндеттемелері арқылы жауап беретін, сотқа талап қоюшы және жауап бере алатын ұйым:  \n Ответ: Заңды тұлға \n\n 8) Мүліктер категориясы:  \n Ответ: Тұтыну заттары мен өндіріс құралдары \n\n 9) Мүліктік қатынастар дегеніміз не? \n Ответ: Адам еңбегінің нәтижесі. \n\n 10) Азаматтық құқық қандай қатынастарды реттейді:  \n Ответ: Мүліктік, мүліктік емес', reply_markup=markup_DO)
	elif message.text == '19. Мәміле түсінігі және оның түрлері':
		await message.reply('1) Даулы мәміле негіздері:  \n Ответ: Қатердің әсерімен жасалғанда \n\n 2) Жалған мәміле кімнің талабы бойынша жарамсыз деп танылады:  \n Ответ: Прокурор \n\n 3) Мәміленің жарамсыз деп танылу негіздері:  \n Ответ: Қажетті рұқсат алмай жасалғанда \n\n 4) Жарамсыз мәмілелер қанша топқа бөлінеді:  \n Ответ: 2 \n\n 5) Тараптардың саны бойынша қаншаға бөлінеді:  \n Ответ: 3 \n\n 6) Нотариалды кәуландырусыз жасалған мәміле түрі:  \n Ответ: Қарапайым жазбаша мәміле \n\n 7) Мәміле белгілерін тапыңыздар:  \n Ответ: Еріктілік \n\n 8) Бұл мәмілені жасау үшін екі жақта да өз еркін білдіру мәмілесі қалай аталады:  \n Ответ: Екіжақты \n\n 9) Мақсатты бағытталған әрекет қай мәліме белгісіне жатады?  \n Ответ: Еріктілік \n\n 10) Талап қою мерзімінің өтуі қанша уақытты құрайды:  \n Ответ: 1 жыл', reply_markup=markup_DO)
	elif message.text == '20. Меншік құқығы түсінігі және оның қорғалуы':
		await message.reply('1) Мемлекеттік емес заңды тұлғалардың меншігі қалай аталады?  \n Ответ: Жеке \n\n 2) Меншік құқығын иемдену негіздері:  \n Ответ: Мүліктің меншік құқығына ие бола алады. \n\n 3) Негаторлық талап дегеніміз не?  \n Ответ: Талапты жоққа шығару әдісі \n\n 4) Мемлекетке тиесілі барлық меншік қалай аталады?  \n Ответ: Мемлекеттік \n\n 5) Меншік құқығының тоқтатылуы:  \n Ответ: Қалауы бойынша, еркінен тыс \n\n 6) Ортақ меншік құқығының түрлері:  \n Ответ: Үлесін анықтайды, үлесін анықтамайды \n\n 7) Виндикациялық талап дегеніміз не?  \n Ответ: Өз мүлкін заңдық жолмен қайтарып алу әдісі \n\n 8) ҚР меншік құқығын қорғаудың қанша жолы қарастырылған?  \n Ответ: 3 \n\n 9) Меншік құқығы қаншаға бөлінеді:  \n Ответ: 3 \n\n 10) Заң бойынша заттың пайдалы табиғи қасиеттерін алу,пайда табу мүмкіндіктері қандай меншік құқығына жатады?  \n Ответ: Пайдалану', reply_markup=markup_DO)
	elif message.text == '21. Міндеттемелік құқық':
		await message.reply('1) Заңмен немесе келісімшартпен анықталған, борышқор несие берушіге төленуге міндетті сома қалай аталады:  \n Ответ: Тұрақсыздық айыбы \n\n 2) Міндеттеме тоқтатылатын жағдайлар:  \n Ответ: Борыштың кешірілуі; \n\n 3) Кепіл түрі:  \n Ответ: Тауарлардың айналымда кепілдікте болуы \n\n 4) Тауарлардың айналымда кепілдікте болуы:  \n Ответ: Тұрақсыздық айыбы \n\n 5) Кепіл ретінде мүлікті берген тұлға қалай аталады:  \n Ответ: Кепіл беруші \n\n 6) Несие берушінің борышқорды жүктелген міндеттемелерден босатылуы:  \n Ответ: Қарызды кешіру \n\n 7) Сатуға арналған келісімшарт бойынша сатушы заттарды не істеуге міндетті?  \n Ответ: Беруге \n\n 8) Міндеттемелік құқық құрлымы қанша бөлімнен тұрады:  \n Ответ: 4 \n\n 9) Борышқорда жаңа міндеттемелер пайда болу қалай аталады:  \n Ответ: Жаңғыртылу \n\n 10) Уағдаласушы тараптардың біреуінің шарт бойынша өзінен алынатын төлем есебінен екінші тарапқа беретін ақшалай сомасы қалай аталады:  \n Ответ: Кепілпұл', reply_markup=markup_DO)
	elif message.text == '22. Қазақстан Республикасында тұтынушылар құқықтарының заңды түрде бекітілуі':
		await message.reply('1) Сатушының міндеттері қандай:  \n Ответ: Тауарды ауыстырып беруге,қайтарылуым қамтамасыз етуге; \n\n 2) Тұтынушылардың құқықтарын қорғаудың басты екі мақсаты қандай?  \n Ответ: Ақпарат беру, қорғау \n\n 3) Жарамдылық мерзімін қарап, оны белгілеу кімнің міндеті:  \n Ответ: Дайындаушы \n\n 4) Электрондық сауда жасау барысында тұтынушыға бірінші нені жасау керек  \n Ответ: Ақы төлеу \n\n 5) Тұтынушы құқығы бұзылатын жағдайлар:  \n Ответ: Тұрғын үй-коммуналдық саласында; \n\n 6) Тұтынушы құқығы қандай:  \n Ответ: Құқықтары мен заңды мүдделерін қорғауға; \n\n 7) Сатушы бағалар заттаңбасымен рәсімделлген тауардың құнын немен көрсетуге міндетті:  \n Ответ: Теңге \n\n 8) Тұтынушының құқығын қорғайтын органдар:  \n Ответ: ҚР Ұлттық экономика министрлігінің Құрлыс және тұрғын үй-коммуналдық шаруашылық істері комитеті; \n\n 9) Тауардың қауіпсіздігін қамтамасыз ету кімнің міндеті болып табылады:  \n Ответ: Сатушы \n\n 10)  Сотқа дейінгі наразылық нысандары қандай? \n Ответ: Ескерту хат жіберу керек;', reply_markup=markup_DO)
	elif message.text == '23. Қазақстан Республикасындағы отбасы құқығының қайнар көздері. Қазақстан Республикасында отбасылық қарым-қатынастардың құқықтық реттелуі':
		await message.reply('1) "Неке және отбасы, ана мен әке және бала мемлекеттің қорғауында болады" ҚР Конституциясының қай бабында айтылған:  \n Ответ: 27- бап \n\n 2) ҚР "Кәмілетке толмағандар арасындағы құқықбұзушылықтардың профилактикасы мен балалардың қадағалауынсыз және панасыз қалуының алдын алу туралы" Заң қашан қабылданды:  \n Ответ: 2004ж \n\n 3) ҚР "Отбасы үлгісіндегі балалар ауылы және жасөспірімдер үйлері туралы" Заң қашан қабылданды:  \n Ответ: 2000 \n\n 4) Төрт және одан да көп баласы бар отбасы- қандай отбасы деп аталады?  \n Ответ: Көпбалалы \n\n 5) ҚР "Неке және отбасы туралы " Заңы қашан қабылданды:  \n Ответ: 2011ж \n\n 6) Ерлі- зайыптылар міндеттері: \n Ответ: Тегі өзгерген жайғдайда 1 ай көлемінде жеке кәулігін өзгертуге міндетті; \n\n 7) Неке шартын азаматтық некедегі ерлі- зайыптылар және қандай тұлғалар жасай алмайды?  \n Ответ: Мемлекеттік органдарда тіркеуге алынбаған тұлғалар \n\n 8) Неке шарты қандай форматта жасалады:  \n Ответ: Жазбаша \n\n 9) ҚР "Бала құқықтары туралы туралы" Заң қашан қабылданды:  \n Ответ: 2002ж \n\n 10) Ерлі-зайыптылар құқықтары:  \n Ответ: Неке бұзылған жағдайларға өз тектерін сақтап қалуға құқығы бар;', reply_markup=markup_DO)

# Обновление бота
if __name__ == '__main__':
	executor.start_polling(dp, skip_updates=True)
