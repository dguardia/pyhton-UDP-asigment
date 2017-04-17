import struct
import binascii

values = (1, 'ab'.encode('utf-8'), 2.7)
st = struct.Struct('I 2s f')
packed_data = st.pack(*values)

print('Original values:', values)
print('Format string  :', st.format)
print('Uses           :', st.size, 'bytes')
print('Packed Value   :', binascii.hexlify(packed_data))


packed_data = binascii.unhexlify(b'0100000061620000cdcc2c40')

s = struct.Struct('I 2s f')
unpacked_data = s.unpack(packed_data)
print('Unpacked Values:', unpacked_data)