data_structure = [
    [1, 2, 3],
    {"a": 4, "b": 5},
    (6, {"cube": 7, "drum": 8}),
    "Hello",
    ((), [{(2, "Urban", ("Urban2", 35))}]),
]

def calculate_structure_sum(iterator):
    total = 0

    for item in iterator:
        if isinstance(item, int):
            total += item
        elif isinstance(item, str):
            total += len(item)
        elif isinstance(item, list) or isinstance(item, tuple) or isinstance(item, set):
            total += calculate_structure_sum(item)
        elif isinstance(item, dict):
            for entry in item.items():
                total += calculate_structure_sum(entry)

    return total


result = calculate_structure_sum(data_structure)

print(result)
