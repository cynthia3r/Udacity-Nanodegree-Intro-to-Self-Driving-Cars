# Project overview

The project involves implementation of the Matrix class using Python3 and supports the following matrix operations and also provides some basic overloaded operators such as addition, subtraction, and multiplication.
- Determinant
- Trace
- Inverse
- Transpose

## Project structure
This workspace contains the following files:
1. matrix.py - This contains the beginnings of a Matrix class as well as some helper functions zeroes and identity. This is the file you will be doing most of your work in.
2. matrix_playground.ipynb - A notebook that imports your Matrix class and calls the test code. You may find it useful to use this notebook as a place to use the matrix math code you will write in matrix.py.
3. matrix_cheat_sheet.ipynb - A Jupyter notebook with a glossary, explanation of matrix notation and list of matrix equations. Use this as a reference when filling out the methods in the Matrix class!
4. kalman_filter_demo.ipynb - Once your matrix class is working properly, the KF implemented here will actually work!
5. test.py - Contains test code which demonstrates the expected functionality of your code.
6. datagenerator.py - this just contains some helper code which is used by the Kalman Filter.

## Constraints and Limitations
Currently the code supports computation of inverse and determinant for matrix size of 1X1 and 2X2 only
