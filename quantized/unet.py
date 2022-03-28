# GENETARED BY NNDCT, DO NOT EDIT!

import torch
import pytorch_nndct as py_nndct
class unet(torch.nn.Module):
    def __init__(self):
        super(unet, self).__init__()
        self.module_0 = py_nndct.nn.Input() #unet::input_0
        self.module_1 = py_nndct.nn.Conv2d(in_channels=3, out_channels=16, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #unet::unet/unetConv2[conv1]/Sequential[conv1]/Conv2d[0]/input.2
        self.module_3 = py_nndct.nn.ReLU(inplace=False) #unet::unet/unetConv2[conv1]/Sequential[conv1]/ReLU[2]/input.4
        self.module_4 = py_nndct.nn.Conv2d(in_channels=16, out_channels=16, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #unet::unet/unetConv2[conv1]/Sequential[conv2]/Conv2d[0]/input.5
        self.module_6 = py_nndct.nn.ReLU(inplace=False) #unet::unet/unetConv2[conv1]/Sequential[conv2]/ReLU[2]/128
        self.module_7 = py_nndct.nn.MaxPool2d(kernel_size=[2, 2], stride=[2, 2], padding=[0, 0], dilation=[1, 1], ceil_mode=True) #unet::unet/MaxPool2d[maxpool1]/input.7
        self.module_8 = py_nndct.nn.Conv2d(in_channels=16, out_channels=32, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #unet::unet/unetConv2[conv2]/Sequential[conv1]/Conv2d[0]/input.8
        self.module_10 = py_nndct.nn.ReLU(inplace=False) #unet::unet/unetConv2[conv2]/Sequential[conv1]/ReLU[2]/input.10
        self.module_11 = py_nndct.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #unet::unet/unetConv2[conv2]/Sequential[conv2]/Conv2d[0]/input.11
        self.module_13 = py_nndct.nn.ReLU(inplace=False) #unet::unet/unetConv2[conv2]/Sequential[conv2]/ReLU[2]/166
        self.module_14 = py_nndct.nn.MaxPool2d(kernel_size=[2, 2], stride=[2, 2], padding=[0, 0], dilation=[1, 1], ceil_mode=True) #unet::unet/MaxPool2d[maxpool2]/input.13
        self.module_15 = py_nndct.nn.Conv2d(in_channels=32, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #unet::unet/unetConv2[conv3]/Sequential[conv1]/Conv2d[0]/input.14
        self.module_17 = py_nndct.nn.ReLU(inplace=False) #unet::unet/unetConv2[conv3]/Sequential[conv1]/ReLU[2]/input.16
        self.module_18 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #unet::unet/unetConv2[conv3]/Sequential[conv2]/Conv2d[0]/input.17
        self.module_20 = py_nndct.nn.ReLU(inplace=False) #unet::unet/unetConv2[conv3]/Sequential[conv2]/ReLU[2]/204
        self.module_21 = py_nndct.nn.MaxPool2d(kernel_size=[2, 2], stride=[2, 2], padding=[0, 0], dilation=[1, 1], ceil_mode=True) #unet::unet/MaxPool2d[maxpool3]/input.19
        self.module_22 = py_nndct.nn.Conv2d(in_channels=64, out_channels=128, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #unet::unet/unetConv2[conv4]/Sequential[conv1]/Conv2d[0]/input.20
        self.module_24 = py_nndct.nn.ReLU(inplace=False) #unet::unet/unetConv2[conv4]/Sequential[conv1]/ReLU[2]/input.22
        self.module_25 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #unet::unet/unetConv2[conv4]/Sequential[conv2]/Conv2d[0]/input.23
        self.module_27 = py_nndct.nn.ReLU(inplace=False) #unet::unet/unetConv2[conv4]/Sequential[conv2]/ReLU[2]/242
        self.module_28 = py_nndct.nn.MaxPool2d(kernel_size=[2, 2], stride=[2, 2], padding=[0, 0], dilation=[1, 1], ceil_mode=True) #unet::unet/MaxPool2d[maxpool4]/input.25
        self.module_29 = py_nndct.nn.Conv2d(in_channels=128, out_channels=256, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #unet::unet/unetConv2[center]/Sequential[conv1]/Conv2d[0]/input.26
        self.module_31 = py_nndct.nn.ReLU(inplace=False) #unet::unet/unetConv2[center]/Sequential[conv1]/ReLU[2]/input.28
        self.module_32 = py_nndct.nn.Conv2d(in_channels=256, out_channels=256, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #unet::unet/unetConv2[center]/Sequential[conv2]/Conv2d[0]/input.29
        self.module_34 = py_nndct.nn.ReLU(inplace=False) #unet::unet/unetConv2[center]/Sequential[conv2]/ReLU[2]/280
        self.module_35 = py_nndct.nn.ConvTranspose2d(in_channels=256, out_channels=128, kernel_size=[2, 2], stride=[2, 2], padding=[0, 0], output_padding=[0, 0], groups=1, bias=True, dilation=[1, 1]) #unet::unet/unetUp[up_concat4]/ConvTranspose2d[up]/290
        self.module_36 = py_nndct.nn.Cat() #unet::unet/unetUp[up_concat4]/input.31
        self.module_37 = py_nndct.nn.Conv2d(in_channels=256, out_channels=128, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #unet::unet/unetUp[up_concat4]/unetConv2[conv]/Sequential[conv1]/Conv2d[0]/input.32
        self.module_38 = py_nndct.nn.ReLU(inplace=False) #unet::unet/unetUp[up_concat4]/unetConv2[conv]/Sequential[conv1]/ReLU[1]/input.33
        self.module_39 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #unet::unet/unetUp[up_concat4]/unetConv2[conv]/Sequential[conv2]/Conv2d[0]/input.34
        self.module_40 = py_nndct.nn.ReLU(inplace=False) #unet::unet/unetUp[up_concat4]/unetConv2[conv]/Sequential[conv2]/ReLU[1]/315
        self.module_41 = py_nndct.nn.ConvTranspose2d(in_channels=128, out_channels=64, kernel_size=[2, 2], stride=[2, 2], padding=[0, 0], output_padding=[0, 0], groups=1, bias=True, dilation=[1, 1]) #unet::unet/unetUp[up_concat3]/ConvTranspose2d[up]/325
        self.module_42 = py_nndct.nn.Cat() #unet::unet/unetUp[up_concat3]/input.35
        self.module_43 = py_nndct.nn.Conv2d(in_channels=128, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #unet::unet/unetUp[up_concat3]/unetConv2[conv]/Sequential[conv1]/Conv2d[0]/input.36
        self.module_44 = py_nndct.nn.ReLU(inplace=False) #unet::unet/unetUp[up_concat3]/unetConv2[conv]/Sequential[conv1]/ReLU[1]/input.37
        self.module_45 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #unet::unet/unetUp[up_concat3]/unetConv2[conv]/Sequential[conv2]/Conv2d[0]/input.38
        self.module_46 = py_nndct.nn.ReLU(inplace=False) #unet::unet/unetUp[up_concat3]/unetConv2[conv]/Sequential[conv2]/ReLU[1]/350
        self.module_47 = py_nndct.nn.ConvTranspose2d(in_channels=64, out_channels=32, kernel_size=[2, 2], stride=[2, 2], padding=[0, 0], output_padding=[0, 0], groups=1, bias=True, dilation=[1, 1]) #unet::unet/unetUp[up_concat2]/ConvTranspose2d[up]/360
        self.module_48 = py_nndct.nn.Cat() #unet::unet/unetUp[up_concat2]/input.39
        self.module_49 = py_nndct.nn.Conv2d(in_channels=64, out_channels=32, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #unet::unet/unetUp[up_concat2]/unetConv2[conv]/Sequential[conv1]/Conv2d[0]/input.40
        self.module_50 = py_nndct.nn.ReLU(inplace=False) #unet::unet/unetUp[up_concat2]/unetConv2[conv]/Sequential[conv1]/ReLU[1]/input.41
        self.module_51 = py_nndct.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #unet::unet/unetUp[up_concat2]/unetConv2[conv]/Sequential[conv2]/Conv2d[0]/input.42
        self.module_52 = py_nndct.nn.ReLU(inplace=False) #unet::unet/unetUp[up_concat2]/unetConv2[conv]/Sequential[conv2]/ReLU[1]/385
        self.module_53 = py_nndct.nn.ConvTranspose2d(in_channels=32, out_channels=16, kernel_size=[2, 2], stride=[2, 2], padding=[0, 0], output_padding=[0, 0], groups=1, bias=True, dilation=[1, 1]) #unet::unet/unetUp[up_concat1]/ConvTranspose2d[up]/395
        self.module_54 = py_nndct.nn.Cat() #unet::unet/unetUp[up_concat1]/input.43
        self.module_55 = py_nndct.nn.Conv2d(in_channels=32, out_channels=16, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #unet::unet/unetUp[up_concat1]/unetConv2[conv]/Sequential[conv1]/Conv2d[0]/input.44
        self.module_56 = py_nndct.nn.ReLU(inplace=False) #unet::unet/unetUp[up_concat1]/unetConv2[conv]/Sequential[conv1]/ReLU[1]/input.45
        self.module_57 = py_nndct.nn.Conv2d(in_channels=16, out_channels=16, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #unet::unet/unetUp[up_concat1]/unetConv2[conv]/Sequential[conv2]/Conv2d[0]/input.46
        self.module_58 = py_nndct.nn.ReLU(inplace=False) #unet::unet/unetUp[up_concat1]/unetConv2[conv]/Sequential[conv2]/ReLU[1]/input
        self.module_59 = py_nndct.nn.Conv2d(in_channels=16, out_channels=2, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #unet::unet/Conv2d[final]/430

    def forward(self, *args):
        self.output_module_0 = self.module_0(input=args[0])
        self.output_module_1 = self.module_1(self.output_module_0)
        self.output_module_3 = self.module_3(self.output_module_1)
        self.output_module_4 = self.module_4(self.output_module_3)
        self.output_module_6 = self.module_6(self.output_module_4)
        self.output_module_7 = self.module_7(self.output_module_6)
        self.output_module_8 = self.module_8(self.output_module_7)
        self.output_module_10 = self.module_10(self.output_module_8)
        self.output_module_11 = self.module_11(self.output_module_10)
        self.output_module_13 = self.module_13(self.output_module_11)
        self.output_module_14 = self.module_14(self.output_module_13)
        self.output_module_15 = self.module_15(self.output_module_14)
        self.output_module_17 = self.module_17(self.output_module_15)
        self.output_module_18 = self.module_18(self.output_module_17)
        self.output_module_20 = self.module_20(self.output_module_18)
        self.output_module_21 = self.module_21(self.output_module_20)
        self.output_module_22 = self.module_22(self.output_module_21)
        self.output_module_24 = self.module_24(self.output_module_22)
        self.output_module_25 = self.module_25(self.output_module_24)
        self.output_module_27 = self.module_27(self.output_module_25)
        self.output_module_28 = self.module_28(self.output_module_27)
        self.output_module_29 = self.module_29(self.output_module_28)
        self.output_module_31 = self.module_31(self.output_module_29)
        self.output_module_32 = self.module_32(self.output_module_31)
        self.output_module_34 = self.module_34(self.output_module_32)
        self.output_module_35 = self.module_35(self.output_module_34)
        self.output_module_36 = self.module_36(dim=1, tensors=[self.output_module_27,self.output_module_35])
        self.output_module_37 = self.module_37(self.output_module_36)
        self.output_module_38 = self.module_38(self.output_module_37)
        self.output_module_39 = self.module_39(self.output_module_38)
        self.output_module_40 = self.module_40(self.output_module_39)
        self.output_module_41 = self.module_41(self.output_module_40)
        self.output_module_42 = self.module_42(dim=1, tensors=[self.output_module_20,self.output_module_41])
        self.output_module_43 = self.module_43(self.output_module_42)
        self.output_module_44 = self.module_44(self.output_module_43)
        self.output_module_45 = self.module_45(self.output_module_44)
        self.output_module_46 = self.module_46(self.output_module_45)
        self.output_module_47 = self.module_47(self.output_module_46)
        self.output_module_48 = self.module_48(dim=1, tensors=[self.output_module_13,self.output_module_47])
        self.output_module_49 = self.module_49(self.output_module_48)
        self.output_module_50 = self.module_50(self.output_module_49)
        self.output_module_51 = self.module_51(self.output_module_50)
        self.output_module_52 = self.module_52(self.output_module_51)
        self.output_module_53 = self.module_53(self.output_module_52)
        self.output_module_54 = self.module_54(dim=1, tensors=[self.output_module_6,self.output_module_53])
        self.output_module_55 = self.module_55(self.output_module_54)
        self.output_module_56 = self.module_56(self.output_module_55)
        self.output_module_57 = self.module_57(self.output_module_56)
        self.output_module_58 = self.module_58(self.output_module_57)
        self.output_module_59 = self.module_59(self.output_module_58)
        return self.output_module_59
