class Array2D:
    def __init__(self, tup, val):
        self.lin = tup[0]
        self.col = tup[1]
        self.val = val

    def __str__(self):
        for l_str in range(self.lin):
            tabR += '['
            for c_str in range(self.col):
                tabR += ' %s' %(self.val)
                if(c_str != self.lin):
                    tabR +=


