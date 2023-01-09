from tkinter import *

# define window
win = Tk()
win.geometry("500x300")

# setting two global health variables
hp = 100

hp2 = 100

# setting them to be read by Tkinter
var = StringVar()
var.set('Player-san     ' + str(hp))

var2 = StringVar()
var2.set('Mr. Fuwa     ' + str(hp2))


# defining destroy class for fainting
def destruct(label):
    label.destroy()
    pass


# defining loss end case labels
l1 = Label(win, justify=CENTER, wraplength=250)
l2 = Label(win, justify=CENTER, wraplength=250)
l3 = Label(win, justify=CENTER, wraplength=250)
# text for loss case
word = 'TERMINATION'
word2 = 'Dear employee,'
word3 = '販どスり算経ノコメ国勢ヒヱ章恵ゃくかレ合一マカ奏付だとぽ団済き比勝ぜ犯存もレ松踊シヱヒ育今見ニツユチ恒病如幡揃きすそぽ。心やがょ消題ミネウヨ員界ちひ射47紀識8' \
        '極カトユキ月高トり査戻青るどがご時院良旅なたこざ先出る一際きイ海学ヘツヒ報藤崎づしいめ。馬ぶッか会康楽コメオニ健間ランちス選3直ヨユエマ法止げー自第ラマヱ自要ヌテ土幕るぼ女2' \
        '面頭ノオワラ術感山ケエホ火店ナテセフ初道ーえさン状6' \
        '崎裁億討病イすぞが。紹書もでかル虚通ねばラ小化とょ不山わたご破作ナテヨ知変ノハカタ院文けちどレ価攻げお強写展カ資語レセワ何敢渓窮胡みうてゃ。東特えりなラ被何ドてょ無蚕ツス政季カアロ均重たす名猪ヱケ乳塾ぽけを経78' \
        '希員さク録地ぶイ業土び賢越84阪ね庁俊ケモリ岩調難職個ドそフ。評北ヘサマ辞象快ぜわげい央教ルラフ語的84得業理買64認マナハ区週レよもざ転左ツユ速合ゆリ竹野創ルハ舗大ネクリレ経待アウス会嶋れて日5休障ッのと。 '


# moving effect for word
def go(counter=1):
    l1.config(text=word[:counter])
    if counter < len(word):
        win.after(150, lambda: go(counter + 1))


# moving effect for word2
def go2(counter=1):
    l2.config(text=word2[:counter])
    if counter < len(word2):
        win.after(150, lambda: go2(counter + 1))


# moving effect for word3
def go3(counter=1):
    l3.config(text=word3[:counter])
    if counter < len(word3):
        win.after(150, lambda: go3(counter + 1))


# defining loss case
def loss():
    # setting up window
    win.geometry("250x250")
    l1.grid(row=0)
    l2.grid(row=1)
    l3.grid(row=2)
    # activating moving text
    go()
    go2()
    go3()

# defining win case
# defining words


word4 = 'DIVORCE DECREE'
word5 = 'Dear Player-san,'
word6 = '販どスり算経ノコメ国勢ヒヱ章恵ゃくかレ合一マカ奏付だとぽ団済き比勝ぜ犯存もレ松踊シヱヒ育今見ニツユチ恒病如幡揃きすそぽ。心やがょ消題ミネウヨ員界ちひ射47紀識8' \
        '極カトユキ月高トり査戻青るどがご時院良旅なたこざ先出る一際きイ海学ヘツヒ報藤崎づしいめ。馬ぶッか会康楽コメオニ健間ランちス選3直ヨユエマ法止げー自第ラマヱ自要ヌテ土幕るぼ女2' \
        '面頭ノオワラ術感山ケエホ火店ナテセフ初道ーえさン状6' \
        '崎裁億討病イすぞが。紹書もでかル虚通ねばラ小化とょ不山わたご破作ナテヨ知変ノハカタ院文けちどレ価攻げお強写展カ資語レセワ何敢渓窮胡みうてゃ。東特えりなラ被何ドてょ無蚕ツス政季カアロ均重たす名猪ヱケ乳塾ぽけを経78' \
        '希員さク録地ぶイ業土び賢越84阪ね庁俊ケモリ岩調難職個ドそフ。評北ヘサマ辞象快ぜわげい央教ルラフ語的84得業理買64認マナハ区週レよもざ転左ツユ速合ゆリ竹野創ルハ舗大ネクリレ経待アウス会嶋れて日5休障ッのと。 '
# defining labels
l4 = Label(win)
l5 = Label(win)
l6 = Label(win, justify=CENTER, wraplength=250)


# moving text effects
def go4(counter=1):
    l4.config(text=word4[:counter])
    if counter < len(word4):
        win.after(150, lambda: go4(counter + 1))


def go5(counter=1):
    l5.config(text=word5[:counter])
    if counter < len(word5):
        win.after(150, lambda: go5(counter + 1))


def go6(counter=1):
    l6.config(text=word6[:counter])
    if counter < len(word6):
        win.after(150, lambda: go6(counter + 1))


# defining movement
def wins():
    win.geometry("250x250")
    l4.grid(row=0)
    l5.grid(row=1)
    l6.grid(row=2)
    # activating moving text
    go4()
    go5()
    go6()


# defining mass destruction of all labels
def mass_destruct(label):
    for i in label:
        i.destroy()
    if hp <= 0:
        loss()
    if hp2 <= 0:
        wins()


# defining a class to take damage from Enemy
def damage2():
    global hp2
    global var2
    move2 = Label(win, text="Prot uses Conformity")
    move2.grid(row=1, column=1)
    move2.after(750, destruct, move2)
    dmg2(10)


# class to take damage from Player
def damage():
    global hp
    if hp > 10:
        move1 = Label(win, text="Mr.Fuwa uses Elder Hierarchy")
        move1.grid(row=1, column=1)
        move1.after(750, destruct, move1)
    dmg(10)


# utility class for Damage to Player
def dmg(num):
    global hp
    global pimg
    if hp > 0:
        hp = hp - num
        var.set('Player-san     ' + str(hp))
        hidden_attacks()
        if hp <= 0:
            var.set('fainted')
            mass_destruct(list_of_labels)


# utility class for Damage to Enemy
def dmg2(num):
    global hp2
    global enemy_img
    if hp2 > 0:
        hp2 = hp2 - num
        move2 = Label(win, text="Player-san uses Overtime")
        if hp2 >= 10:
            move2.grid(row=1, column=1)
            move2.after(750, destruct, move2)
        if hp2 > 0:
            var2.set('Mr. Fuwa     ' + str(hp2))
        else:
            var2.set('fainted')
            mass_destruct(list_of_labels)
            wins()


# counter for hidden attacks
c = 0


# label funky workaround
def griding(label):
    label.grid(row=1, column=1)


# initiating hidden attacks
def work_harder():
    dmg2(30)
    dmg(12)
    l7 = Label(win, text="Mr. Fuwa uses Rampant Sexism")
    l7.after(750, griding, l7)
    l7.after(1500, destruct, l7)


def speak2boss():
    mass_destruct(list_of_labels)
    loss()


attack1 = Button(text='Work Overtime', command=work_harder)
attack2 = Button(text='Speak to His Boss', command=speak2boss)


# class for making hidden attacks appear
def hidden_attacks():
    global c
    c = c + 1
    if c > 4:
        attack1.grid(row=3)
    if c > 6:
        attack2.grid(row=4)


# place Player gif
pi = PhotoImage(file='player-san.png')
pimg = Label(win, image=pi, height=165, width=165)
pimg.grid(row=1, column=0)

# place enemy gif
ei = PhotoImage(file='mr-fuwa.png')
enemy_img = Label(win, image=ei, height=165, width=165)
enemy_img.grid(row=1, column=2)

# place player HP
player_hp_display = Label(win, textvariable=var, fg="red")
player_hp_display.grid(row=0, column=0)

# place enemy HP
enemy_hp_display = Label(win, textvariable=var2, fg="red")
enemy_hp_display.grid(row=0, column=2)

# test button to detract HP from Player
attack = Button(win, text="Do Nothing", command=damage)
damage()
attack.grid(row=2, column=0)
# list of all graphics for mass destroy
list_of_labels = [attack, player_hp_display, enemy_hp_display, enemy_img, pimg, attack1, attack2]

win.mainloop()
