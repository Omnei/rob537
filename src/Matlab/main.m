clear all
clc

load('/home/rdml/Desktop/Classes/Rob537/Project/rob537/src/Matlab/PrevWaveExper.mat')

avgCalm5 = mean(prevWaveCalm5);
stdCalm5 = std(prevWaveCalm5);

avgCalm7 = mean(prevWaveCalm7);
stdCalm7 = std(prevWaveCalm7);

avgCalm10 = mean(prevWaveCalm10);
stdCalm10 = std(prevWaveCalm10);

avgRough5 = mean(prevWaveRough5);
stdRough5 = std(prevWaveRough5);

avgRough7 = mean(prevWaveRough7);
stdRough7 = std(prevWaveRough7);

avgRough10 = mean(prevWaveRough10);
stdRough10 = std(prevWaveRough10);

avgs = [avgCalm5(1), avgRough5(1); avgCalm7(1),avgRough7(1);avgCalm10(1),avgRough10(1)];
stdevs = [stdCalm5(1), stdRough5(1); stdCalm7(1), stdRough7(1);stdCalm10(1), stdRough10(1)];

barwitherr(stdevs,avgs)