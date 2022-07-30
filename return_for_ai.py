from tkinter import *
from time import sleep
from tkinter.messagebox import showinfo
from random import randint
root=Tk()
from win_cal_optimizer import wincal
root.title('dugduy 3T')
lv=3
btn_list=[]
player_turn=0
players=['x','o']
on_play={'x':[],'o':[]}
win_cell=wincal(lv)
aplayer='x'
def win_check():
    for i in win_cell:
        print(set(i)&set(on_play[players[player_turn%2]]))
        if len(set(i)&set(on_play[players[player_turn%2]]))==lv:
            return 'win'
    if player_turn==lv*lv:
        return 'tea'
    return 0
def on_click(i):
    global player_turn
    print(i,'index')
    # if win_check():
    #     for btn in btn_list:
    #         btn.config(state=DISABLED)
    #     showinfo('Game over!',players[player_turn%2]+' win!\nhehe')
    crplayer=players[player_turn%2]
    player_turn+=1
    print(player_turn,'times')
    on_play[crplayer].append(i)
    btn_list[i].config(text=crplayer)
    btn_list[i].config(state=DISABLED,borderwidth=1)
    iswin=win_check()
    if iswin == 'win':
        for btn in btn_list:
            btn.config(state=DISABLED)
        showinfo('Game over!',players[player_turn%2]+' win!\nhehe')
    elif iswin=='tea':
        for btn in btn_list:
            btn.config(state=DISABLED)
        showinfo('Tea!','Oh oh. Game ended without win!\nhehe')
    if aplayer!=players[player_turn%2] and not iswin:
        com_choice=randint(0,lv**2-1)
        # print(com_choice,on_play['x'],on_play['o'])
        while (com_choice in on_play['x']) or (com_choice in on_play['o']):
            print(com_choice,'already exist!',on_play)
            com_choice=randint(0,lv**2-1)
        on_click(com_choice)

    if aplayer==players[player_turn%2] and not iswin:
        com_choice=randint(0,lv**2-1)
        # print(com_choice,on_play['x'],on_play['o'])
        while (com_choice in on_play['x']) or (com_choice in on_play['o']):
            print(com_choice,'already exist!',on_play)
            com_choice=randint(0,lv**2-1)
        sleep(1)
        root.update()
        on_click(com_choice)
    
for i in range(lv*lv):
    btn_list.append(Button(width=10,height=5,fg='red',borderwidth=5,font=(0,20),command=lambda i=i:on_click(i)))
    btn_list[-1].grid(row=int(i/lv),column=i%lv)
on_click(randint(0,lv**2-1))
root.mainloop()