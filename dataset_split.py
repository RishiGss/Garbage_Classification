import os
import random
import shutil
import numpy as np

root_dir="Garbage_classification_data"

train_dir="train_val_test/train"
valid_dir="train_val_test/valid"
test_dir="train_val_test/test"

os.makedirs(train_dir)
os.makedirs(valid_dir)
os.makedirs(test_dir)

for i in os.listdir(root_dir):
    os.makedirs(os.path.join(train_dir,i))
    os.makedirs(os.path.join(valid_dir,i))
    os.makedirs(os.path.join(test_dir,i))
    
    total=len(os.listdir(os.path.join(root_dir,i)))
    class_imgs=os.listdir(os.path.join(root_dir,i))
    #train=random.sample(class_imgs,int(total*0.70))
    train=random.sample(class_imgs,int(total*0.80))
    valid_test=[x for x in class_imgs if x not in train]
    valid=random.sample(valid_test,int(len(valid_test)*0.50))
    test=[x for x in valid_test if x not in valid]

    for img in train:
        shutil.copyfile(os.path.join(root_dir,i,img),os.path.join(train_dir,i,img))

    for img in valid:
        shutil.copyfile(os.path.join(root_dir,i,img),os.path.join(valid_dir,i,img))

    for img in test:
        shutil.copyfile(os.path.join(root_dir,i,img),os.path.join(test_dir,i,img))

    print(i,"completed")

print("\nSUCCESS...!!!")
    
