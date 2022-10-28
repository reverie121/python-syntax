def count_up(start, stop):
    """Print all numbers from start up to and including stop."""
    count = start
    while count <= stop:
        print(count)
        count += 1
    # YOUR CODE HERE

def count(start, stop):
    """Print all numbers from start to stop inclusive. stop may be lower than start."""
    count = start
    if start <= stop:
            while count <= stop:
                print(count)
                count += 1
    else:
            while count >= stop:
                print(count)
                count -= 1


count_up(5, 7)        
count(5, 7)
count(7, 5)
