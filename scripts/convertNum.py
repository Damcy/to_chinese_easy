#!/usr/bin/env python
# -*- encoding=utf-8 -*-
# author: Ian
# e-mail: stmayue@gmail.com
# description: replace numbers in line with N

import os
import sys
import cPickle
import re
import traceback

_DECODE = 'utf-8'
_ENCODE = 'utf-8'

class convertNum:
	def __init__(self):
		self.replace_list = []

	def load_list(self, file_path):
		self.list_cnt = 0
		with open(file_path, 'rb') as f:
			self.replace_list = cPickle.load(f)
		return True

	def save_list(self, file_path):
		with open(file_path, 'wb') as f:
			cPickle.dump(self.replace_list, f)
		return True

	def save_ele(self, ele):
		self.replace_list.append(ele)
		return True

	def process(self, line):
		try:
			numbers = re.findall('[-+]?[0-9]+\.?[0-9]*', line)
			line = re.sub('[-+]?[0-9]+\.?[0-9]*', 'N', line)
			return line, numbers
		except:
			err_line = "Error occur in convert numbers to N : " + \
							line.encode(_ENCODE) + os.linesep
			err_msg = "traceback info: " + str(traceback.format_exc())
			sys.stderr.write(err_line)
			sys.stderr.write(err_msg)
			return False, False

	def decode(self, line):
		try:
			eles = self.replace_list[self.list_cnt]
			for item in eles:
				line = line.replace('N', item, 1)
			return line
		except:
			err_line = "Error occur in decode N to number : " + \
							line.encode(_ENCODE) + os.linesep
			err_msg = "traceback info: " + str(traceback.format_exc())
			sys.stderr.write(err_line)
			sys.stderr.write(err_msg)
			return False
		finally:
			self.list_cnt = self.list_cnt + 1