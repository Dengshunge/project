import os
import random
import cv2

dic_path = '/home/dengshunge/Desktop/data'
save_path = '/home/dengshunge/Desktop'

res = []
for dic in os.listdir(dic_path):
    file_path = os.path.join(dic_path, dic)
    for file in os.listdir(file_path):
        if file[-3:]!='jpg':
            continue
        img_path = os.path.join(dic,file)
        xml_path = os.path.join(dic,'标注信息','导出结果',file[:-3]+'xml')
        res.append([img_path,xml_path])

random.shuffle(res)
train_list = res[:int(len(res)*0.8)]
val_list = res[int(len(res)*0.8):]
train_list.sort()
val_list.sort()

with open(os.path.join(save_path,'trainval.txt'),'w') as f:
    for row in train_list:
        tmp = ' '.join(row)+'\n'
        f.write(tmp)

with open(os.path.join(save_path,'test.txt'),'w') as f:
    for row in val_list:
        tmp = ' '.join(row)+'\n'
        f.write(tmp)

with open(os.path.join(save_path,'test_name_size.txt'),'w') as f:
    for name,_ in val_list:
        img_path = os.path.join(dic_path,name)
        img = cv2.imread(img_path)
        height,width,_=img.shape

        name1 = name.split('/')[-1].split('.jpg')[0]
        tmp = name1 + ' ' + str(height) + ' ' + str(width) + '\n'
        f.write(tmp)
