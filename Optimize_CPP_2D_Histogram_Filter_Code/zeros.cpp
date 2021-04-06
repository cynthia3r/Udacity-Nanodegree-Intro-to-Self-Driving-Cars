#include "headers/zeros.h"

using namespace std;

vector < vector <float> > zeros(int height, int width) {
  
	// OPTIMIZATION: Reserve space in memory for vectors
	vector < vector <float> > newGrid;
  	newGrid.reserve(height);
  
	vector <float> newRow;
  	newRow.assign(width, 0.0);

  	// OPTIMIZATION: removed nested for loop not as its not needed
    // because every row in the matrix is exactly the same
	for (int i = 0; i < height; ++i) {
		newGrid.push_back(newRow);
	}
	return newGrid;
}