#!/usr/bin/python3
'''method that determines if all the boxes can be opened.'''


def canUnlockAll(boxes):
    '''method that determines if all the boxes can be opened.
        args:
            boxes: list of lists
        return:
            true or false depending if all boxes are oppened or not
    '''
    open_boxes = set()
    keys = set()
    if len(boxes[0]) == 0 and len(boxes) > 1:
        return False
    for i in range(len(boxes)):
        for j in range(len(boxes[i])):
            open_boxes.add(i)
            keys.add(boxes[i][j])
    if len(keys) == len(open_boxes):
        return True
    else:
        return False
