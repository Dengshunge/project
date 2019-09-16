cur_dir=$(cd $( dirname ${BASH_SOURCE[0]} ) && pwd )
# caffe的路径
root_dir="/home/dengshunge/Tiny-DSOD-master"

cd $root_dir

redo=1
# 数据的根目录，与txt的文件结合
data_root_dir="/home/dengshunge/Desktop/data"
# trainval.txt和test.txt的路径
txtFileDir="/home/dengshunge/Desktop/LMDB"
# LMDB存储位置
lmdbFile="/home/dengshunge/Desktop/LMDB/lmdb"
# LMDB存储位置的软连接
lmdbLink="/home/dengshunge/Desktop/LMDB/lmdbLink"
# mapfile位置
mapfile="/home/dengshunge/Desktop/LMDB/labelmap.prototxt"
# 任务类型
anno_type="detection"
# 格式
db="lmdb"
# 图片尺寸，若width,height=0,0，说明按原始图片输入尺寸，否则resize到(width,height)
min_dim=0
max_dim=0
width=300
height=300

extra_cmd="--encode-type=jpg --encoded"
if [ $redo ]
then
  extra_cmd="$extra_cmd --redo"
fi
for subset in test trainval
do
  python3 $root_dir/scripts/create_annoset.py --anno-type=$anno_type --label-map-file=$mapfile --min-dim=$min_dim --max-dim=$max_dim --resize-width=$width --resize-height=$height --check-label $extra_cmd $data_root_dir $txtFileDir/$subset.txt $lmdbFile/$subset"_"$db $lmdbLink
done
