from os import name
from keras.models import model_from_json
import operator
import cv2
from flask import Flask, Response, render_template

# Loading the model
json_file = open("model-bw.json", "r")
model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(model_json)
# load weights into new model
loaded_model.load_weights("model-bw.h5")
print("Loaded model from disk")

cap = cv2.VideoCapture(0)
app = Flask(__name__)


def stream():
    while True:
        _, frame = cap.read()
        # imgencode = cv2.imencode('.jpg',frame)[1]
        # stringData = imgencode.tostring()
        # Simulating mirror image
        frame = cv2.flip(frame, 1)

        # Got this from collect-data.py
        # Coordinates of the ROI
        x1 = int(0.5 * frame.shape[1])
        y1 = 10
        x2 = frame.shape[1] - 10
        y2 = int(0.5 * frame.shape[1])
        # Drawing the ROI
        # The increment/decrement by 1 is to compensate for the bounding box
        cv2.rectangle(frame, (x1 - 1, y1 - 1),
                      (x2 + 1, y2 + 1), (255, 0, 0), 1)
        # Extracting the ROI
        roi = frame[y1:y2, x1:x2]

        # Resizing the ROI so it can be fed to the model for prediction
        roi = cv2.resize(roi, (64, 64))
        roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        _, test_image = cv2.threshold(roi, 120, 255, cv2.THRESH_BINARY)
        # cv2.imshow("test", test_image)
        # Batch of 1
        result = loaded_model.predict(test_image.reshape(1, 64, 64, 1))
        prediction = {'A': result[0][0],
                      'B': result[0][1],
                      'C': result[0][2],
                      'D': result[0][3],
                      'E': result[0][4],
                      'F': result[0][5],
                      'G': result[0][6],
                      'H': result[0][7],
                      'I': result[0][8],
                      'J': result[0][9],
                      'K': result[0][10],
                      'L': result[0][11],
                      'M': result[0][12],
                      'N': result[0][13],
                      'O': result[0][14],
                      'P': result[0][15],
                      'Q': result[0][16],
                      'R': result[0][17],
                      'S': result[0][18],
                      'T': result[0][19],
                      'U': result[0][20],
                      'V': result[0][21],
                      'W': result[0][22],
                      'X': result[0][23],
                      'Y': result[0][24],
                      'Z': result[0][25], }

        # Sorting based on top prediction
        prediction = sorted(prediction.items(),
                            key=operator.itemgetter(1), reverse=True)

        # Displaying the predictions
        cv2.putText(frame, prediction[0][0], (10, 120),
                    cv2.FONT_HERSHEY_PLAIN, 10, (0, 0, 255), 1)
        # cv2.imshow("Frame", frame)
        imgencode = cv2.imencode('.jpg', frame)[1]
        stringData = imgencode.tostring()
        # interrupt = cv2.waitKey(10)
        # if interrupt & 0xFF == 27:  # esc key
        yield (b'--frame\r\n'b'Content-Type: text/plain\r\n\r\n'+stringData+b'\r\n')

        # break

# cap.release()
# cv2.destroyAllWindows()


@app.route('/video')
def video():
    return Response(stream(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/predict')
def main():
    return render_template('predict.html')


@app.route('/learn')
def learn():
    return render_template('LEARN.html')


@app.route('/aboutus')
def about():
    return render_template('ABOUT-US.html')


@app.route('/donate')
def donate():
    return render_template('Donate.html')


@app.route('/researchpaper')
def research():
    return render_template('Research-Paper.html')


@app.route('/sourcecode')
def source():
    return render_template('Source-Code.html')


@app.route('/')
def hello():
    return render_template('index.html')


if __name__ == "__main__":
    app.run()
