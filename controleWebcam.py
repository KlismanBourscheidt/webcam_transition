import cv2
import keyboard  # para detectar teclas em segundo plano

# Inicializar a captura de vídeo para a webcam local e o celular
webcam1 = cv2.VideoCapture(0)
webcam2 = cv2.VideoCapture("URL CAM OR NUMBER (1)")

# Definir a largura e altura padrão
WIDTH = 1280
HEIGHT = 720

# Aplicar as configurações de resolução para a webcam local
webcam1.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
webcam1.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)

# Não é garantido que o `set()` funcione no stream do celular, então vamos redimensionar manualmente
current_camera = webcam1

while True:
    # Ler a imagem da câmera ativa
    ret, frame = current_camera.read()
    if not ret:
        print('Erro ao acessar a câmera.')
        break

    # Redimensionar manualmente a imagem para garantir o tamanho correto
    frame_resized = cv2.resize(frame, (WIDTH, HEIGHT))

    # Exibir a imagem em uma janela
    cv2.imshow("Câmera para OBS", frame_resized)

    # Detectar as teclas pressionadas em segundo plano
    if keyboard.is_pressed("1"):  # tecla "1" para webcam1
        current_camera = webcam1
    elif keyboard.is_pressed("2"):  # tecla "2" para webcam2
        current_camera = webcam2
    elif keyboard.is_pressed("esc"):  # tecla "ESC" para sair
        break

    # Pequena pausa para evitar alto uso da CPU
    cv2.waitKey(10)

# Liberar os recursos
webcam1.release()
webcam2.release()
cv2.destroyAllWindows()
