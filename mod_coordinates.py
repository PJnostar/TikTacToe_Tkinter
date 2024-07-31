#----------------------------------------------------------------------------------------------------------
#------------------------------------Position functions----------------------------------------------------
#----------------------------------------------------------------------------------------------------------

#   pixel_xy are xy coordinates in pixels (where players click on the screen)
#   grid_xy are xy coordinates in (0,1,2) values corresponding to squares in the game
def convert_grid_to_pixel(canvas_size, grid_xy):
    pixel_xy = [grid_xy[0]*(canvas_size/3)+canvas_size/6, grid_xy[1]*(canvas_size/3)+canvas_size/6]
    return pixel_xy

def convert_pixel_to_grid(canvas_size, pixel_xy):
    grid_xy = [int(pixel_xy[0]//(canvas_size/3)), int(pixel_xy[1]//(canvas_size/3))]
    return grid_xy

def grid_status(board_status, grid_xy):
    """
    Checks if someone has already used the clicked square. Return True is square has already been clicked (is occupied) 
    """
    if board_status[grid_xy[1]][grid_xy[0]] == 0:
        return False
    else:
        return True
    