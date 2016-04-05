#!/usr/bin/env python
# -*- encoding=utf-8 -*-
# author: Ian
# e-mail: stmayue@gmail.com
# description: replace English in line with M
#			   why not use E, maybe E used to END the sentence:)

import os
import sys
import cPickle
import re
import traceback

_DECODE = 'utf-8'
_ENCODE = 'utf-8'

class convertEng:
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
			english = re.findall(u'[^\u0021-\u002D\u002F\u0030-\u0040\u005B-\u0060\u007B-\u007E\u2000-\u206F\u2E00-\u2EFF\u3000-\u303F\u31C0-\u31EF\u3400-\u9FFF\uF900-\uFAD9\uFF00-\uFFEF]{2,}|[^\u0020-\u002F\u0030-\u0040\u005B-\u0060\u007B-\u007E\u2000-\u206F\u2E00-\u2EFF\u3000-\u303F\u31C0-\u31EF\u3400-\u9FFF\uF900-\uFAD9\uFF00-\uFFEF]+', line)
			line = re.sub(u'[^\u0021-\u002D\u002F\u0030-\u0040\u005B-\u0060\u007B-\u007E\u2000-\u206F\u2E00-\u2EFF\u3000-\u303F\u31C0-\u31EF\u3400-\u9FFF\uF900-\uFAD9\uFF00-\uFFEF]{2,}|[^\u0020-\u002F\u0030-\u0040\u005B-\u0060\u007B-\u007E\u2000-\u206F\u2E00-\u2EFF\u3000-\u303F\u31C0-\u31EF\u3400-\u9FFF\uF900-\uFAD9\uFF00-\uFFEF]+', 'M', line)
			return line, english
		except:
			err_line = "Error occur in convert English to M : " + \
							line.encode(_ENCODE) + os.linesep
			err_msg = "traceback info: " + str(traceback.format_exc())
			sys.stderr.write(err_line)
			sys.stderr.write(err_msg)
			return False, False

	def decode(self, line):
		try:
			eles = self.replace_list[self.list_cnt]
			for item in eles:
				line = line.replace('M', item, 1)
			return line
		except:
			err_line = "Error occur in decode M to English : " + \
							line.encode(_ENCODE) + os.linesep
			err_msg = "traceback info: " + str(traceback.format_exc())
			sys.stderr.write(err_line)
			sys.stderr.write(err_msg)
			return False
		finally:
			self.list_cnt = self.list_cnt + 1