#!/usr/bin/env sh
# Create the imagenet lmdb inputs
# N.B. set the path to the imagenet train + val data dirs
set -e

# 生成的LMDB文件存放的位置
EXAMPLE=/home/gosuncn/Desktop/convertLMDB
# train.txt和test.txt文件放置的位置
DATA=/home/gosuncn/Desktop/convertLMDB
# caffe/build/tools的位置
TOOLS=/home/gosuncn/caffe/build/tools

# 训练集和测试集的位置，记得，最后的 '/' 不要漏了
TRAIN_DATA_ROOT=/home/gosuncn/Desktop/convertLMDB/plate_dataV6/train_data/
VAL_DATA_ROOT=/home/gosuncn/Desktop/convertLMDB/plate_dataV6/test_data/

# Set RESIZE=true to resize the images to 256x256. Leave as false if images have
# already been resized using another tool.
# 如果需要给该输入图片的大小，将RESIZE设置成true，并图片的高度和宽度
RESIZE=true
if $RESIZE; then
  RESIZE_HEIGHT=30
  RESIZE_WIDTH=120
else
  RESIZE_HEIGHT=0
  RESIZE_WIDTH=0
fi

if [ ! -d "$TRAIN_DATA_ROOT" ]; then
  echo "Error: TRAIN_DATA_ROOT is not a path to a directory: $TRAIN_DATA_ROOT"
  echo "Set the TRAIN_DATA_ROOT variable in create_imagenet.sh to the path" \
       "where the ImageNet training data is stored."
  exit 1
fi

if [ ! -d "$VAL_DATA_ROOT" ]; then
  echo "Error: VAL_DATA_ROOT is not a path to a directory: $VAL_DATA_ROOT"
  echo "Set the VAL_DATA_ROOT variable in create_imagenet.sh to the path" \
       "where the ImageNet validation data is stored."
  exit 1
fi

echo "Creating train lmdb..."

# EXAMPLE/ilsvrc12_train_lmdb中的ilsvrc12_train_lmdb为LMDB的命名，可以按需更改
# DATA/train.txt要与自己生成train.txt名字相对应，不然得更改
# test lmdb同理
GLOG_logtostderr=1 $TOOLS/convert_imageset \
    --resize_height=$RESIZE_HEIGHT \
    --resize_width=$RESIZE_WIDTH \
    --shuffle \
    $TRAIN_DATA_ROOT \
    $DATA/train.txt \
    $EXAMPLE/train_lmdb

echo "Creating test lmdb..."

GLOG_logtostderr=1 $TOOLS/convert_imageset \
    --resize_height=$RESIZE_HEIGHT \
    --resize_width=$RESIZE_WIDTH \
    --shuffle \
    $VAL_DATA_ROOT \
    $DATA/test.txt \
    $EXAMPLE/test_lmdb

echo "Done."
