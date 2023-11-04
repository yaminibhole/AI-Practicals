def job_scheduling(arr, t):
    arr.sort(key=lambda x: x[2], reverse=True)
    result = [-1] * t
    job_sequence = []

    for job in arr:
        for slot in range(min(t - 1, job[1] - 1), -1, -1):
            if result[slot] == -1:
                result[slot] = job[0]
                job_sequence.append(job[0])
                break

    return job_sequence

# Driver's Code
if __name__ == '__main__':
    arr = [['a', 2, 100],  # Job Array
           ['b', 1, 19],
           ['c', 2, 27],
           ['d', 1, 25],
           ['e', 3, 15]]

    print("Following is the maximum profit sequence of jobs:")

    job_sequence = job_scheduling(arr, 3)

    print("Job Sequence:", job_sequence)
