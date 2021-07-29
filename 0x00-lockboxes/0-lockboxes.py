#!/usr/bin/python3
'''method that determines if all the boxes can be opened.'''


def canUnlockAll(boxes):
    '''method that determines if all the boxes can be opened.
        args:
            boxes: list of lists
        return:
            true or false depending if all boxes are oppened or not
    '''
    keyPocket = {0}
    for box in range(0, len(boxes)):
        if box in keyPocket:
            keyPocket.update(boxes[box])
            for key in boxes[box]:
                if key < len(boxes):
                    keyPocket.update(boxes[key])
        else:
            return False
    return True
