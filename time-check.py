import time, random

N = 100
arr = [random.randint(0, 9) for _ in range(N)]
graph = [[random.randint(0, 9) for _ in range(N)] for _ in range(N)]
start_time = time.time()
######################################################################
# Copy the code here


######################################################################
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Elapsed Time: {elapsed_time} seconds")
