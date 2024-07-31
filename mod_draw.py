import tkinter as tk

def create_mark(game_canvas: tk.Canvas, player, pixel_xy):
    """
    Create mark X(O) when player A(B) clicks on a board
    """
    size = 40
    if player == 1:
        game_canvas.create_line([pixel_xy[0]-size, pixel_xy[1]-size], [pixel_xy[0]+size, pixel_xy[1]+size], width=8, fill="red")
        game_canvas.create_line([pixel_xy[0]-size, pixel_xy[1]+size], [pixel_xy[0]+size, pixel_xy[1]-size], width=8, fill="red")
    else:
        game_canvas.create_oval([pixel_xy[0]-size, pixel_xy[1]-size], [pixel_xy[0]+size, pixel_xy[1]+size], width=8, outline="green")