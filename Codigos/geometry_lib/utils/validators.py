def check_dimensions(expected_value_quantity: int, *dimensions) -> None:
    if not dimensions:
        raise ValueError("No dimensions were provided.")
    
    if len(dimensions) != expected_value_quantity:
        raise ValueError(f"Expected {expected_value_quantity} values. \
            {len(dimensions)} were provided.")


def validate_positive(value: float) -> None:
    if value is not None and value < 0:
        raise ValueError(f"All values must be positive.")


def validate_polygon(class_name: str, num_sides: int) -> None:
    if num_sides < 3 and class_name != "Circle":
        raise ValueError("Number of sides must be at least 3.")