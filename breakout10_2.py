from collections import deque

#!
"""
U- input is list of strings 
P  - Use a stack for scheduled performances 
main stack is we can use for perfromances, second stack we can use for cancled performances 
I-

"""


def manage_stage_changes(changes):
    scheduled = []
    canceled = []

    for item in changes:
        # print("Current Item:", item)
        # print("Scheduled Stack: ", scheduled)
        # print("Canceled Stack: ", canceled)
        if "Schedule" in item:
            scheduled.append(item.replace("Schedule ", ""))
        elif "Cancel" in item:
            canceled.append(scheduled.pop())
        elif "Reschedule" in item:
            scheduled.append(canceled.pop())

    return scheduled


# print(manage_stage_changes(["Schedule A", "Schedule B", "Cancel", "Schedule C", "Reschedule", "Schedule D"]))
# print(manage_stage_changes(["Schedule A", "Cancel", "Schedule B", "Cancel", "Reschedule", "Cancel"]))
# print(manage_stage_changes(["Schedule X", "Schedule Y", "Cancel", "Cancel", "Schedule Z"]))


#! Problem 2:
"""
U- Implement the priority of the given inputs
P- init the queue from collections 
we pop each request from the queue 
print out each one
"""


def process_performance_requests(requests):

    prio_queue = deque(sorted(requests, reverse=True))
    result = []
    while prio_queue:
        result.append(prio_queue.popleft()[1])

    return result


print(process_performance_requests([(3, "Dance"), (5, "Music"), (1, "Drama")]))
print(
    process_performance_requests(
        [(2, "Poetry"), (1, "Magic Show"), (4, "Concert"), (3, "Stand-up Comedy")]
    )
)
print(
    process_performance_requests(
        [
            (1, "Art Exhibition"),
            (3, "Film Screening"),
            (2, "Workshop"),
            (5, "Keynote Speech"),
            (4, "Panel Discussion"),
        ]
    )
)
