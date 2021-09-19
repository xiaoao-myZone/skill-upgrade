cv.imread(path,model):灰度读取一个图片
	1.cv.IMREAD_COLOR:忽略透明度
	2.cv.IMREAD_GRAYSCALE:转化为灰度图读取，可以以0代替
	3.cv.IMREAD_UNCHANGED:无损读入一张图片

cv.imshow(name,img):展示图片

cv.imwrite(path,img):保存图片

cv.waitKey():
	1.一般参数设置为0，即无限等待按键输入，并返回按键ASCⅡ码值
 	  其单位为ms，在视频播放中其实代表着帧更新的速度，如果是调
	  用摄像头，设为0，只会永远停留在第一帧，设为1最流畅；然而
	  如果是播放视频文件，文件的帧数是一定的，参数越大，播放越
	  慢，通常25ms为宜。

	2.如果规定时间没有按下，那么返回-1
	###3.如果是64位系统，获取其返回值需要设为k = cv.waitKey(0) & 0xFF


cv.destroyAllWindows():
	1.不带参数，关闭所有图片窗口，带窗口名字可以关闭指定窗口

cv.namedWindow():可以提前开一个窗口

	1.第一个为窗口名称参数，第二个为选择是否可拉伸窗口
	  默认cv.WINDOW_AUTOSIZE(不可拉伸)，cv.WINDOW_NORMAL(可拉伸)


#############################################################################
cv.VideoCapture():#程序报错许确定摄像头能否在其他程序中正常工作

	1.其中的参数为设备索引号或者视频文件，一般笔记本自带摄像头参数为0

	其返回对象cap = cv.VideoCapture(0)
	cap.read()返回一个布尔值，通常用来检查视频文件是否结束，与一帧图像。
	cap.isOpened()防止cap.read()因为没有初始化摄像头出错，如果结果为False,需要用
	cap.open()

	##获取视频的信息
	cap.get(propId) 0~18分别代表视频的19种信息,并且可以通过
	cap.set(propId,value)修改
		0 - cv.CAP_PROP_POS_MSEC  	       该帧的时间，单位毫秒
		1 - cv.CAP_PROP_POS_FRAMES 	       该帧的序号(从1开始)
		2 - cv.CAP_PROP_POS_AVI_RATIO  	       该帧相对位置(0~1)
		3 - cv.CAP_PROP_FRAME_WIDTH            宽度
		4 - cv.CAP_PROP_FRAME_HEIGHT           高度
		5 - cv.CAP_PROP_FPS  		       帧率
		6 - cv.CAP_PROP_FOURCC  	       Four-Character Codes 是一种独立标示视频数据流格式的四字符代码
		7 - CAP_PROP_FRAME_COUNT 
		8 - cv.CAP_PROP_FORMAT  
		9 - cv.CAP_PROP_MODE  
	       10 - cv.CAP_PROP_CONTRAST   
	       11 - cv.CAP_PROP_SATURATION  
	       12 - cv.CAP_PROP_HUE Hue  
	       13 - cv.CAP_PROP_GAIN  
	       14 - cv.CAP_PROP_EXPOSURE  
	       15 - cv.CAP_PROP_CONVERT_RGB  
	       16 - cv.CAP_PROP_WHITE_BALANCE 
	       17 - cv.CAP_PROP_RECTIFICATION 
	       18 - cv.CAP_PROP_POS_FRAMES
	       19 - cv.CAP_PROP_POS_FRAMES


out = cv.VideoWrite(path,int_fourcc,fps,(w,h),bool(isColor))
								#若编码器代号为 -1，则运行时会弹出一个编码器选择框.
								#isColor只在windows下支持
out.write(frame)
其中
fourcc = cv.VideoWriter_fourcc(*'XVID')#python3版本

		I420(适合处理大文件) -> .avi
		PIMI -> .avi
		XVID -> .avi
		MJPG -> .avi & .mp4
		THEO -> .ogv
		FLV1(flash video, 流媒体视频) -> .flv

	

##################################################################################
Sobel()



cornerHarris(img,blockSize,ksize,k)

	img必须是float32（灰度？），可以使用np.float32(img)转换
	blockSize - 角点检测中要考虑的领域大小。
	ksize - Sobel 求导中使用的窗口大小
	k - Harris 角点检测方程中的自由参数，取值参数为 [0,04，0.06].
	