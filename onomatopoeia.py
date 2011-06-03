#!/usr/bin/env python

#    Copyright (C) 2011 David Fritz (david.jakob.fritz@gmail.com)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
python-onomatopoeia module

Used for hilarious debugging, logging, or just for fun.
"""

import time
import argparse
import random as r

try:
	from pygame import mixer
except:
	print "could not load pygame mixer!"
	raise

def init():
	"""Initializes the mixer for use. Automatically called on import."""
	mixer.init()
	build_list()

def play(ono_sound, ono_print=True, ono_block=True):
	"""
	Play an onomatopoeia 's'. If 'p' is true, also print onomatopoeia to screen.
	Called by individual onomatopoeia methods. If 'b' is true, block until audio
	completes playback.
	"""
	if ono_print:
		onomatopoeia_log(ono_sound)
	onomatopoeia[ono_sound].play()
	while mixer.get_busy() and ono_block:
		time.sleep(.1) #this is bad bad bad. Python needs a sched_yield() method

def onomatopoeia_log(s):
	"""Print onomatopoeia 's'. Called by onomatopoeia_play()"""
	print(s)

def build_list():
	"""Populate the dictionary with mixer objects. Called by init()"""
	for k in onomatopoeia.keys():
		onomatopoeia[k] = mixer.Sound('resource/' + k + '.ogg')

def list_onomatopoeia():
	"""List all of the available onomatopoeia."""
	for k in onomatopoeia.keys():
		print k

def random(ono_print=True, ono_block=True):
	r.seed(None)
	k = r.choice(onomatopoeia.keys())
	play(k,ono_print,ono_block)

"""Dictionary of onomatopoeia"""
onomatopoeia = {
	'merp':		None,
	'bweep':	None,
	'derp':		None,
	'moop':		None,
	'whep':		None,
	'blagoonga':	None,
	'bonk':		None,
	'choo':		None,
	'funt':		None,
	'meep':		None,
	'poof':		None
	}

if __name__ == "__main__":
	init()

	parser = argparse.ArgumentParser(
		description='Play and read onomatopoeia.',
		epilog='example: ./onomatopoeia.py -o merp -p')
		
	parser.add_argument('-o', help='the onomatopoeia to play')
	parser.add_argument('-p', action='store_true', help='print the onomatopoeia when playing')
	parser.add_argument('-c', action='store_true', help='just go crazy')
	parser.add_argument('-r', action='store_true', help='play an onomatopoeia at random')
	parser.add_argument('-l', action='store_true', help='list the onomatopoeia')
	args = parser.parse_args()

	if args.c: #go crazy
		while True:
			random(args.p, True)
	elif args.r: #random
		random(args.p, True)
	elif args.l: #list
		list_onomatopoeia()
	elif args.o != None:
		play(args.o, args.p, True)
	else:
		parser.print_help()

	
