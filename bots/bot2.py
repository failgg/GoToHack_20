poligon = [['.'] * 30 for i in range(30)]

my_color = '*'

coord_x = coord_y = 0

def Tick(coord_x, coord_y):
    pixel = get_pixel(coord_x, coord_y)

def move(coord_x, coord_y):
    global poligon
    if coord_x > 0 and get_pixel(coord_x, coord_y) != my_color:
        return 'move_left()'
    elif coord_x < len(poligon[coord_y]) - 1 and get_pixel(coord_x, coord_y) != my_color:
        return 'move_right()'
    elif coord_y > 0 and get_pixel(coord_x, coord_y) != my_color:
        return 'move_down()'
    elif coord_y < len(poligon) - 1 and get_pixel(coord_x, coord_y) != my_color:
        return 'move_up()'


def get_pixel(coord_x, coord_y):
    global poligon
    return poligon[coord_y][coord_x]


while True:
