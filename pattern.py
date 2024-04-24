from graphics import Point, Line, Window
import time
        
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
        self.current_point = Point(line_length, line_length)
        self.window = window

    def _animate(self):
        if self.window is None:
            return
        self.window.redraw()
        time.sleep(0.002)

    def draw_pattern(self):

        if self.window is None:
            return None
        else:
            for i in range(len(self._h_lines)):
                for j in range(len(self._v_lines)):
                    if (int(self._h_lines[i]) ^ int(((self.current_point.y / self._line_length) % 2))):
                        point1 = Point(self.current_point.x, self.current_point.y)
                        point2 = Point(self.current_point.x, self.current_point.y + self._line_length)
                        line = Line(point1, point2)
                        print("Drawing Vertical Line")
                        self.window.draw_line(line)
                        self._animate()

                    if (int(self._v_lines[j]) ^ int(((self.current_point.x / self._line_length) % 2))):
                        point1 = Point(self.current_point.x, self.current_point.y)
                        point2 = Point(self.current_point.x + self._line_length, self.current_point.y)
                        line = Line(point1, point2)
                        print("Drawing Horizontal Line")
                        self.window.draw_line(line)
                        self._animate()

                    self.current_point.y += self._line_length

                self.current_point.y = self._line_length
                self.current_point.x += self._line_length