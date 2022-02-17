from cgitb import enable
import pyrtl

# Register file creation
rf = pyrtl.MemBlock(bitwidth=32, addrwidth=5, name='rf')

data = pyrtl.WireVector(bitwidth=32, name='data')
decoder = pyrtl.RomBlock(bitwidth=32, addrwidth=1, romdata=pyrtl.Input(32,name='instr'))

data = decoder[0]

funct = pyrtl.WireVector(bitwidth=6, name='funct')
sh = pyrtl.WireVector(bitwidth=5, name='sh')
rs = pyrtl.WireVector(bitwidth=5, name='rs')
rt = pyrtl.WireVector(bitwidth=5, name='rt')
rd = pyrtl.WireVector(bitwidth=5, name='rd')
alu_out = pyrtl.WireVector(bitwidth=32, name='alu_out')

funct <<= data[0:6]
sh <<= data[6:10]
rs <<= data[21:25]
rt <<= data[16:21]
rd <<= data[11:16]