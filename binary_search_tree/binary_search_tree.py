import sys
sys.path.append('..\queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        node = BinarySearchTree(value) # creating new node with value

        if value < self.value: # if value is less than current node
            if self.left == None: # if left of current node is none
                self.left = node # set left to current node
            else:
                self.left.insert(value) # recursion on left side with value
        elif value > self.value: # if value is greater than current node
            if self.right == None: # if right of current node is none
                self.right = node # set right to current node
            else:
                self.right.insert(value) # recursion on right side with value

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value: # if target equals current node return True
            return True

        if target < self.value: # if target is less than node 
            if self.left: # check if left of node exists
                return self.left.contains(target) # recursion on left of node
            else:
                return False
        
        if target > self.value: # if target is more than node 
            if self.right: # check if right of node exists
                return self.right.contains(target) # recursion on right of node
            else:
                return False
        

    # Return the maximum value found in the tree
    def get_max(self):
        max_node = self
        while max_node.right is not None: # while right of current node exists
            max_node = max_node.right # current node becomes right node
 
        return max_node.value


    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value) # call the callback on the self's value

        if self.right: # if right exists
            self.right.for_each(cb) # call right for_each with the cb

        if self.left: # if left exists
            self.left.for_each(cb) # left for_each with the cb

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint: Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node.left is not None: # check if left exists
            self.in_order_print(node.left) # go down left branch

        print(node.value) # print the current node before going right

        if node.right is not None: #c heck if right exists after left
            self.in_order_print(node.right) # go down right branch

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = Queue() # initialize Queue
        queue.enqueue(node) # add node to queue
        while queue.len() > 0:
            remove = queue.dequeue() # remove end of queue node                         
            print(remove.value) 
            if remove.left is not None: 
                queue.enqueue(remove.left) # add the left of removed node to queue if it exists
            if remove.right is not None:
                queue.enqueue(remove.right) # add the right of removed node to queue if it exists


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()
        stack.push(node)
        while stack.len() > 0:
            remove = stack.pop() # remove top of stack node
            print(remove.value) 
            if remove.left is not None: 
                stack.push(remove.left) # add the left of removed node to queue if it exists
            if remove.right is not None:
                stack.push(remove.right) # add the right of removed node to queue if it exists

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
