from tkinter import *
import time
window = Tk()
window.title('CPM Sayacı')
window.minsize(width=500, height=500)
bpm_list = []
times = [0.0, 0.0]
ortalama = [0]
son = [0.0]
label = Label(text='Başlamak için tıkla')
label.pack()
def say():
    starting_time = time.time()
    times.append(starting_time)
    if times[-2] > 0:
        bpm_list.append(times[-1] - times[-2])
    else:
        bpm_list.append(0)
    ortalama.append(sum(bpm_list) / len(bpm_list))
    if ortalama[-1] != 0:
        son.append(60.0 / ortalama[-1])
        label.config(text=f'{int(son[-1])} CPM')
    else:
        label.config(text=f'0 CPM')

button = Button(text="CPM'ini ölçeyim mi güzellik", command=say)
button.pack()













window.mainloop()
