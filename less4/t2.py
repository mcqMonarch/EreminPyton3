import pyttsx3


def monax(count, s, f):
    if count == 1:
        # return 1
        print(f'перенести диск {count} со стержня {s} на стержень {f}')
    else:
        temp = 6 - s - f
        monax(count - 1, s, temp)
        print(f'перенести диск {count} со стержня {s} на стержень {f}')
        # pyttsx3.speak(f'перенести диск {count} со стержня {s} на стержень {f}')
        monax(count - 1, temp, f)


def monax2(count, s, f):
    if count > 0:
        temp = 6 - s - f
        monax(count - 1, s, temp)
        print(f'перенести диск {count} со стержня {s} на стержень {f}')
        # pyttsx3.speak(f'перенести диск {count} со стержня {s} на стержень {f}')
        monax(count - 1, temp, f)


monax2(4, 1, 3)
