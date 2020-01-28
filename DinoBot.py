from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import email.mime.application
from telebot import types
import telebot, smtplib
import mimetypes
import email


dino_bot = telebot.TeleBot('990880941:AAG5YGQJzogEWHHcFf76JAFD57pren3npB8')

main_menu_markup = types.ReplyKeyboardMarkup(row_width=1)

#order_a_bot = types.KeyboardButton('Заказать бота')
contact = types.KeyboardButton('Контакты')
call_a_consultant = types.KeyboardButton('Вызвать консультанта')
faq = types.KeyboardButton('F.A.Q.')

main_menu_markup.add(contact, call_a_consultant, faq)


FAQ_markup = types.ReplyKeyboardMarkup(row_width=1)

what_is_a_telegram_bot = types.KeyboardButton('Что такое Telegram бот?')
why_should_start_a_bot = types.KeyboardButton('Почему вам стоит завести Telegram бота?')
what_you_need_to_do_to_order_a_bot = types.KeyboardButton('Что нужно сделать для того чтобы заказать Telegram бота?')
what_is_the_terms_of_referenct = types.KeyboardButton('Что такое техническое задание и как его составить?')
where_to_place_the_bot = types.KeyboardButton('Куда мне размещать бота по окончанию заказа?')
how_much_does_the_bot_cost = types.KeyboardButton('Сколько стоит Telegram бот?')
how_long_will_the_bot_be_ready = types.KeyboardButton('За какой срок вы сделаете мне бота?')
examples_of_works = types.KeyboardButton('У вас есть примеры работ?')
go_back = types.KeyboardButton('Назад')

FAQ_markup.add(what_is_a_telegram_bot, why_should_start_a_bot, what_you_need_to_do_to_order_a_bot, what_is_the_terms_of_referenct, where_to_place_the_bot, how_much_does_the_bot_cost, how_long_will_the_bot_be_ready, examples_of_works, go_back)


Back_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

stop_order = types.KeyboardButton('Отмена')

Back_markup.add(stop_order)
@dino_bot.message_handler(commands=['start', 'help'])
def Greeting(message):
    dino_bot.reply_to(message, 'Здравствуйте, я корпоративный бот компании DinoBot и я готов ответить на все ваши вопросы. Должен предупредить, что для того чтобы вызвать консультанта или сделать заказ - необходимо чтобы у вас был ник в Телеграме, иначе я не смогу узнать, кому требуется помощь!', reply_markup=main_menu_markup)
    
@dino_bot.message_handler(regexp='Контакты')
def Contact(message):
     dino_bot.reply_to(message, 'Мессендежры и соц сети: \n 1.Мой создатель и главный администратор по совместительству: @spectralxlx \n 2.Мы в Instagram: https://www.instagram.com/dino_bot_inc/ \n Наши почтовые ящики: \n 1.Mail: dino.bot@bk.ru \n2.GMail: Dino.Bot.INC@gmail.com',reply_markup=main_menu_markup)

@dino_bot.message_handler(regexp='Заказать бота')
def Order(message):
    dino_bot.reply_to(message, 'Отправьте ваше техническое задание (формат .docx)', reply_markup=Back_markup)
    dino_bot.register_next_step_handler(message, GetSpecification)

@dino_bot.message_handler(regexp='Вызвать консультанта')               
def Call_a_consultant(message):
    username = message.from_user.username
    
    msg = MIMEMultipart()
    msg['Subject'] = 'Клиент вызывает консультанта'
    msg['From'] = 'Dino.Bot.INC@gmail.com'
    msg['To'] = 'Dino.Bot.INC@gmail.com'

    msg.attach(MIMEText('Клиент вызывает консультанта. ID клиента: ' + str(username)))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('Dino.Bot.INC@gmail.com', 'RzdrINx4e5')
    server.send_message(msg)
    server.quit()

    dino_bot.reply_to(message, 'Ваш запрос был обработан успешно. В скором времени, вам напишет один из наших администраторов. Пожалуйста, ожидайте.',reply_markup=main_menu_markup)

@dino_bot.message_handler(regexp='F.A.Q.')
def FAQ(message):
     dino_bot.reply_to(message, 'F.A.Q. - часто задаваемые вопросы. Здесь мы собрали самые частые вопросы к нам и ответили на них.', reply_markup=FAQ_markup)

@dino_bot.message_handler(regexp='Что такое Telegram бот?')
def WhatIsTelegramBot(message):
     dino_bot.reply_to(message, 'Это программа, которая выполняет различного рода действия в автоматическом режиме, либо по команде или заданному расписанию.')

@dino_bot.message_handler(regexp='Почему вам стоит завести Telegram бота?')
def WhyYouShouldStartATelegramBot(message):
    dino_bot.reply_to(message, 'Telegram боты могут выполнять множество интересных задач и автоматизировать различные рутинные действия. Например, автоматическая рассылка новостей всем подписчикам канала. Помимо того, Telegram бот может выступать альтернативой целому мобильному приложению и стоить при этом гораздо дешевле.')

@dino_bot.message_handler(regexp='Что нужно сделать для того чтобы заказать Telegram бота?')
def WhatDoINeedToDoToOrderATelegramBot(message):
    dino_bot.reply_to(message, 'Для начала, необходимо составить техническое задание, реализовать его как можно более детально. Далее, вы можете оформить у нас заказ. Вы можете написать нам на Mail (dino.bot@bk.ru) или GMail (Dino.Bot.INC@gmail.com), либо оформить заказ у нашего корпоративного бота. Для того чтобы оформить заказ у нашего корпоративного бота вам необходимо перейти в главное меню, после чего нажать кнопку "Заказать бота".')
    
@dino_bot.message_handler(regexp='Что такое техническое задание и как его составить?')
def WhatIsTheTermsOfReference(message):
    dino_bot.reply_to(message, 'Это такой документ, где должны быть описаны все детали функционирования бота. То, как всё должно работать и какой функционал должен присутствовать, всё то, что вы видите в своём будущем боте. Подобная формальность необходима для того, чтобы наши программисты понимали, какой функционал вы ждёте в итоге. Вы можете составить его по нашему образцу: *ссылка* или попросить у нас помощи с его составлением. Мы вам обязательно поможем!')

@dino_bot.message_handler(regexp='Куда мне размещать бота по окончанию заказа?')
def WhereShouldIPlaceTheBot(message):
    dino_bot.reply_to(message, 'Вы можете разместить его на хостинге или своем персональном компьютере, однако чаще всего выбирают первый вариант т.к. он является наиболее бюджетным и простым. Вы можете разместить бота на хостинге самостоятельно или попросить помощи с его размещением у нас (это совершенно бесплатно!)')

@dino_bot.message_handler(regexp='Сколько стоит Telegram бот?')
def HowMuchDoesTheBotCost(message):
    dino_bot.reply_to(message, 'К сожалению, нет фиксированной и приблизительной цены. Совсем нет. Цена формируется из функционала который вам необходим. Мы сможем назначить цену только после того, как увидим ваше техническое задание.')

@dino_bot.message_handler(regexp='За какой срок вы сделаете мне бота?')
def ForHowLong(message):
    dino_bot.reply_to(message, 'К сожалению, тут всё так же, как и с ценой. Всё зависит от технического задания. Лишь после того, как мы увидим ваше техническое задание - тогда и будет назначена конкретная цена.')

@dino_bot.message_handler(regexp='У вас есть примеры работ?')
def ExamplesOfWorks(message):
    dino_bot.reply_to(message, 'Безусловно есть. С одним из примеров вы сейчас ведете диалог ;) Вот еще некоторые наши примеры: @Roger86bot \n @Elliot86Bot \n @Venturesome_bot')
    
@dino_bot.message_handler(regexp='Назад')
def GetBack(message):
    dino_bot.reply_to(message, 'Здравствуйте, я корпоративный бот компании DinoBot и я готов ответить на все ваши вопросы.', reply_markup=main_menu_markup)

@dino_bot.message_handler(regexp='Отмена')
def StopTheOrder(message):
    dino_bot.reply_to(message, 'Здравствуйте, я корпоративный бот компании DinoBot и я готов ответить на все ваши вопросы.', reply_markup=main_menu_markup)
    

dino_bot.polling(none_stop=True, timeout=10)
