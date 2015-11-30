import ast
import numpy as np


def formatOutput(filename):

  HEIGHTS = 0
  PERIODS = 1
  rough_seas = [[],[]]
  calm_seas = [[],[]]

  with open(filename) as f:
    if "generalizability" in filename:
      for line in f:
        if "Train on" in line:
          if "Calm Seas" in line:
            target = calm_seas
          elif "Rough Seas" in line:
            target = rough_seas

        if "Avg Height Error:" in line:
          height_errors = ast.literal_eval(line[18:])
          target[HEIGHTS].append(height_errors)
        elif "Avg Period Error:" in line:
          period_errors = ast.literal_eval(line[18:])
          target[PERIODS].append(period_errors)





    elif "hidden" in filename:
      print "hidden"


    elif "prev" in filename:
      print "prev"
    else:
      print "Error: Incorrect File"
      return 0
  return [rough_seas, calm_seas]


def formatMat(data):
  HEIGHTS = 0
  PERIODS = 1

  heights = data[HEIGHTS]
  periods = data[PERIODS]


  num_points = len(heights[0])

  height_means = []
  height_devs = []
  for ii in range(0, num_points):
    items = []
    for item in heights:
      items.append(item[ii])
    height_means.append(np.mean(items))
    height_devs.append(np.std(items))


  period_means = []
  period_devs = []
  for ii in range(0, num_points):
    items = []
    for item in heights:
      items.append(item[ii])
    period_means.append(np.mean(items))
    period_devs.append(np.std(items))

  print "height_means", height_means
  print "height_devs", height_devs
  print "period_means", period_means
  print "period_devs", period_devs
