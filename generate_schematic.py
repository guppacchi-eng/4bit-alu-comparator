import schemdraw
import schemdraw.elements as elm

def draw_circuit():
    with schemdraw.Drawing(file='schematic.svg', show=False) as d:
        d.config(fontsize=12)

        # Draw the 74LS283 Adder
        adder = elm.Ic(pins=[
            elm.IcPin(name='A1', side='L', pin='5'),
            elm.IcPin(name='A2', side='L', pin='3'),
            elm.IcPin(name='A3', side='L', pin='14'),
            elm.IcPin(name='A4', side='L', pin='12'),
            elm.IcPin(name='B1', side='L', pin='6'),
            elm.IcPin(name='B2', side='L', pin='2'),
            elm.IcPin(name='B3', side='L', pin='15'),
            elm.IcPin(name='B4', side='L', pin='11'),
            elm.IcPin(name='S1', side='R', pin='4'),
            elm.IcPin(name='S2', side='R', pin='1'),
            elm.IcPin(name='S3', side='R', pin='13'),
            elm.IcPin(name='S4', side='R', pin='10'),
        ], pinspacing=1, edgepadW=1.5, edgepadH=1, leadlen=1, label='74LS283\n4-Bit Adder').at((0, 0))
        d += adder

        # Draw the 74LS85 Comparator below it
        comp = elm.Ic(pins=[
            elm.IcPin(name='A1', side='L', pin='10'),
            elm.IcPin(name='A2', side='L', pin='12'),
            elm.IcPin(name='A3', side='L', pin='13'),
            elm.IcPin(name='A4', side='L', pin='15'),
            elm.IcPin(name='B1', side='L', pin='9'),
            elm.IcPin(name='B2', side='L', pin='11'),
            elm.IcPin(name='B3', side='L', pin='14'),
            elm.IcPin(name='B4', side='L', pin='1'),
            elm.IcPin(name='A>B', side='R', pin='5'),
            elm.IcPin(name='A=B', side='R', pin='6'),
            elm.IcPin(name='A<B', side='R', pin='7'),
        ], pinspacing=1, edgepadW=1.5, edgepadH=1, leadlen=1, label='74LS85\nComparator').at((0, -12))
        d += comp

        # Draw the 74LS47 Decoder to the right of the adder
        dec = elm.Ic(pins=[
            elm.IcPin(name='A', side='L', pin='7'),
            elm.IcPin(name='B', side='L', pin='1'),
            elm.IcPin(name='C', side='L', pin='2'),
            elm.IcPin(name='D', side='L', pin='6'),
            elm.IcPin(name='a', side='R', pin='13'),
            elm.IcPin(name='b', side='R', pin='12'),
            elm.IcPin(name='c', side='R', pin='11'),
            elm.IcPin(name='d', side='R', pin='10'),
            elm.IcPin(name='e', side='R', pin='9'),
            elm.IcPin(name='f', side='R', pin='15'),
            elm.IcPin(name='g', side='R', pin='14'),
        ], pinspacing=1, edgepadW=1.5, edgepadH=1, leadlen=1, label='74LS47\nBCD Decoder').at((12, 1))
        d += dec

        # Draw lines from Adder outputs to Decoder inputs
        d += elm.Line().at(adder.S1).to(dec.A).color('blue')
        d += elm.Line().at(adder.S2).to(dec.B).color('blue')
        d += elm.Line().at(adder.S3).to(dec.C).color('blue')
        d += elm.Line().at(adder.S4).to(dec.D).color('blue')

if __name__ == '__main__':
    draw_circuit()
