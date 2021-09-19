1.创建背景生成算子:
	fgbg = cv.createBackgroundSubtractorMOG2()

2.分析每一帧图像:
	fgmask = fgbg.apply(frame) #得到一个前景灰度图，第一次分析得到的是空白图
	_,fgmask = cv.threshold(fgmask,30,0xff,cv.THRESH_BINARY) #将前景图二值化
	
	还可以对图像进行腐蚀cv.erode()和膨胀运算cv.dilate()
	
	
	
	bgImage = fgbg.getBackgroundImage()#获取背景图
	"值的说的是，fgbg每分析一次图片会将该图片部分信息记忆下来，所以背景图会慢慢变清晰"

	bin,cnts,_=cv.findContours(fgmask.copy(),cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
	#

	对cnts中的每一个轮廓特征i
		area  =cv.contourArea(i)#求取轮廓的面积
			定一个值域，删除干扰

		rect = cv.boundingRect(i)#获取最小内接矩形（不旋转）参数

			minAreaRect = cv.minAreaRect(i)
			rect = cv.boxPoints(minAreaRect)#获取真正意义上的最小内接矩形
		
	i是一个array三维矩阵，但是用二维就可以表示了，最基本的元素是一对平面坐标
		

	