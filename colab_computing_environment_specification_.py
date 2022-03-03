# -*- coding: utf-8 -*-
"""Colab Computing Environment Specification .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uHHLtc3rNOf5G4R5M-Jx2RI6h1HWmdBK
"""

# Separate runtime types:
# **CPU**: Central Processing Unit. Manage all the functions of a computer.
# **GPU**: Graphical Processing Unit. Enhance the graphical performance of the computer.
# **TPU**: Tensor Processing Unit. Custom build ASIC to accelerate TensorFlow projects.
# For below to work, go to 'Runtime > change runtime type > Hardware Accelerator > GPU'

# Operating System
!lsb_release -a

# list of the installed packages
#!apt list |grep 'python3'

# Python version
!python --version

# R version
!R --version

# GPU count and name
!nvidia-smi -L

#use this command to see GPU activity while doing Deep Learning tasks, for this command 'nvidia-smi'
!nvidia-smi

# CPU name
!lscpu |grep 'Model name'

# no.of sockets i.e available slots for physical processors
!lscpu | grep 'Socket(s):'

# no.of cores each processor is having 
!lscpu | grep 'Core(s) per socket:'

# no.of threads each core is having
!lscpu | grep 'Thread(s) per core'

# L3 cache
!lscpu | grep "L3 cache"

# if it had turbo boost it would've shown Min and Max MHz also but it is only showing current frequency this means it always operates at shown frequency
!lscpu | grep "MHz"

# memory that we can use
!free -h --si | awk  '/Mem:/{print $2}'

# hard disk space that we can use
!df -h / | awk '{print $4}'