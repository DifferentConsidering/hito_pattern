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
        self._current_point = [line_length, line_length]
        self.window = window

    def _animate(self):
        if self.window is None:
            return
        self.window.redraw()
        time.sleep(0.02)

    def draw_pattern(self):

        if self.window is None:
            return None
        else:
            for i in range(len(self._h_lines)):
                for j in range(len(self._v_lines)):
                    if (self._h_lines[i] ^ int(((self._current_point[1] / self._line_length) % 2))):
                        point1 = Point(self._current_point[0], self._current_point[1])
                        point2 = Point(self._current_point[0], self._current_point[1] + self._line_length)
                        line = Line(point1, point2)
                        print("Drawing Vertical Line")
                        self.window.draw_line(line)

                    if (self._v_lines[j] ^ int(((self._current_point[0] / self._line_length) % 2))):
                        point1 = Point(self._current_point[0], self._current_point[1])
                        point2 = Point(self._current_point[0] + self._line_length, self._current_point[1])
                        line = Line(point1, point2)
                        print("Drawing Horizontal Line")
                        self.window.draw_line(line)

                    self._current_point[1] += self._line_length

                self._current_point[1] += self._line_length
                self._current_point[0] += self._line_length