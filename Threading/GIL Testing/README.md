#Python GIL Testing

Testing the Python Global Intepreter Lock (GIL).

Fastest -> Slowest:
1. No Threading
2. Threading on Single Core
3. Threading on Multiple Core

These tests were run on a 15 inch Retina Macbook Pro (mid-2012) with the following specifications:

* Processor: 2.6 GHz Intel Core i7
* Memory: 8 GB 1600 MHz DDR3

*A general overview of why this happens:*

When python spawns threads, the threads are assigned to the kernel threading queue and python lets the kernel decide which thread to run. However, the GIL only allows one python process to access the python interpreter at a time. To deal with multiple threads, the GIL forces each python thread to give up the interpreter every 100 ticks (of the interpreter). Then the kernel decides (based on priority) which thread to assign to the CPU (and indirectly the GIL). On multiple core machines, if multiple cores are available, the kernel will want to deploy each thread in its queue to a different core. However, if there are multiple python threads in the kernel threading queue, the GIL will prevent those python threads from running concurrently. This leads to fighting in between the cores and hundreds of wasted system calls (and is one of the major reasons why there is a slowdown when creating multiple compute intensive threads). The GIL essentially makes threading in python more like "advanced multitasking" and less like convential C multithreading (using pthread).

To get around this, you will need to use the Python multiprocessing module, which spawn completely separate python processes (and in turn, separate global interpreter locks).
