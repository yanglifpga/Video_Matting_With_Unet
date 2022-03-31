# Video_Matting_With_Unet
### Story
Background replacement is in strong demand in fields such as live video broadcasting and video conferencing. It needs to distinguish the semantic information of people and backgrounds in real time. Isolate characters from cluttered backgrounds.
unet is often used to handle similar scenarios.
VCK5000 is used to replace GPU, which is usually widely used hardware in CNN inference, but consumes a lot of power.
In this project, a self-built dataset and a GTX1070 graphics card are used to train the CNN network.
Use Vitis-ai1.4 docker to quantify and compile the CNN model and deploy it on the VCK5000 accelerator card.

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

   - Please refer to [vitis-ai 1.4](https://github.com/Xilinx/Vitis-AI/tree/master/) for how to obtain the GPU docker image.
   - ./docker_run.sh xilinx/vitis-ai-gpu:1.4.1.978

   - Copy pytorch virtual envrionment in docker:
   ```shell
   conda create -n vitis-ai-pytorch2 --clone vitis-ai-pytorch
   conda activate vitis-ai-pytorch2
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

  # please download videomatte dataset (https://grail.cs.washington.edu/projects/background-matting-v2/#/datasets) and unzip each zip file.
  # PhotoMatte85(394MB)
  # Backgrounds(55MB)
  
  * `data` directory structure like:
    + data
        +PhotoMatte85/
        +Backgrounds/
        +prepare_img.m
        +importpngfile.m
  ```

3. Data pre-processing
 
   ```matlab
   # Convert dicom format data to PNG format image. Modify you data path as needed.
   matlab_run prepare_img.m
    ```
    
   ```
   * `data` directory structure like:
   + data
        +my
           +Train_Sets
               +lable
                   +lable_10001.png
               +live
                   +live_10001.png
    ```
### Eval

1. Training 
  ```shell
  cd ./code/
  # modify configure if you need, includes data root, weight path,...
  bash run_train.sh
  ```
2. Quantization
  ```shell
  cd ./code/
  # modify configure if you need, includes data root, weight path,...
  bash run_quant.sh
  ```
3. Compile
  ```shell
  cd ./code/compile/
  # modify configure if you need, includes data root, weight path,...
  bash compile.sh
  # compiled module is in lockate /code/compile/compiled_model/
  ```
4. Demo
  ```shell
  cd ./code/demo/
  # modify configure if you need, includes data root, weight path,...
  chmod +x ./build.sh
  ./build.sh
  ./test_jpeg_segmentation ../compile/compiled_model/Unet_vck5000.xmodel <path to image>
  ./test_video_segmentation ../compile/compiled_model/Unet_vck5000.xmodel /dev/video0
  # compiled module is in lockate /code/compile/compiled_model/
  ```  

### Model_info

1. data preprocess
```
1.1). data channel order: BGR(0~255)
1.2). resize: 512*512(H*W)
1.3). mean_value: 104, 117, 123
1.4). scale: 1.0
```
2. system environment

The operation and accuracy provided above are verified in Ubuntu20.04.01, cuda-10.1, Driver Version: 470, GPU NVDIA GTX1070
