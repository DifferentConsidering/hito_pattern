from graphics import Window
from pattern import Pattern



def main():

    horizontal_lines = [1,1,0,1,0,0,1,0,0,0,0,1,1,1,0,1]
    vertical_lines = [0,0,1,1,0,0,1,0,0,1,1,1,1]

    window = Window(len(horizontal_lines), len(vertical_lines))
    new_pattern = Pattern(horizontal_lines, vertical_lines, 10, window)
    new_pattern.draw_pattern()


    print("Drawing Pattern")
    window.wait_for_close()

main()