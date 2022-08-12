# Image Processing for Basic Depth Completion (IP-Basic)
Paper title: In Defense of Classical Image Processing: Fast Depth Completion on the CPU

Abstract: 
With the rise of data driven deep neural networks
as a realization of universal function approximators, most
research on computer vision problems has moved away from
hand crafted classical image processing algorithms. This paper
shows that with a well designed algorithm, we are capable of
outperforming neural network based methods on the task of
depth completion. The proposed algorithm is simple and fast,
runs on the CPU, and relies only on basic image processing
operations to perform depth completion of sparse LIDAR
depth data. We evaluate our algorithm on the challenging
KITTI depth completion benchmark [1], and at the time of
submission, our method ranks f irst on the KITTI test server
among all published methods. Furthermore, our algorithm is
data independent, requiring no training data to perform the
task at hand.

Depth Completion using classical image processing methods like morophology.      
##
- Paper : [arXiv page](https://arxiv.org/abs/1802.00036)
- Main repository : [Github](https://github.com/kujason/ip_basic)
- Presentation File : [Powerpoint](https://github.com/sabadijou/FastDepthCompletionCPU/blob/master/ReadMe/Presentation.pptx)
- Presentation File : [PDF](https://github.com/sabadijou/FastDepthCompletionCPU/blob/master/ReadMe/Presentation.pdf)
##
![Final Output](https://github.com/sabadijou/FastDepthCompletionCPU/blob/master/ReadMe/all_results.png)
##
 
# Setup
- Clone the repository with following command :
```
git clone https://github.com/sabadijou/FastDepthCompletionCPU.git
```
- Download dataset from below :
```
http://www.cvlibs.net/download.php?file=data_depth_selection.zip
```
- Extract downloaded file and copy contents of "Kitti\depth\depth_selection\val_selection_cropped " directory to the "dataset\kitti_validation_cropped"
- Run main.py

