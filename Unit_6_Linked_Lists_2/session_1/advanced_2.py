class Node:
    def __init__(self,value,next = None):
        self.value = value
        self.next = next 
    
def print_linked_list(head):
    current = head
    while current:
        print(current.value,end=" -> " if current.next else "\n")

def game_result(head):
    pass

def cycle_start(path_start):
    pass

def sort_list(head):
    pass 

#! Problem 4: Calculate Prize Money 
def add_two_numbers(head_a,head_b):
    pass

#! Problem 5: Next Contestant to beat 
def next_highest_scoring_contestant(contestant_scores):
    
