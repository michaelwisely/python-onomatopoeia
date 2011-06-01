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
	if p:
		onomatopoeia_log(ono_sound)
	onomatopoeia[ono_sound].play()
	while mixer.get_busy and ono_block:
		time.sleep(.1) #this is bad bad bad. Python needs a sched_yield() method

def onomatopoeia_log(s):
	"""Print onomatopoeia 's'. Called by onomatopoeia_play()"""
	print(s)

def build_list():
	"""Populate the dictionary with mixer objects. Called by init()"""
	for k in onomatopoeia.keys():
		onomatopoeia[k] = mixer.Sound('resource/' + k + '.ogg')

"""Dictionary of onomatopoeia"""
onomatopoeia = {
	'merp': None
	}

if __name__ == "__main__":
	init()
