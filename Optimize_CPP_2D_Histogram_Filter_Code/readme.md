# Project Overview:
The project involves optimization of C++ 2D Histogram Filter code to improve efficiency (mainly execution speed and memory usage) by using various C++ optimization strategies.

## INSTRUCTIONS:

This workspace contains the C++ 2D Histogram filter code. As part of this project, you will optimize the code in these files to see how fast you can get main.cpp to run.

### Project structure
There are eight C++ files and seven header files. Each file other than main.cpp contains a function that carries out a specific part of a histogram filter. 

- main.cpp - prints out how long it takes to run each function

- initialize_beliefs.cpp - converts a 2D char vector to a 2D float vector containing initial probabilities

- sense.cpp - the robot senses the color of the current grid point and calculates the resulting beliefs

- blur.cpp - blur the resulting 2D vector

- normalize.cpp - normalize the results to represent a probability

- move.cpp - move the robot by (x,y) and calculate the new beliefs

- zeros.cpp - outputs a 2D vector with zero for all elements

- print.cpp - contains two different functions for printing out a 2D vector. 

### Functionality of Histogram Filter code
If you open main.cpp, you will see that the program runs each of the histogram filter functions ten-thousand times and then prints out the time taken to run each function. Main.cpp starts off with a 2D char vector representing a discrete color grid. Then the  code: 
- initializes the belief matrix
- senses the color grid
- blurs the results
- normalizes the results to calculate probabilities
- moves the robot

### Task
1. Read through and understand the initial starter code. Run the code using these commands in a terminal window and notedown the current runtime:
	- ```g++ -std=c++17 main.cpp blur.cpp initialize_beliefs.cpp move.cpp normalize.cpp print.cpp sense.cpp zeros.cpp```
	-  ```Note: The -std=c++17 option tells the compiler to use version 17 of C++.```

	- ```./a.out```

2. Optimize the code to make the histogram filter functions run faster utilizing the C++ optimization techniques as learned in the Udacity Self Driving Car course. You can test your results in the terminal using the same commands given previously. Also note down and compare the runtime of the optimized code and the starter code.


## Runtime Starter code:
```
number of iterations: 10000 
duration milliseconds initialize beliefs 48.259
duration milliseconds sense 58.87
duration milliseconds blur 145.719
duration milliseconds normalize 54.776
duration milliseconds move 52.106
```
## Runtime Optimized code:
