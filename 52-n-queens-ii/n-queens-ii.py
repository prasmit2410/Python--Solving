class Solution:
    def totalNQueens(self, n):
        count = 0

        columns = set()
        positive_diagonals = set()  # row + col
        negative_diagonals = set()  # row - col

        def backtrack(row):
            nonlocal count

            # All queens have been placed
            if row == n:
                count += 1
                return

            for col in range(n):

                # Check column and diagonals
                if col in columns:
                    continue

                if row + col in positive_diagonals:
                    continue

                if row - col in negative_diagonals:
                    continue

                # Place queen
                columns.add(col)
                positive_diagonals.add(row + col)
                negative_diagonals.add(row - col)

                # Move to next row
                backtrack(row + 1)

                # Backtrack
                columns.remove(col)
                positive_diagonals.remove(row + col)
                negative_diagonals.remove(row - col)

        backtrack(0)

        return count