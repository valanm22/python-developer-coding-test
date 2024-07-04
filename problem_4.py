def sort_dict_by_values(d: dict) -> dict:
    sorted_dict = {}
    values = sorted(d.values())

    for value in values:
        for key in d:
            if d[key] == value:
                sorted_dict[key] = value

    return sorted_dict


print(sort_dict_by_values(
    {
        "a": 4,
        "c": 4,
        "f": 6,
        "b": 1
    }
))
