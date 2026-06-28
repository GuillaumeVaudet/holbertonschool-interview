#!/usr/bin/python3
"""
Module to resolve Lockboxes algorithm
"""


def canUnlockAll(boxes):
    total_boxes = len(boxes)
    opened_boxes = {0}

    def going_into_box(box_number):
        keys_found = boxes[box_number]

        for key in keys_found:
            if key < total_boxes and key not in opened_boxes:
                opened_boxes.add(key)
                going_into_box(key)
    going_into_box(0)

    return len(opened_boxes) == total_boxes


if __name__ == "__main__":
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))
