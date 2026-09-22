
from tkinter import *

class Gui:
    master = Tk()
    master.geometry("400x400")
    game_still_going = True

    winner = None

    current_player = "X"
    var1 = StringVar()
    var1.set("-")
    var2 = StringVar()
    var2.set("-")
    var3 = StringVar()
    var3.set("-")
    var4 = StringVar()
    var4.set("-")
    var5 = StringVar()
    var5.set("-")
    var6 = StringVar()
    var6.set("-")
    var7 = StringVar()
    var7.set("-")
    var8 = StringVar()
    var8.set("-")
    var9 = StringVar()
    var9.set("-")

    P = StringVar()
    P.set("X")
    E = StringVar()

    def __init__(self):
        self.master.title("Python - Tic-Tac-Toe")
        self.master.option_add("*Font", "Verdana 12 normal")
        self.display_board()
        self.master.mainloop()




    def display_board(self):
        menu_bar = Menu(self.master,fg = "green")
        menu_bar.add_command(label="About", command=self.a)
        self.master.config(menu=menu_bar)
        menu_bar.add_command(label = "Help" ,command = self.help)
        self.master.configure(menu = menu_bar)

        self.label_1 = Label(self.master, text=self.var1.get())
        self.label_2 = Label(self.master, text=self.var2.get())
        self.label_3 = Label(self.master, text=self.var3.get())
        self.label_4 = Label(self.master, text=self.var4.get())
        self.label_5 = Label(self.master, text=self.var5.get())
        self.label_6 = Label(self.master, text=self.var6.get())
        self.label_7 = Label(self.master, text=self.var7.get())
        self.label_8 = Label(self.master, text=self.var8.get())
        self.label_9 = Label(self.master, text=self.var9.get())

        self.l = Label(self.master,text = "Enter the position:")
        self.label = Label(self.master,text = "Current Player\n"+self.P.get())


        self.label_1.grid(row=0, sticky="ewns", padx=1, pady=1)
        self.label_2.grid(row=0, column=1, sticky="ewns", padx=1, pady=1)
        self.label_3.grid(row=0, column=2, sticky="ewns", padx=1, pady=1)
        self.label_4.grid(row=1, column=0, sticky="ewns", padx=1, pady=1)
        self.label_5.grid(row=1, column=1, sticky="ewns", padx=1, pady=1)
        self.label_6.grid(row=1, column=2, sticky="ewns", padx=1, pady=1)
        self.label_7.grid(row=2, column=0, sticky="ewns", padx=1, pady=1)
        self.label_8.grid(row=2, column=1, sticky="ewns", padx=1, pady=1)
        self.label_9.grid(row=2, column=2, sticky="ewns", padx=1, pady=1)
        self.l.grid(row= 4 , sticky = "ewns")
        self.label.grid(row=3, sticky="ewns", padx=2, pady=2,columnspan = 4)
        
        '''Entry and Buttons'''
        display_entry_validate = (self.master.register(self.only_number_entry), '%S', '%d')
        self.entry = Entry(self.master,font=("Verdana", 20, "normal"), validate="key",validatecommand=display_entry_validate, textvariable=self.E)
        self.entry.grid(row=5,sticky="ewns",ipady=5, padx=2, pady=2,columnspan=4)
        self.entry.bind('<Return>', lambda  event = None :self.play_game())
        self.B = Button(self.master, text="Play", command=self.play_game,width = 5,fg = "white",bg = "green")
        self.B.grid(row=6 ,column = 1,sticky="ewns", padx=2, pady=2)
        self.C = Button(self.master, text="Clear",width = 2,command=self.cd,fg = "white",bg = "green")
        self.C.grid(row=6,column = 0,sticky="ewns", padx=2, pady=2)
        self.Q = Button(self.master, text="Esc", command=quit,fg = "white",bg = "green")
        self.Q.grid(row=6 , column = 2,sticky="ewns", padx=2, pady=2)
        self.master.bind("<Escape>", lambda event=None: self.master.destroy())

    def help(self):

        about_window1 = Toplevel(self.master)
        about_window1.title("Help")


        Label(about_window1, text="Positions", font=("Verdana", 15, "bold")).grid(row=0, column=0, padx=5,
                                                                                            pady=5,
                                                                                            sticky="s")
        Label(about_window1, text="1").grid(row=1, column=3, sticky="ewns", padx=4, pady=2)
        Label(about_window1, text="2").grid(row=1, column=4, sticky="ewns", padx=4, pady=2)
        Label(about_window1, text="3").grid(row=1, column=5, sticky="ewns", padx=4, pady=2)
        Label(about_window1, text="4").grid(row=2, column=3, sticky="ewns", padx=4, pady=2)
        Label(about_window1, text="5").grid(row=2, column=4, sticky="ewns", padx=4, pady=2)
        Label(about_window1, text="6").grid(row=2, column=5, sticky="ewns", padx=4, pady=2)
        Label(about_window1, text="7").grid(row=3, column=3, sticky="ewns", padx=4, pady=2)
        Label(about_window1, text="8").grid(row=3, column=4, sticky="ewns", padx=4, pady=2)
        Label(about_window1, text="9").grid(row=3, column=5, sticky="ewns", padx=4, pady=2)


    def a(self):
            about_window = Toplevel(self.master)
            about_window.title("Python - About")
            Label(about_window, text="Python", font=("Verdana", 15, "bold")).grid(row=0, column=0, padx=5, pady=5,
                                                                                     sticky="s")
            Label(about_window, text="Tic-Tac-Toe").grid(row=1, column=0, padx=5, pady=5, sticky="s")
            Label(about_window, text="Developed in Python 3.7.4 and Tkinter by Gabriel Guo").grid(row=2, column=0, sticky="s", padx=5)
            Label(about_window, text="Contact:gabrielguo2019@hotmail.com").grid(row=3, column=0, sticky="s", padx=5)


    def only_number_entry(self, key_press, cod):
        valid_chars = "123456789"
        expression_now = self.E.get()
        num_chars_now = len(expression_now)

        if (num_chars_now == 0):
            valid_chars_for_init = "123456789"
            return key_press in valid_chars_for_init
        else:
            last_char = expression_now[num_chars_now - 1]

            if (last_char in "+-*/" and key_press in "+-*/." and cod == '1'):
                return False

            elif (last_char in "123456789" and key_press in "123456789" and cod == '0'):
                return True
            elif (last_char == '.' and key_press in "+-*/." and cod == '1'):
                return False
            elif (last_char == '.' and key_press in "+-*/." and cod == '0'):
                return True
            elif (self.decimal_point_open and key_press == '.'):
                return False
            elif (not self.decimal_point_open and key_press == '.'):
                self.decimal_point_open = True
                return True
            elif (last_char in "123456789" and key_press in "+-*/"):
                self.decimal_point_open = False
                return True


    def cd(self):
        self.E.set("")



    def play_game(self):
        self.a = 0
        if self.game_still_going:
            self.a  = self.handle_turn(self.current_player)
            print(self.a)
            if self.a == 0 or self.a == None:
                return
            else:
                self.check_if_game_over()
                self.flip_player()
                if self.winner == "X" or self.winner == "O":
                    print(self.winner + " won.")
                elif self.winner == "Tie":
                    print("Tie.")
                else:
                    return

    def handle_turn(self,player):
        self.player = player
        self.position = int(self.E.get())
        self.valid = False
        if  not self.valid:
            while True:
                if self.position  in [x for x in range(1,10)]:
                    break
                else:
                    return 0
            self.ls = [self.var1.get(),self.var2.get(),self.var3.get(),self.var4.get(),self.var5.get(),self.var6.get(),self.var7.get(),self.var8.get(),self.var9.get()]
            self.p = self.ls[self.position-1]
            if self.p == "-":
                self.valid = True
            else:
                return
        if self.position == 1:
            self.var1.set(self.player)
            self.label_1["text"] = self.var1.get()
        elif self.position == 2:
            self.var2.set(self.player)
            self.label_2["text"] = self.var2.get()
        elif self.position == 3:
            self.var3.set(self.player)
            self.label_3["text"] =self.var3.get()
        elif self.position == 4:
            self.var4.set(self.player)
            self.label_4["text"] = self.var4.get()
        elif self.position == 5:
            self.var5.set(self.player)
            self.label_5["text"] =self.var5.get()
        elif self.position == 6:
            self.var6.set(self.player)
            self.label_6["text"] = self.var6.get()
        elif self.position ==7:
            self.var7.set(self.player)
            self.label_7["text"] = self.var7.get()
        elif self.position == 8:
            self.var8.set(self.player)
            self.label_8["text"] =  self.var8.get()
        elif self.position == 9:
            self.var9.set(self.player)
            self.label_9["text"] = self.var9.get()
        else:
            pass
        return 1

    def check_if_game_over(self):
        self.check_for_winner()
        if self.winner == None:
            self.check_for_tie()

    def check_for_winner(self):
        self.row_winner = self.check_rows()
        self.column_winner = self.check_columns()
        self.diagonal_winner = self.check_diagonals()

        if self.row_winner:
            self.winner = self.row_winner
            print("row winner",self.winner,self.row_winner)
        elif self.column_winner:
            self.winner = self.column_winner
            print("column winner",self.winner,self.column_winner)

        elif self.diagonal_winner:
            self.winner = self.diagonal_winner
            print("Diagonal",self.winner,self.diagonal_winner)
        else :
            self.winner = None


    def check_rows(self):
        self.row_1 = self.var1.get() == self.var2.get()== self.var3.get() != "-"
        self.row_2 = self.var4.get() == self.var5.get() == self.var6.get()!= "-"
        self.row_3 = self.var7.get() == self.var8.get() == self.var9.get() != "-"

        if self.row_1 or self.row_2 or self.row_3:
            self.game_still_going = False

        if self.row_1:
            return self.var1.get()
        elif self.row_2:
            return self.var4.get()
        elif self.row_3:
            return self.var7.get()

        else:
            return None

    def check_columns(self):
        self.column_1 =self.var1.get() == self.var4.get()== self.var7.get() != "-"
        self.column_2 = self.var2.get() == self.var5.get()== self.var8.get() != "-"
        self.column_3 = self.var3.get() == self.var6.get()== self.var9.get() != "-"

        if self.column_1 or self.column_2 or self.column_3:
            self.game_still_going = False
        if self.column_1:
            return self.var1.get()
        elif self.column_2:
            return self.var2.get()
        elif self.column_3:
            return self.var3.get()

        else:
            return None

    def check_diagonals(self):
        self.diagonal_1 = self.var1.get() == self.var5.get()== self.var9.get() != "-"
        self.diagonal_2 = self.var7.get() == self.var5.get()== self.var3.get() != "-"

        if self.diagonal_1 or self.diagonal_2:
            self.game_still_going = False

        if self.diagonal_1:
            return self.var1.get()
        elif self.diagonal_2:
            return self.var3.get()

        else:
            return None


    def check_for_tie(self):
        self.ls = [self.var1.get(), self.var2.get(), self.var3.get(), self.var4.get(), self.var5.get(), self.var6.get(),self.var7.get(), self.var8.get(), self.var9.get()]
        print(self.ls)
        if "-" not in self.ls:
            self.game_still_going = False
            self.winner = "Tie"
        else:
            self.game_still_going = True

    def flip_player(self):
        if self.current_player == "X" and self.a != 0:
            self.P.set("O")
            self.current_player = "O"
            self.label["text"] ="Current Player :\n"+ self.P.get()

        elif self.current_player == "O" and self.a != 0:
            self.P.set("X")
            self.current_player = "X"
            self.label["text"] = "Current Player :\n"+self.P.get()
            self.current_player = "X"

g = Gui()
