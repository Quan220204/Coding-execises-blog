class Node(): 
 
    def __init__(self, parent=None, position=None, number = 0): 
        # Initialize all attributes that we want a node to have 
        # List to store child nodes 
        self.children = [] 
        # Store parent node for later path tracing 
        self.parent = parent 
        # Store position of node, with respect to puzzle 
        self.position = position 
 
        # Store the g,h, and f values 
        self.number = number
 
    def expand(self, puzzle): 
        # Loop through all possible movements 
        for movement in [(0, -1), (0, 1), (-1, 0), (1, 0)]: 
 
            # Get node position after moving 
            node_position = (self.position[0] + movement[0], self.position[1] + movement[1]) 
 
            # Check that the new node is within the boundaries of the puzzle 
            if node_position[0] <= (len(puzzle) - 1) and node_position[0] >= 0 and node_position[1] <= (len(puzzle[len(puzzle)-1]) - 1) and node_position[1] >= 0: 
 
                # Check if its trying to move into a position occupied by a wall 
                if puzzle[node_position[0]][node_position[1]] == 0: 

                    # Check if its trying to move into its parent's position:
                        if self.parent != None:
                            if node_position == self.parent.position:
                                continue
                            
                        # Create new child 
                        child = Node(self, node_position, self.number + 1) 
                        self.children.append(child) 

def flood_fill(puzzle, start, end): 

    # initialize node with unknown parent and "end" coords 
    end_node = Node(None, end, 0) 

    # initialize node with no parent and "start" coords 
    start_node = Node(None, start)
 
    # Initialize open list 
    open_list = [] 
 
    # Add the end node 
    open_list.append(end_node) 
 
    # Loop until you find the end 
    while len(open_list) > 0: 
        # Get the current node 
        current_node = open_list.pop(0) 

        # Check if it has found the start node yet:
        if current_node.position == start_node.position:
            path_to_solution = [] 
            current = current_node 
            while current is not None: 
                path_to_solution.append(current.position) 
                current = current.parent 
            return list(path_to_solution)

        current_node.expand(puzzle) 

        for child in current_node.children:
            x, y = child.position
            num = child.number

            # Fill with the number
            puzzle[x][y] = num

            open_list.append(child)


if __name__ == '__main__': 
    puzzle = [[0, 0, 0, 0, -1, 0, 0, 0, 0, 0], 
              [0, 0, 0, 0,  0, 0, 0, 0, 0, 0], 
              [0, 0, 0, 0, -1, 0, 0, 0, 0, 0], 
              [0, 0, 0, 0, -1, 0, 0, 0, 0, 0], 
              [0, 0, 0, 0, -1, 0, 0, 0, 0, 0], 
              [0, 0, 0, 0,  0, 0, 0, 0, 0, 0], 
              [0, 0, 0, 0, -1, 0, 0, 0, 0, 0], 
              [0, 0, 0, 0, -1, 0, 0, 0, 0, 0], 
              [0, 0, 0, 0, -1, 0, 0, 0, 0, 0], 
              [0, 0, 0, 0, -1, 0, 0, 0, 0, 0]] 
            # [15, 14, 13, 12, -1, 10, 9, 8, 7, 8]
            # [14, 13, 12, 11, 10,  9, 8, 7, 6, 7]
            # [13, 12, 11, 10, -1,  8, 7, 6, 5, 6]
            # [12, 11, 10,  9, -1,  7, 6, 5, 4, 5]
            # [11, 10,  9,  8, -1,  6, 5, 4, 3, 4]
            # [10,  9,  8,  7,  6,  5, 4, 3, 2, 3]
            # [11, 10,  9,  8, -1,  4, 3, 2, 1, 2]
            # [12, 11, 10,  9, -1,  3, 2, 1, 0, 1]
            # [13, 12, 11, 10, -1,  4, 3, 2, 1, 2]
            # [14, 13, 12, 11, -1,  5, 4, 3, 2, 3]
 
    start_point = (0, 0) 
    end_point = (7, 8) 

    # 7 rows, 11 columns, start = (0,6), goal = (4,8)
    puzzle = [[0,-1,0, 0, 0, 0, 0, 0, 0, 0,0],
              [0,-1,0,-1,-1,-1,-1,-1,-1,-1,0],
              [0,-1,0,-1, 0, 0, 0, 0, 0, 0,0],
              [0,-1,0,-1, 0,-1,-1,-1, 0,-1,0],
              [0, 0,0,-1, 0,-1, 0,-1, 0,-1,0],
              [0,-1,0,-1, 0,-1, 0,-1,-1,-1,0],
              [0,-1,0, 0, 0, 0, 0, 0, 0, 0,0]]
            # [20, -1, 14, 13, 12, 11, 10,  9,  8,  7, 6]
            # [19, -1, 15, -1, -1, -1, -1, -1, -1, -1, 5]
            # [18, -1, 16, -1,  6,  5,  4,  3,  2,  3, 4]
            # [17, -1, 15, -1,  7, -1, -1, -1,  1, -1, 5]
            # [16, 15, 14, -1,  8, -1, 14, -1,  0, -1, 6]
            # [17, -1, 13, -1,  9, -1, 13, -1, -1, -1, 7]
            # [18, -1, 12, 11, 10, 11, 12, 11, 10,  9, 8]
 
    start_point = (6, 0) 
    end_point = (4, 8) 

    path = flood_fill(puzzle, start_point, end_point)
    print(path) 

    for i in puzzle:
        print(i)
