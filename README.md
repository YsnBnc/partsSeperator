
# Computer Vision-Assisted Parts Separator

An Arduino UNO servomotor controlled by Ultralytics YOLOv26 algorithm.

The dataset has been used for this project is here: https://zenodo.org/records/7504801

The idea of the project is determine which part is on the screen then activate servomotor to represented rotation value for the object that showed to the camera.

There are four objects each has its own rotation value;

Gear: 45° Bolt: 90° Nut: 135° Bearing: 180° and if there is nothing shown on the screen then it goes to 0° as idle.

There is a ```ITERATION_THRESHOLD``` limit for the servomotor to activate. The reason for this the model spams output if something detected or not detected. Problem with this, it can detect object randomly and send false signal to motor. The ```ITERATION_THRESHOLD``` prevents that happening like if model gives 10 consecutive outputs then servomotor turns.
