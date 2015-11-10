from csv import reader

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