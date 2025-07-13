from recursive_modules import (add_object, recursive_delete_object,
                               recursive_environment_exploration,
                               recursive_modify_object, show_objects)
from utils import validated_menu_choice


def menu():
    while True:
        try:
            print("HOME OBJECTS REGISTRY\n")
            print("1. Explore environment (recursive)")
            print("2. Add single object")
            print("3. Modify objects")
            print("4. Delete objects")
            print("5. Display all objects")
            print("6. Exit")

            choice = validated_menu_choice(
                "Choose an option", ["1", "2", "3", "4", "5", "6"]
            )

            if choice == "1":
                print("Take note of all objects you see. Enter empty name to stop.")
                recursive_environment_exploration()
            elif choice == "2":
                print("Manually add a single object:")
                add_object()
            elif choice == "3":
                recursive_modify_object()
            elif choice == "4":
                recursive_delete_object()
            elif choice == "5":
                show_objects()
            elif choice == "6":
                print("Thanks for using. Goodbye")
                break

        except KeyboardInterrupt:
            print("\nOperation interrupted. Returning to main menu...")
        except Exception as e:
            print(f"Unexpected error: {e}")
            print("Returning to main menu...")
