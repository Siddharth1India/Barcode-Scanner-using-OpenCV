import cv2
from pyzbar import pyzbar
# If you need to open website of QR-Code
import webbrowser

def codeReader(frame):
    barcodes = pyzbar.decode(frame)
    for barcode in barcodes:
        x, y , w, h = barcode.rect
        information = barcode.data.decode('utf-8')
        cv2.rectangle(frame, (x, y),(x+w, y+h), (0, 135, 255), 4)
        cv2.putText(frame, information, (x + 6, y - 6), cv2.FONT_HERSHEY_DUPLEX, 2.0, (255, 255, 255), 2)
        with open("barcode_result.txt", mode ='w') as file:
            file.write("Barcode:" + information)
    return frame

def main():
    camera = cv2.VideoCapture(0)
    ret, frame = camera.read()
    
    while ret:
        ret, frame = camera.read()
        frame = codeReader(frame)
        cv2.imshow('Barcode/QR code reader', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    camera.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()