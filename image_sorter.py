import numpy as np
import pandas as pd
import os
import shutil
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.models import load_model
import warnings
warnings.filterwarnings('ignore')

model = load_model('final_model.h5')
print('Model Loaded.')

folder_path = os.getcwd() + '\\' + input('Which folder in this directory needs sorting?')

filenames = os.listdir(folder_path)

for filename in filenames:
    image = load_img(folder_path + '\\' + filename, target_size=(256, 256))
    image_array = img_to_array(image, data_format='channels_last')
    image_array = np.reshape(image_array, (1, 256, 256, 3))
    prediction = model.predict_classes(image_array, batch_size=1, verbose=0)
    if prediction.item() == 0:
        os.makedirs(folder_path + '\\' + 'people', exist_ok=True)
        shutil.move(folder_path + '\\' + filename, folder_path + '\\' + 'people')
        print(f'{filename} has been moved to people.')
    elif prediction.item() == 1:
        os.makedirs(folder_path + '\\' + 'landscapes', exist_ok=True)
        shutil.move(folder_path + '\\' + filename, folder_path + '\\' + 'landscapes')
        print(f'{filename} has been moved to landscapes.')
    else:
        print(f'{filename} could not be moved.')
