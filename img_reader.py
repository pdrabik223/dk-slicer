#
#
# class ImageReader:
#     def __init__(self, path: str) -> None:
#         self._image = cv2.VideoCapture(path, cv2.COLOR_BGR2RGB)
#         self._gray_scale_image = cv2.cvtColor(self._image, cv2.COLOR_BGR2GRAY)
#         self._gray_scaled_edge_detected = cv2.Canny(self._image, 0.6, 0.1)
#
#     def DisplayOriginalImage(self) -> None:
#         # cv2.namedWindow("Display")
#         cv2.imshow("Original image", self._image)
#
#     def DisplaygrayScaleImage(self) -> None:
#         # cv2.namedWindow("Display")
#         cv2.imshow("Gray scale image", self._gray_scale_image)
#
#     def DisplayEdges(self) -> None:
#         # cv2.namedWindow("Display")
#         cv2.imshow("Gray scale image, with detected images",
#                    self._gray_scaled_edge_detected)
