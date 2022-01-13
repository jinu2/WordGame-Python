import tkinter as tk
from tkinter import *
from PIL import ImageTk,Image
import PIL
import random
import sozluk



class SampleApp(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Dil Uygulamasi")
        self.iconbitmap("Book-icon.ico")
        self._frame = None
        self.switch_frame(StartPage)


    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        frame = Frame(master)
        frame.pack()
        tk.Frame.__init__(self, master)

        self.title="nesto"


        canvas_for_image = Canvas(self, bg='white', height=200, width=600, borderwidth=0, highlightthickness=0)
        canvas_for_image.grid(row=0, columnspan=3,  padx=0, pady=0)

        image = Image.open("Welcome.png")
        canvas_for_image.image = ImageTk.PhotoImage(image.resize((600, 200), Image.ANTIALIAS))
        canvas_for_image.create_image(0, 0, image=canvas_for_image.image, anchor='nw')



        Level_1_img = Image.open("Level 1.png")
        canvas_for_image.Level_1_img = ImageTk.PhotoImage(Level_1_img.resize((200, 150), Image.ANTIALIAS))
        Level1 = Button(self, image=canvas_for_image.Level_1_img, borderwidth=0, command=lambda: master.switch_frame(LevelOne)).grid(
            row=1, column=0, pady=2)

        Level_2_img = Image.open("Level 2.png")
        canvas_for_image.Level_2_img = ImageTk.PhotoImage(Level_2_img.resize((200, 150), Image.ANTIALIAS))
        Level2 = Button(self, image=canvas_for_image.Level_2_img , borderwidth=0, command=lambda: master.switch_frame(LevelTwo)).grid(
            row=1, column=1, pady=2)

        Level_3_img = Image.open("Level 3.png")
        canvas_for_image.Level_3_img = ImageTk.PhotoImage(Level_3_img.resize((200, 150), Image.ANTIALIAS))
        Level3 = Button(self, image=canvas_for_image.Level_3_img, borderwidth=0, command=lambda: master.switch_frame(LevelThree)).grid(row=1, column=2, pady=2)

        Level_4_img = Image.open("Level 4.png")
        canvas_for_image.Level_4_img = ImageTk.PhotoImage(Level_4_img.resize((200, 150), Image.ANTIALIAS))
        Level4 = Button(self, image=canvas_for_image.Level_4_img, borderwidth=0, command=lambda: master.switch_frame(LevelFour)).grid(row=2, column=0, pady=2)

        Level_5_img = Image.open("Level 5.png")
        canvas_for_image.Level_5_img = ImageTk.PhotoImage(Level_5_img.resize((200, 150), Image.ANTIALIAS))
        Level5 = Button(self, image=canvas_for_image.Level_5_img, borderwidth=0, command=lambda: master.switch_frame(LevelFive)).grid(row=2, column=1, pady=2)

        Level_6_img = Image.open("Level 6.png")
        canvas_for_image.Level_6_img = ImageTk.PhotoImage(Level_6_img.resize((200, 150), Image.ANTIALIAS))
        Level6 = Button(self, image=canvas_for_image.Level_6_img, borderwidth=0, command=lambda: master.switch_frame(LevelSix)).grid(row=2, column=2, pady=2)

class LevelOne(tk.Frame):
    def __init__(self, master):

        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, bg='pink')
        global soz
        soz = sozluk.sozluk1

        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, bg='pink')

        tk.Label(self, text="Turkish", font=('arial', 16, "bold"), bg='pink').grid(row=0, column=0, pady=5, padx=5)
        tk.Label(self, text="English", font=('arial', 16, "bold"), bg='pink').grid(row=0, column=1, pady=5, padx=5)
        row_sayi=1
        for eng, tur in soz.items():

            tk.Label(self, text=eng, font=('Pursia', 14, "bold")).grid(row=row_sayi, column=0, pady=5,padx=5)
            tk.Label(self, text=tur, font=('Pursia', 14, "bold")).grid(row=row_sayi, column=1, pady=5,padx=5)
            row_sayi=row_sayi+1

        tk.Button(self, text="Next",
                  command=lambda: master.switch_frame(Alistirma)).grid(row=row_sayi, column=1, pady=row_sayi, padx=5)
        tk.Button(self, text="Go back to start page",
                  command=lambda: master.switch_frame(StartPage)).grid(row=row_sayi, column=0,pady=row_sayi, padx=5)

class LevelTwo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, bg='pink')
        global soz
        soz = sozluk.sozluk2

        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, bg='pink')

        tk.Label(self, text="Turkish", font=('arial', 16, "bold"),bg='pink').grid(row=0, column=0, pady=5, padx=5)
        tk.Label(self, text="English", font=('arial', 16, "bold"),bg='pink').grid(row=0, column=1, pady=5, padx=5)
        row_sayi=1
        for eng, tur in soz.items():
            tk.Label(self, text=eng, font=('Pursia', 14, "bold")).grid(row=row_sayi, column=0, pady=5,padx=5)
            tk.Label(self, text=tur, font=('Pursia', 14, "bold")).grid(row=row_sayi, column=1, pady=5,padx=5)
            row_sayi=row_sayi+1
        tk.Button(self, text="Next",
                  command=lambda: master.switch_frame(Alistirma)).grid(row=row_sayi, column=1, pady=row_sayi, padx=5)
        tk.Button(self, text="Go back to start page",
                  command=lambda: master.switch_frame(StartPage)).grid(row=row_sayi, column=0,pady=row_sayi, padx=5)

class LevelThree(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, bg='pink')
        global soz
        soz = sozluk.sozluk3

        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, bg='pink')
        tk.Label(self, text="Turkish", font=('arial', 16, "bold"),bg='pink').grid(row=0, column=0, pady=5, padx=5)
        tk.Label(self, text="English", font=('arial', 16, "bold"),bg='pink').grid(row=0, column=1, pady=5, padx=5)
        row_sayi=1
        for eng, tur in soz.items():
            tk.Label(self, text=eng, font=('Pursia', 14, "bold")).grid(row=row_sayi, column=0, pady=5,padx=5)
            tk.Label(self, text=tur, font=('Pursia', 14, "bold")).grid(row=row_sayi, column=1, pady=5,padx=5)
            row_sayi=row_sayi+1
        tk.Button(self, text="Next",
                  command=lambda: master.switch_frame(Alistirma)).grid(row=row_sayi, column=1, pady=row_sayi, padx=5)
        tk.Button(self, text="Go back to start page",
                  command=lambda: master.switch_frame(StartPage)).grid(row=row_sayi, column=0,pady=row_sayi, padx=5)

class LevelFour(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, bg='pink')
        global soz
        soz = sozluk.sozluk4

        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, bg='pink')
        tk.Label(self, text="Turkish", font=('arial', 16, "bold"),bg='pink').grid(row=0, column=0, pady=5, padx=5)
        tk.Label(self, text="English", font=('arial', 16, "bold"),bg='pink').grid(row=0, column=1, pady=5, padx=5)
        row_sayi=1
        for eng, tur in soz.items():
            tk.Label(self, text=eng, font=('Pursia', 14, "bold")).grid(row=row_sayi, column=0, pady=5,padx=5)
            tk.Label(self, text=tur, font=('Pursia', 14, "bold")).grid(row=row_sayi, column=1, pady=5,padx=5)
            row_sayi=row_sayi+1
        tk.Button(self, text="Next",
                  command=lambda: master.switch_frame(Alistirma)).grid(row=row_sayi, column=1, pady=row_sayi, padx=5)
        tk.Button(self, text="Go back to start page",
                  command=lambda: master.switch_frame(StartPage)).grid(row=row_sayi, column=0,pady=row_sayi, padx=5)

class LevelFive(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, bg='pink')
        global soz
        soz = sozluk.sozluk5

        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, bg='pink')
        tk.Label(self, text="Turkish", font=('arial', 16, "bold"),bg='pink').grid(row=0, column=0, pady=5, padx=5)
        tk.Label(self, text="English", font=('arial', 16, "bold"),bg='pink').grid(row=0, column=1, pady=5, padx=5)
        row_sayi=1
        for eng, tur in soz.items():
            tk.Label(self, text=eng, font=('Pursia', 14, "bold")).grid(row=row_sayi, column=0, pady=5,padx=5)
            tk.Label(self, text=tur, font=('Pursia', 14, "bold")).grid(row=row_sayi, column=1, pady=5,padx=5)
            row_sayi=row_sayi+1
        tk.Button(self, text="Next",
                  command=lambda: master.switch_frame(Alistirma)).grid(row=row_sayi, column=1, pady=row_sayi, padx=5)
        tk.Button(self, text="Go back to start page",
                  command=lambda: master.switch_frame(StartPage)).grid(row=row_sayi, column=0,pady=row_sayi, padx=5)

class LevelSix(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, bg='pink')
        global soz
        soz = sozluk.sozluk6

        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, bg='pink')
        tk.Label(self, text="Turkish", font=('arial', 16, "bold"),bg='pink').grid(row=0, column=0, pady=5, padx=5)
        tk.Label(self, text="English", font=('arial', 16, "bold"),bg='pink').grid(row=0, column=1, pady=5, padx=5)
        row_sayi=1
        for eng, tur in soz.items():
            tk.Label(self, text=eng, font=('Pursia', 14, "bold")).grid(row=row_sayi, column=0, pady=5,padx=5)
            tk.Label(self, text=tur, font=('Pursia', 14, "bold")).grid(row=row_sayi, column=1, pady=5,padx=5)
            row_sayi=row_sayi+1
        tk.Button(self, text="Next",
                  command=lambda: master.switch_frame(Alistirma)).grid(row=row_sayi, column=1, pady=row_sayi, padx=5)
        tk.Button(self, text="Go back to start page",
                  command=lambda: master.switch_frame(StartPage)).grid(row=row_sayi, column=0,pady=row_sayi, padx=5)


class Alistirma(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, bg='pink')
        Alistirma.eslesitirme(self, master, soz)

    def eslesitirme(self,master, soz):
        x = list(soz.keys())
        global a, b
        a = []
        b = []
        result = []
        secenek = random.sample(x, 5)
        global yeni
        yeni = {}
        for i in secenek:
            result.append(soz[i])
        for i in range(5):
            yeni[secenek[i]] = result[i]
        random.shuffle(result)
        x = list(soz.keys())
        result = []
        yeni = {}

        secenek = random.sample(x, 5)
        for i in secenek:
            result.append(soz[i])
        for i in range(5):
            yeni[secenek[i]] = result[i]
        row_sayi = 2

        print(result)
        random.shuffle(result)
        result = random.sample(result, len(result))

        self.but = Label(self, text="Eslestirme yap:",font=('Pursia', 14, "bold"),bg="pink", borderwidth=0)
        self.but.grid(row=0, column=0, columnspan=2, pady=5, padx=5)

        self.but = Label(self, text="Turkish",font=('Pursia', 14, "bold"),bg="pink", borderwidth=0)
        self.but.grid(row=1, column=0, pady=5, padx=5)
        self.but = Label(self, text="English",font=('Pursia', 14, "bold"),bg="pink",borderwidth=0)
        self.but.grid(row=1, column=1, pady=5, padx=5)
        for eng in secenek:
            self.Birinci = Button(self, text=eng, font=('Pursia', 14, "bold"), borderwidth=0)
            self.Birinci.grid(row=row_sayi, column=0, pady=5, padx=5)
            self.Birinci["command"] = lambda y=eng, z=self.Birinci: Alistirma.eslestir_sec(self, y, z)
            row_sayi = row_sayi + 1

        row_sayi = 2
        for tur in result:
            self.Ikinci = Button(self, text=tur, font=('Pursia', 14, "bold"), borderwidth=0)
            self.Ikinci.grid(row=row_sayi, column=1, pady=5, padx=5)
            self.Ikinci["command"] = lambda y=tur, z=self.Ikinci: Alistirma.eslestir_sec(self, y, z)
            row_sayi = row_sayi + 1


        self.but = Button(self, text="Next",command=lambda: master.switch_frame(YazmaGUI))
        self.but.grid(row=row_sayi, column=1, pady=15, padx=5)
        self.Check = Label(self, text="\t\t\t\t",background="pink")
        self.Check.grid(row=row_sayi, column=0, pady=5, padx=5)

    def remove(widget1):
        if widget1["text"] is None:
            widget1["text"]=""
        else:
            widget1.grid_remove()


    def eslestir_sec(self, y, z):
        if len(a) < 2:
            a.append(y)
            b.append(z)
        if len(a) == 2:
            b[0]["bg"] = "magenta"
            b[1]["bg"] = "magenta"
            if a[0] in yeni.keys():
                if (type(yeni[a[0]]) == list and a[1] in yeni[a[0]]) or a[1] == yeni[a[0]]:
                    b[0].config(state="disable")
                    b[1].config(state="disable")
                    self.Check = Label(self, text="\t\t\t\t", background="pink",font=('Pursia', 14, "bold"))
                    self.Check.grid(row=7, column=0, pady=5, padx=5,sticky=E)
                    label = Label(self, text="Cevap doğru! ", bg="green",font=('Pursia', 14, "bold"), borderwidth=0)
                    label.grid(row=7, column=0)

                elif a[0] == a[1]:
                    self.Check = Label(self, text="\t\t\t\t", background="pink", font=('Pursia', 14, "bold"))
                    self.Check.grid(row=7, column=0, pady=5, padx=5,sticky=E)
                    label = Label(self, text="Lütfen farklı bir seçenek seçiniz.", bg="red",font=('Pursia', 14, "bold"), borderwidth=0)
                    label.grid(row=7, column=0)
                    a.pop(1)
                    b.pop(1)
                    b[0]["bg"] = "white"
                    b[1]["bg"] = "white"
                else:
                    b[0].config(state="disable")
                    b[1].config(state="disable")
                    self.Check = Label(self, text="\t\t\t\t", background="pink",font=('Pursia', 14, "bold"))
                    self.Check.grid(row=7, column=0, pady=5, padx=5,sticky=E)
                    label = Label(self, text="Yanlış Cevap!", bg="red" ,font=('Pursia', 14, "bold"), borderwidth=0)
                    label.grid(row=7, column=0)
                    b[0].config(state="active")
                    b[1].config(state="active")
                    b[0]["bg"] = "white"
                    b[1]["bg"] = "white"
            elif a[1] in yeni.keys():
                if (type(yeni[a[1]]) == list and a[0] in yeni[a[1]]) or a[0] == yeni[a[1]]:
                    b[0].config(state="disable")
                    b[1].config(state="disable")
                    self.Check = Label(self, text="\t\t\t\t", background="pink",font=('Pursia', 14, "bold"))
                    self.Check.grid(row=7, column=0, pady=5, padx=5,sticky=E)
                    label = Label(self, text="Cevap doğru! ", bg="green",font=('Pursia', 14, "bold"), borderwidth=0)
                    label.grid(row=7, column=0)


                else:
                    b[0].config(state="disable")
                    b[1].config(state="disable")
                    self.Check = Label(self, text="\t\t\t\t", background="pink",font=('Pursia', 14, "bold"))
                    self.Check.grid(row=7, column=0, pady=5, padx=5,sticky=E)
                    label = Label(self, text="Yanlış Cevap!", bg="red",font=('Pursia', 14, "bold"), borderwidth=0)
                    label.grid(row=7, column=0)
                    b[0].config(state="active")
                    b[1].config(state="active")
                    b[0]["bg"] = "white"
                    b[1]["bg"] = "white"
            elif a[0] == a[1]:
                self.Check = Label(self, text="\t\t\t\t", background="pink",font=('Pursia',14, "bold"))
                self.Check.grid(row=7, column=0, pady=5, padx=5,sticky=E)
                label = Label(self, text="Lütfen farklı bir seçenek seçiniz.", bg="red",font=('Pursia', 14, "bold"), borderwidth=0)
                label.grid(row=7, column=0)
                a.pop(1)
                b.pop(1)
                b[0]["bg"] = "white"
                b[1]["bg"] = "white"
            else:
                b[0]["bg"] = "white"
                b[1]["bg"] = "white"

            a.clear()
            b.clear()

class YazmaGUI(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, bg='pink')
        YazmaGUI.yazma(self, soz,master)

    def yazma(self,soz,master):

        point = 0
        x = list(soz.keys())
        global a
        a = random.choice(x)
        print(a)
        global answer, question
        self.statement = Label(self, text="Write meaning of the following statement: ",font=('Pursia', 14, "bold"),fg="black",bg="pink")
        self.statement.grid(row=0, column=0, columnspan=2,pady=30)

        self.statement = Label(self, text=a, font=('Pursia', 14, "bold"),
                               fg="black", bg="pink")
        self.statement.grid(row=1, column=0, columnspan=2, pady=30)

        self.answer = Entry(self,justify='left')
        self.answer.grid(row=2, column=0, columnspan=2,pady=30)

        self.checkBt=Button(self,text="Check it",font=('Helvetica', 12, "bold"),fg="white",bg="light green",command=lambda fr=self: YazmaGUI.checking(fr,soz))
        self.checkBt.grid(row=3, column=0, columnspan=2,pady=30)



        self.question = Label(self, text="", font=('Pursia', 14, "bold"), bg="pink", fg="black")
        self.question.grid(row=4, column=0, columnspan=2,pady=30)

        self.Next = Button(self, text="Next", font=('Pursia', 14),  borderwidth=2,command=lambda: master.switch_frame(SecmeGUI))
        self.Next.grid(row=5, column=1,pady=30)

    def checking(self,soz):
        t = 0
        temp = soz[a]
        y = str(self.answer.get())
        print(temp)
        print(type(temp))
        if type(temp) == list:
            for i in range(len(temp)):
                if y.lower() == temp[i].lower():
                    t = 1
            if t == 0:
                label = Label(self, text="Wrong. Answer is: " + random.choice(temp), font=('Helvetica', 12, "bold"), fg="white",
                              bg="red")
                label.grid(row=4, column=0, columnspan=2,pady=30)
            elif t == 1:
                self.checkBt.config(state="disable")
                self.answer.config(state="disable")
                label = Label(self, text="\t\t\t\t\t", font=('Helvetica', 12, "bold"), bg="pink")
                label.grid(row=4, column=0, columnspan=2, pady=30)
                label = Label(self, text="Excellent,Congrats!", font=('Helvetica', 12, "bold"), fg="white", bg="green")
                label.grid(row=4, column=0, columnspan=2,pady=30)
        else:
            if y.lower() == temp.lower():
                self.checkBt.config(state="disable")
                self.answer.config(state="disable")
                label = Label(self, text="\t\t\t\t\t\t", font=('Helvetica', 12, "bold"),  bg="pink")
                label.grid(row=4, column=0, columnspan=2, pady=30)
                label = Label(self, text="Excellent,Congrats!", font=('Helvetica', 12, "bold"), fg="white", bg="green")
                label.grid(row=4, column=0, columnspan=2,pady=30)
            else:
                label = Label(self, text="Wrong. Answer is: " + temp, font=('Helvetica', 12, "bold"), fg="white",
                              bg="red")
                label.grid(row=4, column=0, columnspan=2,pady=30)

class SecmeGUI(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, bg='pink')
        SecmeGUI.secme(self, soz,master)




    def secme(self, soz,master):
        x = list(soz.keys())
        global word, label, secim
        word = random.choice(x)
        label = Label(self, text=word, bg="white", fg="magenta", font=('Helvetica', 18, "bold"))
        print()
        y = list(soz.values())
        A = []
        global title, buton
        buton = []
        title = Label(self, text="Select meaning of the Statement", font="Agenty 20", bg="pink")
        title.pack()
        label.pack(padx=5, pady=5)
        secenek = 0
        while secenek != 5:
            b = random.choice(y)
            if type(soz[word]) == list:
                k = random.choice(soz[word])
                if k not in A:
                    A.append(k)
                    secim = Button(self, text=A[secenek], bg="white", font=('Helvetica', 12, "bold"), width=45)
                    secim.pack(padx=5, pady=5)
                    buton.append(secim)
                    secenek += 1
                    secim["command"] = lambda string=secim["text"], sec=secim: SecmeGUI.control_sec1(self, string, sec,
                                                                                                      soz)
            elif type(soz[word]) != list and soz[word] not in A:
                A.append(soz[word])
                secim = Button(self, text=A[secenek], bg="white", font=('Helvetica', 12, "bold"), width=45)
                secim.pack(padx=5, pady=5)
                buton.append(secim)
                secenek += 1
                secim["command"] = lambda string=secim["text"], sec=secim: SecmeGUI.control_sec1(self, string, sec,
                                                                                                  soz)
            elif (type(b) != list) and b not in A:
                A.append(b)
                secim = Button(self, text=A[secenek], bg="white", font=('Helvetica', 12, "bold"), width=45)
                secim.pack(padx=5, pady=5)
                buton.append(secim)
                secenek += 1
                secim["command"] = lambda string=secim["text"], sec=secim: SecmeGUI.control_sec1(self, string, sec,
                                                                                                  soz)
            elif (type(b) == list):
                t = random.choice(b)
                if t not in A:
                    A.append(random.choice(b))
                    secim = Button(self, text=A[secenek], bg="white", font=('Helvetica', 12, "bold"), width=45)
                    secim.pack(padx=5, pady=5)
                    buton.append(secim)
                    secenek += 1
                    secim["command"] = lambda string=secim["text"], sec=secim: SecmeGUI.control_sec1(self, string, sec, soz)
        tk.Button(self, text="Go back to start page",
                  command=lambda: master.switch_frame(StartPage)).pack(padx=5, pady=5)

    def control_sec1(self, string, sec, soz):
        if (string.lower() == str(soz[word]).lower()) or (string in soz[word]):
            label1 = Label(self, text="Good Job!", bg="green", width=45)
            label1.pack(padx=5, pady=5)
        else:
            if type(soz) == list:
                label1 = Label(self, text="Wrong. Answer is: " + random.choice(soz[word]), bg="red", fg="white",
                               width=45)
                label1.pack(padx=5, pady=5)
            else:
                label1 = Label(self, text="Wrong. Answer is: " + soz[word], bg="red", fg="white", width=45)
                label1.pack(padx=5, pady=5)

        for i in range(len(buton)):
            buton[i]["bg"] = "lightgrey"
            buton[i].config(state="disable")



if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
