import urwid


def is_very_long(password):
    return len(password) > 12


def has_digit(password):
    return any(char.isdigit() for char in password)


def has_letters(password):
    return any(char.isalpha() for char in password)


def has_upper_letters(password):
    return any(char.isupper() for char in password)


def has_lower_letters(password):
    return any(char.islower() for char in password)


def has_symbols(password):
    return any(not i.isalnum() for i in password)


def on_ask_change(edit, new_edit_text):
    conditions = [
        is_very_long,
        has_digit,
        has_letters,
        has_upper_letters,
        has_lower_letters,
        has_symbols
    ]
    rating = 0
    for i in conditions:
        if i(new_edit_text):
            rating += 2
    reply.set_text("Рейтинг: %s" % rating)


if __name__ == "__main__":
    ask = urwid.Edit('Тайный ввод: ', mask='*')
    reply = urwid.Text("")
    menu = urwid.Pile([ask, reply])
    menu = urwid.Filler(menu, valign='top')
    urwid.connect_signal(ask, 'change', on_ask_change)
    urwid.MainLoop(menu).run()