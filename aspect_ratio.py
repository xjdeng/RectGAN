"""

Supported aspect ratios:
    
1:4 - 64x256 
1:2 - 64x128, 128x256
9:16 - 144x256
3:4 - 192x256, 96x128
2:3 - 128x192, 64x96
1:1 - 64x64, 128x128, 256x256
3:2 - 192x128, 96x64
4:3 - 256x192, 128x96
16:9 - 256x144
2:1 - 128x64, 256x128
4:1 - 256x64


"""
class UnsupportedDimensions(Exception):
    pass

class InvalidDimensions(Exception):
    pass

def get_strides(w, h):
    dims = (h,w) #WARNING: Flipped!
    if dims == (256,64):
        return [(4,2),(4,2),(2,2)]
    elif dims == (128,64):
        return [(4,2), (2,2), (2,2)]
    elif dims == (256,128):
        return [(4,4),(4,2),(2,2)]
    elif dims == (256,144):
        return [(4,3),(4,3),(2,2)]
    elif dims == (256,192):
        return [(4,4),(4,3),(2,2)]
    elif dims == (128,96):
        return [(4,3),(2,2),(2,2)]
    elif dims == (192,128):
        return [(4,4),(3,2),(2,2)]
    elif dims == (96,64):
        return [(3,2),(2,2),(2,2)]
    elif dims == (64,64):
        return [(2,2),(2,2),(2,2)]
    elif dims == (128,128):
        return [(4,4),(2,2),(2,2)]
    elif dims == (256,256):
        return [(4,4),(4,4),(2,2)]
    elif dims == (128,192):
        return [(3,4),(2,2),(2,2)]
    elif dims == (64,96):
        return [(2,3),(2,2),(2,2)]
    elif dims == (192,256):
        return [(4,4),(3,4),(2,2)]
    elif dims == (96,128):
        return [(3,4),(2,2),(2,2)]
    elif dims == (144,256):
        return [(3,4),(3,4),(2,2)]
    elif dims == (128,256):
        return [(4,4),(2,4),(2,2)]
    elif dims == (64,128):
        return [(2,4), (2,2), (2,2)]
    elif dims == (64,256):
        return [(2,4),(2,4),(2,2)]
    else:
        raise UnsupportedDimensions

def validate_dimensions(w, h, sl):
    s_w = sl[0][1]*sl[1][1]*sl[2][1]*8    
    if s_w != w:
        raise InvalidDimensions
    s_h = sl[0][0]*sl[1][0]*sl[2][0]*8
    if s_h != h:
        raise(InvalidDimensions)
    return True