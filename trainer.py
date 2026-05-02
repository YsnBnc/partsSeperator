from ultralytics import YOLO
import torch

def train_model():
    model = YOLO("yolo26n.pt") 
    model.train(
        data="./dataset/parts.yaml", #Dataset location
        epochs=50,               
        imgsz=640,              
        batch=8, #GPU memory
        device=0 if torch.cuda.is_available() else "cpu"                
    )

if __name__ == "__main__":
    train_model()