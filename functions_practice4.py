def max_num(a, b, c):
    return max(a, b, c)

def mult_list(lst):
    result = 1
    for num in lst:
        result *= num
    return result

def rev_string(s):
    return s[::-1]

def num_within(x, start, end):
    return start <= x <= end

def pascal(n):
    if n <= 0:
        print("Number of rows must be a positive integer.")
        return

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)

    for row in triangle:
        print(row)

# Testing the functions
print(max_num(3, 6, 9))  

print(mult_list([1, 2, 3, 4])) 

print(rev_string("hello")) 

print(num_within(3, 2, 4))  


pascal(5)
