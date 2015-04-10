A collection of onomatopoeia for use in logging, debugging, or just for fun. Merp!

```
usage: onomatopoeia.py [-h] [-o O] [-p] [-c] [-r] [-l]

Play and read onomatopoeia.

optional arguments:
  -h, --help  show this help message and exit
  -o O        the onomatopoeia to play
  -p          print the onomatopoeia when playing
  -c          just go crazy
  -r          play an onomatopoeia at random
  -l          list the onomatopoeia

example: ./onomatopoeia.py -o merp -p
```

Usage as a module:
```
import onomatopoeia

#initialize 
onomatopoeia.init()

#play a sound, print the onomatopoeia, and block until we're done
onomatopoeia.play('merp', True, True)

#play a sound but don't block
onomatopoeia.play('blagoonga', True, False)

#play a random sound, don't block or print to screen
onomatopoeia.random(False, False)
```

And just for fun:
```
import onomatopoeia
import time

onomatopoeia.init()

while True:
        onomatopoeia.random(False, False)
        time.sleep(.25)
```