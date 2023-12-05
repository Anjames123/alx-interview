#!/usr/bin/python3
"""
This module contains a function to solve the lockboxes algorrithm problem
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened

    Args:
        boxes (list): list of boxes

    Return:
        (bool) True if all boxes can be opened, false otherwise
    """
    if not boxes or len(boxes) == 1:
        return True

    total_boxes = len(boxes)
    visited_boxes = set()
    stack = [0]  # Start with the first box

    while stack:
        current_box = stack.pop()
        visited_boxes.add(current_box)

        for key in boxes[current_box]:
            if key not in visited_boxes and 0 <= key < total_boxes:
                stack.append(key)

    return len(visited_boxes) == total_boxes
