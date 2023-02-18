
poems = input('Введите стих : ')

def wp(a):
    volwes = ['а', 'о', 'э', 'е', 'и', 'ы', 'у', 'ё', 'ю', 'я']
    parts = a.split()
    syllable = list()
    for item in parts:
        k = 0
        for letter in item:
            if letter in volwes:
                k += 1
        syllable.append(k)
    if len(set(syllable)) == 1:
        print('Парам пам-пам')
    else:
        print('Пам парам')


wp(poems)

