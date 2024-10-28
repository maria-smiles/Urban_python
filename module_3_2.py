# Задача "Рассылка писем":
#
# Часто при разработке и работе с рассылками писем(e-mail) они отправляются
# от одного и того же пользователя(администрации или службы поддержки).
# Тем не менее должна быть возможность сменить его в редких случаях.
#
# Попробуем реализовать функцию с подробной логикой.


def send_email(message, recipient, sender="university.help@gmail.com"):
# Проверка на корректность e-mail отправителя и получателя.
    recipient_suff = recipient.endswith(".com") or recipient.endswith(".ru" ) or recipient.endswith(".net")
    sender_suff = sender.endswith(".com") or sender.endswith(".ru") or sender.endswith(".net")
    if ('@' not in recipient or '@' not in sender)\
        or recipient_suff == False\
        or sender_suff == False:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')

# Проверка на отправку самому себе.
    elif sender == recipient:
        print("Нельзя отправить письмо самому себе!")

# Проверка на отправителя по умолчанию.
    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    elif sender != "university.help@gmail.com":
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")




send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')

send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')

send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')

send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
