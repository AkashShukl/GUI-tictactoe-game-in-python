from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry('252x380')
root.eval('tk::PlaceWindow %s center' % root.winfo_pathname(root.winfo_id()))
root.title('TicTacToe')
root.resizable(0, 0)
#defining channces of the player
chance=0
NoWin=True
arr=["",100,200,300,400,500,600,700,800,900] #fiiling with randoms 

def showWin(n):
    messagebox.showinfo("Winner!!", "*** Winner Found ***.\n HIT the reset button!")
    
            
def ifWin(li):
    global arr
    global NoWin
    if arr[1]==arr[2]==arr[3] or arr[4]==arr[5]==arr[6] or arr[7]==arr[8]==arr[9]:
        showWin(1)
        NoWin=False
    elif arr[1]==arr[4]==arr[7] or arr[2]==arr[5]==arr[8] or arr[3]==arr[6]==arr[9]:
        showWin(1)
        NoWin=False
    elif arr[1]==arr[5]==arr[9] or arr[3]==arr[5]==arr[7]:
        showWin(1)
        NoWin=False
    else:
        pass


def fillData(buttons,n):
    global chance
    global arr
    global NoWin
    
    if(chance<9 and NoWin):
        if buttons['text']=="" and chance % 2==0:
            buttons['text']='X'
            chance+=1
            arr[n]=1
            ifWin(arr)
           
        if buttons['text']=="" and chance %2 !=0 :
            buttons['text']='O'
            chance+=1
            arr[n]=0
            ifWin(arr)
            
    elif chance>=9:
        messagebox.showinfo("Wasted!", "no one wins. HIT the reset button!")
    else:
        pass



l1=Label(root,text="Tic Tac Toe",height=1,bg="gray",fg="orange",font=('times new roman', 25 )).pack(fill=X)
#frame for buttons
frame2 = Frame(root, bg='black',height=300,width=400)
frame2.pack(expand=TRUE, fill=BOTH)
#making buttons
buttons=StringVar()
button1 = Button(frame2,text="",fg="blue",font=('times new roman',10,'bold'),bg="white",height=5,width=10,command=lambda:fillData(button1,1))
button1.grid(row=0,column=1,padx=(2,2),pady=(4,2))
button2 = Button(frame2,text="",fg="blue",font=('times new roman',10,'bold'),bg="white",height=5,width=10,command=lambda:fillData(button2,2))
button2.grid(row=0,column=2,padx=(2,2),pady=(4,2))
button3 = Button(frame2,text="",fg="blue",font=('times new roman',10,'bold'),bg="white",height=5,width=10,command=lambda:fillData(button3,3))
button3.grid(row=0,column=3,padx=(2,2),pady=(4,2))

button4 = Button(frame2,text="",fg="blue",font=('times new roman',10,'bold'),bg="white",height=5,width=10,command=lambda:fillData(button4,4))
button4.grid(row=1,column=1,padx=(2,2),pady=(2,2))
button5 = Button(frame2,text="",fg="blue",font=('times new roman',10,'bold'),bg="white",height=5,width=10,command=lambda:fillData(button5,5))
button5.grid(row=1,column=2,padx=(2,2),pady=(2,2))
button6 = Button(frame2,text="",fg="blue",font=('times new roman',10,'bold'),bg="white",height=5,width=10,command=lambda:fillData(button6,6))
button6.grid(row=1,column=3,padx=(2,2),pady=(2,2))

button7 = Button(frame2,text="",fg="blue",font=('times new roman',10,'bold'),bg="white",height=5,width=10,command=lambda:fillData(button7,7))
button7.grid(row=3,column=1,padx=(2,2),pady=(2,2))
button8 = Button(frame2,text="",fg="blue",font=('times new roman',10,'bold'),bg="white",height=5,width=10,command=lambda:fillData(button8,8))
button8.grid(row=3,column=2,padx=(2,2),pady=(2,2))
button9 = Button(frame2,text="",fg="blue",font=('times new roman',10,'bold'),bg="white",height=5,width=10,command=lambda:fillData(button9,9))
button9.grid(row=3,column=3,padx=(2,2),pady=(2,2))




def reset():
    global arr
    global chance
    global NoWin
    arr=["",100,200,300,400,500,600,700,800,900]
    chance=0
    NoWin=True
    
    button1['text']=""
    button2['text']=""
    button3['text']=""
    button4['text']=""
    button5['text']=""
    button6['text']=""
    button7['text']=""
    button8['text']=""
    button9['text']=""


resetBtn =Button(root, text='Reset',fg="Orange",font=('times new roman',12,'bold'),bg="gray", width=25, command=reset)
resetBtn.pack(fill=X)   
exitBtn =Button(root, text='Stop', fg="Orange",font=('times new roman',12,'bold'),bg="gray",width=25, command=root.destroy)
exitBtn.pack(fill=X)   



root.mainloop()