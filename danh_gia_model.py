import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('\\yolov5\\runs\\train\\exp15\\results.csv')

# print(df['               epoch'])
plt.figure(figsize=(10, 5))
plt.plot(df['               epoch'], df['      train/obj_loss'], label='Train Objectness Loss') 
plt.plot(df['               epoch'], df['      train/cls_loss'], label='Train Class Loss')
plt.plot(df['               epoch'], df['      train/box_loss'], label='Train Total Loss')
plt.plot(df['               epoch'], df['        val/obj_loss'], label='validation Objectness Loss') 
plt.plot(df['               epoch'], df['        val/cls_loss'], label='validation Class Loss')
plt.plot(df['               epoch'], df['        val/box_loss'], label='validation Total Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()
plt.title('Training and Validation Loss')
plt.show() 


plt.figure(figsize=(10, 5))
plt.plot(df['               epoch'], df['metrics/mAP_0.5:0.95'], label='mAP (Mean Average Precision)')
plt.xlabel('Epoch')
plt.ylabel('mAP')
plt.legend()
plt.title('mAP (Mean Average Precision)')
plt.show() 
