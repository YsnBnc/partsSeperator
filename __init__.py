from ultralytics import YOLO
import serial
import time 

arduino = serial.Serial(port='/dev/ttyUSB0', baudrate=9600, timeout=.1) #Port name might vary in different OS 
time.sleep(2) 

model = YOLO("runs/detect/train/weights/best.pt") #Trained data
results = model.predict(source=0, show=True, stream=True, conf=0.5) #Camera

last_confirmed_state = '0'
candidate_state = '0'
consecutive_count = 0
ITERATION_THRESHOLD = 10 
last_sent = '0'

for r in results:
    
    detected_classes = [model.names[int(c)] for c in r.boxes.cls]
      
    current_target = None
    if 'Gear' in detected_classes: current_target = '1'
    elif 'Bolt' in detected_classes: current_target = '2'
    elif 'Nut' in detected_classes: current_target = '3'
    elif 'Bearing' in detected_classes: current_target = '4'
    else: current_target = '0'

    if current_target == candidate_state:
        consecutive_count += 1
    else:
        candidate_state = current_target
        consecutive_count = 0

    if consecutive_count >= ITERATION_THRESHOLD:
        if candidate_state != last_confirmed_state:
            arduino.write(candidate_state.encode())
            print(f"State: {candidate_state}")
            last_confirmed_state = candidate_state

   