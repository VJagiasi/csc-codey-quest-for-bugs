from typing import List

# 1 - 20 points
def pretty_straightforward(n: int) -> int:
    result = 0
    a = 1
    b = 1
    counter = 0
    
    while counter < n ** 2:
        a, b = b, a + b 
        counter += 3

        if a % 2 == 0:
            result += a * a  
        elif a % 3 == 0:
            result -= a * 2
        else:
            result += b * 5

        if b > 100:
            result -= b // 2
    
    if result < 0:
        return abs(result)
    else:
        return result * 2 

assert pretty_straightforward(5) == 55
assert pretty_straightforward(10) == 385 
assert pretty_straightforward(15) == 1240

# 2 - 20 points
def matrix(matrix: List[List[int]]) -> List[List[int]]:
    result = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    temp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            temp[j][i] = matrix[i][j] 
    
    for i in range(len(temp)):
        for j in range(len(temp[0])):
            result[len(temp) - 1 - i][len(temp[0]) - 1 - j] = temp[i][j]
    
    return result



assert matrix([
    [1, 2, 3],
    [4, 5, 6],  
    [7, 8, 9]
]) == [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

assert matrix([
    [1, 2],
    [3, 4],
    [5, 6]
]) == [
    [6, 5],
    [4, 3],
    [2, 1]
]

assert matrix([[1, 2, 3]]) == [[3, 2, 1]]
assert matrix([[1], [2], [3]]) == [[3], [2], [1]]

# 3 - 30 points
def encode_message(message: str, key: int) -> str:
    result = []
    for i, char in enumerate(message):
        if char.isalpha():
            shift = ((i * key) % 26) + key // 2 
            if i % 2 == 0:
                shift += 5 
            elif i % 3 == 0:
                shift -= 3
            
            new_char = chr(((ord(char) - 65 + shift) % 26) + 65)
            result.append(new_char)
        else:
            result.append(char)
    
    return "".join(result)


assert encode_message("HELLO", 3) == "KHOOR"


assert encode_message("HELLO", 3) == "KHOOR"
assert encode_message("HELLO, WORLD!", 3) == "KHOOR, ZRUOG!"
assert encode_message("XYZ", 3) == "ABC"
assert encode_message("", 5) == ""
assert encode_message("HELLO", 0) == "HELLO"


# 4 - 30 points
def decrypt_sequence(sequence: List[int]) -> int:
    def helper(seq, acc=1):
        if len(seq) < 2: 
            if acc % 3 == 0:
                return acc * 7 
            return acc * 42
        
        total = 0
        for i in range(len(seq)):
            if i % 2 == 0:
                total += seq[i] * (seq[-1] + 1)
            else:
                total -= seq[i] * (seq[0] - 2)

        def nested_helper(n):
            return (n ** 2 + n) // 5 if n % 3 != 0 else n + 5
        for x in seq:
            total += nested_helper(x)

        if len(seq) > 3:
            total *= len(seq) // 2

        return helper(seq[1:], total)

    return (helper(sequence) * 13 + 9) // (len(sequence) if len(sequence) else 1)


assert decrypt_sequence([1, 2, 3, 4, 5]) == 1035 
assert decrypt_sequence([10, 15, 25]) == 3450   
assert decrypt_sequence([7, 14, 21]) == 2898    
