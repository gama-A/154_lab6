from cgitb import enable
import pyrtl

# Register file creation
rf = pyrtl.MemBlock(bitwidth=32, addrwidth=5, name='rf', max_read_ports=2, max_write_ports=1)

data = pyrtl.WireVector(bitwidth=32, name='data')
decoder = pyrtl.RomBlock(bitwidth=32, addrwidth=1, romdata=pyrtl.Input(32,name='instr'))
counter = pyrtl.WireVector(bitwidth=1, name='counter')

counter <<= 0

data <<= decoder[counter]

funct = pyrtl.WireVector(bitwidth=6, name='funct')
sh = pyrtl.WireVector(bitwidth=5, name='sh')
rs = pyrtl.WireVector(bitwidth=5, name='rs')
rt = pyrtl.WireVector(bitwidth=5, name='rt')
rd = pyrtl.WireVector(bitwidth=5, name='rd')
alu_out = pyrtl.WireVector(bitwidth=32, name='alu_out')
data0 = pyrtl.WireVector(bitwidth=32, name='data0')
data1 = pyrtl.WireVector(bitwidth=32, name='data1')

funct <<= data[0:6]
sh <<= data[6:11]
rs <<= data[21:26]
rt <<= data[16:21]
rd <<= data[11:16]

data0 <<= rf[rs]
data1 <<= rf[rt]

with pyrtl.conditional_assignment:
    with funct == 32:
        alu_out |= data0 + data1
    with funct == 34:
        alu_out |= data0 - data1
    with funct == 36:
        alu_out |= data0 & data1
    with funct == 37:
        alu_out |= data0 | data1
    with funct == 38:
        alu_out |= data0 ^ data1
    with funct == 0:
        alu_out |= pyrtl.shift_left_logical(data1, sh)
    with funct == 2:
        alu_out |= pyrtl.shift_right_logical(data1, sh)
    with funct == 3:
        alu_out |= pyrtl.shift_right_arithmetic(data1, sh)
    with funct == 42:
        alu_out |= data0 < data1

rf[rd] <<= alu_out