import threading
import time
from lorem_text import lorem

locker = threading.Lock()


def analysis_text(text):
    # словарь для хранения частот символов
    frequency = {}
    # Подсчитываем общее число символов в тексте
    count_symbols = len(text)
    # Проходимся по каждому символу в тексте
    for symbol in text:
        if symbol in frequency:
            frequency[symbol] += 1
        else:
            frequency[symbol] = 1
    time.sleep(1)
    # Преобразуем частоты символов в пары (символ, частота встречаемости)
    result = [(symbol, frequency / count_symbols) for symbol, frequency in frequency.items()]
    return result


def auto_text():
    #while True:
    text = lorem.paragraph()
    time.sleep(1)
    with locker:
        print(text)

        return text


def menu():
    text = auto_text()
    result = analysis_text(text)
    for symbol, frequency in result:
        print(f"{symbol} - {frequency:.4f}")


for _ in range(5):
    thr = threading.Thread(target=menu(),)
    thr.start()
