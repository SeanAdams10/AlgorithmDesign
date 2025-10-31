import random
from collections import deque

def init_women(n):
    """Initialize a list of n women with randomized preferences."""
    women = []
    for i in range(n):
        preferences = list(range(n))  # Create list [0, 1, 2, ..., n-1]
        random.shuffle(preferences)   # Randomize the preferences
        woman = {
            'id': i,
            'preferences': preferences,
            'husband': None  # Initially no husband
        }
        women.append(woman)
    return women

def init_men(n):
    """Initialize a queue of n men with randomized preferences."""
    men_queue = deque()
    men = []
    for i in range(n):
        preferences = list(range(n))  # Create list [0, 1, 2, ..., n-1]
        random.shuffle(preferences)   # Randomize the preferences
        man = {
            'id': i,
            'preferences': preferences,
            'wife': None  # Initially no wife
        }
        men_queue.append(man)
        men.append(man)
    return men_queue, men

def count_single_men(men):
    """Count the number of single men (men without wives)."""
    single_count = 0
    for man in men:
        if man['wife'] is None:
            single_count += 1

    print(f'Number of single men: {single_count}')
    return single_count

def print_marriages(men, women):
    """Print marriage results in formatted strings."""
    # Sort men by ID and create marriage string
    sorted_men = sorted(men, key=lambda x: x['id'])
    men_marriages = []
    for man in sorted_men:
        men_marriages.append(f"{man['id']}:{man['wife']}")
    men_string = " - ".join(men_marriages)
    print(men_string)
    
    # Sort women by ID and create marriage string
    sorted_women = sorted(women, key=lambda x: x['id'])
    women_marriages = []
    for woman in sorted_women:
        women_marriages.append(f"{woman['id']}:{woman['husband']}")
    women_string = " - ".join(women_marriages)
    print(women_string)


def main():

    n = 5 # Number of men/women

    # Create list of women
    women = init_women(n)
    
    # Create queue of men
    unmarried_men, men = init_men(n)
    
    while len(unmarried_men) > 0:
        # print(f'Current man: {unmarried_men[0]}')
        man = unmarried_men.popleft()
        if man['wife']:
            #this man is married, skip him
            print(f"Man {man['id']} is already married to woman {man['wife']}")
            print()
            men.rotate(1)
            continue

        if len(man['preferences']) == 0:
            print(f"ERROR: Man {man['id']} has no preferences")
            raise Exception("Man has no preferences")

        man_preference = man['preferences'][0]
        man['preferences'].remove(man_preference)
        #remove this preference since we've tried it

        woman = women[man_preference]
        if woman['husband'] is None:
            if man['wife'] is not None:
                print(f"ERROR: Man {man['id']} is already married to woman {man['wife']}")
            woman['husband'] = man['id']
            man['wife'] = woman['id']
            print(f"Man {man['id']} marries woman {woman['id']}")
        else:
            current_man_id = woman['husband']
            if woman['preferences'].index(man['id']) < woman['preferences'].index(current_man_id):
                #if the woman prefers this man over her current husband, switch them
                old_husband = men[current_man_id]
                old_husband['wife'] = None
                woman['husband'] = man['id']
                man['wife'] = woman['id']
                unmarried_men.appendleft(old_husband)
                print(f"Woman {woman['id']} dumped her husband {current_man_id} and married to man {man['id']}")
            else:
                print(f"Woman {woman['id']} prefers her current husband {current_man_id} and rejected offer from {man['id']} " )
                unmarried_men.appendleft(man)
        
        # print_marriages(men, women)
        print("")

    print('Result')
    for man in men:
        print("Man " + str(man['id']) + " is married to woman " + str(man['wife']))




if __name__ == "__main__":
    main()
