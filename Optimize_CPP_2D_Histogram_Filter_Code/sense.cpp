#include "headers/sense.h"

using namespace std;

// OPTIMIZATION: Pass larger variables by reference
vector< vector <float> > sense(char color, vector< vector <char> > &grid, vector< vector <float> > &beliefs,  float p_hit, float p_miss) 
{

	int height = grid.size();
	int width = grid[0].size();

	for (int i = 0; i < height ; ++i) {
		for (int j = 0; j < width; ++j) {
			// OPTIMIZATION: if else statements might be faster than two if statements, so updated the below code
			if (grid[i][j] == color) {
              // OPTIMIZATION: Removed intermediate variables prior and cell instead directly calculating the values and updating in beliefs vector
				beliefs[i][j] = beliefs[i][j] * p_hit;
			}
      		else
            	beliefs[i][j] = beliefs[i][j] * p_miss;   
		}
	}
	return beliefs;
}
