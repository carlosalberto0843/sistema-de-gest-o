import cv2
def camera():
    print('tirar foto - [1]')
    print('abrir camera - [2]')
    nova = input('digite a opcao: ')
    if nova == '2':
        camera = cv2.VideoCapture(0)
        while True:
            ret, frame = camera.read()
            cv2.imshow("Webcam", frame)
            if cv2.waitKey(1) == 27:  # ESC
                break
        camera.release()
        cv2.destroyAllWindows()

    elif nova == '1':
        camera = cv2.VideoCapture(0)
        ret, frame = camera.read()
        cv2.imwrite("foto.jpg", frame)
        camera.release()
    else:
        print('numero invalido, digite novamente \n')