from tkinter import *


from threading import Thread

from selenium import webdriver
from time import sleep
from random import randint
import multiprocessing
import random


root = Tk()
root.title("GUI на Python")
root.geometry("900x650")


class Bot():

    def __init__(self):
        self.spam(sel['text'],message_entry.get())




    def spam(self, link, spam1):
        self.driver = webdriver.Chrome()
        self.driver.get('https://docs.google.com/forms/d/e/1FAIpQLSc3Uq5ts0ywKhZDRMNCrxV5LGfY8pHV6b0timV5Uu3QRODpQA/viewform')
        a = str(link)
        print(a)
        sleep(0.1)
        self.driver.find_element_by_xpath(a).click()
        username_input = self.driver.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
        username_input.send_keys(spam1)



message = StringVar()


message_entry = Entry(textvariable=message)
message_entry.place(relx=.5, rely=.3, anchor="c")

languages = [( 'Вариант1', 1), ('Вариант2', 2)]

language = IntVar()
def select():
    l = language.get()
    if l == 1:
        sel.config(text='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div/span/div/div[1]/label')

    elif l == 2:
        sel.config(text='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div/span/div/div[2]/label')

row = 1
for txt, val in languages:
    Radiobutton(text=txt, value=val, variable=language, padx=15, pady=10, command=select)\
        .grid(row=row, sticky=W)
    row += 1


sel = Label(padx=15, pady=10)
sel.grid(row=row, sticky=W)

def main():
    Bot()
def start():
    processss = []
    for x in range(5):
        proccess = multiprocessing.Process(target=main())
        if __name__ == '__main__':
            processss.append(proccess)
            proccess.start()
            for proccess in processss:
                proccess.join()


btn = Button(text="Запуск спама", background="#555", foreground="#ccc",
                 padx="20", pady="8", font="16", command=start)
btn.grid()





root.mainloop()


