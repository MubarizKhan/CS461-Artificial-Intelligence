from collections import deque

class TreeNode:
    def __init__(self,val):
        self.val = val
        self.right = None
        self.left = None

class BST(TreeNode):
    def __init__(self,val, parent=None):
        super().__init__(val)
        self.parent = parent
        
    def insert(self,val):
        if val < self.val:
            if self.left is None:
                print('inserted at left')
                self.left = new_node = BST(val, parent = self)
                
                return self.left
            else:
                self.left.insert(val)
        elif val > self.val:
            if self.right is None:
                print('inserted at right')
                new_node = BST(val, parent = self)
                self.right = new_node
                return self.right
            else:
                self.right.insert(val)
                

    def ucs_search(self, root, goal):
        dic = {'R':{'M':1, 'V':5}, 'M':{'F':3, 'O':6}, 'V':{'T':9, 'Y':2},
        'F':{'A':3, 'G':4},'O':{'N':4, 'P':5}, 'T':{'S':8, 'U':6}, 'Y':{'X':7,
        'Z':9}}

        paths_def = [['R','M','F','A'], ['R','M','F','G'], ['R','M','O','N'],
        ['R','M','O','P'], ['R','V','T','S'], ['R','V','T','U'], ['R','V','Y','X'],
        ['R','V','Y','Z']]
        # for path to goal state
        path = []
        # to keep track of visited nodes
        visited_nodes = []
        # to calculate path cost
        cost = 0
        que = deque()
        que.append(root)
        # if root is goal
        if goal == root.val:
            path.append(root.val)
            return path, cost
        # if root is not goal
        while que:
            current = que.popleft()
            # to traverse a node only once
            if current not in visited_nodes:
                visited_nodes.append(current.val)
            if current.val == goal:
            # loop to get to root from goal state - for path
                while current:
                
                    path.append(current.val)
                    current = current.parent
            else:
                if current.left:
                    que.append(current.left)
                if current.right:
                    que.append(current.right)
        path.reverse()
        for i in range(0,len(path)-1):
            first = path[i]
            second = path[i+1]
            cost = cost + dic[first][second]
        return path, cost
                
if __name__ == '__main__':
    b = BST('R')
    a1 = b.insert('M')
    a2 = b.insert('F')
    a3 = b.insert('O')
    a4 = b.insert('A')
    a5 = b.insert('G')
    a6 = b.insert('N')
    a7 = b.insert('P')
    a8 = b.insert('V')
    a9 = b.insert('T')
    a10 = b.insert('Y')
    a11 = b.insert('S')
    a12 = b.insert('U')
    a13 = b.insert('X')
    a14 = b.insert('Z')
    # print_tree(b)
    path, cost = b.ucs_search(a8, a14)