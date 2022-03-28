# Chaos CT Segmentation using 2D-UNet Light-weight
### Contents
1. [Installation](#installation)
2. [Preparation](#preparation)
3. [Eval](#eval)
4. [Performance](#performance)
5. [Model_info](#model_info)

### Installation
1. Environment requirement
    - pytorch, opencv, tqdm ...
    - vai_q_pytorch(Optional, required by quantization)
    - XIR Python frontend (Optional, required by quantization)

2. Installation with GPU Docker

   - Please refer to [vitis-ai](https://github.com/Xilinx/Vitis-AI/tree/master/) for how to obtain the GPU docker image.

   - Activate pytorch virtual envrionment in docker:
   ```shell
   conda activate vitis-ai-pytorch
   ```
   - Install all the python dependencies using pip:
   ```shell
   pip install -r requirements.txt
   ```


### Preparation

1. dataset describle.
  ```
  dataset includes image file, groundtruth file and a validation image list file.
  ```
2. prepare dataset.

  ```shell

  # please download Chaos-CT dataset (https://chaos.grand-challenge.org/Download/) and unzip each zip file.
  # put the grundtruth folder and image folder in  `data` directory.
  # CT Train Sets: [1,2,5,6,8,10,14,16,18,19,21,22,23,24,25,26,27,28,29,30]
  # CT Test Sets: [3,4,7,9,11,12,13,15,17,20,31,32,33,34,35,36,37,38,39,40]
  
  * `data` directory structure like:
    + data
        +Chaos
            + Train_Sets
                    + CT
                      ▪ CT Train Sets: [1,2,5,6,8,10,14,16,18,19,21,22,23,24,25,26,27,28,29,30]
                         + DICOM_anon
                         + Ground
                        
            + Test_Sets
                    + CT
                      ▪ CT Test Sets: [3,4,7,9,11,12,13,15,17,20,31,32,33,34,35,36,37,38,39,40]
                         + DICOM_anon
                         + Ground

  ```
  Note：please registere before download dataset. More dataset information [ChaosCT document](https://www.dropbox.com/sh/7rospm65dmr8osd/AAB8imtFkTK37msLlSWxfwwya?dl=0&preview=CHAOS_Submission_Manual_new.pdf)

3. Data pre-processing
 
   ```shell
   # Convert dicom format data to PNG format image. Modify you data path as needed.
   python code/utils/prepare_data.py
    ```
    
   ```
   * `data` directory structure like:
    + data
        +Chaos
            + Train_Sets
                    + CT
                      ▪ CT Train Sets: [1,2,5,6,8,10,14,16,18,19,21,22,23,24,25,26,27,28,29,30]
                         + DICOM_anon
                         + Ground
                         + image
                        
            + Test_Sets
                    + CT
                      ▪ CT Test Sets: [3,4,7,9,11,12,13,15,17,20,31,32,33,34,35,36,37,38,39,40]
                         + DICOM_anon
                         + Ground
                         + image

    ```
### Eval

1. Evaluation
  ```shell
  cd ./code/
  # modify configure if you need, includes data root, weight path,...
  bash run_eval.sh
  ```
2. Training 
  ```shell
  cd ./code/
  # modify configure if you need, includes data root, weight path,...
  bash run_train.sh
  ```
3. Quantization
  ```shell
  cd ./code/
  # modify configure if you need, includes data root, weight path,...
  bash run_quant.sh
  ```
  
### Performance

| Model | Input | FLOPs | Performance on CHAOS_Test_Sets| 
|---- |----|----|----------------------------------|
| 2D-UNet-LightWeight|512x512|23.3G|Dice = 97.58%|

| Model | Input | FLOPs | INT8 Performance on CHAOS_Test_Sets| 
|---- |----|----|----------------------------------|
| 2D-UNet-LightWeight| 512x512 | 23.3G |Dice = 97.47%|


### Model_info

1. data preprocess
```
1.1). data channel order: BGR(0~255)
1.2). resize: 512*512(H*W)
1.3). mean_value: 104, 117, 123
1.4). scale: 1.0
```
2. system environment

The operation and accuracy provided above are verified in Ubuntu16.04.10, cuda-9.0, Driver Version: 460.32.03, GPU NVDIA P100 