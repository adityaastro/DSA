import sys


class TreeHeight:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))

    def compute_height(self):
        maxHeight = 0
        heights = [0] * len(self.parent)
        for vertex in range(self.n):
            if (heights[vertex] != 0):
                # If the node is visited, then skip it
                continue
            height = 0
            i = vertex
            # Calculating the height of vertex
            while i != -1:
                if (heights[i] != 0):
                    # If the parent node has been visited before. ∴ Simply add its value
                    height += heights[i]
                    break
                # Traverse through the nodes respective parents and keep incrementing height by 1
                height += 1
                i = self.parent[i]
            maxHeight = max(maxHeight, height)  # Update the maximum height
            # Update the height for all the parent nodes of the current node
            i = vertex
            while i != -1:
                if (heights[i] != 0):
                    break
                heights[i] = height
                height -= 1
                i = self.parent[i]
        return maxHeight


def main():
    tree = TreeHeight()
    tree.read()
    print(tree.compute_height())


main()
