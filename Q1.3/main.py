from itertools import combinations
from typing import List, Tuple, Set
import random


def partition_into_two_sets(n: int) -> List[Tuple[Set[int], Set[int]]]:
    """
    Takes a number n and returns all possible ways to partition 
    the numbers 1 to 2n into 2 sets, where each set contains exactly n elements.
    
    Args:
        n (int): The size of each set (total numbers are 1 to 2n)
    
    Returns:
        list: A list of tuples, where each tuple contains two sets of size n
    """
    if n <= 0:
        return []
    
    numbers = list(range(1, 2*n + 1))  # Numbers from 1 to 2n
    all_partitions: List[Tuple[Set[int], Set[int]]] = []
    
    # Generate all possible combinations of n numbers for the first set
    for subset in combinations(numbers, n):
        set1 = set(subset)
        set2 = set(numbers) - set1  # The remaining n numbers
        
        # To avoid duplicate partitions like (A,B) and (B,A),
        # we can use a canonical ordering (e.g., first set has smaller min element)
        if min(set1) < min(set2):
            all_partitions.append((set1, set2))
    
    return all_partitions


def default_plan(set1: Set[int], set2: Set[int]) -> Tuple[List[int], List[int]]:
    """
    Takes two sets and creates two schedules by randomly removing elements
    from each set until both sets are empty.
    
    Args:
        set1 (Set[int]): The first set of numbers
        set2 (Set[int]): The second set of numbers
    
    Returns:
        Tuple[List[int], List[int]]: Two schedules (Schedule1, Schedule2)
    """
    # Make copies of the sets so we don't modify the originals
    working_set1 = set1.copy()
    working_set2 = set2.copy()
    
    schedule1: List[int] = []
    schedule2: List[int] = []
    
    # Continue until both sets are empty
    while working_set1 or working_set2:
        # Remove random element from set1 if it's not empty
        if working_set1:
            element1 = random.choice(list(working_set1))
            working_set1.remove(element1)
            schedule1.append(element1)
        
        # Remove random element from set2 if it's not empty
        if working_set2:
            element2 = random.choice(list(working_set2))
            working_set2.remove(element2)
            schedule2.append(element2)
    
    return schedule1, schedule2

def score_schedules(schedule1: List[int], schedule2: List[int]) -> Tuple[List[bool], List[bool]]:
    score1: List[bool] = []
    score2: List[bool] = []
    for x in zip(schedule1, schedule2):
        score1.append(x[0] > x[1])
        score2.append(x[0] < x[1])

    return score1, score2

def better_schedule(set1: Set[int], set2: Set[int]) -> Tuple[List[int], List[int]]:
    # Can schedule 1 be improved
    # Make copies of the sets so we don't modify the originals
    working_set1 = set1.copy()
    working_set2 = set2.copy()
    
    schedule1: List[int] = []
    schedule2: List[int] = []

    while len(working_set1) > 0 and len(working_set2) > 0:
        if max(working_set1) > max(working_set2):
            max_val1 = max(working_set1)
            working_set1.remove(max_val1)
            schedule1.append(max_val1)
            min_val2 = min(working_set2)
            working_set2.remove(min_val2)
            schedule2.append(min_val2)
        else:
            max_val2 = max(working_set2)
            working_set2.remove(max_val2)
            schedule2.append(max_val2)
            min_val1 = min(working_set1)
            working_set1.remove(min_val1)
            schedule1.append(min_val1)

    return schedule1, schedule2


def main():
    print("Hello from q1-3!")

    n = int(input("please enter the number n: "))

    # Example usage
    partitions = partition_into_two_sets(n)

    for i, (set1, set2) in enumerate(partitions, 1):
        print(f"\nPartition {i}: Set1 = {set1}, Set2 = {set2}")
        
        # Generate a default plan for this partition
        schedule1, schedule2 = default_plan(set1, set2)
        score1, score2 = score_schedules(schedule1, schedule2)
        print(f"Schedule1: {schedule1} score: {score1}")
        print(f"Schedule2: {schedule2} score: {score2}")
        print(f'summary: Schedule1 wins {sum(score1)} times, Schedule2 wins {sum(score2)} times')
        schedule1, schedule2 = better_schedule(set1, set2)
        score1, score2 = score_schedules(schedule1, schedule2)
        print(f"Schedule1: {schedule1} score: {score1}")
        print(f"Schedule2: {schedule2} score: {score2}")
        print(f'summary: Schedule1 wins {sum(score1)} times, Schedule2 wins {sum(score2)} times')

        print('----------------------------------------')

    

        # # Show first few partitions as example
        # if i >= 3:
        #     print("\n... (showing first 3 partitions only)")
        #     break
if __name__ == "__main__":
    main()
