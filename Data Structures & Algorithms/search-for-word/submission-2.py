
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtracking(i, j, s, visited):
            if s == len(word):
                return True

            neighbors = [(-1, 0), (0, -1), (1, 0), (0, 1)]

            for dx, dy in neighbors:
                nx, ny = i + dx, j + dy

                if 0 <= nx < len(board) and 0 <= ny < len(board[0]):
                    if board[nx][ny] == word[s] and (nx, ny) not in visited:
                        visited.add((nx, ny))

                        if backtracking(nx, ny, s + 1, visited):
                            return True

                        visited.remove((nx, ny))

            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if backtracking(i, j, 1, {(i, j)}):
                        return True

        return False
