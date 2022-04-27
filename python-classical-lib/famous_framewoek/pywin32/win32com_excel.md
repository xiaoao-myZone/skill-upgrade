·建立一个excel-appliction对象
	xlApp = Dispatch("Excel.Application")

·打开一个word文档或者新建
	xlBook = xlApp.Workbooks.Open("路径",Withwindow=True or False)
	xlBook = xlApp.Workbooks.Add("路径")



·编辑文档
	myRange = doc.Range(start,end)，用int表示
	myRange.InsertBefore("word")

·添加新页面
	pre = doc.Sections(page_num)  从1开始
	pre.Range()返回这一页的内容，以\r结尾，这个对象有End与Start两个属性，返回int
	new_section = doc.Range(pre.Range.End-1,pre.Range.End-1).Sections.Add()
	new_range = new_section.Range
    添加段落
	content_pg = new_range.Paragraphs.Add()
    设置字体
	content_pg.Range.Font.Name,content_pg.Range.Font.Size = 'Times New Roman',24
    设置格式
	content_pg.Range.ParagraphFormat.Alignment = 0 # 0,1,2 分别对应左对齐、居中、右对齐
    插入文字
	content.Range.InsertBefore("Hello,Page.")

·替换文字
	wd.Selection.Find.ClearFormatting()  清除以前的搜索内容
	wd.Selection.Find.Replacement.ClearFormatting()  清除以前的替换内容
	wd.Selection.Find.Execute(Oldstr,False,False,False,False,False,True,1,True,Newstr,2)成功则返回True

·页眉页脚
	wd.ActiveWindow.ActivePane.View.SeekView = 9 #9 - 页眉； 10 - 页脚
	wd.Selection.ParagraphFormat.Alignment = 0
	wd.Selection.Text = 'New Header'
	wd.ActiveWindow.ActivePane.View.SeekView = 0 # 释放焦点，返回主文档
·页眉文字替换
	wd.ActiveDocument.Sections[0].Headers[0].Range.Find.ClearFormatting()
	wd.ActiveDocument.Sections[0].Headers[0].Range.Find.Replacement.ClearFormatting()
	wd.ActiveDocument.Sections[0].Headers[0].Range.Find.Execute(OldStr, False, False, False, False, False, True, 1, False, NewStr, 2)

·添加表格
	new_range = new_seciton.Range
	new_table = new_range.Tables.Add(doc.Range(new_range.End,new_range.End), 5, 5) #在文档末尾添加一个5*5的表格

·表格操作
	doc.Tables[0].Rows[0].Cells[0].Range.Text ='123123'
	doc.Tables[0].Rows.Add() # 增加一行

·另存为
	xlApp.ActiveDocument.SaveAs(r'C:\Users\Administrator\Desktop\python_text1.xls',
				        #FileFormat=constants.wdFormatDocumentDefault#)
·关闭
	xlBook.close(SaveChanges=0)
	xlApp.close(constants.wdDoNotSaveChanges)？
	xlApp.Quit()或者del xlApp




  





