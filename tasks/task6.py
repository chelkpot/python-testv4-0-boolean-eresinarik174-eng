# tasks/task6.py

def solve():
# Ниже пишите решение задачи
a, b, c = sorted(map(int, input().split()))
result = c**2 == a**2 + b**2
print(result)
   
   
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()