from modules import (add_object, ambient_explore, delete_object, home_list,
                     modify_object, search_object)


def menu():
    while True:
        print("\nMENU - Household Items Cataloger")
        print("1. Explore environment (recursive)")
        print("2. Add item manually")
        print("3. Search items")
        print("4. Edit item (recursive)")
        print("5. Delete item (recursive)")
        print("6. Show entire catalog")
        print("7. Exit")

        selection = input("\nSelect an option (1-7): ").strip()

        if selection == "1":
            starting_ambient = input("Insert the name of the first ambient: ")
            if starting_ambient:
                ambient_explore(starting_ambient)
            else:
                print("Ambient name cannot be empty.")

        elif selection == "2":
            add_object()

        elif selection == "3":
            print("\nFound object by:\n1. Name\n2. Position\n3. Category")
            sub_selection = input("Select (1-3): ").strip()
            if sub_selection == "1":
                key = "name"
            elif sub_selection == "2":
                key = "position"
            elif sub_selection == "3":
                key = "category"
            else:
                print("Invalid selection")
                continue
            value = input(f"Insert value for {key}: ").strip()
            results = search_object(key, value)
            if results:
                print("\nResults found:")
                for obj in results:
                    print(f"- {obj}")
            else:
                print("Object not found")

        elif selection == "4":
            key = input("Modify - Found by (name/position/category): ").strip()
            if key not in ["name", "position", "category"]:
                print("Invalid key. Choose: name, position or category.")
                continue
            value = input(f"Insert value for {key}: ").strip()
            if not value:
                print("Value cannot be empty.")
                continue
            modify_object(home_list, key, value)

        elif selection == "5":
            key = input("Delete - Search by (name/position/category): ").strip().lower()
            if key not in ["name", "position", "category"]:
                print("Invalid key. Choose: name, position or category.")
                continue
            value = input(f"Insert value for {key}: ").strip()
            if not value:
                print("Value cannot be empty.")
                continue
            delete_object(home_list, key, value)

        elif selection == "6":
            if not home_list:
                print("Empty catalogue.")
            else:
                print("\nObject in catalogue:")
                for idx, obj in enumerate(home_list, start=1):
                    print(
                        f"{idx}. Name: {obj['name']}  |  Position: {obj['position']}  |  Category: {obj['category']}"
                    )

        elif selection == "7":
            print("Thank you for using. Good By")
            break

        else:
            print("Invalid Selection.")
