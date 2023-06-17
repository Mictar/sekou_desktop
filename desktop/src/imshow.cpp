#include <opencv2/opencv.hpp>

int main(int argc, char** argv)
{
	cv::Mat frame = cv::imread( cv::String( argv[1] ) );

	cv::imshow("image", frame);

	cv::waitKey(0);

	return 0;
}
