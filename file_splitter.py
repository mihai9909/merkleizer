import sys
import math
import os

class FileSplitter:
    def __init__(self, file):  
      self.file = open(file, 'rb')
      self.file_size = os.path.getsize(file)
    
    def split_file(self, chunks): # TO DO: chunks size should be almost the same for all chunks (difference of 1 byte at most)
      chunk_size = math.ceil(self.file_size / chunks)
      chunk_array = []
      for _ in range(chunks):
        chunk = self.file.read(chunk_size)
        chunk_array.append(chunk)
      return chunk_array
