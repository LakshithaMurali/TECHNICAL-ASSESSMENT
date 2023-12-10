def findBestValue(food, people):
    n = len(food)
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + food[i]
    total_people = sum(people)
    starting_index = -1
    whole_remaining_food = float('inf')
    for i in range(n):
        remaining_food = prefix_sum[i] - (i + 1) * people[i % n]
        while remaining_food >= 0 and (remaining_food + prefix_sum[n] - (i + 1) * people[(i + 1) % n]) / (total_people - people[i % n]) >= 1:
            remaining_food -= people[i % n]
            remaining_food += food[(i + 1) % n]
            i += 1
        if i > starting_index and remaining_food < whole_remaining_food:
            starting_index = i
            whole_remaining_food = remaining_food
    if starting_index == -1:
        return -1
    else:
        return (starting_index + 1) % n
