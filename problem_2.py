def square_evens(numbers: list) -> list:
    return [i ** 2 for i in numbers if i % 2 == 0]


print(square_evens([1, 2, 3, 4]))
