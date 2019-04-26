第一步:先执行get_personxml.py  得到只有人的xml
第二步:执行get_peosonimage.py将对应的图片移动（剪切）到相应的地方
第三步：执行creat_list.sh  生成 trian.txt ,test.txt 
第四步：执行creat_data.sh 生成 lmdb

不同的数据集锚点不一样要重新计算 
gen_anchors.py
