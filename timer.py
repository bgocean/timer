import time
from tkinter import *
import pygame


def sound():
    btn_start.pack_forget()
    btn_stop.pack()
    pygame.mixer.music.play()


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
    pygame.mixer.music.pause()


def on_drag(event):
    # Сдвигаем окно с тем, чтобы следить за положением мыши
    root.geometry(f'+{event.x_root}+{event.y_root}')


file = 'blue-nile-vibraslap-188565.mp3'
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(file)

root = Tk()
root.title('Таймер')
root.geometry('150x150')
root.resizable(0, 0)

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
