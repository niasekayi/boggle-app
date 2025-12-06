"""
Nia Greene
Boggle solver for assignment:
- Class name: Boggle
- Data members: Grid, Dictionary, solution
- Methods: setGrid, setDictionary, getSolution
- No imports; use built-in types only
"""


class Boggle:
    """
    Boggle solver class.
    Grid: 2D list of tile-strings (like "A", "Qu", "St")
    Dictionary: set of lowercase words
    solution: final list of found words (lowercase)
    """

    def __init__(self, grid, dictionary):
        self.Grid = []
        self.Dictionary = set()
        self.solution = []
        self._N = 0
        self._prefixes = set()
        self.setGrid(grid)
        self.setDictionary(dictionary)

    def setGrid(self, grid):
        if not grid or (len(grid) == 1 and len(grid[0]) == 0):
            self.Grid = []
            self._N = 0
            return

        N_rows = len(grid)
        N_cols = max(len(row) for row in grid) if grid and any(grid) else 0
        N = max(N_rows, N_cols)

        padded_grid = []
        for row in grid:
            padded_row = [str(cell).lower() for cell in row]
            padded_row += [''] * (N - len(padded_row))
            padded_grid.append(padded_row)

        while len(padded_grid) < N:
            padded_grid.append([''] * N)

        final_grid = []
        for row in padded_grid:
            new_row = []
            i = 0
            while i < len(row):
                if row[i] == 'q' and i + 1 < len(row) and row[i + 1] == 'u':
                    new_row.append('qu')
                    i += 2
                elif row[i] == 's' and i + 1 < len(row) and row[i + 1] == 't':
                    new_row.append('st')
                    i += 2
                else:
                    new_row.append(row[i])
                    i += 1
            final_grid.append(new_row)

        self.Grid = final_grid
        self._N = len(final_grid)

    def setDictionary(self, dictionary):
        if not dictionary:
            self.Dictionary = set()
            self._prefixes = set()
            return

        self.Dictionary = set(str(word).lower() for word in dictionary)
        prefixes = set()
        for w in self.Dictionary:
            for i in range(1, len(w) + 1):
                prefixes.add(w[:i])
        self._prefixes = prefixes

    def getSolution(self):
        found = set()
        if not self.Grid or not self.Dictionary or self._N == 0:
            self.solution = []
            return self.solution

        for y in range(self._N):
            for x in range(len(self.Grid[y])):
                visited = [[False] * len(r) for r in self.Grid]
                self._dfs(y, x, "", visited, found)

        result = sorted(
            w.upper() for w in found if w in self.Dictionary and len(w) >= 3
        )
        self.solution = result
        return self.solution

    def _dfs(self, y, x, cur_word, visited, found_set):
        if (
            y < 0
            or y >= len(self.Grid)
            or x < 0
            or x >= len(self.Grid[y])
            or visited[y][x]
        ):
            return

        tile = self.Grid[y][x]
        new_word = cur_word + tile

        if new_word not in self._prefixes:
            return

        if len(new_word) >= 3 and new_word in self.Dictionary:
            found_set.add(new_word)

        visited[y][x] = True

        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):
                if dy == 0 and dx == 0:
                    continue

                new_x = x + dx
                new_y = y + dy

                if (
                    new_y >= 0
                    and new_y < len(self.Grid)
                    and new_x >= 0
                    and new_x < len(self.Grid[new_y])
                ):
                    self._dfs(new_y, new_x, new_word, visited, found_set)

        visited[y][x] = False


def main():
    grid = [
        ["T", "W", "Y", "R"],
        ["E", "N", "P", "H"],
        ["G", "St", "Qu", "R"],
        ["O", "N", "T", "A"],
    ]
    dictionary = [
        "art",
        "ego",
        "gent",
        "get",
        "net",
        "new",
        "newt",
        "prat",
        "pry",
        "qua",
        "quart",
        "quartz",
        "rat",
        "tar",
        "tarp",
        "ten",
        "went",
        "wet",
        "arty",
        "rhr",
        "not",
        "quar",
    ]
    mygame = Boggle(grid, dictionary)
    found = mygame.getSolution()
    print("Found words:", found)



