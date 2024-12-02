from time import sleep
from datetime import datetime
from threading import Thread

def write_words(word_count, file_name):
    file = open(file_name, 'a', encoding='utf-8')
    for i in range(word_count):
        file.write( f'Какое-то слово №  {i+1}\n')
        sleep(0.1)
    file.close()
    print(f'Завершилась запись в файл {file_name}')

time_start = datetime.now()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

time_stop = datetime.now()
time_result = time_stop - time_start

print(f'Время работы функций {time_result}')

time2_start = datetime.now()

thread_1 = Thread(target = write_words, args = (10, 'example5.txt'))
thread_2 = Thread(target = write_words, args = (30, 'example6.txt'))
thread_3 = Thread(target = write_words, args = (200, 'example7.txt'))
thread_4 = Thread(target = write_words, args = (100, 'example8.txt'))

thread_1.start()
thread_2.start()
thread_3.start()
thread_4.start()

thread_1.join()
thread_2.join()
thread_3.join()
thread_4.join()

time2_stop = datetime.now()
time2_result = time2_stop - time2_start
print(f'Время работы потоков {time2_result}')

# Вывод разницы начала и конца работы потоков
print(f'Использование потоков быстрее функций на {time_result-time2_result} секунд')