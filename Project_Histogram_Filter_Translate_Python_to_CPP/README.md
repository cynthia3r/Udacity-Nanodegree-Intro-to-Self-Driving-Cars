# Project Overview

The goal of this project is to take the python code in **Project_2D_Histogram_Filter_in_Python** and translate it into C++.

## Project files
- The **maps** folder just has data of the map data used in the project
- **tests.cpp** is used for testing
- **debugging_helpers.cpp** is to help debug the code
- **helpers.cpp** - Implement normalize() and blur()
- **localizer.cpp** - Implement initialize_beliefs(), sense() and move()
- **simulate.cpp** - to visualize a simulation of the localizer

## Build commands
```g++ -std=c++17 tests.cpp```
