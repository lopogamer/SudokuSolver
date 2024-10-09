#include <bits/stdc++.h>
using namespace std;

int GRID_SIZE = 9;
vector<vector<int>> Grid(GRID_SIZE, vector<int>(GRID_SIZE, 0));

bool IsValidColumn(int column, int value) {
    for (int i = 0; i < GRID_SIZE; i++) {
        if (Grid[i][column] == value) {
            return true;
        }
    }
    return false;
}

bool IsValidRow(int row, int value) {
    for (int i = 0; i < GRID_SIZE; i++) {
        if (Grid[row][i] == value) {
            return true;
        }
    }
    return false;
}

bool IsValidBox(int column, int row, int value) {
    int startRow = row - row % 3;
    int startColumn = column - column % 3;
    for (int i = startRow; i < startRow + 3; i++) {
        for (int j = startColumn; j < startColumn + 3; j++) {
            if (Grid[i][j] == value) {
                return true;
            }
        }
    }
    return false;
}

bool IsValid(int column, int row, int value) {
    return !IsValidColumn(column, value) && !IsValidRow(row, value) && !IsValidBox(column, row, value);
}

bool solve() {
    for (int row = 0; row < GRID_SIZE; row++) {
        for (int column = 0; column < GRID_SIZE; column++) {
            if (Grid[row][column] == 0) {  
                for (int TryNumber = 1; TryNumber <= GRID_SIZE; TryNumber++) {
                    if (IsValid(column, row, TryNumber)) {
                        Grid[row][column] = TryNumber;
                        if (solve()) {
                            return true;
                        } else {
                            Grid[row][column] = 0;  
                        }
                    }
                }
                return false;  
            }
        }
    }
    return true;  
}

int main(){
    freopen("input.txt", "r", stdin);  
    freopen("output.txt", "w", stdout);

    for (int i = 0; i < GRID_SIZE; i++) {
        for (int j = 0; j < GRID_SIZE; j++) {
            cin >> Grid[i][j];
        }
    }

    if (solve()) {
        for (int i = 0; i < GRID_SIZE; i++) {
            for (int j = 0; j < GRID_SIZE; j++) {
                cout << Grid[i][j] << " ";
            }
            cout << endl;
        }
    } else {
        cout << "No solution" << endl;
    }

    return 0;
}
