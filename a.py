from tkinter import *
from tkinter.messagebox import showinfo
root=Tk()
from win_cal_optimizer import wincal
root.title('dugduy 3T')
lv=3
btn_list=[]
player_turn=0
players=['x','o']
on_play={'x':[],'o':[]}
win_cell=wincal(lv)
def win_check():
    for i in win_cell:
        print(set(i)&set(on_play[players[player_turn%2]]))
        if len(set(i)&set(on_play[players[player_turn%2]]))==lv:
            return 1
    return 0
def on_click(i):
    global player_turn
    crplayer=players[player_turn%2]
    on_play[crplayer].append(i)
    btn_list[i].config(text=crplayer)
    btn_list[i].config(state=DISABLED,borderwidth=1)
    if win_check():
        for btn in btn_list:
            btn.config(state=DISABLED)
        showinfo('Game over!',crplayer+' win!\nhehe')
    player_turn+=1
for i in range(lv*lv):
    btn_list.append(Button(width=10,height=5,fg='red',borderwidth=5,font=(0,20),command=lambda i=i:on_click(i)))
    btn_list[-1].grid(row=int(i/lv),column=i%lv)
root.mainloop()