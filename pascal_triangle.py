# Solution for LeetCode problem: Pascal Triangle

def solution():
    """
    Generates Pascal's Triangle up to numRows. Example usage:
    triangle = generate(numRows)
    """
    def generate(numRows: int):
        triangle = []
        for row_num in range(numRows):
            row = [1] * (row_num + 1)
            for j in range(1, row_num):
                row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]
            triangle.append(row)
        return triangle
    # Example usage:
    # print(generate(5)) # returns [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
    pass
