# python3

def parallel_processing(n, m, data):
    output = []
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    next_t = [0] * n
    thread = list(range(n))
    for job_indx, job_t in enumerate (data):
        next_thrd = min(thread, key=lambda i:next_t[i])
        output.append((next_thrd, next_t[next_thrd]))
        next_t[next_thrd] +=job_t
        
    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    n, m = map(int, input().split())

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = list(map(int,input().split()))

    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line
    for thrd_nr, start_t in result:
        print(thrd_nr, start_t)


if __name__ == "__main__":
    main()
