% Code to Generate Waves based on Daniel's Thesis

%% Setting up Intial Parameters

clear
clc

period = zeros(8,1);
wave_h = zeros(8,1);

% Based on Bouy Data - used Bouy Station 46050
sig_wave_h = 3.4 * 0.3048;
swell_wave_h = 3.4 * 0.3048;
swell_wave_p = 13.8;
wind_wave_h = 0.5 * 0.3048;
wind_wave_p = 3.8;
avg_wave_p = 9.1;

wave_h(1) = swell_wave_h;
period(1) = swell_wave_p;

wave_h(2) = wind_wave_h;
period(2) = wind_wave_p;

wave_h(3) = (wind_wave_h + swell_wave_h) / 2;
period(3) = avg_wave_p;

wave_h(4) = (2/3) * swell_wave_h;
period(4) = (2/3) * swell_wave_p;

wave_h(5) = (4/3) * swell_wave_h;
period(5) = (4/3) * swell_wave_p;

wave_h(6) = (2/3) * wind_wave_h;
period(6) = (2/3) * wind_wave_p;

wave_h(7) = (4/3) * wind_wave_h;
period(7) = (4/3) * wind_wave_p;

wave_h(8) = (4/3) * sig_wave_h;
period(8) = avg_wave_p * sig_wave_h / ((swell_wave_h + wind_wave_h) * 0.5);

% This is in meters
depth = 137.2;

% Period
%period = [ 10, 8, 12, 11, 6, 7, 9, 25 ]; %Intial from Daniel
%period = [ 13.8, 3.8, 9.1, 9.108, 18.354, 2.508, 5.054, 15.867 ];

% Wave Height
%wave_h = [ 2.8956, .48768, 3.858768, 1.69164, 0.4, 0.5, 1.1, 0.7 ]; %Intial from Daniel
%wave_h = [ 1.036, 0.152, 0.594, 0.684, 1.378, 0.101, 0.203, 1.378 ];

% Phase
phase = [ -pi/2, -pi/4, -5*pi/8, 4*pi/13, -pi/15, pi/3, -pi/18, -7*pi/4 ]; %Intial from Daniel

%% Creating Wave Profile

% Our time generation horizon
t = 0.2:0.2:1800;

% Our vector to hold our wave profile
eta = zeros(1, numel(t));

% Gravity?
g = 9.81;

% Something...
[w, L, k] = dispersion(depth, period, g);

x = 0;

% For loop to build our profile
for i = 1:numel(period) 
    eta = eta + wave_h(i) / 2 * cos(k(i)*x - w(i)*t + phase(i));
end

plot(eta,'b')

%% Finding Mins and Max

maxAndMin = zeros(1,2);

if (eta(1) > eta(2))
    % We are finding minimum first
    display('finding min first')
    maxAndMin = find_min(1,eta,maxAndMin);
else
    % We are finding maximum first
    display('finding max first')
    maxAndMin = find_max(1,eta,maxAndMin);
end

%% Generating Height and Period
% Note height is in meters and period is in seconds
hAndP = zeros(length(maxAndMin)-3,2);

for i = 3:(length(maxAndMin)-1)
    hAndP(i-2,1) = abs(maxAndMin(i,1) - maxAndMin(i+1,1)) / 2;
    hAndP(i-2,2) = 4 * (maxAndMin(i+1,2) - maxAndMin(i,2)) / 5;
end

%% Output to CSV File

csvwrite('10_11_1800.csv',hAndP)





