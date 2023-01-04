import sys
sys.path.append('PlotNeuralNet/')
from pycore.tikzeng import *

arch = [
    to_head('PlotNeuralNet'),
    to_cor(),
    to_begin(),

    #input
    to_input('hello.png', width=3, height=3),
    to_Conv("conv1", "", 32, offset="(0,0,0)",
            to="(0,0,0)", height=16, depth=16, width=2),
    to_Conv("conv2", 16, 56, offset="(0,0,0)",
            to="(conv1-east)", height=16, depth=16, width=4),
    to_Pool("pool1", offset="(0,0,0)", to="(conv2-east)", height=16, depth=16),
    to_Conv("conv3", 8, 128, offset="(1,0,0)",
            to="(pool1-east)", height=8, depth=8, width=8),
    to_connection("pool1", "conv3"),
    to_Pool("pool2", offset="(0,0,0)", to="(conv3-east)",
            height=8, depth=8, width=1),
    to_Conv("conv4", 4, 128, offset="(1,0,0)",
            to="(pool2-east)", height=4, depth=4, width=8),
    to_connection("pool2", "conv4"),
    to_Pool("pool3", offset="(0,0,0)", to="(conv4-east)",
            height=4, depth=4, width=1),
    to_SoftMax("soft1", "", "(1,0,0)", "(pool3-east)", depth=1, caption="$\sigma(x)$"),
    to_connection("pool3", "soft1"),
    to_end()
]


def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex')


if __name__ == '__main__':
    main()
