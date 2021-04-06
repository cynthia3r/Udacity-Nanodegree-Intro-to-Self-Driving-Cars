#include "headers/normalize.h"
using namespace std;

// OPTIMIZATION: Pass variable by reference
vector< vector<float> > normalize(vector< vector <float> > &grid) {

  	// OPTIMIZATION: Removed intermediate variables and steps that are not needed.
	float total{0.0};
  	int i, j;
  	int height = grid.size();
  	int width = grid[0].size();
  
	for (i = 0; i < height; ++i) {
		for (j = 0; j < width; ++j)
			total += grid[i][j];
	}

	for (i = 0; i < height; ++i) {
		for (j = 0; j< width; ++j)
			grid[i][j] = grid[i][j]/total;
	}

	return grid;
}
