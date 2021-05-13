from tkinter import *
from selenium import webdriver
# insert ur chrome driver path
chromepath = "E:\\script\\whtsapp blaster\\chromedriver.exe"
driver = webdriver.Chrome(chromepath)


def msging():
    webname = name.get()
    webmsg = msg.get()
    webcount = count.get()
    user = driver.find_element_by_xpath('//span[@title="{}"]'.format(webname))
    user.click()
    msgbox = driver.find_element_by_xpath(
        "//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
    for i in range(webcount):
        msgbox.send_keys(webmsg)
        sendop = driver.find_element_by_xpath(
            "//*[@id='main']/footer/div[1]/div[3]/button/span")
        sendop.click()
    label = Label(window, text="msg blast done")
    label.grid(column=1, row=6)


def scanning():
    driver.get('https://web.whatsapp.com/')
    btn = Button(window, text="start msging", command=msging)
    btn.grid(column=1, row=5)


'''def names():
    x = Label(window, text=name.get())
    x.grid(column=0, row=5)
'''

if __name__ == '__main__':
    window = Tk()
    name = StringVar()
    msg = StringVar()
    count = IntVar()
    window.title("WhatsApp Message Blaster")
    window.geometry('500x600')
    lbl1 = Label(window, text="sender name:")
    txt1 = Entry(window, width=50, textvariable=name)
    lbl1.grid(column=0, row=0)
    txt1.grid(column=1, row=0)
    lbl2 = Label(window, text="msg:")
    txt2 = Entry(window, width=50, textvariable=msg)
    lbl2.grid(column=0, row=1)
    txt2.grid(column=1, row=1)
    lbl3 = Label(window, text="number of messges:")
    spin1 = Spinbox(window, from_=1, to=200, width=47, textvariable=count)
    lbl3.grid(column=0, row=2)
    spin1.grid(column=1, row=2)
    btn = Button(window, text="click to start scan", command=scanning)
    btn.grid(column=1, row=3)
    window.mainloop()
