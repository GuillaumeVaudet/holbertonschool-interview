#!/usr/bin/python3
"""
Module to resolve Lockboxes algorithm
"""


def canUnlockAll(boxes):
    total_boxes = len(boxes)
    opened_boxes = {0}

    keys_to_use = [0]

    while len(keys_to_use) > 0:
        current_key = keys_to_use.pop()

        keys_found = boxes[current_key]

        for key in keys_found:
            if key < total_boxes and key not in opened_boxes:
                opened_boxes.add(key)
                keys_to_use.append(key)

    return len(opened_boxes) == total_boxes


if __name__ == "__main__":
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))
