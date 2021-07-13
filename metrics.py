import cv2
import os
import numpy as np


main_img_path = os.path.expanduser(r'dataset\groundtruth_depth')
main_img_pathes = os.listdir(main_img_path)
main_img_path_e = os.path.expanduser(r'outputs/kitti/depth_for_evaluation')
main_img_pathes_e = os.listdir(main_img_path_e)

# Load Groundtruth
gt = []
for item in main_img_pathes:
    gt.append(np.asarray(cv2.imread(main_img_path + '/' + item, cv2.IMREAD_GRAYSCALE)))


# Load Results
results = []
for item in main_img_pathes_e:
    results.append(np.asarray(cv2.imread(main_img_path_e + '/' + item, cv2.IMREAD_GRAYSCALE)))


class Metrics:

    def calculate_metrics_mm(self, output, gt_item):

        valid_mask = gt_item > 0.1
        output_mm = 1e3 * output[valid_mask]
        gt_mm = 1e3 * gt_item[valid_mask]
        diff = np.abs(output_mm - gt_mm)
        mse = np.mean(np.power(diff, 2))
        rmse = np.sqrt(mse)
        mae = np.mean(diff)
        return rmse, mae

def print_metrics():
    print('Calculating Metrics ....')
    x = Metrics()
    mae = []
    rmse = []
    for i in range(len(gt)):
        _rmse, _mae = x.calculate_metrics_mm(results[i], gt[i])
        rmse.append(_rmse)
        mae.append(_mae)

    print('Evaluation Metrics : RMSE = {h1}     MAE = {h2} '.format(h1 = (np.sum(rmse)/len(rmse)), h2 = np.sum(mae)/len(mae)))



