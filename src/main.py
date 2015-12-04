
# import matplotlib.pyplot as plt
from experiments import prevWavesExp, hiddenNodesExp, generalizabilityExp, baselineExp, avgWavesExp
from fileParse import fileParse, generateDataset, normalizeData
from evaluation import crossValidate, getErrorPercent, trainNN, showPredictedWave
# import numpy as np
# import math
from format import formatOutput, formatMat

def main():


  #[rough_seas, calm_seas] = formatOutput('../output/generalizabilityExp.txt')
  #print rough_seas
  #formatMat(rough_seas)
  avgWavesExp()
  prevWavesExp()

  hiddenNodesExp()
  generalizabilityExp()
  #baselineExp()

  # num_hidden = 20
  # num_prev_waves = 5
  # num_folds = 5
  # num_runs = 1
  # num_epochs = 400
  # # #filename =
  # filenames = ['../data/10_11_0000.csv', '../data/10_11_0600.csv']#, '../data/10_11_1200.csv', '../data/10_11_1800.csv', '../data/11_11_0000.csv', '../data/11_11_0600.csv', '../data/11_11_1200.csv', '../data/11_11_1800.csv', ]
  # datasets = []
  # for filename in filenames:
  #   parsed = fileParse(filename)
  #   normalized_parsed = normalizeData(parsed)
  #   [dataset, num_inputs, num_outputs] = generateDataset(num_prev_waves, normalized_parsed)
  #   datasets.append(dataset)

  # print "Num Inputs:", num_inputs
  # print "Num Outputs:", num_outputs
  # print "Num Hidden Nodes:", num_hidden


  # dataset = datasets[0]
  # NN = trainNN(dataset, num_hidden, num_epochs)
  # showPredictedWave(NN, dataset[5])

  #getErrorPercent(datasets[0], datasets, num_hidden, 400)

  # outfile = open("../output/2_"+filename[8:], 'w')
  # epochs = [10, 25, 50, 75, 100, 150, 200, 250, 300, 400, 500]
  # #epochs = [1, 2, 3]
  # for run in range(0, num_runs):
  #   print "Run:", run
  #   for num_epochs in epochs:
  #     print "Epochs:", num_epochs
  #     [height_error, period_error] = crossValidate(dataset, num_hidden, num_folds, num_epochs)
  #     outfile.write(str(height_error) + ", " + str(period_error) +"\n")
  #   outfile.write("\n")





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
