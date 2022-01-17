
# coding: utf-8

# In[44]:


from tkinter import*
def uppercase(str):
    if str >= 'A' and str <= 'Z':
        return True
    return False
def lowercase(str):
    if str >= 'a' and str <= 'z':
        return True
    return False
def encrypt(word):
    ans = []
    for i in range(len(word)):
        if uppercase(word[i]):
            ans.append(chr(ord('Z') - ord(word[i]) + ord('A')))
            
        elif lowercase(word[i]):
            ans.append( chr(ord('z') -  ord(word[i]) + ord('a')))
    return ans
def encipher():
    result=encrypt(e1.get())
    info.config(text=result)
           
root=Tk() 
root.title('Encryptiom')
root.geometry('500x300')
root.resizable(0,0)
f0=Frame(root,bg='grey')
f0.pack(side=TOP,expand=TRUE,fill=BOTH)
l1=Label(f0,text='encrypt text',bg='blue',fg='cyan',font=30)
l1.place(x = 200, y = 20, width=100, height=25)
f1=Frame(root,bg='grey')
f1.pack(side=TOP,expand=TRUE,fill=BOTH)
l2=Label(f1,text='Input Text',bg='BLUE',fg='cyan')
l2.place(x = 50, y=5, width=100, height=25)
e1=Entry(f1,bg='white')
e1.place(x = 170, y=5, width=300, height=25)
b1=Button(root,text='ENCIPHER',fg='black',command=encipher)
b1.place(x = 90, y = 195, width=100, height=25)
info =Label(text='encrypted text', bg='white', fg='black')
info.place(x =50, y = 250, width=400, height=25)
root.mainloop()

