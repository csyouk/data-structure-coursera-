# python3

import sys
import threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


class TreeHeight:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))
        self.height = [0] * self.n

    def cal_path(self, node_key):
        parent = self.parent[node_key]
        if(parent == -1):
            return 1

        if self.height[node_key]:
            # 이미 지나간 길이 있다면 그 값을 저장해놓는다.
            # print("key ", node_key)
            # print("cache : ", self.height)
            return self.height[node_key]

        self.height[node_key] = 1 + self.cal_path(parent)
        return self.height[node_key]


    def compute_height(self):
        # for i in range(self.n):
        #     print(i, self.cal_path(i))
        return max([self.cal_path(node_key) for node_key in range(self.n)])




def main():
    tree = TreeHeight()
    tree.read()
    print(tree.compute_height())

threading.Thread(target=main).start()
