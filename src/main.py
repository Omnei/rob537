from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.utilities import percentError
from pybrain.structure.modules   import SoftmaxLayer
from pybrain.structure import TanhLayer
from pybrain.structure import SigmoidLayer

import matplotlib.pyplot as plt

from fileParse import fileParse, generateDataset

import numpy as np
import math

def main():
  num_inputs = 1
  num_hidden = 20
  num_outputs = 1

  num_prev_waves = 5


  filename = '../data/10_11_0000.csv'

  parsed = fileParse(filename)
  [dataset, num_inputs, num_outputs] = generateDataset(num_prev_waves, parsed)

  for inp, tar in dataset:
    print "-------------------------------------------"
    print inp, tar
  # for line in parsed:
  #   input_data = line[0:num_inputs]
  #   output_data = line[num_inputs:]
  #   print "Input:", input_data
  #   print "Output:", output_data
  #   dataset.addSample(input_data, output_data)

  # dataset.addSample([1, 1], [0])
  # dataset.addSample([0, 0], [0])
  # dataset.addSample([1, 0], [1])
  # dataset.addSample([0, 1], [1])

  # for item in parsed:
  #   print item


  NN = buildNetwork(num_inputs, num_hidden, num_outputs, bias=True, hiddenclass=TanhLayer, outclass=TanhLayer)


  trainer = BackpropTrainer(NN, dataset=dataset, momentum=0.1, verbose=False, weightdecay=.01)
  
  num_epochs = 500
  for ii in range(0, num_epochs):
    print ii, trainer.train()

  # x = np.arange(-6.28, 6.28, .01)
  # y = []
  # for item in x:
  #   y.append(NN.activate([item]))

  return 0


if __name__ == "__main__":
  main()