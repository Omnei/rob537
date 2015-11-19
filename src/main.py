
import matplotlib.pyplot as plt

from fileParse import fileParse, generateDataset, normalizeData
from crossValidate import crossValidate
import numpy as np
import math

def main():
  num_hidden = 20
  num_prev_waves = 5
  num_epochs = 10
  num_folds = 5

  filename = '../data/10_11_0000.csv'

  parsed = fileParse(filename)
  normalized_parsed = normalizeData(parsed)
  [dataset, num_inputs, num_outputs] = generateDataset(num_prev_waves, normalized_parsed)

  print "Num Inputs:", num_inputs
  print "Num Outputs:", num_outputs
  print "Num Hidden Nodes:", num_hidden


  [height_error, period_error] = crossValidate(dataset, num_hidden, num_folds, num_epochs)
  print "Height Error:", height_error
  print "Period Error:", period_error

  # for inp, tar in dataset:
  #   print "-------------------------------------------"
  #   print inp, tar
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


  
  # trainer = BackpropTrainer(NN, dataset=dataset, momentum=0.0, verbose=False, weightdecay=0.0)
  #evaluation = ModuleValidator.MSE(trainer.module, dataset)
  #validator = CrossValidator(trainer, dataset,val_func=evaluation, n_folds=5, max_epochs=num_epochs, verbose=True)
  #print validator.validate()

  
  # outs = []
  # for ii in range(0, num_epochs):
  #   print ii, trainer.train()

  # x = np.arange(-6.28, 6.28, .01)
  # y = []
  # for item in x:
  #   y.append(NN.activate([item]))

  return 0



    


if __name__ == "__main__":
  main()