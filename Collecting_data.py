##Collect.py

import cv2
import numpy as np
import os

# Create the directory structure
"""if not os.path.exists("data"):
    os.makedirs("data")
    os.makedirs("data/train")
    os.makedirs("data/test")
    os.makedirs("data/train/0")
    os.makedirs("data/train/1")
    os.makedirs("data/train/2")
    os.makedirs("data/train/3")
    os.makedirs("data/train/4")
    os.makedirs("data/train/5")
    os.makedirs("data/test/0")
    os.makedirs("data/test/1")
    os.makedirs("data/test/2")
    os.makedirs("data/test/3")
    os.makedirs("data/test/4")
    os.makedirs("data/test/5")
    os.makedirs("data/test/6")
    os.makedirs("data/test/A")"""

# Train or test
mode = 'train'
directory = 'Data/' + mode + '/'

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    # Simulating mirror image
    frame = cv2.flip(frame, 1)

    # Getting count of existing images
    count = dict(zero=len(os.listdir(directory + "/0")), one=len(os.listdir(directory + "/1")),
                 two=len(os.listdir(directory + "/2")), three=len(os.listdir(directory + "/3")),
                 four=len(os.listdir(directory + "/4")), five=len(os.listdir(directory + "/5")),
                 six=len(os.listdir(directory + "/6")), seven=len(os.listdir(directory + "/7")),
                 A=len(os.listdir(directory + "/A")), B=len(os.listdir(directory + "/B")),
                 C=len(os.listdir(directory + "/C")), D=len(os.listdir(directory + "/D")),
                 E=len(os.listdir(directory + "/E")), F=len(os.listdir(directory + "/F")),
                 G=len(os.listdir(directory + "/G")), H=len(os.listdir(directory + "/H")),
                 I=len(os.listdir(directory + "/I")), J=len(os.listdir(directory + "/J")),
                 K=len(os.listdir(directory + "/K")), L=len(os.listdir(directory + "/L")),
                 M=len(os.listdir(directory + "/M")), N=len(os.listdir(directory + "/N")),
                 O=len(os.listdir(directory + "/O")), P=len(os.listdir(directory + "/P")),
                 Q=len(os.listdir(directory + "/Q")), R=len(os.listdir(directory + "/R")),
                 S=len(os.listdir(directory + "/S")), T=len(os.listdir(directory + "/T")),
                 U=len(os.listdir(directory + "/U")), V=len(os.listdir(directory + "/V")),
                 W=len(os.listdir(directory + "/W")), X=len(os.listdir(directory + "/X")),
                 Y=len(os.listdir(directory + "/Y")), Z=len(os.listdir(directory + "/Z")))

    # Printing the count in each set to the screen
    cv2.putText(frame, "MODE : " + mode, (10, 50), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    """cv2.putText(frame, "IMAGE COUNT", (10, 100), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "ZERO : " + str(count['zero']), (10, 120), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "ONE : " + str(count['one']), (10, 140), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "TWO : " + str(count['two']), (10, 160), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "THREE : " + str(count['three']), (10, 180), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "FOUR : " + str(count['four']), (10, 200), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "FIVE : " + str(count['five']), (10, 220), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)"""

    # Coordinates of the ROI
    x1 = int(0.5 * frame.shape[1])
    y1 = 10
    x2 = frame.shape[1] - 10
    y2 = int(0.5 * frame.shape[1])
    # Drawing the ROI
    # The increment/decrement by 1 is to compensate for the bounding box
    cv2.rectangle(frame, (x1 - 1, y1 - 1), (x2 + 1, y2 + 1), (255, 0, 0), 1)
    # Extracting the ROI
    roi = frame[y1:y2, x1:x2]
    roi = cv2.resize(roi, (64, 64))

    cv2.imshow("Frame", frame)

    roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    _, roi = cv2.threshold(roi, 120, 255, cv2.THRESH_BINARY)
    cv2.imshow("ROI", roi)

    interrupt = cv2.waitKey(10)
    if interrupt & 0xFF == 27:  # esc key
        break
    if interrupt & 0xFF == ord('0'):
        cv2.imwrite(directory + '0/' + str(count['zero']) + '.jpg', roi)
    if interrupt & 0xFF == ord('1'):
        cv2.imwrite(directory + '1/' + str(count['one']) + '.jpg', roi)
    if interrupt & 0xFF == ord('2'):
        cv2.imwrite(directory + '2/' + str(count['two']) + '.jpg', roi)
    if interrupt & 0xFF == ord('3'):
        cv2.imwrite(directory + '3/' + str(count['three']) + '.jpg', roi)
    if interrupt & 0xFF == ord('4'):
        cv2.imwrite(directory + '4/' + str(count['four']) + '.jpg', roi)
    if interrupt & 0xFF == ord('5'):
        cv2.imwrite(directory + '5/' + str(count['five']) + '.jpg', roi)
    if interrupt & 0xFF == ord('6'):
        cv2.imwrite(directory + '6/' + str(count['six']) + '.jpg', roi)
    if interrupt & 0xFF == ord('7'):
        cv2.imwrite(directory + '7/' + str(count['seven']) + '.jpg', roi)
    if interrupt & 0xFF == ord('a'):
        cv2.imwrite(directory + 'A/' + str(count['A']) + '.jpg', roi)
    if interrupt & 0xFF == ord('b'):
        cv2.imwrite(directory + 'B/' + str(count['B']) + '.jpg', roi)
    if interrupt & 0xFF == ord('c'):
        cv2.imwrite(directory + 'C/' + str(count['C']) + '.jpg', roi)
    if interrupt & 0xFF == ord('d'):
        cv2.imwrite(directory + 'D/' + str(count['D']) + '.jpg', roi)
    if interrupt & 0xFF == ord('e'):
        cv2.imwrite(directory + 'E/' + str(count['E']) + '.jpg', roi)
    if interrupt & 0xFF == ord('f'):
        cv2.imwrite(directory + 'F/' + str(count['F']) + '.jpg', roi)
    if interrupt & 0xFF == ord('g'):
        cv2.imwrite(directory + 'G/' + str(count['G']) + '.jpg', roi)
    if interrupt & 0xFF == ord('h'):
        cv2.imwrite(directory + 'H/' + str(count['H']) + '.jpg', roi)
    if interrupt & 0xFF == ord('i'):
        cv2.imwrite(directory + 'I/' + str(count['I']) + '.jpg', roi)
    if interrupt & 0xFF == ord('j'):
        cv2.imwrite(directory + 'J/' + str(count['J']) + '.jpg', roi)
    if interrupt & 0xFF == ord('k'):
        cv2.imwrite(directory + 'K/' + str(count['K']) + '.jpg', roi)
    if interrupt & 0xFF == ord('L'):
        cv2.imwrite(directory + 'l/' + str(count['l']) + '.jpg', roi)
    if interrupt & 0xFF == ord('m'):
        cv2.imwrite(directory + 'M/' + str(count['M']) + '.jpg', roi)
    if interrupt & 0xFF == ord('n'):
        cv2.imwrite(directory + 'N/' + str(count['N']) + '.jpg', roi)
    if interrupt & 0xFF == ord('o'):
        cv2.imwrite(directory + 'O/' + str(count['O']) + '.jpg', roi)
    if interrupt & 0xFF == ord('p'):
        cv2.imwrite(directory + 'P/' + str(count['P']) + '.jpg', roi)
    if interrupt & 0xFF == ord('q'):
        cv2.imwrite(directory + 'Q/' + str(count['Q']) + '.jpg', roi)
    if interrupt & 0xFF == ord('r'):
        cv2.imwrite(directory + 'R/' + str(count['R']) + '.jpg', roi)
    if interrupt & 0xFF == ord('s'):
        cv2.imwrite(directory + 'S/' + str(count['S']) + '.jpg', roi)
    if interrupt & 0xFF == ord('t'):
        cv2.imwrite(directory + 'T/' + str(count['T']) + '.jpg', roi)
    if interrupt & 0xFF == ord('u'):
        cv2.imwrite(directory + 'U/' + str(count['U']) + '.jpg', roi)
    if interrupt & 0xFF == ord('v'):
        cv2.imwrite(directory + 'V/' + str(count['V']) + '.jpg', roi)
    if interrupt & 0xFF == ord('w'):
        cv2.imwrite(directory + 'W/' + str(count['W']) + '.jpg', roi)
    if interrupt & 0xFF == ord('x'):
        cv2.imwrite(directory + 'X/' + str(count['X']) + '.jpg', roi)
    if interrupt & 0xFF == ord('y'):
        cv2.imwrite(directory + 'Y/' + str(count['Y']) + '.jpg', roi)
    if interrupt & 0xFF == ord('z'):
        cv2.imwrite(directory + 'Z/' + str(count['Z']) + '.jpg', roi)

cap.release()
cv2.destroyAllWindows()
