#include "headers/move.h"
#include "headers/zeros.h"

using namespace std;

// OPTIMIZATION: Pass large variable by reference
vector< vector <float> > move(int dy, int dx, 
	vector < vector <float> > &beliefs) 
{
	int height = beliefs.size();
	int width = beliefs[0].size();
  
  	// OPTIMIZATION: Use improved zeros function
	vector < vector <float> > newGrid = zeros(height, width);

// OPTIMIZATION: Eliminate any variables that aren't needed
	int new_i, new_j;
	
  	for (int i = 0; i < height; ++i) {
		for (int j = 0; j < width; ++j) {
			new_i = (i + dy + height) % height;
			new_j = (j + dx + width)  % width;
			newGrid[new_i][new_j] = beliefs[i][j];
		}
	}
	return newGrid;
}
