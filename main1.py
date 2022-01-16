# Импорты

class Doska:
    def __init__(self):
        print("Введите длину массива")
        n = int(input())
        self.cells = [[0 for j in range(n)] for i in range(n)]
        for i in range(n):
            for j in range(n):
                self.cells[i][j] = max(0, min(1,int(input(f"Введите значение на клетке {i + 1} {j + 1}:"))))
    def near(self, pos: list):
        count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i + j == 0 and i == j:
                    continue
                #print(i, j, pos)
                if pos[0] + i < 0 or pos[1] + j < 0 or pos[0] + i >= len(self.cells) or pos[1] + j >= len(self.cells):
                    continue
                if self.cells[(pos[0] + i)][(pos[1] + j)]:
                    count += 1
        return count


class GameOfLife:
    def __init__(self, dosk: Doska):
        self.cell = dosk

    def update(self):
        doska2 = [[0 for j in range(len(self.cell.cells))] for i in range(len(self.cell.cells))]
        for i in range(len(self.cell.cells)):
            for j in range(len(self.cell.cells)):
                if self.cell.cells[i][j]:
                    if self.cell.near([i , j]) not in (2 , 3):
                        doska2[i][j] = 0
                        continue
                    doska2[i][j] = 1
                    continue
                if self.cell.near([i , j]) == 3:
                    doska2[i][j] = 1
                    continue
                doska2[i][j] = 0
                
        self.cell.cells = doska2
B = Doska()
A = GameOfLife(B)
print(A.cell.cells)
while True:
    for i in A.cell.cells:
        for j in i:
            print(j, end=' ')
        print()
    input()
    A.update()