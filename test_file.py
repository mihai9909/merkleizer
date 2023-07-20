from merkle_tree import MerkleTree
from splitter import FileSplitter

def print_enter():  
  for i in range(0, 3):
    print()

data_array_1=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
data_array_2=['1', '2', '3', '4', '5', '6', '7', '6', '9', '10']
m1=MerkleTree(data_array_1)
m2=MerkleTree(data_array_2)
print(m1.root())
print(m2.root())
print_enter()
m1.print_tree()
print_enter()
m2.print_tree()

file1 = FileSplitter('merkle_tree_1.txt')
file2 = FileSplitter('merkle_tree_2.txt')

print(file1_chunks)
print(file2_chunks)

m1 = MerkleTree(file1_chunks)
m2 = MerkleTree(file2_chunks)
if m1.deep_compare(m2):
  print("Files are the same")
else:
  print("Files are different")
  print("Differences:", m1.differences)

