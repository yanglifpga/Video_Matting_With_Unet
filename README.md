# Video_Matting_With_Unet
### Story
Background replacement is in strong demand in fields such as live video broadcasting and video conferencing. It needs to distinguish the semantic information of people and backgrounds in real time. Isolate characters from cluttered backgrounds.
unet is often used to handle similar scenarios.
VCK5000 is used to replace GPU, which is usually widely used hardware in CNN inference, but consumes a lot of power.
In this project, a self-built dataset and a GTX1070 graphics card are used to train the CNN network.
Use Vitis-ai1.4 docker to quantify and compile the CNN model and deploy it on the VCK5000 accelerator card.

At least 100GB of disk space for the disk partition running Docker
Clone the Vitis-AI repository to obtain the examples, reference code, and scripts.

	git clone --recurse-submodules https://github.com/Xilinx/Vitis-AI  
	cd Vitis-AI

GPU Docker
Use below commands to build the GPU docker:

	cd setup/docker
	./docker_build_gpu.sh

To run the GPU docker, use command:

	#./docker_run.sh xilinx/vitis-ai-gpu:latest
	./docker_run.sh xilinx/vitis-ai-gpu:1.4.1.978

Running lspci to check that the VCK5000 Card has been installed

	lspci -vd 10ee:

An output similar to the following example is seen.

	lspci -vd 10ee:
	02:00.0 Memory controller: Xilinx Corporation Device 5044
		Subsystem: Xilinx Corporation Device 000e
		Flags: bus master, fast devsel, latency 0, IRQ 17
		Memory at b0000000 (64-bit, prefetchable) [size=128M]
		Memory at b8020000 (64-bit, prefetchable) [size=128K]
		Capabilities: <access denied>
		Kernel driver in use: xclmgmt
		Kernel modules: xclmgmt
	
	02:00.1 Memory controller: Xilinx Corporation Device 5045
		Subsystem: Xilinx Corporation Device 000e
		Flags: bus master, fast devsel, latency 0, IRQ 18
		Memory at b8000000 (64-bit, prefetchable) [size=128K]
		Memory at a0000000 (64-bit, prefetchable) [size=256M]
		Capabilities: <access denied>
		Kernel driver in use: xocl
		Kernel modules: xocl
	
verify card has been successfully programmed with BASE platform
Enter the following command:
	
	sudo /opt/xilinx/xrt/bin/xbmgmt flash --scan
	---------------------------------------------------------------------
	Deprecation Warning:
    	The given legacy sub-command and/or option has been deprecated
    	to be obsoleted in the next release.
	 
    	Further information regarding the legacy deprecated sub-commands
    	and options along with their mappings to the next generation
    	sub-commands and options can be found on the Xilinx Runtime (XRT)
    	documentation page:
	    
    	https://xilinx.github.io/XRT/master/html/xbtools_map.html
	
    	Please update your scripts and tools to use the next generation
    	sub-commands and options.
	---------------------------------------------------------------------
	Card [0000:02:00.0]
	    Card type:		vck5000-es1
	    Flash type:		OSPI_VERSAL
	    Flashable partition running on FPGA:
	        xilinx_vck5000-es1_gen3x16_base_2,[ID=0xb376430f2629b15d],[SC=4.4.6]
	    Flashable partitions installed in system:	
	        xilinx_vck5000-es1_gen3x16_base_2,[ID=0xb376430f2629b15d],[SC=4.4.6]
		
Open docker:

	#./docker_run.sh xilinx/vitis-ai-gpu:latest
	./docker_run.sh xilinx/vitis-ai-gpu:1.4.1.978
	==========================================
	 
	__      ___ _   _                   _____
	\ \    / (_) | (_)            /\   |_   _|
	 \ \  / / _| |_ _ ___ ______ /  \    | |
	  \ \/ / | | __| / __|______/ /\ \   | |
	   \  /  | | |_| \__ \     / ____ \ _| |_
	    \/   |_|\__|_|___/    /_/    \_\_____|
	 
	==========================================
	
	Docker Image Version: 2.0.0.1103   (GPU) 
	Vitis AI Git Hash: d02dcb604 
	Build Date: 2022-01-28
	
	For TensorFlow 1.15 Workflows do:
	     conda activate vitis-ai-tensorflow 
	For Caffe Workflows do:
	     conda activate vitis-ai-caffe 
	For PyTorch Workflows do:
	     conda activate vitis-ai-pytorch 
	For TensorFlow 2.6 Workflows do:
	     conda activate vitis-ai-tensorflow2 
	For Darknet Optimizer Workflows do:
	     conda activate vitis-ai-optimizer_darknet 
	For Caffe Optimizer Workflows do:
	     conda activate vitis-ai-optimizer_caffe 
	For PyTorch Optimizer Workflows do:
	     conda activate vitis-ai-optimizer_pytorch 
	For TensorFlow 1.15 Optimizer Workflows do:
	     conda activate vitis-ai-optimizer_tensorflow 
	For TensorFlow 2.6 Optimizer Workflows do:
	     conda activate vitis-ai-optimizer_tensorflow2 
	Vitis-AI /workspace >


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
