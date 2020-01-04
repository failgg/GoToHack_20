poligon = [['.'] * 30 for i in range(30)]

my_color = '*'

moves = []


def position(move, coord_x, coord_y):
    global moves
    moves.append((move, coord_x, coord_y))


def bot(coord_x, coord_y, color):
    global poligon
    if coord_x < 0 or coord_x > len(poligon[coord_y]) or coord_y < 0 or coord_y > len(poligon) or color == my_color:
        return
    poligon[coord_y][coord_x] = '*'
    if coord_x > 0 and color != my_color:
        position('coord_x - 1', coord_x - 1, coord_y)
        bot(coord_x - 1, coord_y, poligon[coord_y][coord_x - 1])
    if coord_x < len(poligon[coord_y]) - 1 and color != my_color:
        position('coord_x + 1', coord_x + 1, coord_y)
        bot(coord_x + 1, coord_y, poligon[coord_y][coord_x + 1])
    if coord_y > 0 and color != my_color:
        position('coord_y - 1', coord_x, coord_y - 1)
        bot(coord_x, coord_y - 1, poligon[coord_y - 1][coord_x])
    if coord_y < len(poligon) - 1 and color != my_color:
        position('coord_y + 1', coord_x, coord_y + 1)
        bot(coord_x, coord_y + 1, poligon[coord_y + 1][coord_x])


bot(0, 0, '.')

# print(*poligon, sep='\n')

print(moves[:20])
