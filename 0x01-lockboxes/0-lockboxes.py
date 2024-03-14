#!/usr/bin/python3
""" Python3 lockboxes """


def canUnlockAll(boxes):
    """ Checks if you can unlock all boxes """

    for key in range(1, len(boxes)):
        check = False
        for box in range(len(boxes)):
            if key in boxes[box] and box != key:
                check = True
                break

        if not check:
            return False

    return True
