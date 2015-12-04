from evaluation import getErrorPercent
from fileParse import fileParse, generateDataset, normalizeData, generateDatasetAverage
#filenames = ['../data/10_11_0000.csv', '../data/10_11_0600.csv', '../data/10_11_1200.csv', '../data/10_11_1800.csv', '../data/11_11_0000.csv', '../data/11_11_0600.csv', '../data/11_11_1200.csv', '../data/11_11_1800.csv', ]
rough_seas = '../data/10_11_0000.csv'
calm_seas = '../data/11_11_1200.csv'


def baselineExp():
  outfile = open("../output/baselineExp.txt", 'w')
  num_runs = 5
  print "BaselineExp"
  filenames = ['../data/10_11_0000.csv', '../data/10_11_0600.csv', '../data/10_11_1200.csv', '../data/10_11_1800.csv', '../data/11_11_0000.csv', '../data/11_11_0600.csv', '../data/11_11_1200.csv', '../data/11_11_1800.csv', ]
  outfile.write("Dataset Avg_Height_Error Avg_Period_Error\n")
  for filename in filenames:
    parsed = fileParse(filename)
    normalized_parsed = normalizeData(parsed)
    avg_height_error = 0
    avg_period_error = 0
    for ii, item in enumerate(normalized_parsed[1:]):
      height_error = abs((item[0]-normalized_parsed[ii-1][0])*100)/item[0]
      period_error = abs((item[1]-normalized_parsed[ii-1][1])*100)/item[1]

      avg_period_error += period_error
      avg_height_error += height_error
    avg_height_error = avg_height_error/len(normalized_parsed)
    avg_period_error = avg_period_error/len(normalized_parsed)
    outfile.write(filename+" "+str(avg_height_error)+" "+str(avg_period_error)+"\n")
    print avg_height_error, avg_period_error


def prevWavesExp():
  period_outfile = open("../output/prevWavesExp_period.csv", 'w')
  height_outfile = open("../output/prevWavesExp_height.csv", 'w')

  filenames = [calm_seas, rough_seas]
  num_hidden = 20
  prev_waves = [5, 7, 10, 20]
  num_folds = 5
  num_runs = 10
  num_epochs = 1
  num_after_avg = 5

  for run in range(1, num_runs+1):
    print "\nRun: " + str(run) 
    for waves_id, num_prev_waves in enumerate(prev_waves):
      datasets = []
      for filename in filenames:
        print "Building Dataset:" + str(num_prev_waves) + " - " + filename
        parsed = fileParse(filename)
        normalized_parsed = normalizeData(parsed)
        [dataset, num_inputs, num_outputs] = generateDataset(num_prev_waves, normalized_parsed)
        datasets.append(dataset)

      for ii, training_dataset in enumerate(datasets):
        print "Training on Dataset: "+ str(num_prev_waves) + " - " + filenames[ii]
        errors = getErrorPercent(training_dataset, datasets, num_hidden, num_epochs)
        for item in errors:
          print item
          height_outfile.write(str(item[0]) + ", ")
          period_outfile.write(str(item[1]) + ", ")
    period_outfile.write("\n")
    height_outfile.write("\n")
  return 0




def hiddenNodesExp():
  period_outfile = open("../output/hiddenNodesExp_period.csv", 'w')
  height_outfile = open("../output/hiddenNodesExp_height.csv", 'w')

  filenames = [calm_seas, rough_seas]
  num_prev_waves = 10
  num_folds = 5
  num_runs = 10
  num_epochs = 1
  num_after_avg = 5

  hidden_nodes = [7, 15, 20, 30]

  datasets = []
  for filename in filenames:
    print "Building Dataset:" + str(num_prev_waves) + " - " + filename
    parsed = fileParse(filename)
    normalized_parsed = normalizeData(parsed)
    [dataset, num_inputs, num_outputs] = generateDataset(num_prev_waves, normalized_parsed)
    datasets.append(dataset)

  for run in range(1, num_runs+1):
    print "\nRun: " + str(run) 

    for ii, training_dataset in enumerate(datasets):
      for num_hidden in hidden_nodes:
        print "Training on Dataset: " + filenames[ii] + " - " + str(num_hidden)
        errors = getErrorPercent(training_dataset, datasets, num_hidden, num_epochs)
        for item in errors:
          print item
          height_outfile.write(str(item[0]) + ", ")
          period_outfile.write(str(item[1]) + ", ")
    period_outfile.write("\n")
    height_outfile.write("\n")
  return 0




def generalizabilityExp():
  period_outfile = open("../output/generalizabilityExp_period.csv", 'w')
  height_outfile = open("../output/generalizabilityExp_height.csv", 'w')

  num_hidden = 20
  num_prev_waves = 5
  num_folds = 5
  num_runs = 10
  num_epochs = 1
  eval_filenames = ['../data/10_11_0600.csv', '../data/10_11_1200.csv', '../data/10_11_1800.csv', '../data/11_11_0000.csv', '../data/11_11_0600.csv', '../data/11_11_1800.csv']
  train_filenames = ['../data/11_11_1200.csv', '../data/10_11_0000.csv']


  training_datasets = []
  for filename in train_filenames:
    print "Building Training Dataset:" + str(num_prev_waves) + " - " + filename
    parsed = fileParse(filename)
    normalized_parsed = normalizeData(parsed)
    [dataset, num_inputs, num_outputs] = generateDataset(num_prev_waves, normalized_parsed)
    training_datasets.append(dataset)

  eval_datasets = []
  for filename in eval_filenames:
    print "Building Eval Dataset:" + str(num_prev_waves) + " - " + filename
    parsed = fileParse(filename)
    normalized_parsed = normalizeData(parsed)
    [dataset, num_inputs, num_outputs] = generateDataset(num_prev_waves, normalized_parsed)
    eval_datasets.append(dataset)


  for run in range(1, num_runs+1):
    print "\nRun: " + str(run) 

    for ii, training_dataset in enumerate(training_datasets):
      print "Training on Dataset: " + train_filenames[ii]
      errors = getErrorPercent(training_dataset, eval_datasets, num_hidden, num_epochs)
      for item in errors:
        print item
        height_outfile.write(str(item[0]) + ", ")
        period_outfile.write(str(item[1]) + ", ")
    period_outfile.write("\n")
    height_outfile.write("\n")

  return 0


def avgWavesExp():
  period_outfile = open("../output/avgWavesExp_period.csv", 'w')
  height_outfile = open("../output/avgWavesExp_height.csv", 'w')

  filenames = [calm_seas, rough_seas]
  num_hidden = 20
  prev_waves = 10
  num_folds = 5
  num_runs = 10
  num_epochs = 1
  num_prev_waves = 5
  avg_waves = [5, 10, 15]

  for run in range(1, num_runs+1):
    print "\nRun: " + str(run) 

    for waves_id, num_avg_waves in enumerate(avg_waves):
      datasets = []
      for filename in filenames:
        print "Building Dataset:" + " - " + str(num_avg_waves)+filename
        parsed = fileParse(filename)
        normalized_parsed = normalizeData(parsed)
        [dataset, num_inputs, num_outputs] = generateDatasetAverage(num_prev_waves, num_avg_waves, normalized_parsed)
        datasets.append(dataset)

      for ii, training_dataset in enumerate(datasets):
        print "Training on Dataset: "+ str(num_avg_waves) + " - " + filenames[ii]
        errors = getErrorPercent(training_dataset, datasets, num_hidden, num_epochs)
        for item in errors:
          print item
          height_outfile.write(str(item[0]) + ", ")
          period_outfile.write(str(item[1]) + ", ")
    period_outfile.write("\n")
    height_outfile.write("\n")
  return 0

