

class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.data)
    
class maxHeap(Node):

    def __init__(self):
        self.root = None
        self.items = []
        self.max = None
        self.min = None
        self.row = 0
        self.column = 0

    def __repr__(self):
        return "\n".join([str(l) for l in self.items])

    def swap_up(self, par_cor, chl_cor):
        par_r = par_cor[0]
        par_c = par_cor[1]
        chl_r = chl_cor[0]
        chl_c = chl_cor[1]
        
        if self.items[chl_r][chl_c].data >= self.items[par_r][par_c].data:
            par_data = self.items[par_r][par_c].data
            self.items[par_r][par_c].data = self.items[chl_r][chl_c].data
            self.items[chl_r][chl_c].data = par_data
            chl_r = par_r
            chl_c = par_c
            par_r -= 1
            par_c //= 2
            if par_r == -1 and par_c == 0:
                self.root = self.items[chl_r][chl_c]
            else:
                return self.swap_up([par_r, par_c], [chl_r, chl_c])
            
    def swap_down(self, par_cor, chl_cor):
        par_r = par_cor[0]
        par_c = par_cor[1]
        chl_r = chl_cor[0]
        chl_c = chl_cor[1]
        
        par_data = self.items[par_r][par_c].data
        if chl_r < len(self.items) and chl_c < len(self.items[chl_r]):
            try:
                self.items[par_r][par_c].data = self.items[chl_r][chl_c].data
                self.items[chl_r][chl_c].data = par_data
            except IndexError:
                chl_c = -1
                self.items[par_r][par_c].data = self.items[chl_r][chl_c].data
                self.items[chl_r][chl_c].data = par_data
        par_r = chl_r
        par_c = chl_c
        chl_r += 1
        chl_c *= 2
        if par_r < len(self.items)-1:
            return self.swap_down([par_r, par_c], [chl_r, chl_c])
        


    def insert(self, data):
        if self.min == None:
            self.min = data
        elif data <= self.min:
            self.min = data
        else:
            self.min = self.min
        if self.root == None:
            self.root = Node(data)
            self.items.append([self.root])
        else:
            if len(self.items[-1]) == 2**(len(self.items)-1):
                self.items.append([Node(data)])
                self.row += 1
                self.column = 0
            else:
                self.items[-1].append(Node(data))
                self.column += 1
            if self.items[self.row-1][self.column//2].left == None:
                self.items[self.row-1][self.column//2].left = self.items[self.row][self.column]
            else:
                self.items[self.row-1][self.column//2].right = self.items[self.row][self.column]
            self.swap_up([self.row-1,self.column//2],[self.row,self.column])
            self.max = self.items[0][0]
            
    def find_max(self):
       return self.max
    
    def find_min(self):
        return self.min

class minHeap(Node):

    def __init__(self):
        self.root = None
        self.items = []
        self.max = None
        self.min = None
        self.row = 0
        self.column = 0

    def __repr__(self):
        return "\n".join([str(l) for l in self.items])

    def swap_up(self, par_cor, chl_cor):
        par_r = par_cor[0]
        par_c = par_cor[1]
        chl_r = chl_cor[0]
        chl_c = chl_cor[1]
        
        if self.items[chl_r][chl_c].data <= self.items[par_r][par_c].data:
            par_data = self.items[par_r][par_c].data
            self.items[par_r][par_c].data = self.items[chl_r][chl_c].data
            self.items[chl_r][chl_c].data = par_data
            chl_r = par_r
            chl_c = par_c
            par_r -= 1
            par_c //= 2
            if par_r == -1 and par_c == 0:
                self.root = self.items[chl_r][chl_c]
            else:
                return self.swap_up([par_r, par_c], [chl_r, chl_c])

    def swap_down(self, par_cor, chl_cor):
        par_r = par_cor[0]
        par_c = par_cor[1]
        chl_r = chl_cor[0]
        chl_c = chl_cor[1]
        
        par_data = self.items[par_r][par_c].data
        if chl_r < len(self.items) and chl_c < len(self.items[chl_r]):
            try:
                self.items[par_r][par_c].data = self.items[chl_r][chl_c].data
                self.items[chl_r][chl_c].data = par_data
            except IndexError:
                chl_c = -1
                self.items[par_r][par_c].data = self.items[chl_r][chl_c].data
                self.items[chl_r][chl_c].data = par_data
        par_r = chl_r
        par_c = chl_c
        chl_r += 1
        chl_c *= 2
        if par_r < len(self.items)-1:
            return self.swap_down([par_r, par_c], [chl_r, chl_c])


    def insert(self, data):
        if self.max == None:
            self.max = data
        elif data >= self.max:
            self.max = data
        else:
            self.max = self.max
        if self.root == None:
            self.root = Node(data)
            self.items.append([self.root])
        else:
            if len(self.items[-1]) == 2**(len(self.items)-1):
                self.items.append([Node(data)])
                self.row += 1
                self.column = 0
            else:
                self.items[-1].append(Node(data))
                self.column += 1
            if self.items[self.row-1][self.column//2].left == None:
                self.items[self.row-1][self.column//2].left = self.items[self.row][self.column]
            else:
                self.items[self.row-1][self.column//2].right = self.items[self.row][self.column]
            self.swap_up([self.row-1,self.column//2],[self.row,self.column])
            self.min = self.items[0][0]
            
    def find_max(self):
       return self.max
    
    def find_min(self):
        return self.min

maxh = maxHeap()
minh = minHeap()

maxh.insert(5)
maxh.insert(2)
maxh.insert(7)
maxh.insert(4)
maxh.insert(1)
maxh.insert(3)
maxh.insert(6)


minh.insert(5)
minh.insert(2)
minh.insert(7)
minh.insert(4)
minh.insert(1)
minh.insert(3)
minh.insert(6)

print(maxh)
print()
print(minh)
