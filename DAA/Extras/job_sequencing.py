# Job Sequencing with Deadlines using Greedy Algorithm

class Job:
    def __init__(self, job_id, deadline, profit):
        self.job_id = job_id
        self.deadline = deadline
        self.profit = profit

def job_sequencing(jobs):
    # Step 1: Sort jobs by decreasing profit
    jobs.sort(key=lambda x: x.profit, reverse=True)

    # Step 2: Find maximum deadline
    max_deadline = max(job.deadline for job in jobs)

    # Step 3: Initialize time slots (None = free)
    slots = [None] * (max_deadline + 1)
    total_profit = 0

    # Step 4: Assign jobs to slots
    for job in jobs:
        for slot in range(job.deadline, 0, -1):
            if slots[slot] is None:
                slots[slot] = job.job_id
                total_profit += job.profit
                break

    # Display result
    scheduled_jobs = [job for job in slots if job is not None]
    print("Scheduled Jobs:", scheduled_jobs)
    print("Total Profit:", total_profit)


# --- Driver Code ---
if __name__ == "__main__":
    jobs = [
        Job('J1', 2, 100),
        Job('J2', 1, 19),
        Job('J3', 2, 27),
        Job('J4', 1, 25),
        Job('J5', 3, 15)
    ]

    job_sequencing(jobs)