from evaluation import getErrorPercent
from fileParse import fileParse, generateDataset, normalizeData
#filenames = ['../data/10_11_0000.csv', '../data/10_11_0600.csv', '../data/10_11_1200.csv', '../data/10_11_1800.csv', '../data/11_11_0000.csv', '../data/11_11_0600.csv', '../data/11_11_1200.csv', '../data/11_11_1800.csv', ]
rough_seas = '../data/10_11_0000.csv'
calm_seas = '../data/11_11_1200.csv'
random_seas = '../data/10_11_1800.csv'

def prevWavesExp():
  outfile = open("../output/prevWavesExp.txt", 'w')

  num_hidden = 20
  #num_prev_waves = 5
  prev_waves = [5, 7, 10]
  num_folds = 5
  num_runs = 5
  num_epochs = 400

  print "Previous Waves Experiment"
  outfile.write("Previous Waves Experiment"+"\n")
  #calm seas experiment
  for run in range(1, num_runs+1):
    print "Run", run
    outfile.write("\nRun: " + str(run) + "\n")
    print "==========================================================================="
    print "Train on Calm Seas" 
    outfile.write("===========================================================================\n")
    outfile.write("Train on Calm Seas\n")

    filenames = [calm_seas, rough_seas]
    for num_prev_waves in prev_waves:
      datasets = []
      print "Number of Previous Waves:\n", num_prev_waves
      outfile.write("Number of Previous Waves: " + str(num_prev_waves) +"\n")
      for filename in filenames:
        parsed = fileParse(filename)
        #print len(parsed[0])
        normalized_parsed = normalizeData(parsed)
        [dataset, num_inputs, num_outputs] = generateDataset(num_prev_waves, normalized_parsed)
        datasets.append(dataset)

      training_dataset = datasets[0]
      #print len(training_dataset[0][0])
      errors = getErrorPercent(training_dataset, datasets, num_hidden, num_epochs)
      avg_height_error = []
      avg_period_error = []
      for item in errors:
        avg_height_error.append(item[0])
        avg_period_error.append(item[1])
      print "Avg Height Error:", avg_height_error
      print "Avg Period Error:", avg_period_error

      outfile.write("Avg Height Error: " + str(avg_height_error)+"\n")
      outfile.write("Avg Period Error: " + str(avg_period_error)+"\n")

    #rough seas experiment
    print "==========================================================================="
    print "Train on Rough Seas" 
    outfile.write("==========================================================================="+"\n")
    outfile.write("Train on Rough Seas"+"\n")

    filenames = [rough_seas, calm_seas]
    for num_prev_waves in prev_waves:
      datasets = []
      print "Number of Previous Waves:", num_prev_waves
      outfile.write("Number of Previous Waves: " + str(num_prev_waves)+"\n")
      for filename in filenames:
        parsed = fileParse(filename)
        #print len(parsed[0])
        normalized_parsed = normalizeData(parsed)
        [dataset, num_inputs, num_outputs] = generateDataset(num_prev_waves, normalized_parsed)
        datasets.append(dataset)

      training_dataset = datasets[0]
      #print len(training_dataset[0][0])
      errors = getErrorPercent(training_dataset, datasets, num_hidden, num_epochs)
      avg_height_error = []
      avg_period_error = []
      for item in errors:
        avg_height_error.append(item[0])
        avg_period_error.append(item[1])
      print "Avg Height Error:", avg_height_error
      print "Avg Period Error:", avg_period_error

      outfile.write("Avg Height Error: " + str(avg_height_error)+"\n")
      outfile.write("Avg Period Error: " + str(avg_period_error)+"\n")
  
  return 0

def hiddenNodesExp():
  outfile = open("../output/hiddenNodesExp.txt", 'w')

  num_hidden = 20
  num_prev_waves = 10
  prev_waves = [5, 7, 10]
  num_folds = 5
  num_runs = 5
  num_epochs = 400

  print "Hidden Nodes Experiment"
  outfile.write("Hidden Nodes Experiment"+"\n")
  #calm seas experiment
  for run in range(1, num_runs+1):
    print "Run", run
    outfile.write("\nRun: " + str(run) + "\n")
    print "==========================================================================="
    print "Train on Calm Seas" 
    outfile.write("===========================================================================\n")
    outfile.write("Train on Calm Seas\n")

    filenames = [calm_seas, rough_seas]
    
    datasets = []
    for filename in filenames:
      parsed = fileParse(filename)
      #print len(parsed[0])
      normalized_parsed = normalizeData(parsed)
      [dataset, num_inputs, num_outputs] = generateDataset(num_prev_waves, normalized_parsed)
      datasets.append(dataset)

    training_dataset = datasets[0]
    for num_hidden in [15, 20, 30]:
      print "Num Hidden:", num_hidden
      outfile.write("Num Hidden: " + str(num_hidden) + "\n")
      errors = getErrorPercent(training_dataset, datasets, num_hidden, num_epochs)
      avg_height_error = []
      avg_period_error = []
      for item in errors:
        avg_height_error.append(item[0])
        avg_period_error.append(item[1])
      print "Avg Height Error:", avg_height_error
      print "Avg Period Error:", avg_period_error

      outfile.write("Avg Height Error: " + str(avg_height_error)+"\n")
      outfile.write("Avg Period Error: " + str(avg_period_error)+"\n")

    print "==========================================================================="
    print "Train on Rough Seas" 
    outfile.write("===========================================================================\n")
    outfile.write("Train on Rough Seas\n")

    filenames = [rough_seas, calm_seas]
    
    datasets = []
    for filename in filenames:
      parsed = fileParse(filename)
      #print len(parsed[0])
      normalized_parsed = normalizeData(parsed)
      [dataset, num_inputs, num_outputs] = generateDataset(num_prev_waves, normalized_parsed)
      datasets.append(dataset)

    training_dataset = datasets[0]
    for num_hidden in [15, 20, 30]:
      print "Num Hidden:", num_hidden
      outfile.write("Num Hidden: " + str(num_hidden) + "\n")
      errors = getErrorPercent(training_dataset, datasets, num_hidden, num_epochs)
      avg_height_error = []
      avg_period_error = []
      for item in errors:
        avg_height_error.append(item[0])
        avg_period_error.append(item[1])
      print "Avg Height Error:", avg_height_error
      print "Avg Period Error:", avg_period_error

      outfile.write("Avg Height Error: " + str(avg_height_error)+"\n")
      outfile.write("Avg Period Error: " + str(avg_period_error)+"\n")  
  return 0

def generalizabilityExp():
  outfile = open("../output/generalizabilityExp.txt", 'w')

  num_hidden = 20
  num_prev_waves = 10
  prev_waves = [5, 7, 10]
  num_folds = 5
  num_runs = 5
  num_epochs = 400

  print "Generalizability Experiment"
  outfile.write("Generalizability Experiment"+"\n")
  #calm seas experiment
  for run in range(1, num_runs+1):
    print "Run", run
    outfile.write("\nRun: " + str(run) + "\n")
    print "==========================================================================="
    print "Train on Calm Seas" 
    outfile.write("===========================================================================\n")
    outfile.write("Train on Calm Seas\n")

    filenames = ['../data/11_11_1200.csv', '../data/10_11_0000.csv', '../data/10_11_0600.csv', '../data/10_11_1200.csv', '../data/10_11_1800.csv', '../data/11_11_0000.csv', '../data/11_11_0600.csv', '../data/11_11_1800.csv', ]
    print filenames
    outfile.write(str(filenames)+"\n")

    datasets = []
    for filename in filenames:
      parsed = fileParse(filename)
      #print len(parsed[0])
      normalized_parsed = normalizeData(parsed)
      [dataset, num_inputs, num_outputs] = generateDataset(num_prev_waves, normalized_parsed)
      datasets.append(dataset)

    training_dataset = datasets[0]
    errors = getErrorPercent(training_dataset, datasets, num_hidden, num_epochs)
    avg_height_error = []
    avg_period_error = []
    for item in errors:
      avg_height_error.append(item[0])
      avg_period_error.append(item[1])
    print "Avg Height Error:", avg_height_error
    print "Avg Period Error:", avg_period_error

    outfile.write("Avg Height Error: " + str(avg_height_error)+"\n")
    outfile.write("Avg Period Error: " + str(avg_period_error)+"\n")

    print "==========================================================================="
    print "Train on Rough Seas" 
    outfile.write("===========================================================================\n")
    outfile.write("Train on Rough Seas\n")

    filenames = ['../data/10_11_0000.csv', '../data/10_11_0600.csv', '../data/10_11_1200.csv', '../data/10_11_1800.csv', '../data/11_11_0000.csv', '../data/11_11_0600.csv', '../data/11_11_1200.csv', '../data/11_11_1800.csv', ]

    print filenames
    outfile.write(str(filenames)+"\n")

    datasets = []
    for filename in filenames:
      parsed = fileParse(filename)
      #print len(parsed[0])
      normalized_parsed = normalizeData(parsed)
      [dataset, num_inputs, num_outputs] = generateDataset(num_prev_waves, normalized_parsed)
      datasets.append(dataset)

    training_dataset = datasets[0]
    errors = getErrorPercent(training_dataset, datasets, num_hidden, num_epochs)
    avg_height_error = []
    avg_period_error = []
    for item in errors:
      avg_height_error.append(item[0])
      avg_period_error.append(item[1])
    print "Avg Height Error:", avg_height_error
    print "Avg Period Error:", avg_period_error

    outfile.write("Avg Height Error: " + str(avg_height_error)+"\n")
    outfile.write("Avg Period Error: " + str(avg_period_error)+"\n")





  return 0