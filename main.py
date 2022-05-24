import datetime
import random
from vkbottle.bot import Bot, Message, MessageEvent
from vkbottle import Keyboard, keyboard_gen, KeyboardButtonColor, Text, OpenLink, Location, EMPTY_KEYBOARD, \
    GroupEventType, DocMessagesUploader, PhotoMessageUploader
import keyboards
import DataBase
from pagoda import pagoda, pagoda_t
from rasp import rasp, rasp_day
import json
import asyncio

bot = Bot('')
bot.labeler.vbml_ignore_case = True


# button start
@bot.on.private_message(text=['привет', 'начать', 'ку'])
async def msg(message: Message):
    await message.answer('Здравствуйте, вас привествует чат-бот для помощи студентам университета УрГПУ', keyboard=keyboards.keyboard)
    if DataBase.check_id(message.from_id):
        await message.answer('Ты уже есть у нас в базе')
    else:
        DataBase.vnosim_id(message.from_id)
        await message.answer('Добавили тебя в базу')


# button schedule
@bot.on.message(text=['Расписание', 'расписание'])
async def msg_handler(message: Message):
    await message.answer('Напишите группу \n Пример: группа исит-1801 <ближайшее> или <15 апреля>')


@bot.on.message(text=['группа <group>', 'группа', 'Группа <group>'])
async def schedule(message: Message, group=None):
    if group is not None:
        try:
            d = len(group.split()) < 3
            if d == 1:
                group = group.split()[0]
                ld = rasp(group.split()[0])
                await message.answer(ld)
            elif d == 0:
                dt = (group.split()[1] + ' ' + group.split()[2])
                group = group.split()[0]
                ld = rasp_day(group, dt)
                await message.answer(ld)
        except:
            return 'Технические шоколадки'
    else:
        return 'Вы забыли написать группу'


# button studies

@bot.on.private_message(text='Учеба')
async def notStudy(message: Message):
    await message.answer('&#12288;', keyboard=keyboards.keyboardStudy)


@bot.on.private_message(text='График УП по направлениям подготовки')
async def EPS(message: Message):
    b = await bot.api.messages.get_history(user_id=message.from_id, count=1, offset=1)
    await message.answer('&#12288;', keyboard=keyboards.keyboardEPS)
    b = b.items[0].conversation_message_id
    await bot.api.messages.delete(peer_id=message.from_id, cmids=b,
                                  delete_for_all=True)


@bot.on.private_message(text='График учебного процесса бакалавриат')
async def EPS_1bak(message: Message):
    b = await bot.api.messages.get_history(user_id=message.from_id, count=1, offset=1)
    doc_upd = DocMessagesUploader(bot.api)
    doc = await doc_upd.upload('График учебного процесса бакалавриат.pdf', '!Documents/ГУПБ.pdf',
                               peer_id=message.peer_id)
    await message.answer('&#12288;', keyboard=keyboards.keyboard, attachment=doc)
    b = b.items[0].conversation_message_id
    await bot.api.messages.delete(peer_id=message.from_id, cmids=b,
                                  delete_for_all=True)


@bot.on.private_message(text='График учебного процесса магистратура')
async def EPS_2mag(message: Message):
    b = await bot.api.messages.get_history(user_id=message.from_id, count=1, offset=1)
    doc_upd = DocMessagesUploader(bot.api)
    doc = await doc_upd.upload('График учебного процесса магистратура.pdf', '!Documents/ГУПМ.pdf',
                               peer_id=message.peer_id)
    await message.answer('&#12288;', keyboard=keyboards.keyboard, attachment=doc)
    b = b.items[0].conversation_message_id
    await bot.api.messages.delete(peer_id=message.from_id, cmids=b,
                                  delete_for_all=True)


@bot.on.private_message(text='График учебного процесса ИСИТ')
async def EPS_3ISIT(message: Message):
    b = await bot.api.messages.get_history(user_id=message.from_id, count=1, offset=1)
    doc_upd = DocMessagesUploader(bot.api)
    doc = await doc_upd.upload('График учебного процесса ИСИТ.pdf', '!Documents/ГУПИСИТ.pdf',
                               peer_id=message.peer_id)
    await message.answer('&#12288;', keyboard=keyboards.keyboard, attachment=doc)
    b = b.items[0].conversation_message_id
    await bot.api.messages.delete(peer_id=message.from_id, cmids=b,
                                  delete_for_all=True)

@bot.on.private_message(text='УП на семестр по направлениям, курсам')
async def ZO(message: Message):
    b = await bot.api.messages.get_history(user_id=message.from_id, count=1, offset=1)
    await message.answer('&#12288;', keyboard=keyboards.keyboardZO)
    b = b.items[0].conversation_message_id
    await bot.api.messages.delete(peer_id=message.from_id, cmids=b,
                                  delete_for_all=True)

@bot.on.private_message(text='Заочное')
async def EPS_3ISIT(message: Message):
    b = await bot.api.messages.get_history(user_id=message.from_id, count=1, offset=1)
    doc_upd = DocMessagesUploader(bot.api)
    doc = await doc_upd.upload('График учебного процесса заочное.rar', '!Documents/Z/RUPy_zaochka_2_semestrr.rar',
                               peer_id=message.peer_id)
    await message.answer('&#12288;', keyboard=keyboards.keyboard, attachment=doc)
    b = b.items[0].conversation_message_id
    await bot.api.messages.delete(peer_id=message.from_id, cmids=b,
                                  delete_for_all=True)

@bot.on.private_message(text='Очное')
async def EPS_3ISIT(message: Message):
    b = await bot.api.messages.get_history(user_id=message.from_id, count=1, offset=1)
    doc_upd = DocMessagesUploader(bot.api)
    doc = await doc_upd.upload('График учебного процесса очное.rar', '!Documents/B/RUPy_ochka_2_semestrr.rar',
                               peer_id=message.peer_id)
    await message.answer('&#12288;', keyboard=keyboards.keyboard, attachment=doc)
    b = b.items[0].conversation_message_id
    await bot.api.messages.delete(peer_id=message.from_id, cmids=b,
                                  delete_for_all=True)

# button position
@bot.on.private_message(text='Положения')
async def Position(message: Message):
    await message.answer('&#12288;', keyboard=keyboards.keyboardPosition)


@bot.on.private_message(text='Положение о промежуточной аттестации')
async def Position_1att(message: Message):
    b = await bot.api.messages.get_history(user_id=message.from_id, count=1, offset=1)
    doc_upd = DocMessagesUploader(bot.api)
    doc = await doc_upd.upload('Положение о промежуточной аттестации.pdf', '!Documents/Положение опа.pdf',
                               peer_id=message.peer_id)
    await message.answer('&#12288;', keyboard=keyboards.keyboard, attachment=doc)
    b = b.items[0].conversation_message_id
    await bot.api.messages.delete(peer_id=message.from_id, cmids=b,
                                  delete_for_all=True)


@bot.on.private_message(text='Курсовые работы')
async def Position_2kurw(message: Message):
    b = await bot.api.messages.get_history(user_id=message.from_id, count=1, offset=1)
    doc_upd = DocMessagesUploader(bot.api)
    doc = await doc_upd.upload('Курсовые работы.pdf', '!Documents/ПоКР.pdf',
                               peer_id=message.peer_id)
    await message.answer('&#12288;', keyboard=keyboards.keyboard, attachment=doc)
    b = b.items[0].conversation_message_id
    await bot.api.messages.delete(peer_id=message.from_id, cmids=b,
                                  delete_for_all=True)


@bot.on.private_message(text='Положение о ВКР')
async def Position_1vkr(message: Message):
    b = await bot.api.messages.get_history(user_id=message.from_id, count=1, offset=1)
    doc_upd = DocMessagesUploader(bot.api)
    doc = await doc_upd.upload('Положение о ВКР.pdf', '!Documents/ПоВКР.pdf',
                               peer_id=message.peer_id)
    await message.answer('&#12288;', keyboard=keyboards.keyboard, attachment=doc)
    b = b.items[0].conversation_message_id
    await bot.api.messages.delete(peer_id=message.from_id, cmids=b,
                                  delete_for_all=True)


# button Contacts
@bot.on.private_message(text='Контакты')
async def contacts(message: Message):
    await message.answer('&#12288;', keyboard=keyboards.keyboardContacts)


@bot.on.private_message(text='Директор')
async def director(message: Message):
    b = await bot.api.messages.get_history(user_id=message.from_id, count=1, offset=1)
    ph_upd = PhotoMessageUploader(bot.api)
    ph = await ph_upd.upload('!Photo/Директор.png', peer_id=message.peer_id)
    await message.answer('Антипова Елена Петровна' + '\n' +
                         'Директор института математики, физики, информатики и технологий' +
                         '\n' + 'пр. Космонавтов, 26, кабинет 464' + '\n' +
                         '+7(343)235-76-02' + '\n' + 'antipova@uspu.me', attachment=ph,
                         keyboard=keyboards.keyboard)
    b = b.items[0].conversation_message_id
    await bot.api.messages.delete(peer_id=message.from_id, cmids=b,
                                  delete_for_all=True)


@bot.on.private_message(text='Дирекция')
async def directorate(message: Message):
    b = await bot.api.messages.get_history(user_id=message.from_id, count=1, offset=1)
    await message.answer(
        "Дирекция института математики, физики, информатики и технологий" + "\n" + "пр. Космонавтов, 26, каб. 462, 464" + "\n" +
        "+7 (343) 235-76-29" + "\n" + "+7 (343) 235-76-47" + "\n" + "ifit.dekanat@yandex.ru" + "\n" + "График работы:" + "\n" +
        "ПН-ПТ 9:00-17:00" + "\n" + "СБ, ВС - выходной", keyboard=keyboards.keyboard)
    b = b.items[0].conversation_message_id
    await bot.api.messages.delete(peer_id=message.from_id, cmids=b,
                                  delete_for_all=True)


@bot.on.private_message(text='Заведующие кафедрами')
async def zavKaf(message: Message):
    b = await bot.api.messages.get_history(user_id=message.from_id, count=1, offset=1)
    await message.answer('&#12288;', keyboard=keyboards.keyboardZavKaf)
    b = b.items[0].conversation_message_id
    await bot.api.messages.delete(peer_id=message.from_id, cmids=b,
                                  delete_for_all=True)


@bot.on.private_message(text='Специалисты по УМР')
async def psycho(message: Message):
    b = await bot.api.messages.get_history(user_id=message.from_id, count=1, offset=1)
    await message.answer('Специалист по УМР (очная форма)' + "\n" +
                         'Спас Татьяна Леонидовна' + "\n" +
                         'каб. № 259, +7 (343) 235-76-45, spastl_ipipd@mail.ru' + "\n" +
                         'Специалист по УМР (заочная форма)' + "\n" +
                         'Колясникова Виталина Борисовна' + "\n" +
                         'каб. № 271, +7 (343) 336-14-13, zaochnoe.ipipd@uspu.ru' + '\n' +
                         'Мальчихина Юлия Николаевна' + '\n' +
                         'каб. № 269, +7(343)336-15-40, zaochnoe.ipipd@uspu.ru', keyboard=keyboards.keyboard)
    b = b.items[0].conversation_message_id
    await bot.api.messages.delete(peer_id=message.from_id, cmids=b,
                                  delete_for_all=True)


@bot.on.private_message(text='Кафедра ФТиМОФиТ')
async def physics(message: Message):
    b = await bot.api.messages.get_history(user_id=message.from_id, count=1, offset=1)
    ph_upd = PhotoMessageUploader(bot.api)
    ph = await ph_upd.upload('!Photo/Кафедра ФТиМОФиТ.png', peer_id=message.peer_id)
    await message.answer("Усольцев Александр Петрович" + "\n" +
                         "Заведующий кафедрой физики, технологии и методики обучения физике и технологии" + "\n" + "пр. Космонавтов, 26, кабинет 459" + "\n" +
                         "+7(922)118-44-46" + "\n" + "alusolzev@gmail.com", attachment=ph, keyword=keyboards.keyboard)
    b = b.items[0].conversation_message_id
    await bot.api.messages.delete(peer_id=message.from_id, cmids=b, delete_for_all=True)


@bot.on.private_message(text='Кафедра ИИТиМОИ')
async def ifit(message: Message):
    b = await bot.api.messages.get_history(user_id=message.from_id, count=1, offset=1)
    ph_upd = PhotoMessageUploader(bot.api)
    ph = await ph_upd.upload('!Photo/Кафедра ИИТиМОИ.png', peer_id=message.peer_id)
    await message.answer("Рожина Ирина Венокентьевна" + "\n" +
                         "Заведующая кафедрой информатики, информационных технологий и методики обучения информатике" + "\n" +
                         "ул. Карла Либкнехта, 9, кабинет 3б" + "\n" +
                         "+7(343)235-76-57" + "\n" + "irozhina@ya.ru", attachment=ph, keyword=keyboards.keyboard)
    b = b.items[0].conversation_message_id
    await bot.api.messages.delete(peer_id=message.from_id, cmids=b, delete_for_all=True)


@bot.on.private_message(text='Кафедра ВМиМОМ')
async def math(message: Message):
    b = await bot.api.messages.get_history(user_id=message.from_id, count=1, offset=1)
    ph_upd = PhotoMessageUploader(bot.api)
    ph = await ph_upd.upload('!Photo/Кафедра ВМиМОМ.png', peer_id=message.peer_id)
    await message.answer("Бодряков Владимир Юрьевич" + "\n" +
                         "Заведующий кафедрой высшей математики и методики обучения математике" + "\n" +
                         "пр. Космонавтов, 26, кабинет 465" + "\n" +
                         "+7(343)235-76-59" + "\n" + "Bodryakov_VYu@e1.ru", attachment=ph, keyword=keyboards.keyboard)
    b = b.items[0].conversation_message_id
    await bot.api.messages.delete(peer_id=message.from_id, cmids=b, delete_for_all=True)


# Questions txt
@bot.on.private_message(text='Questions')
async def questions(message: Message):
    doc_upd = DocMessagesUploader(bot.api)
    doc = await doc_upd.upload('Questions.txt', '!Documents/Questions.txt', peer_id=message.peer_id)
    await message.answer(attachment=doc)


@bot.on.private_message(text='Назад')
async def back(message: Message):
    b = await bot.api.messages.get_history(user_id=message.from_id, count=1, offset=1)
    await message.answer('&#12288;', keyboard=keyboards.keyboard)
    b = b.items[0].conversation_message_id
    await bot.api.messages.delete(peer_id=message.from_id, cmids=b,
                                  delete_for_all=True)


@bot.on.private_message(text='Выход')
async def handler(message: Message):
    b = await bot.api.messages.get_history(user_id=message.from_id, count=1, offset=1)
    await message.answer("Чем могу вам помочь?", keyboard=keyboards.keyboard)
    b = b.items[0].conversation_message_id
    await bot.api.messages.delete(peer_id=message.from_id, cmids=b,
                                  delete_for_all=True)


# mainlinglist
@bot.on.private_message(text=['Рассылка', 'рассылка'])
async def mailinglist(message: Message):
    if DataBase.check_is_admin(message.from_id):
        rows = DataBase.get_sql('SELECT * FROM ids')
        rassilka = open('!Documents/Рассылка.txt', 'r', encoding="utf-8")
        textmsg = rassilka.read()
        for row in rows:
            try:
                await bot.api.messages.send(user_id=row[0], message=textmsg, random_id=random.randint(0, 2048),
                                            keyboards=keyboards.keyboard)
                await bot.api.messages.send(sticker_id=51590, user_id=row[0], random_id=random.randint(0, 2048),
                                            keyboards=keyboards.keyboard)
            except:
                continue
    else:
        await message.answer('У вас нет прав, ВЫ ЖЕНЩИНА', keyboards=keyboards.keyboard)


@bot.on.private_message()
async def anyoneprivate(message: Message):
    list = ['Я вас не понимаю', 'что', 'чего']
    await message.answer(random.choice(list))
    uid = message.peer_id
    usr_info = await bot.api.users.get(message.from_id)
    f = open('!Documents/Questions.txt', 'a+', encoding='utf-8')
    dt = datetime.datetime.now()
    dt_s = dt.strftime("%d/%m/%Y %H:%M")
    f.write(
        str(uid) + " | " + usr_info[0].first_name + " " + usr_info[0].last_name + " | " + message.text + " | " + dt_s)
    f.write('\n')
    f.close()


# событие (callback)
@bot.on.raw_event(GroupEventType.MESSAGE_EVENT, dataclass=MessageEvent)
async def handle_message_event(event: MessageEvent):
    await bot.api.messages.send_message_event_answer(
        event_id=event.object.event_id,
        user_id=event.object.user_id,
        peer_id=event.object.peer_id,
        event_data=json.dumps(event.payload))


# беседы
@bot.on.chat_message(text=['погода <day>', 'Погода <day>'])
async def weather(message: Message, day='сегодня'):
    if day == 'сегодня':
        pp = pagoda(day)
        await message.answer(pp)
    elif day == 'завтра':
        ppt = pagoda_t(day)
        await message.answer(ppt)
    else:
        await message.answer('Вы ввели что то не так')


@bot.on.chat_message(text=['/help'])
async def helper(message: Message):
    await message.answer(
        'У меня есть две команды \n/Для расписания: группа <исит-1801> <ближайшее> или <20 апреля> \nдля погоды: погода на <сегодня> или <завтра>')


@bot.on.chat_message()
async def anyone(message: Message):
    user = await bot.api.users.get(message.from_id)
    await message.answer(f'@id{message.from_id}({user[0].first_name}), Ты что дурачок? Пиши /bot -> help')
    await asyncio.sleep(5)
    await bot.api.messages.edit(peer_id=message.peer_id,
                                message=f'Ну давай уже, @id{message.from_id}({user[0].first_name})',
                                conversation_message_id=message.conversation_message_id + 1)


print('Бот запущен')
bot.run_forever()
