from typing import List, Tuple
from collections import deque
import heapq

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

class SearchAlgorithm:
  # Implement Uniform search
  @staticmethod
  def uniform_search(grid: List[List[str]]) -> Tuple[int, List[List[str]]]:
    # Your code here
    xhat, yhat = -1, -1
    
    for i in range(len(grid)):
      for j in range(len(grid[i])):
        if grid[i][j] == "s":
          x_i, y_i = i, j
        elif grid[i][j] == "t":
          xhat, yhat = i, j
          
    visited = set()
    q = [(0, (x_i, y_i))]
    order = 1
    
    while q:
      cost, (x, y) = heapq.heappop(q)
      
      if (x, y) == (xhat, yhat):
        return 1, grid
      
      if (x, y) in visited:
        continue
      
      visited.add((x, y))
      
      if grid[x][y] != "s" and grid[x][y] != "t":
        grid[x][y] = str(order)
        order += 1
      
      for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[nx]) and grid[nx][ny] != "-1":
          nc = cost + 1
          heapq.heappush(q, (nc, (nx, ny)))
          
    return -1, grid
  
  # Implement Depth First Search
  @staticmethod
  def dfs(grid: List[List[str]]) -> Tuple[int, List[List[str]]]:
    # Your code here
    x_i, y_i, xhat, yhat = -1, -1, -1, -1
    
    for i in range(len(grid)):
      for j in range(len(grid[i])):
        if grid[i][j] == "s":
          x_i, y_i = i, j
        if grid[i][j] == "t":
          xhat, yhat = i, j
  
    s = [(x_i, y_i)]
    visited = set()
    order = 1
    
    while s:
      x, y = s.pop()
      
      if (x, y) == (xhat, yhat):
        return 1, grid
      
      if (x, y) in visited:
        continue
      
      visited.add((x, y))
      
      if grid[x][y] != "s" and grid[x][y] != "t":
        grid[x][y] = str(order)
        order += 1
      
      for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[nx]) and grid[nx][ny] != "-1": 
          s.append((nx, ny))
          
    return -1, grid

  # Implement Breadth First Search
  @staticmethod
  def bfs(grid: List[List[str]]) -> Tuple[int, List[List[str]]]:
    # Your code here
    q = deque()
    xhat, yhat = -1, -1
    
    for i in range(len(grid)):
      for j in range(len(grid[i])):
        if grid[i][j] == "s":
          q.append((i, j))
        if grid[i][j] == "t":
          xhat, yhat = i, j
          
    visited = set()
    order = 1
          
    while q:
      x, y = q.popleft()
      
      if (x, y) == (xhat, yhat):
        return 1, grid
      
      if (x, y) in visited:
        continue
      
      visited.add((x, y))
      
      if grid[x][y] != "s" and grid[x][y] != "t":
        grid[x][y] = str(order)
        order += 1
      
      for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[nx]) and grid[nx][ny] != "-1":
          q.append((nx, ny))
          
    return -1, grid
  
  # Implement Best First Search
  @staticmethod
  def best_first_search(grid: List[List[str]]) -> Tuple[int, List[List[str]]]:
    # Your code here
    for i in range(len(grid)):
      for j in range(len(grid[i])):
        if grid[i][j] == "s":
          x_i, y_i = i, j
        if grid[i][j] == "t":
          xhat, yhat = i, j
          
    visited = set()
    q = [(0, (x_i, y_i))]
    order = 1
    
    while q:
      _, (x, y) = heapq.heappop(q)
      
      if (x, y) == (xhat, yhat):
        return 1, grid
      
      if (x, y) in visited:
        continue
      
      visited.add((x, y))
      
      if grid[x][y] != "s" and grid[x][y] != "t":
        grid[x][y] = str(order)
        order += 1
      
      for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[nx]) and grid[nx][ny] != "-1":
          dist = abs(nx - xhat) + abs(ny - yhat)
          heapq.heappush(q, (dist, (nx, ny)))
    
    return -1, grid
  
  # Implement A* Search
  @staticmethod
  def a_star_search(grid: List[List[str]]) -> Tuple[int, List[List[str]]]:
    # Your code here
    x_i, y_i, xhat, yhat = -1, -1, -1, -1
    order = 1
    
    for i in range(len(grid)):
      for j in range(len(grid[i])):
        if grid[i][j] == "s":
          x_i, y_i = i, j
        if grid[i][j] == "t":
          xhat, yhat = i, j
          
    def heuristic(x, y):
      return abs(x - xhat) + abs(y - yhat)
    
    def is_valid(x, y):
      return 0 <= x < len(grid) and 0 <= y < len(grid[x]) and grid[x][y] != "-1"
          
    visited = set()
    q = [(0, (x_i, y_i), 0)]
    
    while q:
      _, (x, y), cost = heapq.heappop(q)
      
      if (x, y) == (xhat, yhat):
        return 1, grid
      
      if (x, y) in visited:
        continue
      
      visited.add((x, y))
      
      if grid[x][y] != "s" and grid[x][y] != "t":
        if grid[x][y] == "0":
          grid[x][y] = str(order)
          order += 1
      
      for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        
        if is_valid(nx, ny) and (nx, ny) not in visited:
          g = cost + 1
          h = heuristic(nx, ny)
          f = g + h
 
          heapq.heappush(q, (f, (nx, ny), g))
      
    return -1, grid
  
  # Implement Greedy Search
  @staticmethod
  def greedy_search(grid: List[List[str]]) -> Tuple[int, List[List[str]]]:
    # Your code here
    x_i, y_i, xhat, yhat = -1, -1, -1, -1
    
    for i in range(len(grid)):
      for j in range(len(grid[i])):
        if grid[i][j] == "s":
          x_i, y_i = i, j
        if grid[i][j] == "t":
          xhat, yhat = i, j
          
    def heuristic(x, y):
      return abs(x - xhat) + abs(y - yhat)
    
    def is_valid(x, y): 
      return 0 <= x < len(grid) and 0 <= y < len(grid[x]) and grid[x][y] != "-1"
          
    visited = set()
    x, y = x_i, y_i
    order = 1
    
    best_dist = heuristic(x, y)
    while (x, y) != (xhat, yhat):
      best_x, best_y = x, y
      found_move = False
      counter = 0
      
      if (x, y) not in visited:
        visited.add((x, y))
      
      for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        
        if (nx, ny) in visited or not is_valid(nx, ny):
          counter += 1
          if counter == 4:
            return -1, grid
          continue
          
        if grid[nx][ny] == "-1":
          counter += 1
          if counter == 4:
            return -1, grid

        dist = heuristic(nx, ny)
        if dist < best_dist:
          best_dist = dist
          best_x, best_y = nx, ny
          found_move = True

        if dist > best_dist:
          counter += 1
          if counter == 4:
            return -1, grid
          continue
          
      if counter == 4 or not found_move:
        return -1, grid
      
      x, y = best_x, best_y
      if grid[x][y] != "t":
        grid[x][y] = str(order)
      order += 1
          
    return 1, grid
    
if __name__ == "__main__":
  example = [
  ['0', '0', '0', '0'],
  ['0', '-1', '-1', 't'],
  ['s', '0', '-1', '0'],
  ['0', '0', '0', '-1']
  ]
  # example = [
  #   ['s', '0', '0', '0', '-1', '-1', '-1', '-1'],
  #   ['0', '0', '0', '0', '0', '-1', '-1', '-1'],
  #   ['-1', '-1', '0', '-1', '-1', '0', '0', '0'],
  #   ['-1', '0', '0', '0', '0', '0', '0', 't']
  # ]
  # example = [
  #   ['s', '0', '0', '-1', '0'],
  #   ['0', '-1', '0', '-1', 't'],
  #   ['0', '-1', '0', '0', '0'],
  #   ['0', '0', '0', '-1', '0'],
  #   ['0', '-1', '-1', '-1', '0']
  # ]
  # example = [
  #   ['s', '0', '0', '0', '0'],
  #   ['-1', '-1', '0', '0', '0'],
  #   ['t', '-1', '0', '0', '0'],
  #   ['-1', '0', '0', '-1', '0'],
  #   ['0', '-1', '0', '-1', '0']
  # ]
  # example = [
  #   ['0', '0', '0', '-1', '0'],
  #   ['0', '0', '0', '-1', '0'],
  #   ['s', '0', '0', '0', '0'],
  #   ['0', '0', '0', '-1', 't'],
  #   ['0', '0', '0', '-1', '0']
  # ]
  # example = [
  #   ['0', '0', '0', '0', '0', '0', '0', '-1', '0', '0'],
  #   ['0', '0', '-1', '0', '0', '0', '0', '0', '0', '-1'],
  #   ['0', '-1', '-1', '0', '-1', '-1', '-1', '0', '-1', '0'],
  #   ['0', '0', '0', '0', '-1', '0', '0', '0', '-1', '0'],
  #   ['0', '-1', 't', '0', '0', '0', '-1', '-1', '0', '-1'],
  #   ['0', '0', '-1', '0', '-1', '0', '0', '0', '0', '0'],
  #   ['0', '0', '0', '0', '-1', '0', '-1', '0', '0', '0'],
  #   ['0', '0', '0', '0', '0', '0', '0', '-1', '0', '0'],
  #   ['0', 's', '-1', '0', '-1', '0', '0', '0', '0', '0'],
  #   ['-1', '0', '0', '0', '0', '-1', '-1', '-1', '0', '-1']
  # ]
  # example = [
  #   ['0', '0', '-1', '0', '0', '0', '0', '0', '0', '-1'],
  #   ['-1', '0', '-1', '0', 't', '-1', '0', '0', '-1', '-1'],
  #   ['-1', '0', '-1', '0', '0', '0', '0', '-1', '0', '0'],
  #   ['-1', '0', '0', '0', '0', '0', '0', '-1', '0', '-1'],
  #   ['-1', '0', '-1', '0', '-1', '-1', '0', '-1', '-1', '-1'],
  #   ['-1', '0', '0', '0', '-1', '0', '0', '-1', '0', '-1'],
  #   ['-1', '0', '-1', '-1', '-1', '-1', '0', '0', '0', '-1'],
  #   ['-1', '0', '0', '-1', 's', '0', '0', '0', '-1', '0'],
  #   ['0', '-1', '0', '0', '0', '0', '0', '-1', '-1', '0'],
  #   ['0', '-1', '0', '0', '0', '0', '0', '0', '0', '0']
  # ]
  
  found, final_state = SearchAlgorithm.dfs(example)
  if found == 1:
    print("Target found!")
  else:
    print("Target not found.")
  
  for row in final_state:
    print(' '.join(row))
