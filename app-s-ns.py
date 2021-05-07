#!/usr/bin/env python3

from os import system

class Water:
    
    def __init__ ( self, volume = 1, temp = 18 ):
        self.volume  = volume
        self.temp    = temp
        if( temp > 100 ):
            self.state   = "vapor"
        elif( temp <= 0 ):
            self.state = "solid"
        else:
            self.state = "liquid"

    def __str__ ( self ):
        return f"WATER <{self.volume}> L | <{self.temp}> C | <{self.state}> "
################################################################


def heet( water, deltaTemp = 0 ):
    result = Water( water.volume, water.temp + deltaTemp )
    return result

def cool( water, deltaTemp = 0 ):
    result = Water( water.volume, water.temp - deltaTemp )
    return result





w = Water()
w = heet( w, 100 )
w = cool( w, 150 )
system( "clear" )
print(w)


