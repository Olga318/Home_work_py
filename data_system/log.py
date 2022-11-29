from datetime import datetime as dt


def log_info(action):
    act = ''
    if action == '1':
        act = 'register'
    elif action == '2':
        act = 'read'
    time = dt.now().strftime("%d:%m:%Y  %H:%M:%S")
    with open('log.txt', 'a', encoding='utf-8') as rec:
        rec.write(f'Время события: {act} {time}'+'\n')
