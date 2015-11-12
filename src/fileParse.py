from csv import reader
from pybrain.datasets import SupervisedDataSet

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

def normalizeData(dataset, num_in, num_out):
  inputset = []
  curr_max = [0] * num_in
  for item in dataset:
    inputs = item[0:num_in]
    inputset.append(inputs)
    for input_id, num in enumerate(inputs):
      curr_max[input_id] = max(abs(num), curr_max[input_id])

  for input_id, inputs in enumerate(inputset):
    for val_id, val in enumerate(inputs):
      inputset[input_id][val_id] = val/curr_max[val_id]

  returnset = []

  for input_num, inputs in enumerate(inputset):
    returnset.append(inputs+dataset[input_num][num_in:])

  print curr_max
  return returnset

def generateDataset(prev_waves, parsed):
  # input_dataset = []
  # output_dataset = []
  num_inputs = len(parsed[0]*prev_waves)
  num_outputs = len(parsed[0])

  dataset = SupervisedDataSet(num_inputs, num_outputs)

  for point_id, point in enumerate(parsed[prev_waves:]):
    print "Adding Sample:", point_id
    input_data = []

    for ii in range(-prev_waves, 0):
      input_data = input_data + parsed[point_id + ii]

    output_data = point
    dataset.addSample(input_data, output_data)
    # input_dataset.append(input_data)
    # output_dataset.append(output_data)
  return [dataset, num_inputs, num_outputs]
  # return input_dataset, output_dataset


