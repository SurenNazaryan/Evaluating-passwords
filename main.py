import urwid


def on_ask_change(edit, new_edit_text):
    rating = 0
    conditions = []

    def is_very_long(password):
        return len(password) > 12

    conditions.append(is_very_long)

    def has_digit(password):
        return any(char.isdigit() for char in password)

    conditions.append(has_digit)

    def has_letters(password):
        return any(char.isalpha() for char in password)

    conditions.append(has_letters)

    def has_upper_letters(password):
        return any(char.isupper() for char in password)

    conditions.append(has_upper_letters)

    def has_lower_letters(password):
        return any(char.islower() for char in password)

    conditions.append(has_lower_letters)

    def has_symbols(password):
        return any(not i.isalnum() for i in password)

    conditions.append(has_symbols)

    for i in conditions:
        if i(new_edit_text):
            rating += 2
    reply.set_text("Рейтинг: %s" % rating)


if __name__ == '__main__':
    ask = urwid.Edit('Тайный ввод: ', mask='*')
    reply = urwid.Text("")
    menu = urwid.Pile([ask, reply])
    menu = urwid.Filler(menu, valign='top')
    urwid.connect_signal(ask, 'change', on_ask_change)
    urwid.MainLoop(menu).run()
