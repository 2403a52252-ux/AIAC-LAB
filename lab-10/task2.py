def area_of_rectangle(length: float, breadth: float) -> float:
    """Calculate the area of a rectangle. 
    Args:
        length (float): The length of the rectangle.
        breadth (float): The breadth of the rectangle.   
    Returns:
        float: The area of the rectangle (length * breadth).     
    Raises:
        ValueError: If length or breadth is negative.     
    Example:
        >>> area_of_rectangle(10, 20)
        200
    """
    if length < 0:
        raise ValueError("Length cannot be negative")
    if breadth < 0:
        raise ValueError("breadth cannot be negative")   
    return length * breadth
if __name__ == "__main__":
    print(area_of_rectangle(10, 20))
