1.����������������:
	fgbg = cv.createBackgroundSubtractorMOG2()

2.����ÿһ֡ͼ��:
	fgmask = fgbg.apply(frame) #�õ�һ��ǰ���Ҷ�ͼ����һ�η����õ����ǿհ�ͼ
	_,fgmask = cv.threshold(fgmask,30,0xff,cv.THRESH_BINARY) #��ǰ��ͼ��ֵ��
	
	�����Զ�ͼ����и�ʴcv.erode()����������cv.dilate()
	
	
	
	bgImage = fgbg.getBackgroundImage()#��ȡ����ͼ
	"ֵ��˵���ǣ�fgbgÿ����һ��ͼƬ�Ὣ��ͼƬ������Ϣ�������������Ա���ͼ������������"

	bin,cnts,_=cv.findContours(fgmask.copy(),cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
	#

	��cnts�е�ÿһ����������i
		area  =cv.contourArea(i)#��ȡ���������
			��һ��ֵ��ɾ������

		rect = cv.boundingRect(i)#��ȡ��С�ڽӾ��Σ�����ת������

			minAreaRect = cv.minAreaRect(i)
			rect = cv.boxPoints(minAreaRect)#��ȡ���������ϵ���С�ڽӾ���
		
	i��һ��array��ά���󣬵����ö�ά�Ϳ��Ա�ʾ�ˣ��������Ԫ����һ��ƽ������
		

	