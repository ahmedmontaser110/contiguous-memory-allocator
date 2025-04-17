# the memory is implemented as an array of objects, each object is for a memory portion allocated to a specific process 
# or empty block between two other allocated partitions.
memory = []

# the total memory size specified as an environment variable.
memory_size = 0

# initialization phase
def initialize_memory(size):
  global memory, memory_size
  memory_size = size
  memory = [{'start': 0, 'size': size, 'process': None}]


# allocation algorthms implementations
def find_best_fit(size):
  best_fit_index = -1
  min_diff = float('inf')
 
  for i, block in enumerate(memory):
    if block['process'] is None and block['size'] >= size:
      diff = block['size'] - size
      if diff < min_diff:
        min_diff = diff
        best_fit_index = i
 
  return best_fit_index
 
 
 
def find_first_fit(size):
  for i, block in enumerate(memory):
    if block['process'] is None and block['size'] >= size:
      return i
  return -1
 
 
 
def find_worst_fit(size):
  worst_fit_index = -1
  max_diff = float('-inf')
 
  for i, block in enumerate(memory):
    if block['process'] is None and block['size'] >= size:
      diff = block['size'] - size
      if diff > max_diff:
        max_diff = diff
        worst_fit_index = i
 
  return worst_fit_index


if __name__ == "__main__":
  import sys

  if len(sys.argv) != 2:
    print('Use the format to run to program: python allocator.py <memory_size>')
    exit(1)

  initial_memory_size = int(sys.argv[1])
  initialize_memory(initial_memory_size)

  while True:
    command = input('\nallocator> ')
    execute_command(command)