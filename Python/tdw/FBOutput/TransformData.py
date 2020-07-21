# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FBOutput

import tdw.flatbuffers

class TransformData(object):
    __slots__ = ['_tab']

    # TransformData
    def Init(self, buf, pos):
        self._tab = tdw.flatbuffers.table.Table(buf, pos)

    # TransformData
    def Id(self): return self._tab.Get(tdw.flatbuffers.number_types.Int32Flags, self._tab.Pos + tdw.flatbuffers.number_types.UOffsetTFlags.py_type(0))
    # TransformData
    def Position(self, obj):
        obj.Init(self._tab.Bytes, self._tab.Pos + 4)
        return obj

    # TransformData
    def Rotation(self, obj):
        obj.Init(self._tab.Bytes, self._tab.Pos + 16)
        return obj

    # TransformData
    def Forward(self, obj):
        obj.Init(self._tab.Bytes, self._tab.Pos + 32)
        return obj


def CreateTransformData(builder, id, position_x, position_y, position_z, rotation_x, rotation_y, rotation_z, rotation_w, forward_x, forward_y, forward_z):
    builder.Prep(4, 44)
    builder.Prep(4, 12)
    builder.PrependFloat32(forward_z)
    builder.PrependFloat32(forward_y)
    builder.PrependFloat32(forward_x)
    builder.Prep(4, 16)
    builder.PrependFloat32(rotation_w)
    builder.PrependFloat32(rotation_z)
    builder.PrependFloat32(rotation_y)
    builder.PrependFloat32(rotation_x)
    builder.Prep(4, 12)
    builder.PrependFloat32(position_z)
    builder.PrependFloat32(position_y)
    builder.PrependFloat32(position_x)
    builder.PrependInt32(id)
    return builder.Offset()