#���߶�
cv.line(img,tuple_start,tuple_end,tuple_color,int_width)

#������
cv.rectangle(img,tuple_start,tuple_end,tuple_color,int_width)

#��Բ
cv.circle(img,tuple_center,radius,tuple_color,int_width)
		#width=-1ʱ����ʾʵ�ģ��������з����״Ӧ�ö�����

#����Բ
cv.ellipse(img,tuple_center,tuple_long&short-axis,tuple_color,int_width)

#�������		####ò��ֻ�����
cv.polylines(img,plts,bool_is-closed,color,int_width)
		#���Ա��������ܶ����ߡ�ֻ��Ҫ����Ҫ�����߷���һ
		���б��У�������б��������Ϳ�����
#������
cv.putText(img,str_content,tuple_location,font,int_size,tuple_color,int_linetype)

##����font = cv.FONT_HERSHEY_SIMPLEX


