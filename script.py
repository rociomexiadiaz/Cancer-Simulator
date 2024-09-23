# Parameters
rows = 10
columns = 40
probability_alive = 0.5

# Instantiate the Tissue
tissue = cellsim.Tissue(rows,columns)
tissue.seed_random(probability_alive,cellsim.Cell)
print('time step:', 0)
print(tissue)

# For 100 time steps update the tissue
for i in range(1,100):
    os.system('cls') 
    print('time step:', i) 
    tissue.next_state()
    print(tissue)
    time.sleep(0.1)
