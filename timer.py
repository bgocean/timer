import os
import sys
import time
from tkinter import *
from playsound import playsound  # Лёгкая библиотека для воспроизведения звука


def sound():
    btn_start.pack_forget()
    btn_stop.pack()
    playsound(file, block=False)  # Воспроизводим звук без блокировки интерфейса


def start(event=None):  # Мы добавляем event=None, чтобы функция могла работать с клавишей
    duration = int(seconds.get())
    while duration:
        m, s = divmod(int(duration), 60)
        min_sec_format = '{:02d}:{:02d}'.format(m, s)
        count_digit['text'] = min_sec_format
        count_digit.update()
        time.sleep(1)
        duration -= 1

    # Когда таймер достигает 00:00, обновляем отображение и вызываем звук
    count_digit['text'] = '00:00'
    sound()


def stop():
    btn_start.pack()
    btn_stop.pack_forget()
    # `playsound` не имеет встроенной функции для паузы, но звук закончится автоматически.


def on_drag(event):
    # Сдвигаем окно с тем, чтобы следить за положением мыши
    root.geometry(f'+{event.x_root}+{event.y_root}')


# Путь к звуковому файлу
file = os.path.join(os.path.dirname(__file__), '188565.mp3')

# Определение пути для иконки в зависимости от того, скомпилирован ли скрипт
if getattr(sys, 'frozen', False):  # Если скрипт запущен из экзешника
    icon_path = os.path.join(sys._MEIPASS, "Clock.ico")
else:
    icon_path = os.path.join(os.path.dirname(__file__), "Clock.ico")  # Если скрипт запущен как файл Python

root = Tk()
root.title('Таймер')
root.geometry('209x150')
root.resizable(width=False, height=False)
root.iconbitmap(icon_path)  # Используем переменную для пути к иконке

count_digit = Label(root, text='0', font='Arial 15 bold')
count_digit.pack()

seconds = Entry(root, font='Arial 15 bold', width=7)
seconds.pack(pady=10)

btn_start = Button(root, text='Старт', font='Arial 15 bold', command=start)
btn_start.pack()

btn_stop = Button(root, text='Стоп', font='Arial 15 bold', command=stop)

# Перетаскивание окна
root.bind("<B1-Motion>", on_drag)

# Привязываем событие нажатия клавиши Enter к функции start
root.bind("<Return>", start)

root.mainloop()
