import numpy as np
import matplotlib.pyplot as plt


def _GenerateCircle():
    shape = (256, 256)
    center1, diameter = (50, 50), 20 # 圆
    center2, center_line = (70, 150), 15 # 菱形
    center3, edge = (190, 130), 20 # 正方形

    array = np.zeros(shape)
    mask1 = np.zeros(shape)
    mask2 = np.zeros(shape)
    mask3 = np.zeros(shape)
    for x in range(shape[0]):
        for y in range(shape[1]):
            if (x - center1[0]) ** 2 + (y - center1[1]) ** 2 < diameter ** 2:
                array[x, y] = 1
                mask1[x, y] = 1
            if abs(x - center2[0]) + abs(y - center2[1]) < center_line:
                array[x, y] = 1
                mask2[x, y] = 1
            if abs(x - center3[0]) < edge and abs(y - center3[1]) < edge:
                array[x, y] = 1
                mask3[x, y] = 1

    classes = [0, 1, 2]
    boxes = [[30, 30, 70, 70], [55, 135, 85, 165], [170, 110, 210, 150]]
    masks = [mask1, mask2, mask3]
    return array[np.newaxis, np.newaxis, ...], \
           np.array(classes)[np.newaxis, ...], \
           np.array(boxes)[np.newaxis, ...], \
           np.array(masks)[np.newaxis, ...]


if __name__ == '__main__':
    array, classes, boxes, masks = _GenerateCircle()
    print(array.shape, classes.shape, boxes.shape, masks.shape)
    plt.imshow(array[0,0])
    plt.show()
    plt.imshow(masks[0,0])
    plt.show()
    plt.imshow(masks[0,1])
    plt.show()
    plt.imshow(masks[0,2])
    plt.show()
