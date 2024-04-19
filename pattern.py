from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Pattern Generator")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False

    def draw_line(self, line, fill_color="black"):
        self.__canvas.create_line(
            line.p1.x, line.p1.y, line.p2.x, line.p2.y, fill=fill_color, width=2
        )
        self.__canvas.pack(fill=BOTH, expand=1)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed...")

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

class Pattern:
    def __init__(
            self,
            h_lines,
            v_lines,
            line_length,
            window = None
    ):
        self._h_lines = h_lines
        self._v_lines = v_lines
        self._line_length = line_length
        self._current_point = [line_length, line_length]
        self.window = window

    def draw_pattern(self):
        for i in range(len(self._h_lines)):
            for j in range(len(self._v_lines)):
                if (self._h_lines[i] ^ int(((self._current_point[1] / self._line_length) % 2))):
                    point1 = Point(self._current_point[0], self._current_point[1])
                    point2 = Point(self._current_point[0], self._current_point[1] + self._line_length)
                    line = Line(point1, point2)
                    print("Drawing Vertical Line")
                    self.window.draw_line(self, line)

                if (self._v_lines[j] ^ int(((self._current_point[0] / self._line_length) % 2))):
                    point1 = Point(self._current_point[0], self._current_point[1])
                    point2 = Point(self._current_point[0] + self._line_length, self._current_point[1])
                    line = Line(point1, point2)
                    print("Drawing Horizontal Line")
                    self.window.draw_line(self, line)

                self._current_point[1] += self._line_length

            self._current_point[1] += self._line_length
            self._current_point[0] += self._line_length

horizontal_lines = [1,1,0,1,0,0,1,0,0,0,0,1,1,1,0,1]
vertical_lines = [0,0,1,1,0,0,1,0,0,1,1,1,1]

window = Window(len(horizontal_lines), len(vertical_lines))
new_pattern = Pattern(horizontal_lines, vertical_lines, 10, window)
new_pattern.draw_pattern()

print(new_pattern._h_lines, new_pattern._v_lines)