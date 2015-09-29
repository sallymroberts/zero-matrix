def zero_matrix(matrix):
    """Given an NxM matrix, if a cell is zero, set entire row and column to zeroes.

    A matrix without zeroes doesn't change:

        >>> zero_matrix([[1, 2 ,3], [4, 5, 6], [7, 8, 9]])
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    But if there's a zero, zero both that row and column:

        >>> zero_matrix([[1, 0, 3], [4, 5, 6], [7, 8, 9]])
        [[0, 0, 0], [4, 0, 6], [7, 0, 9]]

    Make sure it works with non-square matrices:

        >>> zero_matrix([[1, 0, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
        [[0, 0, 0, 0], [5, 0, 7, 8], [9, 0, 11, 12]]
    """

# If empty matrix, return empty list
    if not matrix:
        return []

    row_index = 0

# Initialize lists that will hold the indices of rows
# and columns that will be set to zero in the matrix    
    zero_row_indices = []
    zero_col_indices = []

# For each zero found in the matrix, load the row and 
# column indices of that element into the list of indices of 
# rows and columns that will be set to zero in the matrix 
    for row in matrix:
        col_index = 0
        for num in row:
            if num == 0:
                zero_row_indices.append(row_index)
                zero_col_indices.append(col_index)
            col_index += 1
        row_index += 1

# Set the values of rows and columns in the matrix to zero
# based on the lists of indices loaded above 
    for row_index in zero_row_indices:
        for i in range(len(matrix[row_index])):
            matrix[row_index][i] = 0

    for i in range(len(matrix)):
        for col_index in zero_col_indices:
            matrix[i][col_index] = 0
    return matrix

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** TESTS PASSED! YOU'RE DOING GREAT!\n"
