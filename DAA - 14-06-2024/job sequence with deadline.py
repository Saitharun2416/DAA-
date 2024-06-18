class Job:
    def __init__(self, id, deadline, profit):
        self.id = id
        self.deadline = deadline
        self.profit = profit

def job(jobs):
    jobs.sort(key=lambda x: x.profit, reverse=True)
    max_deadline = max(job.deadline for job in jobs)
    result = [None] * max_deadline
    occupied = [False] * max_deadline
    for job in jobs:
        for slot in range(job.deadline - 1, -1, -1):
            if not occupied[slot]:
                result[slot] = job
                occupied[slot] = True
                break
    s = [job.id for job in result if job is not None]
    t= sum(job.profit for job in result if job is not None)
    
    return s,t


jobs = [
        Job('Job1', 2, 100),
        Job('Job2', 1, 19),
        Job('Job3', 2, 27),
        Job('Job4', 1, 25),
        Job('Job5', 3, 15)
]
    
s,t = job(jobs)
print("schedule jobs:",s)
print("total profit:",t)
