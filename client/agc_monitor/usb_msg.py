# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# ! AUTOGENERATED BY generate_interface.py, DO NOT EDIT !
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
from collections import namedtuple
import struct

DATA_FMT = '>BHH'
READ_FMT = '>BH'
DATA_FLAG = 0x80

def pack(msg):
    return globals()['_pack_' + type(msg).__name__](msg)

def unpack(msg_bytes):
    if len(msg_bytes) != struct.calcsize(DATA_FMT):
        raise RuntimeError('Cannot unpack data with unexpected length %u' % len(msg_bytes))

    group, addr, data = struct.unpack(DATA_FMT, msg_bytes)
    if group in _unpack_mem_fns:
        return _unpack_mem_fns[group](addr, data)
    else:
        return _unpack_reg_fns[(group, addr)](data)

ReadSimErasable = namedtuple('ReadSimErasable', ['addr'])
ReadSimErasable.__eq__ = lambda a,b: (type(a) is type(b)) and (tuple(a) == tuple(b))
SimErasable = namedtuple('SimErasable', ['addr', 'data'])
SimErasable.__eq__ = lambda a,b: (type(a) is type(b)) and (tuple(a) == tuple(b))
WriteSimErasable = namedtuple('WriteSimErasable', ['addr', 'data'])
WriteSimErasable.__eq__ = lambda a,b: (type(a) is type(b)) and (tuple(a) == tuple(b))
ReadFixed = namedtuple('ReadFixed', ['addr'])
ReadFixed.__eq__ = lambda a,b: (type(a) is type(b)) and (tuple(a) == tuple(b))
Fixed = namedtuple('Fixed', ['addr', 'data'])
Fixed.__eq__ = lambda a,b: (type(a) is type(b)) and (tuple(a) == tuple(b))
ReadSimFixed = namedtuple('ReadSimFixed', ['addr'])
ReadSimFixed.__eq__ = lambda a,b: (type(a) is type(b)) and (tuple(a) == tuple(b))
SimFixed = namedtuple('SimFixed', ['addr', 'data'])
SimFixed.__eq__ = lambda a,b: (type(a) is type(b)) and (tuple(a) == tuple(b))
WriteSimFixed = namedtuple('WriteSimFixed', ['addr', 'data'])
WriteSimFixed.__eq__ = lambda a,b: (type(a) is type(b)) and (tuple(a) == tuple(b))
ReadChannels = namedtuple('ReadChannels', ['addr'])
ReadChannels.__eq__ = lambda a,b: (type(a) is type(b)) and (tuple(a) == tuple(b))
Channels = namedtuple('Channels', ['addr', 'data'])
Channels.__eq__ = lambda a,b: (type(a) is type(b)) and (tuple(a) == tuple(b))
ReadErasable = namedtuple('ReadErasable', ['addr'])
ReadErasable.__eq__ = lambda a,b: (type(a) is type(b)) and (tuple(a) == tuple(b))
Erasable = namedtuple('Erasable', ['addr', 'data'])
Erasable.__eq__ = lambda a,b: (type(a) is type(b)) and (tuple(a) == tuple(b))
WriteControlStart = namedtuple('WriteControlStart', ['start'])
WriteControlStart.__eq__ = lambda a,b: (type(a) is type(b)) and (tuple(a) == tuple(b))
ReadControlStop = namedtuple('ReadControlStop', [])
ReadControlStop.__eq__ = lambda a,b: (type(a) is type(b)) and (tuple(a) == tuple(b))
ControlStop = namedtuple('ControlStop', ['t12', 'nisq'])
ControlStop.__eq__ = lambda a,b: (type(a) is type(b)) and (tuple(a) == tuple(b))
WriteControlStop = namedtuple('WriteControlStop', ['t12', 'nisq'])
WriteControlStop.__eq__ = lambda a,b: (type(a) is type(b)) and (tuple(a) == tuple(b))
ReadControlStopCause = namedtuple('ReadControlStopCause', [])
ReadControlStopCause.__eq__ = lambda a,b: (type(a) is type(b)) and (tuple(a) == tuple(b))
ControlStopCause = namedtuple('ControlStopCause', ['t12', 'nisq'])
ControlStopCause.__eq__ = lambda a,b: (type(a) is type(b)) and (tuple(a) == tuple(b))
WriteControlProceed = namedtuple('WriteControlProceed', ['proceed'])
WriteControlProceed.__eq__ = lambda a,b: (type(a) is type(b)) and (tuple(a) == tuple(b))
ReadControlMNHRPT = namedtuple('ReadControlMNHRPT', [])
ReadControlMNHRPT.__eq__ = lambda a,b: (type(a) is type(b)) and (tuple(a) == tuple(b))
ControlMNHRPT = namedtuple('ControlMNHRPT', ['mnhrpt'])
ControlMNHRPT.__eq__ = lambda a,b: (type(a) is type(b)) and (tuple(a) == tuple(b))
WriteControlMNHRPT = namedtuple('WriteControlMNHRPT', ['mnhrpt'])
WriteControlMNHRPT.__eq__ = lambda a,b: (type(a) is type(b)) and (tuple(a) == tuple(b))
ReadControlMNHNC = namedtuple('ReadControlMNHNC', [])
ReadControlMNHNC.__eq__ = lambda a,b: (type(a) is type(b)) and (tuple(a) == tuple(b))
ControlMNHNC = namedtuple('ControlMNHNC', ['mnhnc'])
ControlMNHNC.__eq__ = lambda a,b: (type(a) is type(b)) and (tuple(a) == tuple(b))
WriteControlMNHNC = namedtuple('WriteControlMNHNC', ['mnhnc'])
WriteControlMNHNC.__eq__ = lambda a,b: (type(a) is type(b)) and (tuple(a) == tuple(b))
ReadControlNHALGA = namedtuple('ReadControlNHALGA', [])
ReadControlNHALGA.__eq__ = lambda a,b: (type(a) is type(b)) and (tuple(a) == tuple(b))
ControlNHALGA = namedtuple('ControlNHALGA', ['nhalga'])
ControlNHALGA.__eq__ = lambda a,b: (type(a) is type(b)) and (tuple(a) == tuple(b))
WriteControlNHALGA = namedtuple('WriteControlNHALGA', ['nhalga'])
WriteControlNHALGA.__eq__ = lambda a,b: (type(a) is type(b)) and (tuple(a) == tuple(b))
ReadControlSTRT1 = namedtuple('ReadControlSTRT1', [])
ReadControlSTRT1.__eq__ = lambda a,b: (type(a) is type(b)) and (tuple(a) == tuple(b))
ControlSTRT1 = namedtuple('ControlSTRT1', ['strt1'])
ControlSTRT1.__eq__ = lambda a,b: (type(a) is type(b)) and (tuple(a) == tuple(b))
WriteControlSTRT1 = namedtuple('WriteControlSTRT1', ['strt1'])
WriteControlSTRT1.__eq__ = lambda a,b: (type(a) is type(b)) and (tuple(a) == tuple(b))
ReadControlSTRT2 = namedtuple('ReadControlSTRT2', [])
ReadControlSTRT2.__eq__ = lambda a,b: (type(a) is type(b)) and (tuple(a) == tuple(b))
ControlSTRT2 = namedtuple('ControlSTRT2', ['strt2'])
ControlSTRT2.__eq__ = lambda a,b: (type(a) is type(b)) and (tuple(a) == tuple(b))
WriteControlSTRT2 = namedtuple('WriteControlSTRT2', ['strt2'])
WriteControlSTRT2.__eq__ = lambda a,b: (type(a) is type(b)) and (tuple(a) == tuple(b))

class AddressGroup(object):
    SimErasable = 0x10
    Fixed = 0x01
    SimFixed = 0x11
    Channels = 0x02
    Erasable = 0x00
    Control = 0x20

class Control(object):
    Start = 0x0000
    Stop = 0x0001
    StopCause = 0x0002
    Proceed = 0x0003
    MNHRPT = 0x0004
    MNHNC = 0x0005
    NHALGA = 0x0040
    STRT1 = 0x0041
    STRT2 = 0x0042

def _pack_ReadSimErasable(msg):
    return _pack_read_msg(AddressGroup.SimErasable, msg.addr)

def _pack_WriteSimErasable(msg):
    return _pack_write_msg(AddressGroup.SimErasable, msg.addr, msg.data)

def _pack_ReadFixed(msg):
    return _pack_read_msg(AddressGroup.Fixed, msg.addr)

def _pack_ReadSimFixed(msg):
    return _pack_read_msg(AddressGroup.SimFixed, msg.addr)

def _pack_WriteSimFixed(msg):
    return _pack_write_msg(AddressGroup.SimFixed, msg.addr, msg.data)

def _pack_ReadChannels(msg):
    return _pack_read_msg(AddressGroup.Channels, msg.addr)

def _pack_ReadErasable(msg):
    return _pack_read_msg(AddressGroup.Erasable, msg.addr)

def _pack_WriteControlStart(msg):
    data = 0x0000
    data |= (msg.start & 0x0001) << 0
    return _pack_write_msg(AddressGroup.Control, Control.Start, data)

def _pack_ReadControlStop(msg):
    return _pack_read_msg(AddressGroup.Control, Control.Stop)

def _pack_WriteControlStop(msg):
    data = 0x0000
    data |= (msg.t12 & 0x0001) << 0
    data |= (msg.nisq & 0x0001) << 1
    return _pack_write_msg(AddressGroup.Control, Control.Stop, data)

def _pack_ReadControlStopCause(msg):
    return _pack_read_msg(AddressGroup.Control, Control.StopCause)

def _pack_WriteControlProceed(msg):
    data = 0x0000
    data |= (msg.proceed & 0x0001) << 0
    return _pack_write_msg(AddressGroup.Control, Control.Proceed, data)

def _pack_ReadControlMNHRPT(msg):
    return _pack_read_msg(AddressGroup.Control, Control.MNHRPT)

def _pack_WriteControlMNHRPT(msg):
    data = 0x0000
    data |= (msg.mnhrpt & 0x0001) << 0
    return _pack_write_msg(AddressGroup.Control, Control.MNHRPT, data)

def _pack_ReadControlMNHNC(msg):
    return _pack_read_msg(AddressGroup.Control, Control.MNHNC)

def _pack_WriteControlMNHNC(msg):
    data = 0x0000
    data |= (msg.mnhnc & 0x0001) << 0
    return _pack_write_msg(AddressGroup.Control, Control.MNHNC, data)

def _pack_ReadControlNHALGA(msg):
    return _pack_read_msg(AddressGroup.Control, Control.NHALGA)

def _pack_WriteControlNHALGA(msg):
    data = 0x0000
    data |= (msg.nhalga & 0x0001) << 0
    return _pack_write_msg(AddressGroup.Control, Control.NHALGA, data)

def _pack_ReadControlSTRT1(msg):
    return _pack_read_msg(AddressGroup.Control, Control.STRT1)

def _pack_WriteControlSTRT1(msg):
    data = 0x0000
    data |= (msg.strt1 & 0x0001) << 0
    return _pack_write_msg(AddressGroup.Control, Control.STRT1, data)

def _pack_ReadControlSTRT2(msg):
    return _pack_read_msg(AddressGroup.Control, Control.STRT2)

def _pack_WriteControlSTRT2(msg):
    data = 0x0000
    data |= (msg.strt2 & 0x0001) << 0
    return _pack_write_msg(AddressGroup.Control, Control.STRT2, data)


def _unpack_SimErasable(addr, data):
    return SimErasable(addr=addr, data=data)

def _unpack_Fixed(addr, data):
    return Fixed(addr=addr, data=data)

def _unpack_SimFixed(addr, data):
    return SimFixed(addr=addr, data=data)

def _unpack_Channels(addr, data):
    return Channels(addr=addr, data=data)

def _unpack_Erasable(addr, data):
    return Erasable(addr=addr, data=data)

def _unpack_ControlStop(data):
    return ControlStop(
        t12 = (data >> 0) & 0x0001,
        nisq = (data >> 1) & 0x0001,
    )

def _unpack_ControlStopCause(data):
    return ControlStopCause(
        t12 = (data >> 0) & 0x0001,
        nisq = (data >> 1) & 0x0001,
    )

def _unpack_ControlMNHRPT(data):
    return ControlMNHRPT(
        mnhrpt = (data >> 0) & 0x0001,
    )

def _unpack_ControlMNHNC(data):
    return ControlMNHNC(
        mnhnc = (data >> 0) & 0x0001,
    )

def _unpack_ControlNHALGA(data):
    return ControlNHALGA(
        nhalga = (data >> 0) & 0x0001,
    )

def _unpack_ControlSTRT1(data):
    return ControlSTRT1(
        strt1 = (data >> 0) & 0x0001,
    )

def _unpack_ControlSTRT2(data):
    return ControlSTRT2(
        strt2 = (data >> 0) & 0x0001,
    )


_unpack_reg_fns = {
    (DATA_FLAG | AddressGroup.Control, Control.Stop): _unpack_ControlStop,
    (DATA_FLAG | AddressGroup.Control, Control.StopCause): _unpack_ControlStopCause,
    (DATA_FLAG | AddressGroup.Control, Control.MNHRPT): _unpack_ControlMNHRPT,
    (DATA_FLAG | AddressGroup.Control, Control.MNHNC): _unpack_ControlMNHNC,
    (DATA_FLAG | AddressGroup.Control, Control.NHALGA): _unpack_ControlNHALGA,
    (DATA_FLAG | AddressGroup.Control, Control.STRT1): _unpack_ControlSTRT1,
    (DATA_FLAG | AddressGroup.Control, Control.STRT2): _unpack_ControlSTRT2,
}

_unpack_mem_fns = {
    (DATA_FLAG | AddressGroup.SimErasable): _unpack_SimErasable,
    (DATA_FLAG | AddressGroup.Fixed): _unpack_Fixed,
    (DATA_FLAG | AddressGroup.SimFixed): _unpack_SimFixed,
    (DATA_FLAG | AddressGroup.Channels): _unpack_Channels,
    (DATA_FLAG | AddressGroup.Erasable): _unpack_Erasable,
}

def _pack_write_msg(group, addr, data):
    return struct.pack(DATA_FMT, DATA_FLAG | group, addr, data)

def _pack_read_msg(group, addr):
    return struct.pack(READ_FMT, group, addr)

