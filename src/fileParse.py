from csv import reader
from pybrain.datasets import SupervisedDataSet
import numpy as np

def fileParse(filename):
  res = []
  with open(filename, "r") as f:
    csv_file = reader(f)
    for row in csv_file:
      newrow = []
      for item in row:
        newitem = float(item)
        newrow.append(newitem)
      res.append(newrow)
  return res

def normalizeData(dataset):
  curr_max = [0] * len(dataset[0])
  for item in dataset:
    for item_id, num in enumerate(item):
      curr_max[item_id] = max(abs(num), curr_max[item_id])


  returnset = []
  for data_id, datapoint in enumerate(dataset):
    return_data = []
    for val_id, val in enumerate(datapoint):
      return_data.append(val/curr_max[val_id])
    returnset.append(return_data)


  # print curr_max
  return returnset

def generateDataset(prev_waves, parsed):
  # input_dataset = []
  # output_dataset = []
  dataset = []
  num_inputs = len(parsed[0]*prev_waves)
  num_outputs = len(parsed[0])

  #dataset = SupervisedDataSet(num_inputs, num_outputs)

  for point_id, point in enumerate(parsed[prev_waves:]):
    input_data = []

    for ii in range(-prev_waves, 0):
      input_data = input_data + parsed[point_id + ii]
    output_data = point

    dataset.append([input_data, output_data])
    #dataset.addSample(input_data, output_data)
    # input_dataset.append(input_data)
    # output_dataset.append(output_data)
  #print "IO Len", len(input_data), len(output_data)
  #datapoint = [height0, period0, height1, period1, ... ,heightN, periodN]
  #print "Datapoint_len",len(dataset[0][0])
  return [dataset, num_inputs, num_outputs]
  # return input_dataset, output_dataset

def generateDatasetAverage(prev_waves, num_avg, parsed):
    dataset = []
    num_inputs = len(parsed[0]*prev_waves)


    for point_id, point in enumerate(parsed[prev_waves:-num_avg]):
        input_data = []

        for j in range(-prev_waves,0):
            input_data = input_data + parsed[point_id + j]

        avg_height = 0
        avg_period = 0

        for j in range(0,num_avg):
            avg_height += parsed[point_id + j][0]
            avg_period += parsed[point_id + j][1]

        output_data = [avg_height/num_avg, avg_period/num_avg]

        dataset.append([input_data, output_data])

    num_outputs = len(output_data)
    return [dataset, num_inputs, num_outputs]
