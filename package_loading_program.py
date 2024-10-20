def package_loading_system():
    try:
        max_items = int(input("Enter the maximum number of items to be shipped: "))
        if max_items <= 0:
            print("The maximum number of items must be greater than 0.")
            return
    except ValueError:
        print("Please enter a valid integer.")
        return

    package_weight = 0
    total_weight = 0
    package_count = 0
    unused_capacity_per_package = []
    package_with_max_unused_capacity = 0
    max_unused_capacity = 0

    for i in range(max_items):
        try:
            item_weight = float(input(f"Enter the weight of item {i + 1} (1-10 kg, or 0 to stop): "))

            if item_weight == 0:
                print("Terminating the program as 0 kg weight was entered.")
                break

            if item_weight < 1 or item_weight > 10:
                print("Invalid item weight. Please enter a weight between 1 and 10 kg.")
                continue

            if package_weight + item_weight > 20:
                # Send the current package
                package_count += 1
                total_weight += package_weight
                unused_capacity = 20 - package_weight
                unused_capacity_per_package.append(unused_capacity)

                if unused_capacity > max_unused_capacity:
                    max_unused_capacity = unused_capacity
                    package_with_max_unused_capacity = package_count

                print(f"Package {package_count} sent with {package_weight} kg.")

                package_weight = item_weight
            else:
                package_weight += item_weight

        except ValueError:
            print("Invalid input. Please enter a valid number for the weight.")
            continue

    if package_weight > 0:
        package_count += 1
        total_weight += package_weight
        unused_capacity = 20 - package_weight
        unused_capacity_per_package.append(unused_capacity)

        if unused_capacity > max_unused_capacity:
            max_unused_capacity = unused_capacity
            package_with_max_unused_capacity = package_count

        print(f"Package {package_count} sent with {package_weight} kg.")

    total_unused_capacity = package_count * 20 - total_weight
    print("\nFinal Summary:")
    print(f"Total packages sent: {package_count}")
    print(f"Total weight of packages: {total_weight} kg")
    print(f"Total unused capacity: {total_unused_capacity} kg")
    if package_with_max_unused_capacity > 0:
        print(f"Package {package_with_max_unused_capacity} had the most unused capacity: {max_unused_capacity} kg")


package_loading_system()
