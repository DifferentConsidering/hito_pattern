from graphics import Window
from pattern import Pattern



def main():
    # Typically first and last name. Input will be split for horizontal and vertical lines.
    text = input('Enter text for the pattern: \r \n')
    all_bytes = ''.join(format(ord(i), '08b') for i in text)
    print(all_bytes)
    horizontal_lines = all_bytes[:len(all_bytes) // 2]
    vertical_lines = all_bytes[len(all_bytes) // 2 :]
    line_width = int(input('Enter line length: (Recommend increments of 5)'))

    window = Window(800, 600)
    new_pattern = Pattern(horizontal_lines, vertical_lines, line_width, window)
    new_pattern.draw_pattern()

    window.wait_for_close()

main()