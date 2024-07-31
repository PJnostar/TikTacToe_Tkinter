import tkinter as tk
import mod_coordinates
import mod_draw
import mod_status


class Board():
    starting_winner_value = -3
    def __init__(self) -> None:
        self.screen_size = 800
        self.screen = tk.Tk()
        self.screen.title("Tic Tac Toe")
        self.canvas = tk.Canvas(self.screen, width=self.screen_size, height=self.screen_size)
        self.canvas.pack()
        self.canvas.configure(background='purple')

        self.screen.bind("<Button-1>", self.click)

        self.reset_game = False
        self.board_status = [[0,0,0], [0,0,0], [0,0,0]]
        self.active_player = 1      #1: player A, -1: player B
        self.winner = Board.starting_winner_value
        self.playerA_score = 0
        self.playerB_score = 0

        self.create_board() 

    def mainloop(self):
        self.screen.mainloop()

    def create_board(self):
        for i in range(1,3):
            self.canvas.create_line([i*float(self.screen_size)/3,0], [i*float(self.screen_size)/3, self.screen_size], width=5, fill="black")
            self.canvas.create_line([0, i*float(self.screen_size)/3], [self.screen_size, i*float(self.screen_size)/3], width=5, fill="black")

    def play_again(self):
        self.board_status = [[0,0,0], [0,0,0], [0,0,0]]
        self.canvas.delete("all")
        self.winner = Board.starting_winner_value
        self.reset_game = False
        self.create_board()    

    def display_score(self):
        score_text = 'Scores \n'
        self.canvas.create_text(self.screen_size / 2, 5 * self.screen_size / 8, font="cmr 40 bold", fill="Black",
                                text=score_text)
        score_text = 'Player 1 (X) : ' + str(self.playerA_score) + '\n'
        score_text += 'Player 2 (O): ' + str(self.playerB_score) + '\n'
        self.canvas.create_text(self.screen_size / 2, 3 * self.screen_size / 4, font="cmr 30 bold", fill="Black",
                                text=score_text)
        self.reset_game = True

    def click(self, event):
        pixel_xy = [event.x, event.y]
        grid_xy = mod_coordinates.convert_pixel_to_grid(self.screen_size, pixel_xy)
        pixel_xy = mod_coordinates.convert_grid_to_pixel(self.screen_size, grid_xy)
        
        if self.reset_game == False:
            #If player clicked on an unoccupied grid square, then draw mark and change players
            if not mod_coordinates.grid_status(self.board_status, grid_xy):
                mod_draw.create_mark(self.canvas, self.active_player, pixel_xy)
                self.board_status[grid_xy[1]][grid_xy[0]] = self.active_player
                self.active_player *= -1
                # print(self.board_status)
            
            #after every click check if there is a winner. IF there isnt a winner, check if the game is over (all fields are marked)
            [self.winner, self.playerA_score, self.playerB_score] = mod_status.game_result(self.board_status, self.winner, self.playerA_score, self.playerB_score)
            if mod_status.is_over(self.board_status):
                self.canvas.create_text([self.screen_size/2]*2, text="Game over", font=("Arial", 25))
                self.display_score()
            if self.winner == 1 or self.winner == -1 or self.winner == 0:
                self.display_score()
        #After someone wins a game and hte current score is displayed, force one more click to start a new game using the self.reset_game flag
        else:
            self.play_again()            