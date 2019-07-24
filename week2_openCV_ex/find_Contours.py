#include <cstdio>
#include <opencv2/opencv.hpp>
using namespace cv;


int main(){
    Mat src = imread("/home/rachel/Documents/data/1.jpeg", CV_LOAD_IMAGE_COLOR);
    Mat src_gray = imread("/home/rachel/Documents/data/1.jpeg", CV_LOAD_IMAGE_GRAYSCALE);
    Mat contoursImg = src.clone();

    Mat edge;
    blur(src_gray, src_gray, Size(3,3));
    Canny(src_gray, edge, 50, 150, 3);

    vector<vector<Point>> contours;
    vector<Vec4i> hierarchy;
    RNG rng(12345);
    findContours(edge, contours, hierarchy, CV_RETR_TREE, CV_CHAIN_APPROX_NONE);
    for(int i = 0; i<contours.size(); i++){
        Scalar color = Scalar( rng.uniform(0, 255), rng.uniform(0, 255), 255);
        drawContours(contoursImg, contours, i, color, 2, 8, hierarchy);
    }

    imshow("origin", src);
    imshow("result", contoursImg);
    waitKey(0);

    return 0;
}

