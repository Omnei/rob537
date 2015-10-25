from pybrain.tools.shortcuts import buildNetwork
from pybtain.datasets import SupervisedDataSet

def main():
  num_inputs = 1
  num_hidden = 3
  num_outputs = 1

  NN = buildNetwork(num_inputs, num_hidden, num_outputs)
  dataset = SupervisedDataSet(1, 1)

  x = range(0, 314)
  y = 


  res = NN.activate([1, 1])
  print res
  return 0


if __name__ == "__main__":
  main()