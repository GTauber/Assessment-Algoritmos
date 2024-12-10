def find_square(grain_target):
    if grain_target < 1:
        return "Invalid amount of grains"

    square = 1
    grains = 1

    while grains != grain_target:

        if grains > grain_target:
            return "This amount of grains doesnt represent any square"

        square += 1
        grains *= 2

    return square