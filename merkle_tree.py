from hashlib import sha256

def merkle_hash(left, right=''):
  res = "%s%s" % (left ,right)
  return sha256(res.encode('utf-8')).hexdigest()

class MerkleTree:
  def __init__(self, data_array):
    self.leaves = self.build_leaves(data_array)
    self.tree = self.build_tree()
    self.differences = []

  def build_leaves(self, data_array):
    leaves = []
    for data in data_array:
      leaves.append(merkle_hash(data))
    return leaves

  def build_tree(self):
    levels = []
    levels.append(self.leaves)
    level = self.leaves
    while len(level) > 1:
      level = self.build_level(level)
      levels.append(level)
    return levels

  def build_level(self, lower_level):
    level = []
    for i in range(0, len(lower_level), 2):
      left = lower_level[i]
      if i+1 < len(lower_level):
        right = lower_level[i+1]
        level.append(merkle_hash(left, right))
      else:
        level.append(merkle_hash(left))
    return level

  def root(self):
    return self.tree[-1][0]

  def root_index(self):
    return [len(self.tree) - 1, 0]

  def get_level(self, level):
    return self.tree[level]

  def print_tree(self):
    for level in self.tree:
      for node in level:
        print(node, end=' ')
      print()

  def get_children(self, height=-1, node=0):
    children = []
    for child_offset in self.get_children_indexes(height, node):
      children.append(self.get_key(height-1, child_offset))
    return children
  
  def get_key(self, height, node):
    return self.tree[height][node]
  
  def get_children_indexes(self, height, node):
    if height < 1:
      return []

    left = node*2
    if left+1 < len(self.tree[height-1]):
      return [left, left+1] # left, right
    else:
      return [left]

  def compare(self, other): # TO DO: maybe override __eq__ instead
    return self.root() == other.root()

  def equal_keys(self, other, height, offset):
    return self.get_key(height, offset) == other.get_key(height, offset)

  def compare_tree(self, other, current_index):
    current_height, current_offset = current_index

    if self.equal_keys(other, current_height, current_offset):
      return True

    if current_height == 0:
      if self.get_key(0, current_offset) != other.get_key(0, current_offset):
        self.differences.append(current_offset)
        return False
      else:
        return True

    children_height = current_height - 1
    for child_offset in self.get_children_indexes(current_height, current_offset):
      self.compare_tree(other, [children_height, child_offset])

  def deep_compare(self, other):
    self.differences = []
    return self.compare_tree(other, self.root_index())

# TODO: generate merkle proof and verify it