# Cancer-Simulator

The file cellsim.py simulates the growth and death of a population of cells within a tissue represented as a two-dimensioned grid. Each location on the grid will represent either a Cell or Cancer; a healthy alive cell is represented as 'O' while a dead cell is represented as '.' and a cancer cell as 'X'.

## Classes Overview
### Cells
If a cell is alive, it will die under the following circumstances:  
· Overpopulation: If the cell has four or more alive neighbours, it dies  
· Loneliness:  If the cell has one or fewer alive neighbours, it dies  
If a cell is dead, it will come back to live if it has exactly 3 neighbours  
In all other cases, the cell state doesn't change  
### Cancer
If a cell is alive, it will die under the following circumstances:  
· Overpopulation:  If the cell has five or more alive neighbours, it dies  
· Loneliness: If the cell has one or fewer alive neighbours, it dies  
If a cell is dead, it will come to life if it has exactly three alive neighbours  
In all other cases, the cell state does not change  
