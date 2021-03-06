# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FBOutput

import tdw.flatbuffers

class LogMessage(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsLogMessage(cls, buf, offset):
        n = tdw.flatbuffers.encode.Get(tdw.flatbuffers.packer.uoffset, buf, offset)
        x = LogMessage()
        x.Init(buf, n + offset)
        return x

    # LogMessage
    def Init(self, buf, pos):
        self._tab = tdw.flatbuffers.table.Table(buf, pos)

    # LogMessage
    def MessageType(self):
        o = tdw.flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(tdw.flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 1

    # LogMessage
    def ObjectType(self):
        o = tdw.flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # LogMessage
    def Message(self):
        o = tdw.flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

def LogMessageStart(builder): builder.StartObject(3)
def LogMessageAddMessageType(builder, messageType): builder.PrependUint8Slot(0, messageType, 1)
def LogMessageAddObjectType(builder, objectType): builder.PrependUOffsetTRelativeSlot(1, tdw.flatbuffers.number_types.UOffsetTFlags.py_type(objectType), 0)
def LogMessageAddMessage(builder, message): builder.PrependUOffsetTRelativeSlot(2, tdw.flatbuffers.number_types.UOffsetTFlags.py_type(message), 0)
def LogMessageEnd(builder): return builder.EndObject()
