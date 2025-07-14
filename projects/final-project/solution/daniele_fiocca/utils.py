from typing import List, Optional

from data import object_list


def validated_input(message: str, required: bool = True) -> Optional[str]:
    value: str = input(message + ": ").strip()

    if value == "" and not required:
        return None
    elif value == "" and required:
        print("This field is required. Please try again.")
        return validated_input(message, required)
    elif not value.replace(" ", "").isalnum() and not all(
            c.isalnum() or c.isspace() for c in value
    ):
        print(
            "Value contains invalid characters. Use only letters, numbers and spaces."
        )
        return validated_input(message, required)
    else:
        return value


def validated_menu_choice(message: str, valid_options: List[str]) -> str:
    choice: str = input(message + ": ").strip()
    if choice in valid_options:
        return choice
    else:
        print(f"Invalid choice. Available options: {', '.join(valid_options)}")
        return validated_menu_choice(message, valid_options)


def confirm_operation(message: str) -> bool:
    response: str = input(message + " (y/n): ").strip().lower()
    if response in ["y", "yes"]:
        return True
    elif response in ["n", "no"]:
        return False
    else:
        print("Enter 'y' for yes or 'n' for no.")
        return confirm_operation(message)


def object_name_exists(name: str) -> bool:
    return any(obj["name"].lower() == name.lower() for obj in object_list)
