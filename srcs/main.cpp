#include "my_lib.h"



/* main */
int main(int argc, const char* argv[]) 
{
    MatrixXd m(2,2);
    m(0,0) = 3;
    m(1,0) = 2.5;
    m(0,1) = -1;
    m(1,1) = m(1,0) + m(0,1);
    std::cout << "eigen3 m: \n" << m << std::endl;

    at::Tensor zz = torch::rand({3, 3});
     /**********************/
    double t = (double)getTickCount();
    Mat results = tensorToMat(zz);
    t = (double)cv::getTickCount() - t;
    cout<<"point execution time ="<<setprecision(4) << t / getTickFrequency()<<"s\n";  //  cout.width(6); //设置输出宽度

    /**********************/
    zz = torch::ones({3, 3})+3;
    zz = zz.to(at::kInt);
    Mat m_results;

    t = (double)getTickCount();
    tensor2Mat(zz, m_results);
    t = (double)cv::getTickCount() - t;
    cout<<"execution time ="<<setprecision(4) << t / getTickFrequency()<<"s\n";
    cout<<" results: \n"<< setprecision(4) << m_results <<endl;

    //计算最大值和最小值
    double minv = 0.0, maxv = 0.0;
    minMaxIdx(m_results,  &minv, &maxv);
    cout<<"results max: "<< maxv <<" results min: "<< minv <<endl;


    //计算均值和方差
    Scalar  mean , std;
    meanStdDev(m_results,  mean, std);
    double mean_pxl = mean.val[0];
    double stddev_pxl = std.val[0];
    cout<<"results max: "<< mean_pxl <<"\nresults std: "<< stddev_pxl <<endl;


    string img_path = "./test_image.jpg";
    at::Tensor m_result =  MatToTensor(img_path);
    cout<< m_result.sizes()<<endl;
//    cout<< m_result.slice(0,0,1).slice(1,0,6).slice(2,0,1)<<endl;

    return 0;
}

