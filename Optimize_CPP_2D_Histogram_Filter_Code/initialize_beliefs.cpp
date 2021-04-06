#include "headers/initialize_beliefs.h"

using namespace std;

// OPTIMIZATION: pass large variables by reference
vector< vector <float> > initialize_beliefs(int height, int width) {
  
	// OPTIMIZATION: Removed use of intermediate variables as the calculated value will be only used once
  	float prob_per_cell = 1.0 / static_cast<float>(height * width);
  
	// OPTIMIZATION: Reserve space in memory for vectors as the vectors are not of variable length
  	vector< vector <float> > newGrid;
  	newGrid.reserve(height);
	vector<float> newRow;
  	newRow.reserve(width);
  
  	// OPTIMIZATION: removed nested for loops as each element of the 2D vector has the same exact value
  	// so we only need to define the row variable once
  	for (int i = 0; i < width ; ++i)
			newRow.push_back(prob_per_cell);
  
	for (int j = 0; j < height; ++j)
		newGrid.push_back(newRow);
  
	return newGrid;
}