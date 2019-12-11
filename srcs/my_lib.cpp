//
// Created by zf on 2019/12/4.
//

#include "my_lib.h"

int my_add(int x,int y)
{
  return x+y;
}
/**
 *
 * @param one_heat_map at::tensor (H,W)
 * @return cv::Mat (H,W)
 */
Mat tensorToMat(const at::Tensor &one_heat_map)
{
    //one_heat_map pytorch tensor:(H,W)
    Mat result(one_heat_map.size(0), one_heat_map.size(1), CV_32FC1);

    for( int i = 0; i < one_heat_map.size(0); ++i )
    {
        for(int j=0;j<one_heat_map.size(1);j++)
        {
            result.at<float>(i,j)=one_heat_map[i][j].item<float>();
        }
    }
    return result;
}

/**
 *
 * @param t :  at::tensor (H,W) float32
 * @param image: cv::Mat (H,W)
 */
void tensor2Mat(at::Tensor &t, Mat &image) {
    image = Mat(t.sizes()[0], t.sizes()[1], CV_32FC1, t.data_ptr());
    image.convertTo(image, CV_8UC1);
}


/***
 *
 * @param path  type:string   image path
 * @return type: at::Tensor  (1, H, W, C)
 */
at::Tensor MatToTensor(string path)
{
    // load image with opencv
    cv::Mat image = cv::imread(path);
    cv::cvtColor(image, image, CV_BGR2RGB);

    cv::Mat img_float;
    cv::resize(image, img_float, cv::Size(512, 512));

    at::Tensor img_tensor = torch::from_blob(img_float.data, {1, img_float.rows, img_float.cols, 3}, at::kByte);
    img_tensor = img_tensor.to(at::kFloat);
    return img_tensor;
}
