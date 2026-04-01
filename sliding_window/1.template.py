#Fixed Window Template

start = 0
sum = 0

for end in range(n):
    sum += arr[end]   # expand

    if end - start + 1 == k:   # window size reached
        # do calculation (answer update)

        sum -= arr[start]  # remove start element
        start += 1         # shrink

#Variable Window Template

start = 0

for end in range(n):
    # expand window
    add arr[end]

    while condition is WRONG:
        remove arr[start]
        start += 1   # shrink

    # update answer