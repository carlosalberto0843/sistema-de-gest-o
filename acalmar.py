import cv2
import winsound
import threading
def acalmar():
    def tocar_som():
        winsound.PlaySound(
            r"C:\Users\CARLOS ALBERTO NETO\Downloads\SOM-DE-BOI-BERRANDO-Vaca-e-Bezerro-Berrando-Vaca-Mugindo-Cow-Sound.wav",
            winsound.SND_FILENAME)
    threading.Thread(target=tocar_som).start()

    img = cv2.imread(
        r"C:\Users\CARLOS ALBERTO NETO\Downloads\wolfgang-hasselmann-0q13m5wTOlw-unsplash.jpg")

    cv2.namedWindow("Imagem", cv2.WINDOW_NORMAL)
    cv2.imshow("Imagem", img)
    cv2.waitKey(0)

    winsound.PlaySound(None, 0)
    cv2.destroyAllWindows()

