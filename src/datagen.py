


def main():
  sig_wave_h = 3.4
  swell_h = 3.4
  swell_p = 13.8
  wind_wave_h = 0.5
  wind_wave_p = 3.8
  avg_wave_p = 9.1

  sig_wave_h = ft2m(sig_wave_h)
  swell_h = ft2m(swell_h)
  wind_wave_h = ft2m(wind_wave_h)


  wave_heights = []
  wave_periods = []

  wave_heights.append(swell_h)
  wave_periods.append(swell_p)

  wave_heights.append(wind_wave_h)
  wave_periods.append(wind_wave_p)

  wave_heights.append((wind_wave_h + swell_h)/2)
  wave_periods.append(avg_wave_p)

  wave_heights.append(.66*swell_h)
  wave_periods.append(.66*swell_p)

  wave_heights.append(1.33*swell_h)
  wave_periods.append(1.33*swell_p)

  wave_heights.append(.66*wind_wave_h)
  wave_periods.append(.66*wind_wave_p)

  wave_heights.append(1.33*wind_wave_h)
  wave_periods.append(1.33*wind_wave_p)

  wave_heights.append(1.33*sig_wave_h)
  wave_periods.append(avg_wave_p*sig_wave_h/((swell_h+wind_wave_h)/2))

  print "Heights:", wave_heights
  print "Periods:", wave_periods

















  return 0







def ft2m(feet):
  return feet*.3048




if __name__ == "__main__":
  main()