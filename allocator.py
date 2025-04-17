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