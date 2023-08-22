from tkinter import *
import random
import time

### VAR ###
count={"val": 0}
StoricoNumeri={}


### FUNC ###
def conteggio():
   count["val"] += 1
   countNum.config(text=count["val"])

def lancio():
    for i in range(10):
        numero = random.randint(1, 6)
        app.update()
        dado.config(text=numero)
        time.sleep(0.1)
    conteggio()
    storico(numero)


def storico(num):
    if num not in StoricoNumeri:
        StoricoNumeri[num] = 1
        storicoNum.config(text=StoricoNumeri)
    else:
        StoricoNumeri[num] += 1
        storicoNum.config(text=StoricoNumeri)

def pulisci():
    StoricoNumeri.clear()
    count["val"] = 0
    storicoNum.config(text="{ : }")
    countNum.config(text="0")


### GUI ###
app=Tk()
app.title("Il Dado è tratto")
app.configure(bg="darkgreen")

nameApp=Label(app, text="Lancia il Dado!", font=("bold", 20), bg="darkgreen")
nameApp.grid(column=0, row=0, columnspan=2, padx=25, pady=15)

dado=Label(app, text="8", bg="white", font=("bold", 36), padx=35, pady=20)
dado.grid(column=0, row=1, columnspan=2, padx=(20), pady=(10,20))

btnLancio=Button(app, text="Vai!", width=5, height=1, bg="lightgreen", font=("bold", 18), command=lancio)
btnLancio.grid(column=0, row=2, columnspan=2)

countTxt=Label(app, text="Lancio n.", bg="darkgreen", fg="white")
countTxt.grid(column=0, row=3, columnspan=1, sticky=E, pady=(20,5))

countNum=Label(app, text="0", bg="darkgreen", fg="white")
countNum.grid(column=1, row=3, sticky=W, pady=(20,5))

storicoTxt=Label(app, text="Storico dei lanci", bg="darkgreen", fg="white")
storicoTxt.grid(column=0, row=4,columnspan=2)

storicoNum=Label(app, text="{ : }", bg="darkgreen", fg="white")
storicoNum.grid(column=0,row=5, columnspan=2, pady=(0, 10))

clearData=Button(app, text="Pulisci dati", bg="red", border=1, command=pulisci)
clearData.grid(column=0, row=6, pady=(0,10), columnspan=2)



app.mainloop()