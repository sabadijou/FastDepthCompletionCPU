import design_depth_map
import numpy as np
import cv2
import os


class DepthCompletion:

    def __init__(self):

        self.main_img_path = os.path.expanduser(r'dataset\kitti_validation_cropped\image')
        self.input_depth_dir = os.path.expanduser(r'dataset\kitti_validation_cropped\velodyne_raw')
        self.img_size = (450, 130)
    def save_for_evaluation(self, sufficient_depth, img_name):

        path = r'outputs/kitti/depth_for_evaluation/'
        cv2.imwrite(path + img_name, sufficient_depth)

    def save_final_outputs(self, img, img_name):

        path = r'outputs/kitti/final_output/'
        img = cv2.applyColorMap(np.uint8(img / np.amax(img) * 255), cv2.COLORMAP_JET)
        cv2.imwrite(path + img_name, img)


    def process(self):

        main_img_pathes = os.listdir(self.main_img_path)
        main_image_list = []
        for item in main_img_pathes:
            main_image_list.append(cv2.imread(self.main_img_path + '/' + item))
        img_pathes = os.listdir(self.input_depth_dir)
        image_list = []
        for item in img_pathes:
            image_list.append(cv2.imread(self.input_depth_dir + '/' + item, cv2.IMREAD_ANYDEPTH))
        num_images = len(image_list)
        for i in range(num_images):
            depth_image = image_list[i]
            main_image = main_image_list[i]
            projected_depths = np.float32(depth_image / 255.0)
            final_depths, process_dict = design_depth_map.create_map(main_image,
                                                                     projected_depths,
                                                                     show_process=True)
            self.show_result(process_dict, main_image)
            self.save_for_evaluation(process_dict['s9_depths_out'], img_pathes[i])
            self.save_final_outputs(process_dict['s9_depths_out'], img_pathes[i])
        import metrics
        metrics.print_metrics()
    def show_image(self, window_name, image, size_wh=None, location_xy=None):

        if size_wh is not None:
            cv2.namedWindow(window_name,
                            cv2.WINDOW_KEEPRATIO | cv2.WINDOW_GUI_NORMAL)
            cv2.resizeWindow(window_name, *size_wh)
        else:
            cv2.namedWindow(window_name, cv2.WINDOW_AUTOSIZE)

        if location_xy is not None:
            cv2.moveWindow(window_name, *location_xy)
        cv2.imshow(window_name, image)


    def show_result(self, process_dict, main_image):

        x_offset = self.img_size[0]
        y_offset = self.img_size[1]
        x_padding = 0
        y_padding = 28
        x_start = 0
        y_start = 100
        img_x = x_start
        img_y = y_start
        max_x = 1500
        row_idx = 0
        for key, value in process_dict.items():
            if key == 'main_image' :
                image_jet = main_image
                self.show_image(
                    key, image_jet,
                    self.img_size, (img_x, img_y))
                img_x += x_offset + x_padding
                if (img_x + x_offset + x_padding) > max_x:
                    img_x = x_start
                    row_idx += 1
                img_y = y_start + row_idx * (y_offset + y_padding)
            else:
                image_jet = cv2.applyColorMap(
                    np.uint8(value / np.amax(value) * 255),
                    cv2.COLORMAP_JET)
                self.show_image(
                    key, image_jet,
                    self.img_size, (img_x, img_y))
                img_x += x_offset + x_padding
                if (img_x + x_offset + x_padding) > max_x:
                    img_x = x_start
                    row_idx += 1
                img_y = y_start + row_idx * (y_offset + y_padding)
        cv2.waitKey(delay=1)



if __name__ == '__main__':
    depth = DepthCompletion()
    depth.process()
