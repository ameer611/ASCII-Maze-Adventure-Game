import os
import random

list_of_elements = []

congratulation_image = """
╔════════════════════════════════════════╗
║                                        ║
║       🎉  CONGRATULATIONS! 🎉          ║
║                                        ║
║     You have achieved victory!         ║
║                                        ║
║    Thanks for playing the game!        ║
║                                        ║
╚════════════════════════════════════════╝
"""


def generate_random_number():
    return random.randint(15, 25)

def generate_maze(random_number):
    double_random_number = random_number * 2

    for i in range(random_number):  # column
        # rows
        if i == 0 or i == random_number - 1:
            list_of_elements.append(['-' for _ in range(double_random_number)])
        else:
            list_of_elements.append(
                ['|' if i == 0 or i == double_random_number - 1 else " " for i in range(double_random_number)])
    list_of_elements[0][0] = "+"
    list_of_elements[0][-1] = "+"
    list_of_elements[-1][0] = "+"
    list_of_elements[-1][-1] = "+"


def put_barriers(random_number):
    number_of_barriers = int(random_number**2*0.25)
    for i in range(number_of_barriers):
        choice = '*'
        random_row_index = random.randint(2, random_number-3)
        random_column_index = random.randint(1, random_number*2-2)
        list_of_elements[random_row_index][random_column_index] = choice


def find_position(list_of_elements):
    index_column = 1
    index_row = 1
    for i in range(1, len(list_of_elements) - 1):
        for j in range(1, len(list_of_elements[i]) - 1):
            if list_of_elements[i][j] == '😊':
                index_column = j
                index_row = i
                break
    return index_row, index_column

# movements
def move_right(index_row, index_column):
    list_of_elements[index_row][index_column] = ' '
    for i in range(index_column, len(list_of_elements[index_row])):
        if list_of_elements[index_row][i] == '*' or list_of_elements[index_row][i] == '|':
            list_of_elements[index_row][i-1] = '😊'
            break

def move_left(index_row, index_column):
    list_of_elements[index_row][index_column] = ' '
    for i in range(index_column, -1, -1):
        if list_of_elements[index_row][i] == '*' or list_of_elements[index_row][i] == '|':
            list_of_elements[index_row][i+1] = '😊'
            break

def move_up(index_row, index_column):
    list_of_elements[index_row][index_column] = ' '
    for i in range(index_row, -1, -1):
        if list_of_elements[i][index_column] == '*' or list_of_elements[i][index_column] == '-':
            list_of_elements[i+1][index_column] = '😊'
            break

def move_down(index_row, index_column):
    list_of_elements[index_row][index_column] = ' '
    for i in range(index_row, len(list_of_elements)):
        if list_of_elements[i][index_column] == '*' or list_of_elements[i][index_column] == '-':
            list_of_elements[i-1][index_column] = '😊'
            break

def print_menu():
    for i in list_of_elements:
        print(' '.join(i))

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def main():
    random_number = generate_random_number()
    generate_maze(random_number)
    list_of_elements[1][1] = '😊'
    list_of_elements[random_number-2][random_number*2-2] = '🚩'
    put_barriers(random_number)

    message = None
    while True:
        clear()
        if message is not None:
            print(message)
        print_menu()
        movement = input('Enter your movement: (<, >, ^, v) -> ')
        match movement:
            case '<':
                message = 'Moved left'
                index_row, index_column = find_position(list_of_elements)
                move_left(index_row, index_column)
            case '>':
                message = 'Moved right'
                index_row, index_column = find_position(list_of_elements)
                move_right(index_row, index_column)

            case '^':
                message = 'Moved up'
                index_row, index_column = find_position(list_of_elements)
                move_up(index_row, index_column)

            case 'v':
                message = 'Moved down'
                index_row, index_column = find_position(list_of_elements)
                move_down(index_row, index_column)

            case _:
                message = '!!! Invalid movement !!!'

        if list_of_elements[random_number-2][random_number*2-2] == "😊":
            clear()
            return congratulation_image

print(main())








