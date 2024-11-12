def name_duplicated(x):
    """
    Handle Duplicated Names by Appending Sequence Number

    This function checks for duplicated elements in a list. If duplicated elements are found,
    it appends an underscore and a sequence number to each occurrence of the duplicated element.

    Parameters:
    - x (list of str): A list of strings.

    Returns:
    - list of str: A list where duplicated names are made unique by appending a sequence number.

    Example:
    >>> vec = ["apple", "orange", "apple", "banana", "orange"]
    >>> name_duplicated(vec)
    ['apple_1', 'orange_1', 'apple_2', 'banana', 'orange_2']
    """
    counts = {}
    result = []

    for item in x:
        if item in counts:
            counts[item] += 1
            result.append(f"{item}_{counts[item]}")
        else:
            counts[item] = 1
            result.append(f"{item}_{counts[item]}" if x.count(item) > 1 else item)
    
    return result

# # Example usage
# vec = ["apple", "orange", "apple", "banana", "orange"]
# print(name_duplicated(vec))
