import cv2
class color_finger():
    def color_line(img, lmList):
        cv2.line(img, (lmList[0][1], lmList[0][2]),
                (lmList[1][1], lmList[1][2]), (0, 153, 255), 2)
        cv2.line(img, (lmList[1][1], lmList[1][2]),
                (lmList[2][1], lmList[2][2]), (0, 153, 255), 2)
        cv2.line(img, (lmList[2][1], lmList[2][2]),
                (lmList[3][1], lmList[3][2]), (0, 153, 255), 2)
        cv2.line(img, (lmList[3][1], lmList[3][2]),
                (lmList[4][1], lmList[4][2]), (0, 153, 255), 2)

        cv2.line(img, (lmList[0][1], lmList[0][2]),
                (lmList[5][1], lmList[5][2]), (0, 255, 0), 2)
        cv2.line(img, (lmList[5][1], lmList[5][2]),
                (lmList[6][1], lmList[6][2]), (0, 255, 0), 2)
        cv2.line(img, (lmList[6][1], lmList[6][2]),
                (lmList[7][1], lmList[7][2]), (0, 255, 0), 2)
        cv2.line(img, (lmList[7][1], lmList[7][2]),
                (lmList[8][1], lmList[8][2]), (0, 255, 0), 2)

        cv2.line(img, (lmList[0][1], lmList[0][2]),
                (lmList[9][1], lmList[9][2]), (255, 255, 0), 2)
        cv2.line(img, (lmList[9][1], lmList[9][2]),
                (lmList[10][1], lmList[10][2]), (255, 255, 0), 2)
        cv2.line(img, (lmList[10][1], lmList[10][2]),
                (lmList[11][1], lmList[11][2]), (255, 255, 0), 2)
        cv2.line(img, (lmList[11][1], lmList[11][2]),
                (lmList[12][1], lmList[12][2]), (255, 255, 0), 2)

        cv2.line(img, (lmList[0][1], lmList[0][2]),
                (lmList[13][1], lmList[13][2]), (255, 153, 0), 2)
        cv2.line(img, (lmList[13][1], lmList[13][2]),
                (lmList[14][1], lmList[14][2]), (255, 153, 0), 2)
        cv2.line(img, (lmList[14][1], lmList[14][2]),
                (lmList[15][1], lmList[15][2]), (255, 153, 0), 2)
        cv2.line(img, (lmList[15][1], lmList[15][2]),
                (lmList[16][1], lmList[16][2]), (255, 153, 0), 2)

        cv2.line(img, (lmList[0][1], lmList[0][2]),
                (lmList[17][1], lmList[17][2]), (255, 153, 204), 2)
        cv2.line(img, (lmList[17][1], lmList[17][2]),
                (lmList[18][1], lmList[18][2]), (255, 153, 204), 2)
        cv2.line(img, (lmList[18][1], lmList[18][2]),
                (lmList[19][1], lmList[19][2]), (255, 153, 204), 2)
        cv2.line(img, (lmList[19][1], lmList[19][2]),
                (lmList[20][1], lmList[20][2]), (255, 153, 204), 2)


    def color_circle(img, lmList):
        cv2.circle(img, (lmList[0][1], lmList[0][2]),
                    2, (0, 102, 250), 2, cv2.FILLED)
        cv2.circle(img, (lmList[4][1], lmList[4]
                    [2]), 2, (0, 102, 250), 2, cv2.FILLED)
        cv2.circle(img, (lmList[8][1], lmList[8][2]),
                    2, (0, 102, 250), 2, cv2.FILLED)

        cv2.circle(img, (lmList[12][1], lmList[12][2]),
                    2, (0, 102, 250), 2, cv2.FILLED)
        cv2.circle(img, (lmList[16][1], lmList[16]
                    [2]), 2, (0, 102, 250), 2, cv2.FILLED)
        cv2.circle(img, (lmList[20][1], lmList[20]
                    [2]), 2, (0, 102, 250), 2, cv2.FILLED)



        cv2.circle(img, (lmList[5][1], lmList[5][2]),
                    2, (0, 102, 250), 2, cv2.FILLED)
        cv2.circle(img, (lmList[9][1], lmList[9]
                    [2]), 2, (0, 102, 250), 2, cv2.FILLED)
        cv2.circle(img, (lmList[13][1], lmList[13]
                    [2]), 2, (0, 102, 250), 2, cv2.FILLED)
        cv2.circle(img, (lmList[17][1], lmList[17][2]),
                    2, (0, 102, 250), 2, cv2.FILLED)