# Cancer Simulator

The file cellsim.py simulates the growth and death of a population of cells within a tissue represented as a two-dimensioned grid. Each location on the grid will represent either a Cell or Cancer; a healthy alive cell is represented as 'O' while an alive cancer cell is represented as 'X' and a dead cell as '.'.

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

## Running the code
This code should be run from the terminal or command prompt. From terminal, move to current working directory where the script.py and cellsim.py are located. Then run script.py, in this code you can edit the size of the tissue and the percentage of alive cells at time zero.
