def study_schedule(permanence_period, target_time):
    # print(permanence_period)
    # print(target_time)
    try:
        count = 0
        for el in permanence_period:
            if el[0] <= target_time and el[1] >= target_time:
                count += 1
        return count
    except (TypeError, ValueError):
        return None


# print(study_schedule([(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)], 5))
