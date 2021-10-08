

class Node(object):
  value = None
  left = None
  right = None

  def __init__(self, value, left_node, right_node):

    self.set_value(value) 
    self.set_left_node(left_node)
    self.set_right_node(right_node)

  def set_value(self, value: int) -> None:
    try: 
      self.value = int(value)
    except TypeError:
      raise ValueError(f'Node value {value} must be an integer.')

  def set_left_node(self, node: 'Node') -> None:
    if not node:
      self.left = None
      return 

    if type(node) != Node:
      raise ValueError(f'Set left node provided is not of type Node.')
    self.left = node

  def set_right_node(self, node: 'Node') -> None:
    if not node:
      self.right = None
      return 

    if type(node) != Node:
      raise ValueError(f'Set right node provided is not of type Node.')
    self.right = node
      

  def __str__(self) -> str: 
    ls = ""
    rs = ""
    if self.left is not None: 
      ls = self.left.__str__()

    if self.right is not None:
      rs = self.right.__str__()

    return ls + (", " + str(self.value) if len(ls) > 0 else str(self.value)) + (", " + rs if len(rs) > 0 else "")
    

class BinaryTree(object):
  
  def __init__(self) -> None:
    self.root = None

  def insert(self, value: int) -> None: 
    if self.root == None:
      self.root = Node(value, None, None)
      return
    
    node = self.root
    while node:
      if value == node.value: 
        raise ValueError(f'Value {value} already exists')

      if value < node.value:
        if node.left is None:
          node.left = Node(value, None, None) 
          return
        else: 
          node = node.left
      
      else:
        if node.right is None: 
          node.right = Node(value, None, None)
          return
        else: 
          node = node.right
      
  def search(self, value: int) -> bool:
    node = self.root
    while node:

      if node.value == value:
        return True 
      
      if value < node.value:
        node = node.left
      else:
        node = node.right
    
    return False

  def remove(self, value: int) -> None:
    parent_node = None
    parents_left = True
    node = self.root
    while node:

      if node.value == value:
        
        # Remove node with value less than parent
        if parents_left:
          if node.right is not None:
            replacing_node = node.right
            parent_node.left = replacing_node

            smallest_sub_node = replacing_node
            while smallest_sub_node.left:
              smallest_sub_node = smallest_sub_node.left
            smallest_sub_node.left = node.left
          
          else: 
            replacing_node = node.left 
            parent_node.left = replacing_node

        # Remove node with value greater than parent
        else:
          if node.left is not None:
            replacing_node = node.left
            parent_node.right = replacing_node

            largest_sub_node = replacing_node
            while largest_sub_node.right:
              largest_sub_node = largest_sub_node.right
            largest_sub_node.right = node.right
          
          else: 
            replacing_node = node.right
            parent_node.right = replacing_node

      if value < node.value:
        parent_node = node
        parents_left = True
        node = node.left
      else:
        parent_node = node
        parents_left = False
        node = node.right
    
    return False
      
      

  def __str__(self) -> str:
    return "\nBinary Tree: [" + self.root.__str__() + "]"
