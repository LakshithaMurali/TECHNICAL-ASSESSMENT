def findBestValue(food, people):
    n = len(food)
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + food[i]
    total_people = sum(people)
    best_starting_index = -1
    best_remaining_food = float('inf')
    for i in range(n):
        current_remaining_food = prefix_sum[i] - (i + 1) * people[i % n]
        while current_remaining_food >= 0 and (current_remaining_food + prefix_sum[n] - (i + 1) * people[(i + 1) % n]) / (total_people - people[i % n]) >= 1:
            current_remaining_food -= people[i % n]
            current_remaining_food += food[(i + 1) % n]
            i += 1
        if i > best_starting_index and current_remaining_food < best_remaining_food:
            best_starting_index = i
            best_remaining_food = current_remaining_food
    if best_starting_index == -1:
        return -1
    else:
        return (best_starting_index + 1) % n
