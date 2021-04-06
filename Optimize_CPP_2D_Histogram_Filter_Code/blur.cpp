#include "headers/blur.h"
#include "headers/zeros.h"

using namespace std;

// OPTIMIZATION: Pass large variable by reference
vector < vector <float> > blur(vector < vector < float> > &grid, float blurring) {
	// OPTIMIZATION: window, DX and  DY variables have the 
    // same value each time the function is run.
  	// It's very inefficient to recalculate the vectors
    // every time the function runs. 
  	static float CENTER = 1.0 - blurring;
	static float CORNER = blurring / 12.0;
	static float ADJACENT = blurring / 6.0;
  
  	// The const and/or static operator could be useful.
  	// Define and declare window, DX, and DY using the
    // bracket syntax: vector<int> foo = {1, 2, 3, 4} 
    // instead of calculating these vectors with for loops 
    // and push back
  	static vector <int> DX{-1, 0, 1};
  	static vector <int> DY{-1, 0, 1};
  
  	static vector < vector <float> > WINDOW = { {CORNER, ADJACENT, CORNER}, {ADJACENT, CENTER, ADJACENT}, {CORNER, ADJACENT, CORNER} };
  
	vector < vector <float> > newGrid;
	vector <float> row;
	vector <float> newRow;

	int height = grid.size();
	int width = grid[0].size();

	int dx, dy, new_i, new_j;
	float multiplier, newVal;

	// OPTIMIZATION: used zeros function to populate the grid
  	newGrid = zeros(height, width);

	for (int i = 0; i < height; ++i ) {
		for (int j = 0; j < width; ++j ) {
			newVal = grid[i][j];
			for (int ii = 0; ii < 3; ++ii) {
				dy = DY[ii];
				for (int jj = 0; jj < 3; ++jj) {
					dx = DX[jj];
					new_i = (i + dy + height) % height;
					new_j = (j + dx + width) % width;
					multiplier = WINDOW[ii][jj];
					newGrid[new_i][new_j] += newVal * multiplier;
				}
			}
		}
	}

	return newGrid;
}
