cv.imread(path,model):�Ҷȶ�ȡһ��ͼƬ
	1.cv.IMREAD_COLOR:����͸����
	2.cv.IMREAD_GRAYSCALE:ת��Ϊ�Ҷ�ͼ��ȡ��������0����
	3.cv.IMREAD_UNCHANGED:�������һ��ͼƬ

cv.imshow(name,img):չʾͼƬ

cv.imwrite(path,img):����ͼƬ

cv.waitKey():
	1.һ���������Ϊ0�������޵ȴ��������룬�����ذ���ASC����ֵ
 	  �䵥λΪms������Ƶ��������ʵ������֡���µ��ٶȣ�����ǵ�
	  ������ͷ����Ϊ0��ֻ����Զͣ���ڵ�һ֡����Ϊ1��������Ȼ��
	  ����ǲ�����Ƶ�ļ����ļ���֡����һ���ģ�����Խ�󣬲���Խ
	  ����ͨ��25msΪ�ˡ�

	2.����涨ʱ��û�а��£���ô����-1
	###3.�����64λϵͳ����ȡ�䷵��ֵ��Ҫ��Ϊk = cv.waitKey(0) & 0xFF


cv.destroyAllWindows():
	1.�����������ر�����ͼƬ���ڣ����������ֿ��Թر�ָ������

cv.namedWindow():������ǰ��һ������

	1.��һ��Ϊ�������Ʋ������ڶ���Ϊѡ���Ƿ�����촰��
	  Ĭ��cv.WINDOW_AUTOSIZE(��������)��cv.WINDOW_NORMAL(������)


#############################################################################
cv.VideoCapture():#���򱨴���ȷ������ͷ�ܷ���������������������

	1.���еĲ���Ϊ�豸�����Ż�����Ƶ�ļ���һ��ʼǱ��Դ�����ͷ����Ϊ0

	�䷵�ض���cap = cv.VideoCapture(0)
	cap.read()����һ������ֵ��ͨ�����������Ƶ�ļ��Ƿ��������һ֡ͼ��
	cap.isOpened()��ֹcap.read()��Ϊû�г�ʼ������ͷ����������ΪFalse,��Ҫ��
	cap.open()

	##��ȡ��Ƶ����Ϣ
	cap.get(propId) 0~18�ֱ������Ƶ��19����Ϣ,���ҿ���ͨ��
	cap.set(propId,value)�޸�
		0 - cv.CAP_PROP_POS_MSEC  	       ��֡��ʱ�䣬��λ����
		1 - cv.CAP_PROP_POS_FRAMES 	       ��֡�����(��1��ʼ)
		2 - cv.CAP_PROP_POS_AVI_RATIO  	       ��֡���λ��(0~1)
		3 - cv.CAP_PROP_FRAME_WIDTH            ���
		4 - cv.CAP_PROP_FRAME_HEIGHT           �߶�
		5 - cv.CAP_PROP_FPS  		       ֡��
		6 - cv.CAP_PROP_FOURCC  	       Four-Character Codes ��һ�ֶ�����ʾ��Ƶ��������ʽ�����ַ�����
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
								#������������Ϊ -1��������ʱ�ᵯ��һ��������ѡ���.
								#isColorֻ��windows��֧��
out.write(frame)
����
fourcc = cv.VideoWriter_fourcc(*'XVID')#python3�汾

		I420(�ʺϴ�����ļ�) -> .avi
		PIMI -> .avi
		XVID -> .avi
		MJPG -> .avi & .mp4
		THEO -> .ogv
		FLV1(flash video, ��ý����Ƶ) -> .flv

	

##################################################################################
Sobel()



cornerHarris(img,blockSize,ksize,k)

	img������float32���Ҷȣ���������ʹ��np.float32(img)ת��
	blockSize - �ǵ�����Ҫ���ǵ������С��
	ksize - Sobel ����ʹ�õĴ��ڴ�С
	k - Harris �ǵ��ⷽ���е����ɲ�����ȡֵ����Ϊ [0,04��0.06].
	