������һ��word-appliction����
	wd = Dispatch("Word.Application")

����һ��word�ĵ������½�
	doc = wd.Documents.Open("·��",Withwindow=True or False)
	doc = wd.Documents.Add("·��")

���༭�ĵ�
	myRange = doc.Range(start,end)����int��ʾ
	myRange.InsertBefore("word")

�������ҳ��
	pre = doc.Sections(page_num)  ��1��ʼ
	pre.Range()������һҳ�����ݣ���\r��β�����������End��Start�������ԣ�����int
	new_section = doc.Range(pre.Range.End-1,pre.Range.End-1).Sections.Add()
	new_range = new_section.Range
    ��Ӷ���
	content_pg = new_range.Paragraphs.Add()
    ��������
	content_pg.Range.Font.Name,content_pg.Range.Font.Size = 'Times New Roman',24
    ���ø�ʽ
	content_pg.Range.ParagraphFormat.Alignment = 0 # 0,1,2 �ֱ��Ӧ����롢���С��Ҷ���
    ��������
	content.Range.InsertBefore("Hello,Page.")
	content.Range.Text = u''

������ҳ��(�б�)
	doc.Sections
�����ж���(�б�)
	doc.Paragraphs

���滻����
	wd.Selection.Find.ClearFormatting()  �����ǰ����������
	wd.Selection.Find.Replacement.ClearFormatting()  �����ǰ���滻����
	wd.Selection.Find.Execute(Oldstr,False,False,False,False,False,True,1,True,Newstr,2)�ɹ��򷵻�True

��ҳüҳ��
	wd.ActiveWindow.ActivePane.View.SeekView = 9 #9 - ҳü�� 10 - ҳ��
	wd.Selection.ParagraphFormat.Alignment = 0
	wd.Selection.Text = 'New Header'
	wd.ActiveWindow.ActivePane.View.SeekView = 0 # �ͷŽ��㣬�������ĵ�
��ҳü�����滻
	wd.ActiveDocument.Sections[0].Headers[0].Range.Find.ClearFormatting()
	wd.ActiveDocument.Sections[0].Headers[0].Range.Find.Replacement.ClearFormatting()
	wd.ActiveDocument.Sections[0].Headers[0].Range.Find.Execute(OldStr, False, False, False, False, False, True, 1, False, NewStr, 2)

����ӱ��
	new_range = new_seciton.Range
	new_table = new_range.Tables.Add(doc.Range(new_range.End,new_range.End), 5, 5) #���ĵ�ĩβ���һ��5*5�ı��

��������
	doc.Tables[0].Rows[0].Cells[0].Range.Text ='123123'
	doc.Tables[0].Rows.Add() # ����һ��

�����Ϊ
	wd.ActiveDocument.SaveAs(r'C:\Users\Administrator\Desktop\python_text1.docx',
				        FileFormat=constants.wdFormatDocumentDefault)
���ر�
	doc.close()
	wd.close(constants.wdDoNotSaveChanges)
	wd.Quit()




  





