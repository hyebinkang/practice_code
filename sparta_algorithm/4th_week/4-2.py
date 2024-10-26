def meeting(time):
    sorted_meetings = sorted(time, key=lambda x:x[1])
    # print(sorted_meetings)      #[4,5,6,7,8,9]

    count = 0
    last_end_time = -1

    for start, end in sorted_meetings:
        if start > last_end_time:
            count +=1
            last_end_time = end
    return count


time = [(0, 6), (1, 4), (3, 5), (3, 8), (5, 7), (8, 9)]
print(meeting(time))