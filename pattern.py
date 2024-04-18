from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Pattern Generator")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed...")

    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)

    def close(self):
        self.__running = False

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(
        self,
        p1,
        p2,
    ):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_color="black"):
        canvas.create_line(
            self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2
        )
        canvas.pack(fill=BOTH, expand=1)

class Pattern:
    def __init__(
            self,
            h_lines,
            v_lines
    ):
        self._h_lines = horizontal_lines
        self._v_lines = vertical_lines

    def _draw_pattern(self):
        for i in range(self.h_lines):
            for j in range(self.v_lines):
                pass

horizontal_lines = [1,1,0,1,0,0,1,0,0,0,0,1,1,1,0,1]
vertical_lines = [0,0,1,1,0,0,1,0,0,1,1,1,1]

new_pattern = Pattern(horizontal_lines, vertical_lines)

print(new_pattern._h_lines)