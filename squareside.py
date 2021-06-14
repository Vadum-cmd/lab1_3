"""
Module for solving problem.
Git link: 
"""
def user_input():
    '''
    This function takes data from user: 3 sides of triangle and accuracy.
    Return tuple with this data.
    '''
    print("Enter only 4 parameters: 3 sides of triangle and accuracy")
    first_side = input()
    sec_side = input()
    third_side = input()
    accuracy = input() 
    return first_side, sec_side, third_side, accuracy


def triangle_area(first_side: float, sec_side: float, third_side: float) -> float:
    '''
    This function counts area of big triangle by using Geron's formula.
    Return area.
    >>> triangle_area(3, 4, 5)
    6.0
    '''
    semi_perim = (first_side + sec_side + third_side) / 2
    geron_area = (semi_perim * (semi_perim-first_side) * (semi_perim-sec_side) * (semi_perim-third_side))**0.5
    return geron_area


def square_area(geron_area: float, third_side: float, accuracy: int) -> float:
    '''
    This function counts side of square in triangle.
    Return this side.
    >>> square_area(6, 4)
    4.760330578512396
    '''
    height = 2 * geron_area / third_side
    side = 2 * geron_area / (height + third_side)
    side = '{:.{}f}'.format(side, accuracy)
    return side


def write_in_file(side: float) -> None:
    '''
    This function writes area of aquare into a file.
    Returns None
    '''
    with open("solution", "w", encoding="utf-8") as file:
        file.write(side)


def main():
    tpl = user_input()
    triangle = triangle_area(float(tpl[0]), float(tpl[1]), float(tpl[2]))
    square = square_area(triangle, float(tpl[2]), int(tpl[3]))
    write_in_file(square)
    print("Done!")


if __name__ == '__main__':
    main()
