#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    Determine if all the boxes can be opened.

    Args:
    - boxes (list of lists): Each box is numbered sequentially from 0 to n - 1
      and may contain keys to the other boxes.

    Returns:
    - bool: True if all boxes can be opened, False otherwise.
    """

    if not boxes or not boxes[0]:
        return False

    n = len(boxes)
    visited = [False] * n
    visited[0] = True
    stack = [0]

    while stack:
        current_box = stack.pop()

        for key in boxes[current_box]:
            if 0 <= key < n and not visited[key]:
                visited[key] = True
                stack.append(key)

    return all(visited)
