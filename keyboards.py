import json


def get_but(text, color, type, payload):
    return {
        "action": {
            "type": f"{type}",
            "payload": f"{payload}",
            "label": f"{text}"
        },
        "color": f"{color}"
    }


keyboard = {
    "one_time": False,
    "buttons": [
        [get_but('Контакты', 'primary', 'text', ''), get_but('Расписание', 'primary', 'text', '')],
        [get_but('Положения', 'primary', 'text', ''), get_but('Учеба', 'primary', 'text', '')]
    ]
}

keyboardStudy = {
    "one_time": False,
    "buttons": [
        [get_but('График УП по направлениям подготовки', 'primary', 'text', '')],
        [get_but('УП на семестр по направлениям, курсам', 'primary', 'text', '')],
        [get_but('Назад', 'negative', 'text', '')]
    ],
    "inline": False
}
keyboardEPS = {
    "one_time": False,
    "buttons": [
        [get_but('График учебного процесса бакалавриат', 'primary', 'text', '')],
        [get_but('График учебного процесса магистратура', 'primary', 'text', '')],
        [get_but('График учебного процесса ИСИТ', 'primary', 'text', '')],
        [get_but('Назад', 'negative', 'text', '')]
    ],
    "inline": False
}
keyboardZO = {
    "one_time": False,
    "buttons": [
        [get_but('Заочное', 'primary', 'text', '')],
        [get_but('Очное', 'primary', 'text', '')],
        [get_but('Назад', 'negative', 'text', '')]
    ],
    "inline": False
}
keyboardPosition = {
    "one_time": False,
    "buttons": [
        [get_but('Положение о промежуточной аттестации', 'primary', 'text', '')],
        [get_but('Курсовые работы', 'primary', 'text', '')],
        [get_but('Положение о ВКР', 'primary', 'text', '')],
        [get_but('Назад', 'negative', 'text', '')]
    ],
    "inline": False
}

keyboardContacts = {
    "one_time": False,
    "buttons": [
        [get_but('Директор', 'primary', 'text', ''), get_but('Дирекция', 'primary', 'text', '')],
        [get_but('Специалисты по УМР', 'primary', 'text', ''), get_but('Заведующие кафедрами', 'primary', 'text', '')],
        [get_but('Назад', 'negative', 'text', '')]

    ],
    "inline": False
}
keyboardZavKaf = {
    "one_time": False,
    "buttons": [
        [get_but('Кафедра ФТиМОФиТ', 'primary', 'text', '')],
        [get_but('Кафедра ИИТиМОИ', 'primary', 'text', '')],
        [get_but('Кафедра ВМиМОМ', 'primary', 'text', '')],
        [get_but('Назад', 'negative', 'text', '')]
    ],
    "inline": False
}
keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
keyboard = str(keyboard.decode('utf-8'))

keyboardStudy = json.dumps(keyboardStudy, ensure_ascii=False).encode('utf-8')
keyboardStudy = str(keyboardStudy.decode('utf-8'))

keyboardPosition = json.dumps(keyboardPosition, ensure_ascii=False).encode('utf-8')
keyboardPosition = str(keyboardPosition.decode('utf-8'))

keyboardEPS = json.dumps(keyboardEPS, ensure_ascii=False).encode('utf-8')
keyboardEPS = str(keyboardEPS.decode('utf-8'))

keyboardZO = json.dumps(keyboardZO, ensure_ascii=False).encode('utf-8')
keyboardZO = str(keyboardZO.decode('utf-8'))

keyboardContacts = json.dumps(keyboardContacts, ensure_ascii=False).encode('utf-8')
keyboardContacts = str(keyboardContacts.decode('utf-8'))

keyboardZavKaf = json.dumps(keyboardZavKaf, ensure_ascii=False).encode('utf-8')
keyboardZavKaf = str(keyboardZavKaf.decode('utf-8'))
