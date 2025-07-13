from typing import Dict, List, Optional

from utils import (confirm_operation, object_name_exists, validated_input,
                   validated_menu_choice)

from data import object_list


def get_input() -> Optional[Dict[str, str]]:
    name = validated_input("Enter object name (empty to stop)", False)
    if name is None:
        return None

    if object_name_exists(name):
        print(f"Warning: an object with name '{name}' already exists!")
        if not confirm_operation("Do you want continue anyway?"):
            return None

    category = validated_input("Enter category")
    if category is None:
        return None

    environment = validated_input("Enter environment/room")
    if environment is None:
        return None

    return {"name": name, "category": category, "environment": environment}


def recursive_environment_exploration() -> List[Dict[str, str]]:
    try:
        obj = get_input()
        if obj is None:
            return object_list
        else:
            object_list.append(obj)
            print(f"Object '{obj['name']}' added!")
            return recursive_environment_exploration()
    except KeyboardInterrupt:
        print("\nOperation interrupted by user.")
        return object_list


def show_objects(index: int = 0) -> None:
    if not object_list:
        print("No object to display.")
        return

    if index == 0:
        print(f"{'#':<3} {'Name':<20} {'Category':<20} {'Environment':<20}")

    if index >= len(object_list):
        print(f"Total objects: {len(object_list)}")
        return

    obj = object_list[index]
    print(
        f"{index + 1:<3} {obj['name']:<20} {obj['category']:<20} {obj['environment']:<20}"
    )
    show_objects(index + 1)


def add_object() -> None:
    try:
        obj = get_input()
        if obj:
            object_list.append(obj)
            print("Object added successfully!")
        else:
            print("Operation cancelled.")
    except KeyboardInterrupt:
        print("\nOperation interrupted by user.")


def recursive_object_index_search(searched_name: str, index: int = 0) -> int:
    if not searched_name or not searched_name.strip():
        return -1
    if index >= len(object_list):
        return -1
    if object_list[index]["name"].lower() == searched_name.lower():
        return index
    return recursive_object_index_search(searched_name, index + 1)


def recursive_modify_object() -> None:
    if not object_list:
        print("No objects to modify.")
        return

    try:
        name_to_modify = validated_input("Enter name to search for")
        if name_to_modify is None:
            print("Operation cancelled.")
            return

        object_index = recursive_object_index_search(name_to_modify)

        if object_index < 0 or object_index >= len(object_list):
            print("Object not found.")
            return

        obj = object_list[object_index]
        print(
            f"Object Found: {obj['name']}  -  {obj['category']}  -  {obj['environment']}"
        )

        print("\nMODIFY OBJECT")
        print("1. Modify name")
        print("2. Modify category")
        print("3. Modify environment")
        print("4. Stop modification")

        choice = validated_menu_choice("Choose what to modify", ["1", "2", "3", "4"])

        if choice == "4":
            return
        elif choice == "1":
            new_name = validated_input("Enter new name")
            if new_name:
                object_list[object_index]["name"] = new_name
                print("Name modified successfully")
        elif choice == "2":
            new_category = validated_input("Enter new category")
            if new_category:
                object_list[object_index]["category"] = new_category
                print("Category modified successfully.")
        elif choice == "3":
            new_environment = validated_input("Enter new environment")
            if new_environment:
                object_list[object_index]["environment"] = new_environment
        if confirm_operation("Do you want to modify something else fot this object?"):
            recursive_modify_object()
    except KeyboardInterrupt:
        print("\nOperation interrupted by user.")


def recursive_delete_object() -> None:
    if not object_list:
        print("No object to delete.")
        return

    try:
        name_to_delete = validated_input("Enter the name of the object to delete")
        if name_to_delete is None:
            print("Operation cancelled.")
            return

        index = recursive_object_index_search(name_to_delete)
        if index != -1:
            obj = object_list[index]
            print(
                f"Object found: {obj['name']}  -  {obj['category']}  -  {obj['environment']}"
            )

            if confirm_operation("Are you sure you want delete this object?"):
                deleted_object = object_list.pop(index)
                print(f"Object '{deleted_object['name']}' deleted successfully!")
            else:
                print("Deletion cancelled")
        else:
            print("Object not found")
            if confirm_operation("Do you want to search fot another object to delete?"):
                recursive_delete_object()
    except KeyboardInterrupt:
        print("\nOperation interrupted by user.")
