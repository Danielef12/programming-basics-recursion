home_list = []


def control_validation_input(prompt):
    while True:
        validation = input(prompt).strip().lower()
        if validation in ["y", "n"]:
            return validation
        print("Please enter 'y' or 'n'.")


def non_empty_input(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty.")


def ambient_explore(ambient):
    if control_validation_input(f"Are there objects in {ambient}? (y/n)\n") == "y":
        while True:
            name = non_empty_input("Insert the name of the object: \n")
            category = non_empty_input("Insert the category: \n")
            home_list.append({"name": name, "position": ambient, "category": category})
            if (
                control_validation_input(f"Insert another object in {ambient}? (y/n)\n")
                != "y"
            ):
                break

    while (
        control_validation_input(
            f"Are there subsections (e.g. drawers, shelves) in {ambient}? (y/n)\n"
        )
        == "y"
    ):
        sub_name = non_empty_input(f"Insert subsection name of {ambient}: \n").lower()
        new_ambient = f"{ambient} > {sub_name}"
        ambient_explore(new_ambient)


def add_object():
    name = non_empty_input("Insert the object name: \n")
    position = non_empty_input("Insert object position: \n")
    category = non_empty_input("Insert category: \n")
    home_list.append({"name": name, "position": position, "category": category})
    print("Object created successfully!")


def search_object(key, value):
    return [obj for obj in home_list if obj.get(key) == value]


def modify_object(object_list, key, value, index=0):
    if index >= len(object_list):
        print("No object to verify")
        return

    home_object = object_list[index]
    if home_object.get(key) == value:
        print("\nObject Found:")
        print(
            f"Name: {home_object['name']}  |  Position: {home_object['position']}  |  Category: {home_object['category']}"
        )

        if control_validation_input("Would modify this object? (y/n): ") == "y":
            print("Which field do you want to change?")
            print("1.Name\n2. Position\n3. Category")
            while True:
                field = input("Choose (1-3): ").strip()
                if field == "1":
                    new_key = "name"
                    break
                elif field == "2":
                    new_key = "position"
                    break
                elif field == "3":
                    new_key = "category"
                    break
                else:
                    print("Invalid selection. Chose 1, 2 or 3.")

            new_value = non_empty_input(f"Insert new value for {new_key}: ")
            home_object[new_key] = new_value
            print("Object modify success!")
    modify_object(object_list, key, value, index + 1)


def delete_object(object_list, key, value, index=0):
    if index >= len(object_list):
        print("End of list, no object to verify.")
        return
    home_object = object_list[index]
    if home_object.get(key) == value:
        print("Found Object:")
        print(
            f"Name: {home_object['name']}  |  Position: {home_object['position']}  |  Category: {home_object['category']}"
        )

        if control_validation_input("Delete this object? (y/n): ") == "y":
            del object_list[index]
            print("Object deleted.\n")
            delete_object(object_list, key, value, index)
            return
    delete_object(object_list, key, value, index + 1)
