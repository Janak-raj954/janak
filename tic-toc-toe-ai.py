from random import  choice

import tkinter as tk


class blue_print():

    def __init__(self):
        self.first_move = 0
        self.second_move = 1
        self.result = 2
        self.temp_move = None
        self.won = False
        self.chracter = 'player'
        self.game_mode = 'player'
        self.shape = ['c','X' , 'O']
        self.i = 1
        self.check = 0
        self.root = tk.Tk()
        self.topmenu = tk.Menu(self.root)
        self.root.config(menu = self.topmenu)

        self.options = tk.Menu(tearoff= 0)
        self.topmenu.add_cascade(menu = self.options , label= 'options')

        self.options.add_command(label='Restart' , command = self.restat)
        self.options.add_command(label="player" , command=lambda : self.restat( 'player'))
        self.options.add_command(label='Computer' , command= lambda :self.restat( 'computer'))
        self.root.title('tic toc toe')



        self.b1 = tk.Button(height=5 , width=10 , background='yellow' , command = lambda :self.player_move(self.b1))
        self.b2 = tk.Button(height=5 , width=10 , background='yellow' , command = lambda :self.player_move(self.b2))
        self.b3 = tk.Button(height=5 , width=10 , background='yellow' , command = lambda :self.player_move(self.b3))
        self.b4 = tk.Button(height=5 , width=10 , background='yellow' , command = lambda :self.player_move(self.b4))
        self.b5 = tk.Button(height=5 , width=10 , background='yellow' , command = lambda :self.player_move(self.b5))
        self.b6 = tk.Button(height=5 , width=10 , background='yellow' , command = lambda :self.player_move(self.b6))
        self.b7 = tk.Button(height=5 , width=10 , background='yellow' , command = lambda :self.player_move(self.b7))
        self.b8 = tk.Button(height=5 , width=10 , background='yellow' , command = lambda :self.player_move(self.b8))
        self.b9 = tk.Button(height=5 , width=10 , background='yellow' , command = lambda :self.player_move(self.b9))

        self.board = tk.Label(text = f'{self.shape[self.i]} Turns', background='blue' , height=5 , width=10 , padx=4)


        self.board.grid(column=2 , row = 0)
        self.b1.grid(column= 1 , row = 1)
        self.b2.grid(column= 2 , row = 1)
        self.b3.grid(column= 3 , row = 1)
        self.b4.grid(column= 1 , row = 2)
        self.b5.grid(column= 2 , row = 2)
        self.b6.grid(column= 3 , row = 2)
        self.b7.grid(column= 1 , row = 3)
        self.b8.grid(column= 2 , row = 3)
        self.b9.grid(column= 3 , row = 3)
        tk.mainloop()

    def disabled(self , state = tk.DISABLED, text = None , is_won = True, color = None):
        if is_won and self.game_mode:
            self.board.config(text = f'{self.shape[self.i * -1]} Won')


        if is_won and self.game_mode == 'computer':
            self.board.config(text = f'{self.chracter} Won')
            self.won = True

        self.b1.config(state=state , text = text , background= color)
        self.b2.config(state=state , text = text , background= color)
        self.b3.config(state=state , text = text , background= color)
        self.b4.config(state=state , text = text , background= color)
        self.b5.config(state=state , text = text , background= color)
        self.b6.config(state=state , text = text , background= color)
        self.b7.config(state=state , text = text , background=color)
        self.b8.config(state=state , text = text , background= color)
        self.b9.config(state=state ,text = text , background=color)



    def restat(self , game_mode = None):

        if game_mode:
            self.game_mode = game_mode

        self.check = 0
        self.move_count = 0
        self.won = False
        state = tk.NORMAL
        self.disabled(state , '' , False , 'yellow')


        if self.game_mode == 'player':
            self.i *= -1

        else:
            player.move_chooser(self)

        self.board.config(text = f'{self.shape[self.i]} turn')


class player(blue_print):


    def player_move(self , n ):

        self.chracter = 'player'

        n.config(text = self.shape[self.i] , state = tk.DISABLED , foreground= 'blue' , disabledforeground='blue')
        if self.game_mode == 'player':
            self.i *= -1
        self.board.config(text = f'{self.shape[self.i ]} Turns')
        self.check_winner()



        if self.game_mode == 'computer':
            self.computer_move()


    def move_chooser(self):

            self.choosing = choice(self.shape[1::])

            if self.choosing == 'X':
                self.player_angle = self.choosing
                self.computer_angle = 'O'
                self.i = 1

            else:

                self.player_angle = self.choosing
                self.computer_angle = "X"
                self.i = -1
                self.computer_move()



        
    def swaping(self):



        self.temp_move = self.first_move
        self.first_move = self.second_move
        self.second_move = self.result
        self.result = self.temp_move


    def defending(self, value):

        self.is_move = True
        value.config(text = self.computer_angle ,
                state = tk.DISABLED ,foreground= 'blue' , disabledforeground='blue')


        self.check_winner()



    def computer_move(self):

        if not self.won:
            self.chracter = 'computer'

        self.moves = [[self.b1 , self.b2 , self.b3] ,
                 [self.b4 , self.b5,  self.b6] ,
                 [self.b7 , self.b8 , self.b9]]

        '''
        b1 == b2 
        b1 == b3
        b2 == b3
     
        
        '''

        self.is_move = False


        for move_num,move in enumerate(self.moves):
            for i in range(3):

                if self.won:
                    break

                elif not move_num:
                    if(self.moves[self.first_move][self.first_move]['text'] == self.moves[self.second_move][self.second_move]['text'] != ''
                    and self.moves[self.result][self.result]['text'] == ''):
                        self.defending(self.moves[self.result][self.result])

                    elif(self.moves[self.first_move][2 - self.first_move]['text'] ==  self.moves[self.second_move][2 - self.second_move]['text'] != ''
                    and self.moves[self.result][2 - self.result]['text'] == ''):

                        self.defending(self.moves[self.result][2 - self.result])





                if not self.is_move:
                    if(move[self.first_move]['text'] == move[self.second_move]['text'] != '' and move[self.result]['text'] == '') and not self.is_move:

                            self.defending(move[self.result])



                    elif(self.moves[self.second_move][move_num]['text'] == self.moves[self.first_move][move_num]['text'] != ''
                        and self.moves[self.result][move_num]['text'] == ''):

                            self.defending(self.moves[self.result][move_num])



                self.swaping()





        if not self.is_move:
            self.raindom_move()

    def raindom_move(self):

        while not self.is_move and not self.won :



            thinking = choice(choice(self.moves))
            if thinking['text'] == '':

                thinking.config(text = self.computer_angle ,
                state = tk.DISABLED ,foreground= 'blue' , disabledforeground='blue')
                self.is_move = True

            if self.check == 9:
                break




        self.check_winner()





    def check_winner(self):

        self.check += 1



        if self.b1['text'] == self.b2['text'] == self.b3['text'] != '':

            self.b1.config(background='red')
            self.b2.config(background='red')
            self.b3.config(background='red')
            self.disabled()

        elif self.b4['text'] == self.b5['text'] == self.b6['text'] != '':

            self.b4.config(background='red')
            self.b5.config(background='red')
            self.b6.config(background='red')
            self.disabled()

        elif self.b7['text'] == self.b8['text'] == self.b9['text'] != '':

            self.b7.config(background='red')
            self.b8.config(background='red')
            self.b9.config(background='red')
            self.disabled()


        elif self.b1['text'] == self.b4['text'] == self.b7['text'] != '':

            self.b1.config(background='red')
            self.b4.config(background='red')
            self.b7.config(background='red')
            self.disabled()

        elif self.b2['text'] == self.b5['text'] == self.b8['text'] != '':

            self.b2.config(background='red')
            self.b5.config(background='red')
            self.b8.config(background='red')
            self.disabled()

        elif self.b3['text'] == self.b6['text'] == self.b9['text'] != '':

            self.b3.config(background='red')
            self.b6.config(background='red')
            self.b9.config(background='red')
            self.disabled()

        elif self.b1['text'] == self.b5['text'] == self.b9['text'] != '':


            self.b1.config(background='red')
            self.b5.config(background='red')
            self.b9.config(background='red')
            self.disabled()

        elif self.b3['text'] == self.b5['text'] == self.b7['text'] != '':

            self.b3.config(background='red')
            self.b5.config(background='red')
            self.b7.config(background='red')
            self.disabled()

        elif self.check == 9:
            self.board.config(text = 'Tied')





player = player()
