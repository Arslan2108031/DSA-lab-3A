def activity_selection(activities):
    activities.sort(key=lambda x: x[1])
    selected = []
    last_end_time = 0
    for start, end in activities:
        if start >= last_end_time:
            selected.append((start, end))
            last_end_time = end  
    return selected
activities = [(1, 3), (2, 5), (3, 9), (6, 8), (8, 11)]
print(activity_selection(activities))
