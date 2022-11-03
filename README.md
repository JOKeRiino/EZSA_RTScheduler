# EZSA_RTScheduler

A real-time scheduler for the M.Sc. CS subject EZSA (Realtime Systems in Automotive Computing) at TH Nuremberg

## What it does:

The scheduler can be used to test task scheduling on a CPU.
Current possible scheduling algorithms include:
* RMS - Rate-Monotonic Scheduling, including Liu/Layland-Test
* DMS - Deadline-Monotonic Scheduling

## Preparation:

Tasks need to be provided in a .txt file within the same directory.
The file structure has to look like this:
```
task_name, computation_time, period, deadline (optional)
```
Example:
```
A,1,3,3
B,1,6,6
C,1,5,5
D,2,10,9
```
## How to run:

Within the main method, read the file data into a variable,
then call one of the scheduling methods, currently:
* rms_from_file( /path ) or
* dms_from_file( /path )

## Output:
For the above example the output looks as follows:

### RMS:
```
Hyperperiode:  30
Prozessorauslastung:  0.8999999999999999 , Max:  0.7568284600108841
==> RMS-Test nicht bestanden!
['A', 'C', 'B', 'A', 'D', 'C', 'A', 'B', 'D', 'A', 'C', 'D', 'A', 'B', 
'D', 'A', 'C', 'i', 'A', 'B', 'C', 'A', 'D', 'D', 'A', 'C', 'B', 'A', 'i', 'i']
```

### DMS:
```
Hyperperiode:  30
Prozessorauslastung:  0.8999999999999999
['A', 'C', 'B', 'A', 'D', 'C', 'A', 'B', 'D', 'A', 'C', 'D', 'A', 'B', 
'D', 'A', 'C', 'i', 'A', 'B', 'C', 'A', 'D', 'D', 'A', 'C', 'B', 'A', 'i', 'i']
```

### Error Handling:
If the program is not able to schedule the given tasks, it will identify where the error occured and throw an exception:

Example:
```
A,1,3,3
B,1,6,6
C,1,5,5
D,2,10,8 <= Using DMS, this Task will not meet its deadline of 8 ticks
```
Output:
```
Exception: ('D', 'cannot be scheduled, because comp time', 1, 
'is longer than remaining deadline time', 0, 'on tick', 8)
```


