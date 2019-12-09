#读取并输出docx文档中所有表格里的内容

from docx import Document
from docx.shared import RGBColor

doc=Document('test.docx')
for tables in doc.tables:
    for row in tables.rows:
        print(*map(lambda cell:cell.text,row.cells))
        



