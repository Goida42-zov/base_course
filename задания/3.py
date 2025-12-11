import time

M, N = 2, 1
start = time.time()

for i in range(M+1):
    print(i)
    time.sleep(1)
    for j in range(N+1):
        print(j)
        time.sleep(1)
        print(f"Время: {time.time()-start:.1f}")