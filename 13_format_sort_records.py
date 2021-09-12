PEOPLE = [('Donald', 'Trump', 7.85),
          ('Vladimir', 'Putin', 3.626),
          ('Jinping', 'Xi', 10.603)]

def format_sort_records():
    result = ''
    for person in PEOPLE:
        result += f"{person[1]}\t\t{person[0]}\t{person[2]}\n"
    return result

print(format_sort_records())