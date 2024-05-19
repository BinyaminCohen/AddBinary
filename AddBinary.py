def add_binary(a: str, b: str) -> str:
    result = []  # To store the binary result
    carry = 0  # Initialize carry to 0
    i, j = len(a) - 1, len(b) - 1  # Start from the end of both strings


    while i >= 0 or j >= 0 or carry:
        total = carry  # Start with the carry from the last operation

        if i >= 0:
            total += int(a[i])  # Add the current bit from a
            i -= 1

        if j >= 0:
            total += int(b[j])  # Add the current bit from b
            j -= 1

        result.append(str(total % 2))  # Append the current bit to result
        carry = total // 2  # Update the carry

    result.reverse()  # The result is built in reverse order, so reverse it back
    return ''.join(result)  # Join the list to form the final binary string


# Example usage
#print(add_binary("11", "1"))

print(add_binary("1010", "1011"))
