#!/usr/bin/python3
"""
Module to resolve the nqueens puzzle, is the challenge of placing
N non-attacking queens on an NxN chessboard.
"""

import sys

if len(sys.argv) != 2:
	print("Usage: nqueens N")
	sys.exit(1)

if not sys.argv[1].isdigit():
	print("N must be a number")
	exit(1)

if int(sys.argv[1]) <= 4:
	print("N must be at least 4")
	exit(1)

queens_list = []


	

