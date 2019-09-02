"""
The Jumping Cloud challenge is about a girl, Emma, that has to jump
through the clouds to reach the end point. In order to arrive safe, she
has to avoid the thunder clouds.

The path is given as an array (c) containing binary integers.
0 means that a cloud is safe and 1 means it must be avoided.

The objective is to find out the minimum number of jumps that Emma has to perform.
She can either jump 1 cloud or 2 clouds at a time.
"""

def jumpingOnClouds(c):
    # Index of current cloud
    current = 0

    # Path ending
    end = len(c) -1

    # Number of jumps
    jumps = 0


    while current < end:
        # If there is a cloud 2 jumps ahead and it's safe update current index by 2 and add jump
        if ((current+2) <= end) and c[current+2] == 0:
            current += 2
            jumps += 1

        # If not and the next cloud is safe, update index by 1 and add jump
        elif c[current + 1] == 0:
            current += 1
            jumps += 1

    return jumps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()