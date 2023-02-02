from collections import defaultdict
import matplotlib.pyplot as plt

class TwoJarProblem:
    capacity1 = 0
    capacity2 = 0
    target = 0
    visitedDic = defaultdict(lambda: False)
    renderList = []
    waterLevel1 = []
    waterLevel2 = []

    def __init__(self, capacity1, capacity2, target):
        self.capacity1 = capacity1
        self.capacity2 = capacity2
        self.target = target
        self.solve(capacity1, capacity2)
        self.display()

    #         x,y
    # initially assume x = capacity1 and y = capacity2

    '''
        c1 = 3, c2 = 4 , t = 2
          initially x = c1, initially x2 = c2
          
          (3,4)  (3,0) (0,3) (3,3) (4,2)
          
          (0,4)
          (3,1)
          
          
    '''
    def display(self):
        print(self.renderList)
        for i in self.renderList:
            self.waterLevel1.append(i)

    def solve(self, x, y):
        if (x == self.target) or y == self.target:
            self.renderList.append((x, y))
            return True

        else:
            if self.visitedDic[(x, y)] == False:
                self.renderList.append((x, y))
                self.visitedDic[(x, y)] = True

                return (self.solve(0, y) or
                        self.solve(x, 0) or
                        self.solve(self.capacity1, y) or
                        self.solve(x, self.capacity2) or

                        self.solve(x + min(y, (self.capacity1 - x)),
                                   y - min(y, (self.capacity1 - x))) or
                        self.solve(x - min(x, (self.capacity2 - y)),
                                   y + min(x, (self.capacity2 - y))))
            else:
                return False

if __name__ == "__main__":
    TwoJarProblem(3, 4, 2)

    pass
