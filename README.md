# Contiguous Memory Allocator

This program simulates contiguous memory allocation using first-fit, best-fit, and worst-fit algorithms. It supports requesting, releasing, and compacting memory, and provides a status report.

## Video Tutorial

https://github.com/user-attachments/assets/afea7d90-ac59-45f6-bace-2ed5fca228e9

## Features

- Implements first-fit, best-fit, and worst-fit allocation strategies.
- Supports requesting memory (`RQ` command).
- Supports releasing memory (`RL` command).
- Supports compacting memory (`C` command).
- Reports the regions of free and allocated memory (`STAT` command).
- Handles errors such as insufficient memory and invalid commands.
- Combines adjacent free blocks when memory is released.

## Usage

1.  Clone the repository: `git clone <repository_url>` (You'll get the repository URL after creating it on GitHub/GitLab).
2.  Navigate to the project directory: `cd memory-allocator`
3.  Run the program: `python allocator.py <memory_size>`
4.  Enter commands at the `allocator>` prompt.

## Commands

The program responds to the following commands:

- **RQ \<process\> \<size\> \<strategy\>**: Requests a contiguous block of memory.
  - `<process>`: The name of the process (e.g., P1).
  - `<size>`: The size of the memory block in bytes.
  - `<strategy>`: The allocation strategy:
    - `F`: First-fit
    - `B`: Best-fit
    - `W`: Worst-fit
  - Example: `RQ P1 100 F`
- **RL \<process\>**: Releases the memory block allocated to the specified process.
  - `<process>`: The name of the process.
  - Example: `RL P1`
- **C**: Compacts the unused memory holes into a single large hole. The program updates the starting addresses of any processes affected by the compaction.
- **STAT**: Reports the regions of free and allocated memory. For each region, the program displays the starting address, ending address, and status (allocated to a process or unused).
- **X**: Exits the program.

## Written Example

1.  **Start the program with 1000 bytes of memory:**

    ```
    python allocator.py 1000
    allocator>
    ```

2.  **Request 100 bytes for process P1 using first-fit:**

    ```
    allocator> RQ P1 100 F
    ```

3.  **Check the memory status:**

    ```
    allocator> STAT
    Current Memory Status:
    Addresses [0:99] Process P1
    Addresses [100:999] Unused
    ```

    - The first 100 bytes (0-99) are allocated to P1.
    - The remaining 900 bytes (100-999) are free.

4.  **Request 200 bytes for process P2 using best-fit:**

    ```
    allocator> RQ P2 200 B
    ```

5.  **Check the memory status:**

    ```
    allocator> STAT
    Current Memory Status:
    Addresses [0:99] Process P1
    Addresses [100:299] Process P2
    Addresses [300:999] Unused
    ```

    - The next 200 bytes (100-299) are allocated to P2.
    - The remaining 700 bytes (300-999) are free.

6.  **Request 300 bytes for process P3 using worst-fit:**

    ```
    allocator> RQ P3 300 W
    ```

7.  **Check the memory status:**

    ```
    allocator> STAT
    Current Memory Status:
    Addresses [0:99] Process P1
    Addresses [100:299] Process P2
    Addresses [300:599] Process P3
    Addresses [600:999] Unused
    ```

    - The next 300 bytes (300-599) are allocated to P3.
    - The remaining 400 bytes (600-999) are free.

8.  **Release the memory used by process P2:**

    ```
    allocator> RL P2
    allocator>
    ```

9.  **Check the memory status:**

    ```
    allocator> STAT
    Current Memory Status:
    Addresses [0:99] Process P1
    Addresses [100:299] Unused
    Addresses [300:599] Process P3
    Addresses [600:999] Unused
    allocator>
    ```

    - The 200 bytes previously allocated to P2 (100-299) are now free.

10. **Compact the memory:**

    ```
    allocator> C
    ```

11. **Check the memory status after compaction:**

    ```
    allocator> STAT
    Current Memory Status:
    Addresses [0:99] Process P1
    Addresses [100:399] Process P3
    Addresses [400:999] Unused
    allocator>
    ```

    - The allocated blocks have been moved to the beginning of the memory.
    - The free space is now a single contiguous block at the end (400-999).

12. **Exit the program:**

    ```
    allocator> X
    ```

## Some concepts

### Allocation Strategies

- **First-fit:** The program scans the memory blocks from the beginning and allocates the first free block that is large enough to satisfy the request.
- **Best-fit:** The program searches the entire list of free blocks and allocates the smallest free block that is large enough to satisfy the request.
- **Worst-fit:** The program searches the entire list of free blocks and allocates the largest free block that is large enough to satisfy the request.

### Compaction

When the `C` command is entered, the program compacts the free memory holes into a single contiguous block. This is done by moving all allocated blocks to one end of the memory, and then combining the free blocks into one large block. The starting addresses of the allocated blocks are updated accordingly.

## Error Handling

The program handles the following errors:

- **Insufficient memory:** If there is not enough free memory to satisfy a request, the program displays an error message and rejects the request.
- **Invalid command:** If the user enters an invalid command, the program displays an error message and prompts the user to enter a valid command.
- **Process not found (on release):** If the user tries to release memory for a process that does not exist, the program displays an error message.

## File Description

- `allocator.py`: The Python source code for the memory allocation simulator.
- `README.md`: Documentation for the project.
