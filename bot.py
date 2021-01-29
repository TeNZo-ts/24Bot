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
button_10a = KeyboardButton('10(A)')
button_10ae = KeyboardButton('10(AE)')
button_10b = KeyboardButton('10(B)')
button_10v = KeyboardButton('10(V)')
# Timetable 10(ae)
button_timetable = KeyboardButton('Расписание')
# Zoom
button_monday = KeyboardButton('Понедельник')
button_tuesday = KeyboardButton('Вторник')
button_wednesday = KeyboardButton('Среда')
button_thursday = KeyboardButton('Четверг')
button_friday = KeyboardButton('Пятница')
# 10(ae)
infor = KeyboardButton('Информатика')
physEng = KeyboardButton('Физика (English)')
phystrain = KeyboardButton('Физкультура')
geo_phys = KeyboardButton('География/Физика')
kz = KeyboardButton('Казахский язык')
bio = KeyboardButton('Биология')
law_bas1 = KeyboardButton('Основы права (1-я гр.)')
kz_litr = KeyboardButton('Казахская литература')
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
law_bas2 = KeyboardButton('Основы права (2-я гр.)')
audarma = KeyboardButton('Аударма')
samo_pozn = KeyboardButton('Самопознание')
ist_kz = KeyboardButton('История Казахстана')
# Teachers 
Aizada_A = KeyboardButton('Айзада Адильханкызы')
Gulmira_A = KeyboardButton('Гульмира Апарбаева')
Aigerim_E = KeyboardButton('Айгерим Еркинбекова')
Maulet_K = KeyboardButton('Маулет Кисса')
Murat_B = KeyboardButton('Мурат Буланов')
Asem_B = KeyboardButton('Асем Буланова')
Asel_M = KeyboardButton('Асель Муханова')
Kyrmyzy_N = KeyboardButton('Кырмызы Нурахметова')
Gulbarshin_D = KeyboardButton('Гульбаршын Долаева')
Zhanna_B = KeyboardButton('Жанна Баелова')
Zhanna_Z = KeyboardButton('Жанна Жунисбекова')
Zhadyra_B = KeyboardButton('Жадыра Бекбаева')
Gulzhat_D = KeyboardButton('Гульшат Д.')
Zharkyn = KeyboardButton('Жаркын')
#Предметы для Daryn (a,e,o)
button_daryn_1 = KeyboardButton('Гeометрия')
button_daryn_2 = KeyboardButton('Физикa')
button_daryn_3 = KeyboardButton('Всeмирнaя истoрия')
button_daryn_4 = KeyboardButton('Истoрия Кaзaхстaнa')
button_daryn_5 = KeyboardButton('Кaзахский язык')
button_daryn_6 = KeyboardButton('Кaзахская литература')
button_daryn_7 = KeyboardButton('Xимия')
button_daryn_8 = KeyboardButton('Инфoрматика')
button_daryn_9 = KeyboardButton('Русcкий язык')
button_daryn_10 = KeyboardButton('Руcская литература')
button_daryn_11 = KeyboardButton('Основы права')
button_daryn_12 = KeyboardButton('Гeография')
#Темы Предметов
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

# Main
markup_back = ReplyKeyboardMarkup(resize_keyboard=True).add(button_back)
markup_menu = ReplyKeyboardMarkup(resize_keyboard=True).row(button_lyceum, button_daryn).add(button_info)
markup_DOsub = ReplyKeyboardMarkup(resize_keyboard=True).add(button_back)
# Classes
markup_classes = ReplyKeyboardMarkup(resize_keyboard=True).row(button_10a, button_10ae).row(button_10b, button_10v)
# Class 10AE
markup_week = ReplyKeyboardMarkup(resize_keyboard=True).row(button_monday, button_tuesday).row(button_wednesday, button_thursday, button_friday).row(button_timetable, button_back)
markup_mon = ReplyKeyboardMarkup(resize_keyboard=True).row(infor, physEng, phystrain).row(geo_phys).row(kz, bio, law_bas1).row(button_timetable, button_back)
markup_infor = ReplyKeyboardMarkup(resize_keyboard=True).row(Aizada_A, Gulmira_A)
markup_geo_phys = ReplyKeyboardMarkup(resize_keyboard=True).row(Aigerim_E, Maulet_K)
markup_tue = ReplyKeyboardMarkup(resize_keyboard=True).row(kz_litr, voen, class_hour).row(algebra, mir_ist).row(button_timetable, button_back)
markup_algebra = ReplyKeyboardMarkup(resize_keyboard=True).row(Murat_B, Asem_B)
markup_wed =ReplyKeyboardMarkup(resize_keyboard=True).row(phys_geo, geom, eng).add(eco).row(button_timetable, button_back)
markup_phys_geo = ReplyKeyboardMarkup(resize_keyboard=True).row(Maulet_K, Aigerim_E)
markup_geom = ReplyKeyboardMarkup(resize_keyboard=True).row(Murat_B, Asem_B)
markup_english = ReplyKeyboardMarkup(resize_keyboard=True).row(Asel_M, Kyrmyzy_N)
markup_thu = ReplyKeyboardMarkup(resize_keyboard=True).row(chem, rus_lit).add(ling).row(abai, phystrain, law_bas2).row(button_timetable, button_back)
markup_rus_lit = ReplyKeyboardMarkup(resize_keyboard=True).row(Zhanna_B, Zhanna_Z)
markup_ling = ReplyKeyboardMarkup(resize_keyboard=True).row(Zhadyra_B, Kyrmyzy_N)
markup_fri = ReplyKeyboardMarkup(resize_keyboard=True).row(physEng, audarma, geo_phys).row(phys_geo, samo_pozn, ist_kz).add(algebra).row(button_timetable, button_back)
markup_audarma = ReplyKeyboardMarkup(resize_keyboard=True).row(Gulzhat_D, Zharkyn)
# Daryn Online
markup_DO = ReplyKeyboardMarkup(resize_keyboard=True).add(button_back).row(button_daryn_1, button_daryn_2).row(button_daryn_3, button_daryn_4, button_daryn_5).row(button_daryn_6, button_daryn_7).row(button_daryn_8, button_daryn_9, button_daryn_10).row(button_daryn_11, button_daryn_12)
markup_ist_kz = ReplyKeyboardMarkup(resize_keyboard=True).add(answer_ist_kz_1).add(answer_ist_kz_2).add(answer_ist_kz_3).add(answer_ist_kz_4).add(answer_ist_kz_5).add(answer_ist_kz_6).add(answer_ist_kz_7).add(answer_ist_kz_8).add(answer_ist_kz_9).add(answer_ist_kz_10).add(answer_ist_kz_11).add(answer_ist_kz_12)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
	# Welcome!:)
	start = open('symbol.jpg', "rb")
	await bot.send_photo(message.chat.id, start, '🔔Добро пожаловать!🔔\nЯ бот🤖, выполняю команды моих разработчиков.\nМоя задача сэкономить вам приличное время и оказать незаменимую помощь!\n\nПриятного пользования!💫', reply_markup=markup_menu)

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
		await message.reply('Введите код доступа:\n\nЕсли у вас нет кода доступа, свяжитесь с Администрацией либо покиньте раздел.', reply_markup=markup_DOsub)
	# Info
	elif message.text == 'Info': 
		await message.reply('Привет👋\nЯ бот🤖, как Вы уже могли догадаться, моя работа быть Вам верным асситентом и оказывать помощь. Мои разработчики хорошо постарались и развивают проект с двух сторон и на достигнутом останавливаться не собираються👌\nПроект на стадии разработки и мы примем любую помощь. Если ваш класс отстутсвует, обратитесь к Администрации и мы его добавим - @TeNZo_ts\n\nКоманды:\n/start - Запустить бота\n/open - Открыть меню\n/close - Закрыть меню\n\nНа данный момент доступно:⤵️\n10(ае) класс: FULL\nDaryn Online\n\nБот обновляется ежедневно и становиться лучше каждым днем!🤟', reply_markup=markup_back)
	# Lyceum
	elif message.text == 'Lyceum':
		await message.reply('➡️', reply_markup=markup_classes)
	# CLASS A
	elif message.text == '10(A)':
		await message.reply('На данный момент доступен только класс "10(AE)". Разработка уже в процессе, ждите обновлений!➡️', reply_markup=markup_menu)
	# Class AE
	elif message.text == '10(AE)':
		timetable = open('tt10ae.jpg', "rb")
		await bot.send_photo(message.chat.id, timetable, '⚡️Ниже, выберите день недели, для получения идентификатора Zoom⤵️', reply_markup=markup_week)
	elif message.text == 'Расписание':
		timetable2 = open('tt10ae.jpg', "rb")
		await bot.send_photo(message.chat.id, timetable2, '➡️', reply_markup=markup_week)
	# CLASS B
	elif message.text == '10(B)':
		await message.reply('На данный момент доступен только класс "10(AE)". Разработка уже в процессе, ждите обновлений!➡️', reply_markup=markup_menu)
	# CLASS A
	elif message.text == '10(V)':
		await message.reply('На данный момент доступен только класс "10(AE)". Разработка уже в процессе, ждите обновлений!➡️', reply_markup=markup_menu)
	# Monday
	elif message.text == 'Понедельник':
		await message.reply('➡️', reply_markup=markup_mon)
	elif message.text == 'Информатика':
		await message.reply('Выберите своего учителя➡️', reply_markup=markup_infor)
	elif message.text == 'Айзада Адильханкызы':
		await message.answer('Информатика\nАйазада Адилханова -\nПодключиться:\nhttps://us04web.zoom.us/j/6739738314?pwd=UlQzc2hxcVR4QWlnMFQ3YTVnSjcxQT09\nИдентификатор: 673 973 8314\nКод: 112076', reply_markup=markup_week)
	elif message.text == 'Гульмира Апарбаева':
		await message.answer('Информатика\nГульмира Апарбаева -\nПодключиться:\nhttps://us04web.zoom.us/j/6671115307?pwd=K1JsQ3ZPczJVRHRNVGgrTlF6VVhiUT09\nИдентификатор: 667 111 5307\nКод: 551171', reply_markup=markup_week)
	elif message.text == 'Физика (English)':
		await message.answer('Физика\nКуаныш Жакпаев -\nПодключиться:\nhttps://us04web.zoom.us/j/5883286704?pwd=dG9sUkVkazFTNUEvTDJCcUNKNEUrQT09\nИдентификатор: 588 328 6704\nКод: 24', reply_markup=markup_week)
	elif message.text == 'Физкультура':
		await message.answer('Физкультура\nАзат Жақияұлы -\nПодключиться:https://us05web.zoom.us/j/9940612911?pwd=djNmdktPY0oyc2Iva2w0aXFBOXc2UT09\nИдентификатор: 994 061 2911\nКод: 24', reply_markup=markup_week)
	elif message.text == 'География/Физика':
		await message.reply('Выберите своего учителя➡️', reply_markup=markup_geo_phys)
	elif message.text == 'Айгерим Еркинбекова':
		await message.answer('География\nАйгерим Еркинбекова -\nПодключиться:\nhttps://us04web.zoom.us/j/6281342021?pwd=S3lZdERoT3lmVVJKeDJpN1djbE9oQT09\nИдентификатор: 628 134 2021\nКод:897756', reply_markup=markup_week)
	elif message.text == 'Маулет Кисса':
		await message.answer('Физика\nМаулет Кисса -\nПодключиться:\nhttps://us04web.zoom.us/j/5261561075?pwd=SUdYcXZoalFEVkhDV0RFN0U0NjZ1QT09\nИдентификатор: 526 156 1075\nКод: 172522', reply_markup=markup_week)
	elif message.text == 'Казахский язык':
		await message.answer('Казахский язык\nБакыт Нуркожаева -\nПодключиться:https://us04web.zoom.us/j/4865772347?pwd=SWhwNHNjRWE1TTlwRjJvZjFpNnphQT09\nИдентификатор: 486 577 2347\nКод: jBdv6e', reply_markup=markup_week)
	elif message.text == 'Биология':
		await message.answer('Биология\nДаулен Муталиев -\nПодключиться:\nhttps://us04web.zoom.us/j/5953647658?pwd=SFlWOU9YVXlnc1h4MXFYcUt3K3JyUT09\nИдентификатор: 595 364 7658\nКод: 434547', reply_markup=markup_week)
	elif message.text == 'Основы права (1-я гр.)':
		await message.answer('Основы права\nРысхан Байшыгашова -\nПодключиться:\nhttps://us04web.zoom.us/j/4182789875?pwd=S3Z2UG9taUlaajRVV05IUktHblMzdz09\nИдентификатор: 418 278 9875\nКод: 029958', reply_markup=markup_week)
	elif message.text == 'Вторник':
		await message.reply('➡️', reply_markup=markup_tue)
	elif message.text == 'Казахская литература':
		await message.answer('Казахская литература\nБақыт Нуркожаева -\nПодключиться:\nhttps://us04web.zoom.us/j/4865772347?pwd=SWhwNHNjRWE1TTlwRjJvZjFpNnphQT09\nИдентификатор: 486 577 2347\nКод: jBdv6e', reply_markup=markup_week)
	elif message.text == 'Военная подготовка':
		await message.answer('Военная подготовка\nАзат Жакиянов -\nПодключиться:\nhttps://us04web.zoom.us/j/4620412083?pwd=amV6eExyYUEzOXVUaGhYYURVcnVMQT09\nИдентификатор: 462 041 2083\nКод: 24', reply_markup=markup_week)
	elif message.text == 'Классный час':
		await message.answer('Классный час\nЖанна Баелова -\nПодключиться:\nhttps://us04web.zoom.us/j/9712435106?pwd=UlIwQ1B0b0M4MTJmVVFhSnMyNzBZQT09\nИдентификатор: 971 243 5106\nКод: 046044', reply_markup=markup_week)	
	elif message.text == 'Алгебра':
		await message.reply('Выберите своего учителя➡️', reply_markup=markup_algebra)
	elif message.text == 'Мурат Буланов':	
		await message.answer('Алгебра\nМурат Буланов -\nПодключиться:\nhttps://us04web.zoom.us/j/5803259738?pwd=QUphOEhPNlgzSmxMajkxV3VrbkhrZz09\nИдентификатор: 580 325 9738\nКод: 123456', reply_markup=markup_week)
	elif message.text == 'Асем Буланова':
		await message.answer('Алгебра\nАсем Буланова -\nПодключиться:\nhttps://us02web.zoom.us/j/2147576084?pwd=c3A0WjJqMHA5UjdlbjRYcVJ5ZGtqUT09\nИдентификатор: 214 757 6084\nКод: 24', reply_markup=markup_week)
	elif message.text == 'Всемирная история':
		await message.answer('Всемирная история\nРысхан Байшыгашова\nПодключиться:\nhttps://us04web.zoom.us/j/4182789875?pwd=S3Z2UG9taUlaajRVV05IUktHblMzdz09\nИдентификатор: 418 278 9875\nКод: 029958', reply_markup=markup_week)
	elif message.text == 'Среда':
		await message.reply('➡️', reply_markup=markup_wed)
	elif message.text == 'Физика/География':
		await message.reply('Выберите своего учителя➡️', reply_markup=markup_phys_geo)
	elif message.text == 'Mаулет Кисса':
		await message.answer('Физика\nМаулет Кисса -\nПодключиться:\nhttps://us04web.zoom.us/j/5261561075?pwd=SUdYcXZoalFEVkhDV0RFN0U0NjZ1QT09\nИдентификатор: 526 156 1075\nКод: 172522', reply_markup=markup_week)
	elif message.text == 'Aйгерим Еркинбекова':
		await message.answer('География \nАйгерим Еркинбекова -\nПодключиться:\nhttps://us04web.zoom.us/j/6281342021?pwd=S3lZdERoT3lmVVJKeDJpN1djbE9oQT09\nИдентификатор: 628 134 2021\nКод:897756', reply_markup=markup_week)
	elif message.text == 'Геометерия':
		await message.reply('Выберите своего учителя➡️', reply_markup=markup_geom)
	elif message.text == 'Mурат Буланов':	
		await message.answer('Алгебра\nМурат Буланов -\nПодключиться:\nhttps://us04web.zoom.us/j/5803259738?pwd=QUphOEhPNlgzSmxMajkxV3VrbkhrZz09\nИдентификатор: 580 325 9738\nКод: 123456', reply_markup=markup_week)
	elif message.text == 'Aсем Буланова':
		await message.answer('Алгебра\nАсем Буланова -\nПодключиться:\nhttps://us02web.zoom.us/j/2147576084?pwd=c3A0WjJqMHA5UjdlbjRYcVJ5ZGtqUT09\nИдентификатор: 214 757 6084\nКод: 24', reply_markup=markup_week)
	elif message.text == 'English':
		await message.reply('Выберите своего учителя➡️', reply_markup=markup_english)
	elif message.text == 'Асель Муханова':	
		await message.answer('English\nАсель Муханова -\nПодключиться:\nhttps://us04web.zoom.us/j/3705039375?pwd=dnl3SUpDTGVBR0NSYWhUVXl4dEtsZz09\nИдентификатор: 370 503 9375\nКод: 464196', reply_markup=markup_week)
	elif message.text == 'Кырмызы Нурахметова':	
		await message.answer('English\nКырмызы Нурахметова -\nПодключиться:\nhttps://us04web.zoom.us/j/3705039375?pwd=dnl3SUpDTGVBR0NSYWhUVXl4dEtsZz09\nИдентификатор: 370 503 9375\nКод: 464196', reply_markup=markup_week)
	elif message.text == 'Экономика':
		await message.answer('Экономика\nГульбаршын Долаева -\nПодключиться:\nhttps://us04web.zoom.us/j/6659425539?pwd=ak9PdEJqZnlhYkp0cTc5VkxRQW13UT09\nИдентификатор: 665 942 5539\nКод: 99999', reply_markup=markup_week)
	elif message.text == 'Четверг':
		await message.reply('➡️', reply_markup=markup_thu)
	elif message.text == 'Химия':
		await message.answer('Химия\nСаулетхан Амир -\nПодключиться:\nnone\nИдентификатор: none\nКод: none', reply_markup=markup_week)
	elif message.text == 'Русский язык и Литература':
		await message.reply('Выберите своего учителя➡️', reply_markup=markup_rus_lit)
	elif message.text == 'Жанна Баелова':
		await message.answer('Русский язык и Литература\nЖанна Баелова -\nПодключиться:\nhttps://us04web.zoom.us/j/9712435106?pwd=UlIwQ1B0b0M4MTJmVVFhSnMyNzBZQT09\nИдентификатор: 971 243 5106\nКод: 046044', reply_markup=markup_week)
	elif message.text == 'Жанна Жунисбекова':
		await message.answer('Русский язык и Литература\nЖанна Жунисбекова -\nПодключиться:\nhttps://us04web.zoom.us/j/3494752418?pwd=ZVZwYm5paUxoS3ZrNytUc3d5RWhYdz09\nИдентификатор: 349 475 2418\nКод: 453743', reply_markup=markup_week)
	elif message.text == 'Лингвистика':	
		await message.reply('Выберите своего учителя➡️', reply_markup=markup_ling)
	elif message.text == 'Жадыра Бекбаева':	
		await message.answer('Лингвистика\nЖадыра Бекбаева -\nПодключиться:\nhttps://us04web.zoom.us/j/8288810097?pwd=ellzVFpzVlFLT0JPU3ZOZ3A4WTE0QT09\nИдентификатор: 828 881 0097\nКод: 12345', reply_markup=markup_week)
	elif message.text == 'Абайтану':
		await message.answer('Абайтану\nБақыт Нуркожаева -\nПодключиться:\nhttps://us04web.zoom.us/j/4865772347?pwd=SWhwNHNjRWE1TTlwRjJvZjFpNnphQT09\nИдентификатор: 486 577 2347\nКод: jBdv6e', reply_markup=markup_week)
	elif message.text == 'Основы права (2-я гр.)':
		await message.answer('Основы права\nРысхан Байшыгашова -\nПодключиться:\nhttps://us04web.zoom.us/j/4182789875?pwd=S3Z2UG9taUlaajRVV05IUktHblMzdz09\nИдентификатор: 418 278 9875\nКод: 029958', reply_markup=markup_week)
	elif message.text == 'Пятница':
		await message.reply('➡️', reply_markup=markup_fri)
	elif message.text == 'Аударма':
		await message.reply('Выберите своего учителя➡️', reply_markup=markup_audarma)
	elif message.text == 'Гульшат Д.':
		await message.answer('Аударма\nГульшат Д. -\nПодключиться:\nhttps://us04web.zoom.us/j/6776997623?pwd=eWhSSUE5TlFGc2hmWXpsU0poSDFsZz09\nИдентификатор: 677 699 7623\nКод: 192105', reply_markup=markup_week)
	elif message.text == 'Жаркын':
		await message.answer('Аударма\nЖаркын -\nПодключиться:\n\nИдентификатор: 677 699 7623\nКод: 192105', reply_markup=markup_week)
	elif message.text == 'Самопознание':
		await message.answer('Самопознание\nСымбат Майкен -\nПодключиться:\nhttps://us04web.zoom.us/j/7661181251?pwd=RnpKN2RtUS9GSmw1VUNiMWZBUC9jUT09\nИдентификатор: 766 118 1251\nКод: FT6KE5', reply_markup=markup_week)
	elif message.text == 'История Казахстана':
		await message.answer('История Казахстана\nРысхан Байшыгашова -\nПодключиться:\nhttps://us04web.zoom.us/j/4182789875?pwd=S3Z2UG9taUlaajRVV05IUktHblMzdz09\nИдентификатор: 418 278 9875\nКод: 029958', reply_markup=markup_week)
	#Daryn
	elif message.text == '2San':
		await message.reply('Доступ получен\n\nВ наличии:\nИстория Казахстана - 12 тем\n\nВыберите предмет:', reply_markup=markup_DO)
	# ist_kz
	elif message.text == 'Истoрия Кaзaхстaнa':
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

# Обновление бота
if __name__ == '__main__':
	executor.start_polling(dp, skip_updates=True)