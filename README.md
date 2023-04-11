# Rotation-invariant-deep-pointcloud-analysis


#### Code for the ICCV 2021 paper: [A-closer-look-at-rotation-invariant-deep-pointcloud-analysis](https://openaccess.thecvf.com/content/ICCV2021/html/Li_A_Closer_Look_at_Rotation-Invariant_Deep_Point_Cloud_Analysis_ICCV_2021_paper.html).

##### Authors: [Feiran Li](https://sites.google.com/view/feiranlihomepage/home), [Kent Fujiwara](https://kfworks.com/), [Fumio Okura](http://cvl.ist.osaka-u.ac.jp/user/okura/), and [Yasuyuki Matsushita](http://cvl.ist.osaka-u.ac.jp/en/member/matsushita/)




![Teaser](teaser.png)



### 1. Environment
The provide codes have been tested with Pytorch-1.6.0 on a Tesla-V100.


### 1. Run the code
1. Download the PCA-processed datasets ([ModelNet40](https://drive.google.com/file/d/1-DrgEU8vO17SXpU-Aio0S4Ap-rAEdiAU/view?usp=share_link), [ShapeNet-PartSeg](https://drive.google.com/file/d/1-6PkQsGy1_ao0FJ2JT0g3kcW6PPotK5U/view?usp=share_link), and [ScanObjectNN](https://drive.google.com/file/d/1-GN-GIja4c8KaSrLiV19q8vnzoAGHH4m/view?usp=share_link)) and unzip them to the `dataset` folder. 
2. Note that the `ScanObjectNN` dataset is originally provided [here](https://hkust-vgd.github.io/scanobjectnn/). Please pay attention to citation.
3. Run respective `*_test.ipynb` to test the pretrained model and `*_train.ipynb` to train from scratch.
4. If you want to generate the 24 ambiguities of your own dataset, please see the `generate_24_pca_poses.py` script.



### 3. Contact
Please feel free to raise an issue or email to [li.feiran@ist.osaka-u.ac.jp](li.feiran@ist.osaka-u.ac.jp) if you have any question regarding the paper or any suggestions for further improvements. 


### 4. Citation
If you find this code helpful, thanks for citing our work as
```
@inproceedings{li2021rotinv,
title = {A Closer Look at Rotation-invariant Deep Point Cloud Analysis},
author = {Feiran Li and Kent Fujiwara and Fumio Okura and Yasuyuki Matsushita},
booktitle = {IEEE/CVF International Conference on Computer Vision (ICCV)},
year = {2021}
}
