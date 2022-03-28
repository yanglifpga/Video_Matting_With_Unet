import SimpleITK as sitk
import numpy as np
import cv2
import pdb
import os

def convert_from_dicom_to_jpg(img,low_window,high_window,save_path):
    lungwin = np.array([low_window*1.,high_window*1.])
    newimg = (img-lungwin[0])/(lungwin[1]-lungwin[0])
    newimg = (newimg*255).astype('uint8')
    cv2.imwrite(save_path, newimg, [int(cv2.IMWRITE_JPEG_QUALITY), 100])

if __name__ == '__main__':
    #ids = [11, 12, 13, 15, 17, 20, 3, 31, 32, 33, 34, 35, 36, 37, 38, 39, 4, 40, 7, 9]
    
    mode = 'train'
    
    if mode == 'train':
        data_path = 'Train_Sets'
        ids = [1,2,5,6,8,10,14,16,18,19,21,22,23,24,25,26,27,28,29,30]
    elif mode == 'test':
        data_path = 'Test_Sets'
        ids = [3,4,7,9,11,12,13,15,17,20,31,32,33,34,35,36,37,38,39,40]
    
    for index in ids:
        print(index)
        count = 0
        dcm_image_root = os.path.join('data/Chaos', data_path, 'CT', str(index), 'DICOM_anon/')
        save_image_root = os.path.join('data/Chaos', data_path,'CT', str(index), 'image/')
        if not os.path.exists(save_image_root):
            os.makedirs(save_image_root)
        for name in os.listdir(dcm_image_root):
            print(index, name)
            dcm_image_path = os.path.join(dcm_image_root, name)
            out_name = 'Liver_image_'+name[:-4].split(',')[0][-3:]+'.png'
            output_jpg_path = os.path.join(save_image_root, out_name)
            #print(output_jpg_path)
            #pdb.set_trace()
            ds_array = sitk.ReadImage(dcm_image_path)
            img_array = sitk.GetArrayFromImage(ds_array)
            #print(img_array)
            img_array[img_array > 10000]=0    
            #print(img_array) 
            shape = img_array.shape
            img_array = np.reshape(img_array, (shape[1], shape[2]))
            high = np.max(img_array)
            low = np.min(img_array)
            convert_from_dicom_to_jpg(img_array, low, high, output_jpg_path)
    print('FINISHED')

