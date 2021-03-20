def factorial_(num):
    factorial = 1
    if num > 0:
        for i in range(1,num+1):
            factorial *= i

    return factorial

def pascals_tria(n):
    pascal_triangle = []

    re = n+1
    for j in range(re):
        pascal_triangle.append([])
        for i in range(j+1):
            pascal_triangle[j].append(int(factorial_(j)/(factorial_(i)*(factorial_(j-i)))))
        
    return pascal_triangle    

if __name__ == '__main__':
    for bruh in pascals_tria(69):
        print(bruh)

