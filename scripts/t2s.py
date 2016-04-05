#!/usr/bin/env python
# -*- encoding=utf-8 -*-
# author: Ian
# e-mail: stmayue@gmail.com
# description: translate traditional chinese to simple

import os
import sys
import traceback

import langconv

_DECODE = 'utf-8'
_ENCODE = 'utf-8'


def process(line):
	"""Convert a line content traditional chinese character to 
	a line only have simple chinese

	Args:
		line: a line decoded

	Returns:
		a line trans to simple chinese

	Raises:
		print error message
	"""
	try:
		simple_version = langconv.Converter('zh-hans').convert(line)
		return simple_version
	except:
		err_line = "Error occur in traditional to simple : " + \
						line.encode(_ENCODE) + os.linesep
		err_msg = "traceback info: " + str(traceback.format_exc())
		sys.stderr.write(err_line)
		sys.stderr.write(err_msg)
		return False
