from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.utilities import percentError
from pybrain.structure.modules   import SoftmaxLayer
from pybrain.structure import TanhLayer
from pybrain.structure import SigmoidLayer
from pybrain.tools.validation import CrossValidator, ModuleValidator
import operator


def crossValidate(full_dataset, num_hidden, num_folds, num_epochs):
  print len(full_dataset)
  num_datapoints = len(full_dataset)
  num_inputs = len(full_dataset[0][0])
  num_outputs = len(full_dataset[0][1])
  # not_fancy_dataset = []
  fold_size = num_datapoints/num_folds
  print "Fold Size", fold_size

  # for data_in, data_out in dataset:
  #   not_fancy_dataset.append([data_in, data_out])
  mean_error = [0]*num_outputs
  for ii in range(0, num_folds):
    print "Fold:", ii
    NN = buildNetwork(num_inputs, num_hidden, num_outputs, bias=True, hiddenclass=SigmoidLayer, outclass=SigmoidLayer)
    eval_set = full_dataset[fold_size*ii:min(num_datapoints, fold_size*(ii+1))]
    training_set = full_dataset[0:fold_size*ii]+full_dataset[min(num_datapoints, fold_size*(ii+1)):]
    

    dataset = SupervisedDataSet(num_inputs, num_outputs)
    for datapoint in training_set:
      dataset.addSample(datapoint[0], datapoint[1])

    trainer = BackpropTrainer(NN, dataset=dataset, momentum=0.0, verbose=False, weightdecay=0.0)
    for jj in range(0, num_epochs):
      print jj, trainer.train()

    total_error = [0]*num_outputs
    for jj in range(0, len(eval_set)):
      nn_out = NN.activate(eval_set[jj][0])
      error = eval_set[jj][1] - nn_out
      error = map(pow, error, [2]*num_outputs)
      total_error = map(operator.add, error, total_error)
    fold_error = map(operator.div, total_error, [len(eval_set)]*num_outputs)
    mean_error = map(operator.add, mean_error, fold_error)
    print "Fold Error:", fold_error
  mean_error = map(operator.div, mean_error, [num_folds]*num_outputs)
  return mean_error

def getErrorPercent(training_dataset, eval_dataset_list, num_hidden, num_epochs):
  num_datapoints = len(training_dataset)
  num_inputs = len(training_dataset[0][0])
  num_outputs = len(training_dataset[0][1])
  NN = buildNetwork(num_inputs, num_hidden, num_outputs, bias=True, hiddenclass=SigmoidLayer, outclass=SigmoidLayer)
  
  dataset = SupervisedDataSet(num_inputs, num_outputs)
  for datapoint in training_dataset:
    dataset.addSample(datapoint[0], datapoint[1])


  trainer = BackpropTrainer(NN, dataset=dataset, momentum=0.0, verbose=False, weightdecay=0.0)
  
  for epoch in range(0, num_epochs):
    #print epoch 
    trainer.train()
  
  errors = []
  for eval_set in eval_dataset_list:
    total_percent_errors = [0]*num_outputs
    for jj in range(0, len(eval_set)):
      nn_out = NN.activate(eval_set[jj][0])
      percent_error = computeError(eval_set[jj][1], nn_out)
      #print percent_error
      total_percent_errors = map(operator.add, percent_error, total_percent_errors)
    #print total_percent_errors
    errors.append(map(operator.div, total_percent_errors, [len(dataset)]*num_outputs))
  print errors
  return errors

def computeError(actual, calculated):
  diff = map(operator.sub, calculated, actual)
  print diff
  abs_diff = map(abs, diff)
  abs_actual = map(abs, actual)
  res = map(operator.div, abs_diff, abs_actual)
  res = map(operator.mul, res, [100]*len(calculated))
  #print res
  return res
