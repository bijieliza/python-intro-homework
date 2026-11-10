def find_min(numbers):
    minimum = numbers[0]
    for num in numbers:
        if num < minimum:
            minimum = num
    return minimum


def find_max(numbers):
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    return maximum


def search(numbers, target):
    for index in range(len(numbers)):
        if numbers[index] == target:
            return index
    return -1


def bubble_sort(numbers):
    sorted_list = numbers[:] 
    n = len(sorted_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if sorted_list[j] > sorted_list[j + 1]:
                sorted_list[j], sorted_list[j + 1] = (
                    sorted_list[j + 1],
                    sorted_list[j],
                )

    return sorted_list


def show_menu():
    print("\nMenu")
    print("1. Find Minimum")
    print("2. Find Maximum")
    print("3. Search")
    print("4. Sort")
    print("5. Quit")

    return input("Enter your choice: ")


def main():
    numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]

    while True:
        choice = show_menu()

        if choice == "1":
            print("Minimum value:", find_min(numbers))

        elif choice == "2":
            print("Maximum value:", find_max(numbers))

        elif choice == "3":
            target = int(input("Enter a number to search for: "))
            index = search(numbers, target)

            if index == -1:
                print("Number not found.")
            else:
                print(f"Found at index {index}.")

        elif choice == "4":
            print("Sorted list:", bubble_sort(numbers))

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


main()