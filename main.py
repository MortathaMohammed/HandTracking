import numpy as np
import cv2
import mediapipe as mp
from ret import Return as rt
from color import color_finger as cf
import time

cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)
mpDraw = mp.solutions.drawing_utils
img2show = []
tipIds = [1, 5, 9, 13, 17]

initial_time = time.time()
to_time = time.time()

set_fps = 5  # Set your desired frame rate

# Variables Used to Calculate FPS
prev_frame_time = 0  # Variables Used to Calculate FPS
new_frame_time = 0

while cap.isOpened():
    while_running = time.time()  # Keep updating time with each frame

    # If time taken is 1/fps, then read a frame
    new_time = while_running - initial_time

    if new_time >= 1 / set_fps:
        ret, frame = cap.read()
        if ret:
            # Calculating True FPS
            new_frame_time = time.time()
            fps = 1 / (new_frame_time - prev_frame_time)
            prev_frame_time = new_frame_time
            fps = int(fps)
            fps = str(fps)
            print(fps)

            success, img = cap.read()
            img = cv2.flip(img, 1)

            imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            # img2 = cv2.imread('C:/Users/mdraz/OneDrive/Desktop/Hand Tracking/wallpaperflare.com_wallpaper.jpg')
            # img2array = np.ones_like(img2) * 38

            results = hands.process(imgRGB)

            lmList = []

            if results.multi_hand_landmarks:
                for handLms in results.multi_hand_landmarks:
                    for id, lm in enumerate(handLms.landmark):
                        h, w, c = img.shape
                        cx, cy = int(lm.x * w), int(lm.y * h)
                        lmList.append([id, cx, cy])
                        # mpDraw.draw_landmarks(
                        #       img,
                        #       results.multi_hand_landmarks[0],
                        #       # mpHands.HAND_CONNECTIONS
                        # )
                        if len(lmList) == 21:
                            cf.color_line(img, lmList)
                            cf.color_circle(img, lmList)

                            cv2.putText(img, f'{rt.all_char(lmList, tipIds)}', (250, 450), cv2.FONT_HERSHEY_DUPLEX,
                                        2, (255, 153, 204), 3)

            initial_time = while_running  # Update the initial time with current time

        else:
            # To get the total time of the video
            total_time_of_video = while_running - to_time
            print(total_time_of_video)
            break

        cv2.imshow('Hand Tracker', img)
        if cv2.waitKey(5) & 0xff == 27:
            break

cap.release()
cv2.destroyAllWindows()
