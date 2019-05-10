import os
import shutil
import random

'''
**********注意*********
由于每个模块是单独写的，所以参数设置很笨，需要手改
建议每个模块单独使用，即把不需要的模块给注释
记得修改每个模块里面的路径
'''

# # 整理和复制文件
# path = r'C:\Users\dengshunge\Desktop\生成数据集\生成的数据集'
# ToRestore_train = r'C:\Users\dengshunge\Desktop\plate_dataV6\train_data'
# ToRestore_test = r'C:\Users\dengshunge\Desktop\plate_dataV6\test_data'
# # subPath = ['ao_plate','black_plate','doubleYellow_plate','gang_plate','jing_plate','lingshiguan_plate','newEnergy_plate','nongyong_plate']
# subPath = ['nongyong_plate']
# fileNumber_train = 35
# fileNumber_test = 13
# for s in subPath:
#     path1 = os.path.join(path, s)
#     ToRestore_train1 = os.path.join(ToRestore_train, s)
#     ToRestore_test1 = os.path.join(ToRestore_test, s)
#     if not os.path.exists(path) or not os.path.exists(ToRestore_train1) or not os.path.exists(ToRestore_test1):
#         raise Exception("文件夹不存在")
#     files = []
#     files = os.listdir(path1)
#     random.shuffle(files)
#     if fileNumber_train >= 5000:
#         break
#     for i in range(5000-fileNumber_train):
#         di = os.path.join(path1, files[i])
#         shutil.copy(di, ToRestore_train1)
#     if fileNumber_test >=1200:
#         break
#     for i in range(5000-fileNumber_train,5000-fileNumber_train+1200-fileNumber_test):
#         di = os.path.join(path1, files[i])
#         shutil.copy(di, ToRestore_test1)



# #为每个文件改名
# ToRename_train = r'C:\Users\dengshunge\Desktop\plate_dataV6\train_data'
# ToRename_test = r'C:\Users\dengshunge\Desktop\plate_dataV6\test_data'
# # subDict为子目录的文件夹名，需要手动填写
# subDict = ['ao_plate','black_plate','blue_plate','doubleYellow_plate','gang_plate','gua_plate','jiaolian_plate','jing_plate','lingshiguan_plate','newEnergy_plate','nongyong_plate','yellow_plate']
# for i in range(len(subDict)):
#     ToRename_train1 = os.path.join(ToRename_train,subDict[i])
#     ToRename_test1 = os.path.join(ToRename_test,subDict[i])
#     if not os.path.exists(ToRename_train1) or not os.path.exists(ToRename_test1):
#         raise Exception('ERROR')
#     files_train = list(os.listdir(ToRename_train1))
#     random.shuffle(files_train)
#     files_test = list(os.listdir(ToRename_test1))
#     random.shuffle(files_test)
#     for s in range(len(files_train)):
#         oldname = os.path.join(ToRename_train1,files_train[s])
#         # newname为新的文件名
#         newname = ToRename_train1+'\\newname_train_'+str(s)+'.jpg'
#         os.rename(oldname,newname)
#     for s in range(len(files_test)):
#         oldname = os.path.join(ToRename_test1,files_test[s])
#         # newname为新的文件名
#         newname = ToRename_test1+'\\newname_test_'+str(s)+'.jpg'
#         os.rename(oldname,newname)



# 形成train和test.txt文件
# 需要更换path和restoreFile
# path为test_data或者train_data文件夹
train_path = r'C:\Users\dengshunge\Desktop\plate_dataV6\train_data'
test_path = r'C:\Users\dengshunge\Desktop\plate_dataV6\test_data'
# 文件夹下的子目录名称
subPath = ['ao_plate','black_plate','blue_plate','doubleYellow_plate','gang_plate','gua_plate','jiaolian_plate','jing_plate','lingshiguan_plate','newEnergy_plate','nongyong_plate','yellow_plate']
# 生成的train.txt或者test.txt存放的位置
restoreFile = r'C:\Users\dengshunge\Desktop'
# 生成train.txt
for i in range(len(subPath)):
    train_path1 = os.path.join(train_path,subPath[i])
    if not os.path.exists(train_path1):
        raise Exception('error')
    restoreFile_train = os.path.join(restoreFile,'train.txt')
    with open(restoreFile_train,'a') as f:
        files = os.listdir(train_path1)
        for s in files:
            f.write(os.path.join(subPath[i],s)+' '+str(i)+'\n')
# 生成test.txt
for i in range(len(subPath)):
    test_path1 = os.path.join(test_path,subPath[i])
    if not os.path.exists(test_path1):
        raise Exception('error')
    restoreFile_test = os.path.join(restoreFile,'test.txt')
    with open(restoreFile_test,'a') as f:
        files = os.listdir(test_path1)
        for s in files:
            f.write(os.path.join(subPath[i],s)+' '+str(i)+'\n')





