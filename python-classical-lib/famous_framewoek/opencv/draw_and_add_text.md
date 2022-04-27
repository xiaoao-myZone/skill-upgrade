#画线段
cv.line(img,tuple_start,tuple_end,tuple_color,int_width)

#画矩形
cv.rectangle(img,tuple_start,tuple_end,tuple_color,int_width)

#画圆
cv.circle(img,tuple_center,radius,tuple_color,int_width)
		#width=-1时，表示实心，对于所有封闭形状应该都成立

#画椭圆
cv.ellipse(img,tuple_center,tuple_long&short-axis,tuple_color,int_width)

#画多边形		####貌似只能描点
cv.polylines(img,plts,bool_is-closed,color,int_width)
		#可以被用来画很多条线。只需要把想要画的线放在一
		个列表中，将这个列表传给函数就可以了
#加文字
cv.putText(img,str_content,tuple_location,font,int_size,tuple_color,int_linetype)

##另外font = cv.FONT_HERSHEY_SIMPLEX


