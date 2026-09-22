
from tkinter import*

fenetre=Tk()
fenetre.geometry("700x400")
fenetre.title("Codage et Décodage 1.0")
fenetre['background']='LightSlateGray'

class Lotfi(Entry):
    def __init__(self, master=None, **kwargs):
        self.var = StringVar()
        Entry.__init__(self, master, textvariable=self.var, **kwargs)
        self.old_value = ''
        self.var.trace('w', self.check)
        self.get, self.set = self.var.get, self.var.set

    def check(self, *args):
        if self.get().isdigit(): 
            # the current value is only digits; allow this
            self.old_value = self.get()
        else:
            # there's non-digit characters in the input; reject this 
            self.set(self.old_value)

    
def CreateCodeFenetre():
    
    codeFenetre=Toplevel(fenetre)
    codeFenetre.geometry("500x275")
    codeFenetre.title("Session de codage")
    codeFenetre['background']='LightSlateGray'
    
    codeLabel=Label(codeFenetre,text="Entrer votre message à coder",font=("ComicSansMS",20),width=60)
    codeLabel.pack(pady=10)

    codeEntry=Entry(codeFenetre,width=60)
    codeEntry.pack()

    codeLabel2=Label(codeFenetre,text="Entrer votre code",font=("ComicSansMS",20),width=60)
    codeLabel2.pack(pady=10)

    keyBox=Lotfi(codeFenetre,width=60)
    keyBox.pack()

    codeButton1=Button(codeFenetre,text="Coder le message",font=("ComicSansMS",20),width=60)
    codeButton1.pack(pady=10)

    def encrypt(event):
        alphabet="abcdefghijklmnopqrstuvwxyz"
        ponctuation=" ,.!?'"
        original=codeEntry.get()
        key=int(keyBox.get())
        code=""
        for x in original:
            num=alphabet.find(x)
            Num=ponctuation.find(x)
            if Num==0:
                code=code+" "
            elif Num==1:
                code=code+","
            elif Num==2:
                code=code+"."
            elif Num==3:
                code=code+"!"
            elif Num==4:
                code=code+"?"
            elif Num==5:
                code=code+"'"
            else:
                newNum=num+key
                newNum=newNum % 26
                code=code+alphabet[newNum]
        secretmessagelabel=Text(codeFenetre,height=1,borderwidth=0,width=60)
        secretmessagelabel.insert(1.0,code)
        secretmessagelabel.pack()
        secretmessagelabel.configure(state="disabled")


    codeButton1.bind("<Button-1>",encrypt)

    codeFenetre.mainloop()
    
def CreateDecodeFenetreChoose():

    def acceuil():
        CreateDecodeFenetreAvecCode()
        
    def acceuil2():
        CreateDecodeFenetreSansCode()

    def test():
        decodeFenetreChoose.destroy()
        acceuil()

    def test2():
        decodeFenetreChoose.destroy()
        acceuil2()
            
    decodeFenetreChoose=Toplevel(fenetre)
            
    decodeButtonChoose = Button(decodeFenetreChoose,text="Decoder avec un code", command=test)
    decodeButtonChoose.pack()
            
    decodeButtonChoose1 = Button(decodeFenetreChoose, text="Decoder sans code",command=test2)
    decodeButtonChoose1.pack()
            
    decodeFenetreChoose.mainloop()


def CreateDecodeFenetreAvecCode():
    decodeFenetreAvecCode=Toplevel(fenetre)
    decodeFenetreAvecCode.geometry("500x275")
    decodeFenetreAvecCode.title("Session de décodage")
    decodeFenetreAvecCode['background']='LightSlateGray'
    
    decodeLabel=Label(decodeFenetreAvecCode,text="Entrer votre message à décoder",font=("ComicSansMS",20),width=60)
    decodeLabel.pack(pady=10)

    decodeEntry=Entry(decodeFenetreAvecCode,width=60)
    decodeEntry.pack()

    decodeLabel2=Label(decodeFenetreAvecCode,text="Entrer votre code",font=("ComicSansMS",20),width=60)
    decodeLabel2.pack(pady=10)

    keyBox1=Lotfi(decodeFenetreAvecCode,width=60)
    keyBox1.pack()

    decodeButton1=Button(decodeFenetreAvecCode,text="Décoder le message",font=("ComicSansMS",20),width=60)
    decodeButton1.pack(pady=10)

    def decrypt(event):
        alphabet="abcdefghijklmnopqrstuvwxyz"
        original=decodeEntry.get()
        ponctuation=" ,.!?'"
        key=int(keyBox1.get())
        key=26-key
        code=""
        for x in original:
            num=alphabet.find(x)
            Num=ponctuation.find(x)
            if Num==0:
                code=code+" "
            elif Num==1:
                code=code+","
            elif Num==2:
                code=code+"."
            elif Num==3:
                code=code+"!"
            elif Num==4:
                code=code+"?"
            elif Num==5:
                code=code+"'"
            else:
                newNum=num + key
                newNum=newNum % 26
                code=code+alphabet[newNum]
        secretmessagedecodedlabel=Text(decodeFenetreAvecCode,height=1,borderwidth=0,width=60)
        secretmessagedecodedlabel.insert(1.0,code)
        secretmessagedecodedlabel.pack()
        secretmessagedecodedlabel.configure(state="disabled")
    decodeButton1.bind("<Button-1>",decrypt)

    decodeFenetreAvecCode.mainloop()

def CreateDecodeFenetreSansCode():
    decodeFenetreSansCode=Toplevel(fenetre)
    decodeFenetreSansCode.geometry("500x275")
    decodeFenetreSansCode.title("Session de décodage")
    decodeFenetreSansCode['background']='LightSlateGray'

    DecodeLabel=Label(decodeFenetreSansCode,text="Entrer votre message à décoder",font=("ComicSansMS",20),width=60)
    DecodeLabel.pack(pady=10)

    DecodeEntry=Entry(decodeFenetreSansCode,width=60)
    DecodeEntry.pack()

    DecodeButton=Button(decodeFenetreSansCode,text="Decoder",font=("ComicSansMS",20),width=60)
    DecodeButton.pack(pady=10)

    def decrypt2(event):
        alphabet="abcdefghijklmnopqrstuvwxyz"
        original=DecodeEntry.get()
        ponctuation=" ,.!?'"
        code=""
        for i in range(25):
            for x in original:
                num=alphabet.find(x)
                Num=ponctuation.find(x)
                key=int(i+1)
                if Num==0:
                    code=code+" "
                elif Num==1:
                    code=code+","
                elif Num==2:
                    code=code+"."
                elif Num==3:
                    code=code+"!"
                elif Num==4:
                    code=code+"?"
                elif Num==5:
                    code=code+"'"
                else:
                    newNum=num + key
                    newNum=newNum % 26
                    code=code+alphabet[newNum]
            secretmessagedecodedlabel=Text(decodeFenetreSansCode,height=1,borderwidth=0,width=60)
            secretmessagedecodedlabel.insert(1.0,code)
            secretmessagedecodedlabel.pack()
            secretmessagedecodedlabel.configure(state="disabled")
            code=""
    DecodeButton.bind("<Button-1>",decrypt2)
    
space=Label(fenetre,bg="LightSlateGray")
space.pack(pady=10)

welcomeLabel=Label(fenetre,text="Bienvenue dans le centre",font=("ComicSansMS",30))
welcomeLabel.pack()

welcomeLabel2=Label(fenetre,text="de Codage et Décodage 1.0",font=("ComicSansMS",30))
welcomeLabel2.pack()

codeButton=Button(fenetre,width=7,text="Coder",font=("ComicSansMS",20),command=CreateCodeFenetre)
codeButton.pack(side="left",padx=100)

decodeButton=Button(fenetre,width=7,text="Decoder",font=("ComicSansMS",20),command=CreateDecodeFenetreChoose)
decodeButton.pack(side="right",padx=100)

fenetre.mainloop()
