import cv2
import numpy as np
import time
# 四个点的坐标
points = []
# 回调函数，用于鼠标事件
def mouse_callback(event, x, y, flags, param):
    image = param['image']
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append((x, y))
        if len(points) == 4:
            # 透视变换
            transformed_img = img_perspective_transform(image, points)
            # 保存透视变换后的图片
            cv2.imwrite('transformed_image.jpg', transformed_img)
            cv2.namedWindow('Transformed Image', cv2.WINDOW_NORMAL) 
            cv2.resizeWindow('Transformed Image', 1200, 800)
            cv2.imshow('Transformed Image', transformed_img)
            return 

# 透视变换
def img_perspective_transform(img, points):
    h, w, c = img.shape
    pts1 = np.float32(points)
    pts2 = np.float32([[0, 0], [0, w - 2], [h - 2, w - 2], [h - 2, 0]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    result = cv2.warpPerspective(img, matrix, (h, w))
    # cv2.imshow("Perspective transformation", result)
    return result
# 读取图片








def process_image():
    print("在图片上按下  q   退出程序")
    # 指定图片
    image = cv2.imread('test.jpg')
    image_copy = image.copy()  # 复制原始图片，用于在上面绘制选择的点

    # 创建窗口并展示原始图片
    cv2.namedWindow('Original Image', cv2.WINDOW_NORMAL)  # 设置为可调节窗口
    cv2.resizeWindow('Original Image', 1200, 800)
    cv2.imshow('Original Image', image)

    # 设置鼠标事件回调函数
    param = {'image': image}
    cv2.setMouseCallback('Original Image', mouse_callback,param)

    # 等待用户选择四个点
    while True:
        # 在复制的图片上绘制选择的点
        for point in points:
            cv2.circle(image_copy, point, 5, (0, 0, 255), -1)  # 将选择的点绘制为红色圆点
        cv2.imshow('Original Image', image_copy)
        # print(cv2.waitKey(1) & 0xFF == ord('q'))
        # time.sleep(1)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        if len(points) == 4:
            break

    # 关闭窗口
    cv2.destroyAllWindows()

    # 执行其他处理或返回结果
    return points




process_image()







