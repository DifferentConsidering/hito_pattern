

class Pattern:
    def __init__(
            self,
            line_length,
            x1,
            y1,
            row_nums,
            col_nums,
            win=None
    ):
        self.line_length = line_length
        self._window = win
        self._x1 = x1
        self._y1 = y1
        self.row_nums = row_nums
        self.col_nums = col_nums

    def draw_lines(self):
        for y in self.row_nums:
            for x in self.col_nums:
                if y % 2 != 0:


    def draw_line(self, )

