# RC_Switch_Code_Converter
Convert between rc-switch-codes and their logical (human-readable!) representations.

I'm assuming default pulselengths and protocols here (pulselength 308, protocol 1), 
I don't have any other devices to test against.

Sockets used: Brennenstuhl RCS 1000SN, very easy and generic device with DIPs for channel selection

    Switches    ->   Code



## Pattern Explanation between (system id + device id + state) and the rpi-rf code
rpi-rf-code-format: AAAA ABBB BBCC

A: System code, inverted
B: unit code, inverted
C: ON = 01; OFF = 10

Pad with 0 on every second position (starting with pos 0).

24 bits

## Recordings (view as raw)


(default config, default pins)
["01010", "2"] true: 4477265 [pulselength 308, protocol 1]
-> 100 0100 0101 0001 0101 0001
["01010", "2"] false: 4477268 [pulselength 310, protocol 1]
-> 100 0100 0101 0001 0101 0100

["01010", "1"] true: 4474193 [pulselength 308, protocol 1]
-> 100 0100 0100 0101 0101 | 0001‬

["01010", "1"] false: 4474196
-> 100 0100 0100 0101 0101 0100


SYS, DEV        RECEIVED        REC (BIN)
"01011", 1" ON: 4457809     -> 0100 0100 0000 0101 0101 0001‬ -> 440551
"01011", 1" OFF: 4457812    -> 0100 0100 0000 0101 0101 0100 -> 440554

"01010", "1" ON: 4474193    -> 0100 0100 0100 0101 0101 0001‬ -> 444551
"01010", "1" OFF: 4474196   -> 0100 0100 0100 0101 0101 0100 -> 444554

"01010", "2" ON: 4477265    -> 0100 0100 0101 0001 0101 0001 -> 445151
"01010", "2" OFF: 4477268   -> 0100 0100 0101 0001 0101 0100 -> 445154

"11010", 1" ON: 279889      -> 0000 0100 0100 0101 0101 0001 -> 044551
"11010", 1" OFF: 279892     -> 0000 0100 0100 0101 0101 0100‬ -> 044554

"01010", 5" ON: 4478273     -> 0100 0100 0101 0101 0100 0001
"01010", 5" OFF: 4478276‬    -> 0100 0100 0101 0101 0100 0100



## Other implementations

https://github.com/HeptaSean/SocketPi/blob/master/socket_switch.py

24 bits
every second bit is 0 and can be ignored -> [0, 1, 4, 5]

last block is on/off -> 1 is on, 4 is off

TODO: diff INPUT -> OUTPUT line by line to find corresponding bits

system is first 5 codes (minus 0-pads) inverted.

https://github.com/sui77/rc-switch/blob/master/RCSwitch.cpp
https://github.com/r10r/rcswitch-pi/blob/master/RCSwitch.cpp
switchOn(SYS: str, DEV: int)

