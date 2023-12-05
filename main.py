import math
from pyscript import document


def create_matrix_from_text_auto_columns_filled(text, rows):
    text = text.replace(" ", "").upper()
    columns = math.ceil(len(text) / rows)
    matrix = [["#" for _ in range(columns)] for _ in range(rows)]

    index = 0
    for col in range(columns):
        for row in range(rows):
            if index < len(text):
                matrix[row][col] = text[index]
                index += 1

    return matrix


def print_matrix(matrix):
    return '<br>'.join([' '.join(row) for row in matrix])


def generate_matrix(event):
    event.preventDefault()
    plain_text = document.querySelector("#clearTextInput").value
    rows = int(document.querySelector("#key_rowInput").value)
    matrix = create_matrix_from_text_auto_columns_filled(plain_text, rows)
    matrix_html = print_matrix(matrix)
    output_div = document.querySelector("#matrixOutput")
    output_div.innerHTML = matrix_html

    cipherText = read_matrix_spiral_right_top_down(matrix)
    document.querySelector(
        "#cipherText_right_top_clockwise").innerHTML = cipherText

    counterclickwiseText = read_matrix_right_top_counterclockwise(matrix)
    document.querySelector(
        "#cipherText_right_top_counterclockwise").innerHTML = counterclickwiseText

    document.querySelector("#clock_key_display").innerHTML = rows
    document.querySelector("#counter_clock_key_display").innerHTML = rows
    document.querySelector("#encrypted_resuls_div").style.display = ""


def read_matrix_spiral_right_top_down(matrix):
    if not matrix or not matrix[0]:
        return ""

    result = []
    rows, columns = len(matrix), len(matrix[0])

    # Define the boundaries
    left, right = 0, columns - 1
    top, bottom = 0, rows - 1

    while left <= right and top <= bottom:
        # Traverse from top right to bottom right
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1

        # Traverse from right to left
        for i in range(right, left - 1, -1):
            result.append(matrix[bottom][i])
        bottom -= 1

        if left <= right:
            # Traverse from bottom to top
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

        if top <= bottom:
            # Traverse from left to right
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1

    return ''.join(result)


def read_matrix_right_top_counterclockwise(matrix):
    if not matrix or not matrix[0]:
        return ""

    result = ""
    top, left = 0, 0
    bottom, right = len(matrix) - 1, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        # Traverse left across the top row
        for i in range(right, left - 1, -1):
            result += str(matrix[top][i])
        top += 1

        # Traverse down the leftmost column
        for i in range(top, bottom + 1):
            result += str(matrix[i][left])
        left += 1

        # Traverse right across the bottom row
        if top <= bottom:
            for i in range(left, right + 1):
                result += str(matrix[bottom][i])
            bottom -= 1

        # Traverse up the rightmost column
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result += str(matrix[i][right])
            right -= 1

    return result.strip()
