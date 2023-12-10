def calculate_function(x):
    return 2 * x**2 - 5 * x - 8

def main():
    start_x = -4
    end_x = 4
    step = 0.5

    print(" x    |    y")
    print("--------------")
    current_x = start_x
    while current_x <= end_x:
        y = calculate_function(current_x)
        print(f"{current_x} | {y}")
        current_x += step

if __name__ == "__main__":
    main()