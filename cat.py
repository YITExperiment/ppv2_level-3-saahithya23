from tkinter import HIDDEN, NORMAL, Tk, Canvas
def toggle_eyes():
    current_color= c.itemcget (eye_left, 'fill')
    new_color= C.body_color if current_color='white' else
'white'
current state =c,itemcget (pupil_left, 'state')
new_state= NORMAL if current_state == HIDDEN else HIDDEN
c,itemconfigure (pupil_left, state=new_state)
c,itemconfigure (pupil_right, state=new_state)
c.itemconfigure(eye_left, fill-new_color)
c.itemconfigure(eye_right, fill=new_color)
def blink():
toggle_eyes()
root, after (250, toggle_eyes)
root, after (3000, blink)
root=Tk()
c=Canvas(root, width=400, height=400)
c.configure(bg='dark blue', highlight thickness=0)
c.body_color= 'SkyBluel'
body = c.create_oval (35, 20, 365, 350, outlinesc,body_color,
fill=c.body_color)
ear_left= c.create_polygon (75, 80, 75, 10, 165, 70,
outlinesc,body_color, fill-c.body_color)
ear_right = c.create_polygon (255, 45, 325, 10, 320, 70,
outlinesc.body_color, \
fill=c.body_color)
foot left = c.create oval (65, 320, 145, 360,
outline=c.body_color, fill= c.body_color)
foot_right = c.create oval(250, 320, 330, 360,
outline=c.body_color, fill= c.body_color)
eye left = c.create oval(130, 110, 160, 170, outline='black',
fill='white')
pupil_left = c.create oval (140, 145, 150, 155, outline= 'black',
fill='black')
eye_right = c.create oval(230, 110, 260, 170, outline='black',
fill='white')

    pupil c .create_oval(240, 145, 250, 155, outline='black',fill='black')
    mouth_normal= c.create_line(170, 250, 200, 272, 230,250,
    smooth=1, width=2, state= normal)

    mouth_happy = c.create_line(170, 250, 200, 282, 230, 250,
                   smooth=1, width=2, state=HIDDEN)
                   mouth_sad = c.create_ 1ine (170, 250, 200, 232, 230, 250,
                     smooth=1, width=2, state=HIDDEN)
                   cheek_left = c.create_ oval (70, 180, 120,230, otline='pink'.
                    Fil ='Pink' State= 'Hidden'


root.after(1000, blink)
def show_happy(event):
    if (20 <= event.x <= 350) and (20 <= event.y<= 350):
        c.itemconfigure(cheek_left, state=NORMAL)
        c.itemconfigure(cheek_right, state=NORMAL )
        c.itemconfigure(mouth_happy, state=NORMAL )
        C.itemconfigure(mouth_normal , state=HIDDEN)
        c.itemconfigure(mouth_sad, state=HIDDEN)
    return
def hide_happy(event):
        c.itemconfigure(cheek_left, state=NORMAL)
        c.itemconfigure(cheek_right, state=NORMAL )
        c.itemconfigure(mouth_happy, state=NORMAL )
        C.itemconfigure(mouth_normal , state=HIDDEN)
        c.itemconfigure(mouth_sad, state=HIDDEN)
    return
c.binf('<Motion>', show_happy)
c.bind('leave>',Hide_Happy
root.mainloop()
