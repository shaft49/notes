# Operating System Theories

### What is OS?

- Simple piece of software that simplifies what the hardwares actually look like and control the hardware use.
- Sits between the application and hardware
- Resource Management
- READ/WRITE to the disk
- Send/Recieve to the SOCKET Network
  - I don't wanna think about the bits while connecting to the internet.
- Provide isolation and protection between the H/W components

### Monolithic OS

- Everything that applications or hardware required will be in the OS

### Modular OS (Linux)

- Basic API/Services are included but everything can be added as a module.

### Process

- When an application launches it becomes a process.
- Process is an active entity.
- Instance of an executable application.

### How does the OS know what a process is doing?

- PCB (Process Control Block) maintains a stack of process.
- PCB is created when the process first initialized.

### Context Switching

- Switching the CPU from context of one process to the context of another.
- Cons: Colde Cache (Cache Misses) happens frquently because of frequently context switching.

### Inter Process Communication

- Message Passing IPC
- Shared Memory IPC

### Threads

- Thread executes an unit of work on behalf of a process
- Concurrent (Multithreading): Happening at the same time.
  - Requires coordination of sharing of i/o, devices, cpu, memory

### Why thresding is useful?

- Parallelization: Speed up
- Specialization: Hot Cache

### Multiprocess vs Multithreading

- Process can't share address space but thread can.
- Multiprocess consumes more memory.
- Expensive IPC
- Are multithreading useful when no of thread is greater than no of CPU?
  - t_idle : Thread T1 makes a request on disk, time taken to complete the request is t_idle
  - t_ctx_switch: Time to context Switch between threads
  - If t_idle > 2 \* t_ctx_switch then it makes sense to use multithreading

### MUTEX (Mutual Exclusion)

- Exclusive access to only thread at a time. So the problem of accessing same resources by multiple threads don't arise.
- Mutex is like a lock. When a thread successfuly locks a mutex only that thread has access to the resource.
- Never use different mutex in the same resource file

### Spurious Wake Ups

- Unnecessary wake ups. If a thread is awake knowingly they may not proceed.
- It unlocks a mutex befor signal/broadcast

### Deadlocks

- Problems related to multithreading
- Two or more competing threads are waiting on each other to complete but none of them do.
- Solution: Maintain Lock Order
- Deadlock can arise if following four conditions hold simultaneously (Necessary Conditions):

  - Mutual Exclusion – One or more than one resource are non-sharable (Only one process can use at a time).
  - Hold and Wait – A process is holding at least one resource and waiting for resources.
  - No Preemption – A resource cannot be taken from a process unless the process releases the resource.
  - Circular Wait – A set of processes are waiting for each other in circular form.

### Multi threading patterns

- Boss-Worker Patterns
  - Boss assign work to workers
  - worker performs entire tasks
- Boss Workers Variant
  - All workers created equal
  - Workers specialized for certain task
- Pipleline Pattern
- Layered Pattern

### Data Race or Race Condition

- A thread tries to read a value, when another thread modifies it
- Solution: Use locking
