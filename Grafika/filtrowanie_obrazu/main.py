import cv2
import numpy as np


# Wczytaj obraz z podanej ścieżki
img_path = "kyc.png"  # Zmień na faktyczną ścieżkę do Twojego obrazu
img = cv2.imread(img_path)

# Sprawdź, czy obraz został poprawnie wczytany
if img is None:
    print("Nie można wczytać obrazu. Sprawdź ścieżkę.")
else:
    print("Obraz wczytany pomyślnie.")

# kernels
sharpening = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
mean = np.array([[1 / 9, 1 / 9, 1 / 9], [1 / 9, 1 / 9, 1 / 9], [1 / 9, 1 / 9, 1 / 9]])
mean_removal = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
gauss = np.array(
    [[1 / 16, 2 / 16, 1 / 16], [2 / 16, 4 / 16, 2 / 16], [1 / 16, 2 / 16, 1 / 16]]
)
gauss2 = np.array(
    [
        [1 / 52, 1 / 52, 2 / 52, 2 / 52, 1 / 52],
        [1 / 52, 2 / 52, 4 / 52, 2 / 52, 1 / 52],
        [2 / 52, 4 / 52, 8 / 52, 4 / 52, 2 / 52],
        [1 / 52, 2 / 52, 4 / 52, 2 / 52, 1 / 52],
        [1 / 52, 1 / 52, 2 / 52, 2 / 52, 1 / 52],
    ]
)
# horizontal = np.array([[0, 0, 0], [-1, 1, 0], [0, 0, 0]])
horizontal = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
# gradient kernels
east = np.array([[-1, 1, 1], [-1, -2, 1], [-1, 1, 1]])
south_east = np.array([[-1, -1, 1], [-1, -2, 1], [1, 1, 1]])
south = np.array([[-1, -1, -1], [1, -2, 1], [1, 1, 1]])
south_west = np.array([[1, -1, -1], [1, -2, -1], [1, 1, 1]])
west = np.array([[1, 1, -1], [1, -2, -1], [1, 1, -1]])
north_west = np.array([[1, 1, 1], [1, -2, -1], [1, -1, -1]])
north = np.array([[1, 1, 1], [1, -2, 1], [-1, -1, -1]])
north_east = np.array([[1, 1, 1], [-1, -2, 1], [-1, -1, 1]])
# Laplace kernels
lapl1 = np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])
lapl1 = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
lapl1 = np.array([[1, -2, 1], [-2, 4, -2], [1, -2, 1]])
# transformations
sharpened_img = cv2.filter2D(img, -1, sharpening)
mean_img = cv2.filter2D(img, -1, mean)
mean_removed_img = cv2.filter2D(img, -1, mean_removal)
gauss_img = cv2.filter2D(img, -1, gauss)
gauss2_img = cv2.filter2D(img, -1, gauss2)
detail_enhanced_img = cv2.detailEnhance(sharpened_img, sigma_s=10, sigma_r=0.15)
horizontal_edges_img = cv2.filter2D(img, -1, horizontal)
gradient_east_img = cv2.filter2D(detail_enhanced_img, -1, east)
lap1_img = cv2.filter2D(detail_enhanced_img, -1, lapl1)

# Wyświetl obraz w oknie OpenCV
cv2.imwrite("ladny_kyc.png", sharpened_img)
cv2.waitKey(0)  # Czeka na dowolny klawisz, aby zamknąć okno
cv2.destroyAllWindows()  # Zamknij wszystkie okna

