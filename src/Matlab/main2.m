clear all
clc

load('/home/rdml/Desktop/Classes/Rob537/Project/rob537/src/Matlab/hiddenNodes.mat')

avgCalm15 = mean(calm_heights_15);
stdCalm15 = std(calm_heights_15);

avgCalm20 = mean(calm_heights_20);
stdCalm20 = std(calm_heights_20);

avgCalm30 = mean(calm_heights_30);
stdCalm30 = std(calm_heights_30);

avgRough15 = mean(rough_heights_15);
stdRough15 = std(rough_heights_15);

avgRough20 = mean(rough_heights_20);
stdRough20 = std(rough_heights_20);

avgRough30 = mean(rough_heights_30);
stdRough30 = std(rough_heights_30);

avgs = [avgCalm15(1), avgRough15(1); avgCalm20(1),avgRough20(1);avgCalm30(1),avgRough30(1)];
stdevs = [stdCalm15(1), stdRough15(1); stdCalm20(1), stdRough20(1);stdCalm30(1), stdRough30(1)];

barwitherr(stdevs,avgs)