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

# allocating a memory portion with size using the specific strategy algorithm
def allocate_memory(process, size, strategy):
  global memory
  if strategy == 'F':
    index = find_first_fit(size)
  elif strategy == 'B':
    index = find_best_fit(size)
  elif strategy == 'W':
    index = find_worst_fit(size)
  else:
    print('Invalid allocation strategy.')
    return

  if index == -1:
    print(f'Error: Not enough memory for process {process}')
    return

  if memory[index]['size'] == size:
    memory[index]['process'] = process
  else:
    new_block = {
        'start': memory[index]['start'],
        'size': size,
        'process': process
    }
    memory[index]['start'] += size
    memory[index]['size'] -= size
    memory.insert(index, new_block)



def release_memory(process):
  global memory
  for i, block in enumerate(memory):
    if block['process'] == process:
      block['process'] = None
      merge_free_blocks(i)
      return
  print(f'Error: Process {process} not found.')


def merge_free_blocks(index):
  global memory

  # check with the next block
  if (index + 1 < len(memory) and memory[index + 1]['process'] is None):
    memory[index]['size'] += memory[index + 1]['size']
    memory.pop(index + 1)

  # check with the previous block
  if index - 1 >= 0 and memory[index - 1]['process'] is None:
    memory[index - 1]['size'] += memory[index]['size']
    memory.pop(index)


# compaction to move all empty memory blocks to the end of the memory to provide one single large empty 
# block available for new processes to allocate
def compact_memory():
  global memory, memory_size
  offset = 0
  for block in memory:
    if block['process'] is not None:
      block['start'] = offset;
      offset += block['size']

  new_memory = [block for block in memory if block['process'] is not None]
  free_size = memory_size - offset
  if free_size > 0:
    new_memory.append({'start': offset, 'size': free_size, 'process': None})
  memory = new_memory


# printing a report of the memory status, blocks available, block allocated, and unused memory spaces along with its addresses. 
def report_status():
  global memory
  print('Current Memory Status:')
  for block in memory:
    status = f'Process {block["process"]}' if block['process'] else 'Unused'
    print(
        f'Addresses [{block["start"]}:{block["start"] + block["size"] - 1}] {status}')
 
 
# reading user commands after creating the initializing the memory
def execute_command(command):
  parts = command.split()
  action = parts[0]
 
  if action == 'RQ':
    if len(parts) == 4:
      process = parts[1]
      size = int(parts[2])
      strategy = parts[3]
      allocate_memory(process, size, strategy)
    else:
      print('Invalid RQ command format.')
  elif action == 'RL':
    if len(parts) == 2:
      process = parts[1]
      release_memory(process)
    else:
      print('Invalid RL command format.')
  elif action == 'C':
    compact_memory()
  elif action == 'STAT':
    report_status()
  elif action == 'X':
    print('Exiting memory allocator.')
    exit()
  else:
    print('Invalid command.')




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
