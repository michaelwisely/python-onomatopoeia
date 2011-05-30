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

#probably not the best library to depend on, but it works
from pygame import mixer

#the onomatopoeia methods
def merp(p):
	onomatopoeia_play("merp", p)	

#helpers
def init():
	mixer.init()

def onomatopoeia_play(s, p):
	if p:
		onomatopoeia_log(s)
	onomatopoeia[s].play()

def onomatopoeia_log(s):
	print(s)

#dictionary of onomatopoeia methods
onomatopoeia_methods = {
	'merp': merp
	}

#add this to the end of the module
if __name__ == "__main__":
	init()
