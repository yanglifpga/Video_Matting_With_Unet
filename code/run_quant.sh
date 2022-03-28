# Copyright 2019 Xilinx Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


export PYTHONPATH=${PWD}:${PYTHONPATH}
export W_QUANT=1

CUDA_VISIBLE_DEVICES='0' python test/test.py  \
        --data_root '../data/Chaos/Train_Sets/CT/' \
        --input_size 512,512 \
        --weight '../float/ChaosCT_0.9770885167.pth' \
        --quant_mode calib

CUDA_VISIBLE_DEVICES='0' python test/test.py  \
        --data_root '../data/Chaos/Train_Sets/CT/' \
        --input_size 512,512 \
        --weight '../float/ChaosCT_0.9770885167.pth' \
        --quant_mode test

echo "dump xmodel"
CUDA_VISIBLE_DEVICES='0' python test/test.py  \
        --dump_xmodel \
        --data_root '../data/Chaos/Train_Sets/CT/' \
        --input_size 512,512 \
        --weight '../float/ChaosCT_0.9770885167.pth' \
        --quant_mode test


