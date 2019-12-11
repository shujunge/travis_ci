//
// Created by zf on 2019/12/4.
//

#ifndef TENSOR_MAT_MY_LIB_H
#define TENSOR_MAT_MY_LIB_H

#include <torch/script.h>
#include <torch/torch.h>
#include <opencv2/opencv.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <Eigen/Dense> /* 使用c++的eigen矩阵库*/
#include <iostream>
#include <memory>
#include <string>
#include <vector>

using namespace cv;
using namespace std;
using namespace Eigen;

extern int my_add(int x,int y);
/**
 *
 * @param one_heat_map at::tensor (H,W)
 * @return cv::Mat (H,W)
 */
extern  Mat tensorToMat(const at::Tensor &one_heat_map);


/**
 *
 * @param t :  at::tensor (H,W) float32
 * @param image: cv::Mat (H,W)
 */

extern void tensor2Mat(at::Tensor &t, Mat &image);

/***
 *
 * @param path  type:string   image path
 * @return type: at::Tensor  (1, H, W, C)
 */
extern at::Tensor MatToTensor(string path);

#endif //TENSOR_MAT_MY_LIB_H
