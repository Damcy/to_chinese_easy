#!/usr/bin/env python
# -*- encoding=utf-8 -*-
# author: Ian
# e-mail: stmayue@gmail.com
# description: 

import os
import sys
from optparse import OptionParser

import t2s
import convertNum
import convertEng

_DECODE = 'utf-8'
_ENCODE = 'utf-8'

_NUM_CONVERT_CLASS = ""
_ENG_CONVERT_CLASS = ""


def read_opts():
	usage = "usage: %prog required all options args"
	parser = OptionParser(usage)
	parser.add_option("-c", "--convert", dest="convert", \
			type = "string", help="do convert or decode")
	parser.add_option("-t", "--t2s", dest="t2s", \
			  type = "int", help="trans traditional chinese to simple")
	parser.add_option("-n", "--numConvert", dest="numConvert", \
			type = "int", help="replace number")
	parser.add_option("-e", "--engConvert", dest="engConvert", \
			type = "int", help="replace other character, include english")
	parser.add_option("-m", "--numConvert_file", dest="numConvert_file", \
			type = "string", help="file path to read or save number convert data")
	parser.add_option("-z", "--engConvert_file", dest="engConvert_file", \
			type = "string", help="file path to read or save English convert data")
	(options, args) = parser.parse_args()
	if not options.convert or not options.t2s or not options.numConvert \
		or not options.engConvert or not options.numConvert_file or not options.engConvert_file:
		sys.stderr.write("incorrect number of arguments, use --help read options" + os.linesep)
		exit(1)
	
	return {'convert': int(options.convert), 't2s': options.t2s, 
			'numConvert': options.numConvert, 'engConvert': options.engConvert,
			'numConvert_file': options.numConvert_file, 'engConvert_file': options.engConvert_file}


def do_nothing(line):
	return line


def convert_process(t2s_func, numConvert_func, engConvert_func, num_file, eng_file):
	for line in sys.stdin:
		line = line.strip().decode(_DECODE)
		if len(line) > 0:
			line = t2s_func(line)
		if line:
			line, eng_list = engConvert_func(line)
		else:
			continue
		if line:
			line, num_list = numConvert_func(line)
		else:
			continue
		if line:
			_NUM_CONVERT_CLASS.save_ele(num_list)
			_ENG_CONVERT_CLASS.save_ele(eng_list)
			print(line.encode(_ENCODE))
		else:
			continue
	if numConvert_func != do_nothing:
		_NUM_CONVERT_CLASS.save_list(num_file)
	if engConvert_func != do_nothing:
		_ENG_CONVERT_CLASS.save_list(eng_file)


def decode_process(num_decode, eng_decode, num_file, eng_file):
	if num_decode != do_nothing:
		_NUM_CONVERT_CLASS.load_list(num_file)
	if eng_decode != do_nothing:
		_ENG_CONVERT_CLASS.load_list(eng_file)
	for line in sys.stdin:
		line = line.strip().decode(_DECODE)
		line = num_decode(line)
		if line:
			line = eng_decode(line)
		else:
			continue
		if line:
			print(line.encode(_ENCODE))
		else:
			continue



if __name__ == '__main__':
	opts = read_opts()
	_NUM_CONVERT_CLASS = convertNum.convertNum()
	_ENG_CONVERT_CLASS = convertEng.convertEng()
	if opts['convert'] == 1:
		# do convert
		t2s_func = do_nothing
		numConvert_func = do_nothing
		engConvert_func = do_nothing

		if opts['t2s']:
			# need trans traditional to simple
			t2s_func = t2s.process
		if opts['numConvert']:
			# need trans numbe
			numConvert_func = _NUM_CONVERT_CLASS.process
		if opts['engConvert']:
			# need trans english
			engConvert_func = _ENG_CONVERT_CLASS.process

		convert_process(t2s_func, numConvert_func, engConvert_func, opts['numConvert_file'], opts['engConvert_file'])
	
	elif opts['convert'] == 0:
		# do decode
		# docode not include s2t
		num_decode = do_nothing
		eng_decode = do_nothing
		if opts['numConvert']:
			num_decode = _NUM_CONVERT_CLASS.decode
		if opts['engConvert']:
			eng_decode = _ENG_CONVERT_CLASS.decode
		decode_process(num_decode, eng_decode, opts['numConvert_file'], opts['engConvert_file'])
	else:
		sys.stderr.write("Error convert option(0/1)!" + os.linesep)