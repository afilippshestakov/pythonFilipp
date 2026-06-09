from typing import Tuple
Coordinate = Tuple[int, int]

def circolari_in_quadro(side: int, pos: int) -> Coordinate:
	'''
	traduce le cordinate circolari_in_quadro(righe e colone) 
	'''
	
	if pos <= (side - 1) * 1 - 1:
		return (side - 1, side - pos - 1)
	elif pos <= (side - 1) * 2 - 1:
		return (side - 1 - pos % (side - 1), 0)
	elif pos <= (side - 1) * 3 - 1:
		return (0, pos % (side - 1))

	else:
		return (pos % (side - 1), side - 1)




def square_board(side: int, token: int, steps: int) -> Coordinate:
	circolari_range = (side - 1) * 4
	pos_new = (token + steps) % circolari_range
	if pos_new < 0:
		pos_new = pos_new + circolari_range
	return circolari_in_quadro(side, pos_new)

if __name__ == '__main__':
    print("Example:")
    print(square_board(10, 7, 0))
    assert square_board(10,7,36) == (9, 2)
    assert circolari_in_quadro(4, 2) == (3, 1)
    assert circolari_in_quadro(6, 6) == (4, 0)
    assert circolari_in_quadro(6, 16) == (1, 5)
    assert square_board(4, 1, 4) == (1, 0)
    assert square_board(6, 2, -3) == (4, 5)

    print("Coding complete? Click 'Check' to earn cool rewards!")