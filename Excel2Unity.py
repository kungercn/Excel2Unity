
import os
import xlrd
from Config import EXCEL_Dir
from Gen.UnityFileGen import UnityFileGen
from Gen.UnityCodeGen import UnityCodeGen


class Excel2Unity:
	# 构造函数
	def __init__(self):
		self.mExcelFiles = []		# 所有的excel文件

	# 外部处理函数
	def process(self):
		self.recursive_searchexcel(EXCEL_Dir)
		self.process_excel()
		print(self.mExcelFiles)

	# 递归查找文件
	def recursive_searchexcel(self, path):
		for pathdir in os.listdir(path):		# 遍历当前目录
			fullpath = os.path.join(path, pathdir)

			if os.path.isdir(fullpath):
				self.recursive_searchexcel(fullpath)
			elif os.path.isfile(fullpath):
				if os.path.splitext(fullpath)[1] == ".xlsx":
					self.mExcelFiles.append(fullpath)

	# 处理excel文件
	def process_excel(self):
		for filename in self.mExcelFiles:
			data = xlrd.open_workbook(filename)
			table = data.sheets()[0]

			if table.nrows == 0 or table.ncols == 0:
				print("empty files : " + filename)

			rows = table.nrows
			cols = table.ncols
			print(rows)
			print(cols)

			UnityFileGen().process(filename)
			UnityCodeGen().process(filename)


