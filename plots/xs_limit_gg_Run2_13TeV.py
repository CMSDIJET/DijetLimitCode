#!/usr/bin/env python

import sys, os, subprocess, string, re
from ROOT import *
from array import array
import CMS_lumi


gROOT.SetBatch(kTRUE);
gStyle.SetOptStat(0)
gStyle.SetOptTitle(0)
gStyle.SetTitleFont(42, "XYZ")
gStyle.SetTitleSize(0.06, "XYZ")
gStyle.SetLabelFont(42, "XYZ")
gStyle.SetLabelSize(0.05, "XYZ")
gStyle.SetCanvasBorderMode(0)
gStyle.SetFrameBorderMode(0)
gStyle.SetCanvasColor(kWhite)
gStyle.SetPadTickX(1)
gStyle.SetPadTickY(1)
gStyle.SetPadLeftMargin(0.15)
gStyle.SetPadRightMargin(0.05)
gStyle.SetPadTopMargin(0.06)
gStyle.SetPadBottomMargin(0.14)
gROOT.ForceStyle()

masses = array('d')
xs_obs_limits = array('d')
xs_exp_limits = array('d')
masses_exp = array('d')
xs_exp_limits_1sigma = array('d')
xs_exp_limits_1sigma_up = array('d')
xs_exp_limits_2sigma = array('d')
xs_exp_limits_2sigma_up = array('d')


syst = True
#syst = False

mass_min = 1500
mass_max = 7000

########################################################
## Uncomment this part if running the limit code


### for running the limit code
#for mass in range(mass_min,mass_max+100,100):

  #masses.append(float(mass))
  #masses_exp.append(float(mass))

  #cmd = "./stats " + str(int(mass)) + " gg | tee stats_" + str(int(mass)) + "_gg.log"
  #print "Running: " + cmd
  #proc = subprocess.Popen( cmd, shell=True, stdout = subprocess.PIPE, stderr = subprocess.STDOUT )
  #output = proc.communicate()[0]
  #if proc.returncode != 0:
    #print output
    #sys.exit(1)
  ##print output

  #outputlines = output.split("\n")

  #for line in outputlines:
    #if re.search("observed bound =", line):
      #xs_obs_limits.append(float(line.split()[6]))
    #if re.search("median:", line):
      #xs_exp_limits.append(float(line.split()[1]))
    #if re.search("1 sigma band:", line):
      #xs_exp_limits_1sigma.append(float(line.split()[4]))
      #xs_exp_limits_1sigma_up.append(float(line.split()[6]))
    #if re.search("2 sigma band:", line):
      #xs_exp_limits_2sigma.append(float(line.split()[4]))
      #xs_exp_limits_2sigma_up.append(float(line.split()[6]))

##------------------------------------------------------

### for reading the limit code log files
#for mass in range(mass_min,mass_max+100,100):

  #masses.append(float(mass))
  #masses_exp.append(float(mass))

  #log_file = open("stats_" + str(int(mass)) + "_gg.log",'r')
  #outputlines = log_file.readlines()
  #log_file.close()

  #for line in outputlines:
    #if re.search("observed bound =", line):
      #xs_obs_limits.append(float(line.split()[6]))
    #if re.search("median:", line):
      #xs_exp_limits.append(float(line.split()[1]))
    #if re.search("1 sigma band:", line):
      #xs_exp_limits_1sigma.append(float(line.split()[4]))
      #xs_exp_limits_1sigma_up.append(float(line.split()[6]))
    #if re.search("2 sigma band:", line):
      #xs_exp_limits_2sigma.append(float(line.split()[4]))
      #xs_exp_limits_2sigma_up.append(float(line.split()[6]))

##------------------------------------------------------

#for i in range(0,len(masses)):
  #masses_exp.append( masses[len(masses)-i-1] )
  #xs_exp_limits_1sigma.append( xs_exp_limits_1sigma_up[len(masses)-i-1] )
  #xs_exp_limits_2sigma.append( xs_exp_limits_2sigma_up[len(masses)-i-1] )


#print "masses =", masses
#print "xs_obs_limits =", xs_obs_limits
#print "xs_exp_limits =", xs_exp_limits
#print ""
#print "masses_exp =", masses_exp
#print "xs_exp_limits_1sigma =", xs_exp_limits_1sigma
#print "xs_exp_limits_2sigma =", xs_exp_limits_2sigma

##
########################################################

########################################################
## Comment out this part if running the limit code

masses = array('d', [1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4100.0, 4200.0, 4300.0, 4400.0, 4500.0, 4600.0, 4700.0, 4800.0, 4900.0, 5000.0, 5100.0, 5200.0, 5300.0, 5400.0, 5500.0, 5600.0, 5700.0, 5800.0, 5900.0, 6000.0, 6100.0, 6200.0, 6300.0, 6400.0, 6500.0, 6600.0, 6700.0, 6800.0, 6900.0, 7000.0])
xs_obs_limits = array('d', [12.292, 11.1613, 4.66571, 1.84314, 1.04291, 0.777015, 1.05077, 1.65442, 1.89949, 1.64311, 1.93199, 2.09924, 1.87003, 1.25188, 0.807536, 0.755385, 0.947204, 1.0134, 0.916394, 0.752066, 0.551647, 0.480825, 0.430062, 0.339736, 0.259111, 0.219167, 0.181339, 0.168709, 0.170135, 0.168461, 0.161905, 0.15092, 0.143298, 0.149543, 0.156085, 0.158695, 0.16199, 0.162997, 0.160913, 0.15699, 0.152083, 0.146292, 0.139368, 0.132384, 0.126673, 0.122171, 0.122027, 0.120568, 0.119602, 0.119931, 0.128213, 0.130565, 0.133476, 0.136966, 0.141213, 0.146015])
xs_exp_limits = array('d', [5.47802, 4.36122, 4.19892, 3.37816, 2.97497, 2.7817, 2.13559, 1.95129, 1.76424, 1.53202, 1.31067, 1.16192, 0.974604, 0.91502, 0.848704, 0.742918, 0.658287, 0.554933, 0.494442, 0.466983, 0.432907, 0.399693, 0.350458, 0.343739, 0.320855, 0.295009, 0.282642, 0.257422, 0.231262, 0.225847, 0.209487, 0.198307, 0.188087, 0.171077, 0.159239, 0.155893, 0.14491, 0.138011, 0.129519, 0.124969, 0.123212, 0.122361, 0.120889, 0.119612, 0.115196, 0.113749, 0.118831, 0.119123, 0.119866, 0.121635, 0.121348, 0.123078, 0.12475, 0.127124, 0.130585, 0.134835])

masses_exp = array('d', [1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4100.0, 4200.0, 4300.0, 4400.0, 4500.0, 4600.0, 4700.0, 4800.0, 4900.0, 5000.0, 5100.0, 5200.0, 5300.0, 5400.0, 5500.0, 5600.0, 5700.0, 5800.0, 5900.0, 6000.0, 6100.0, 6200.0, 6300.0, 6400.0, 6500.0, 6600.0, 6700.0, 6800.0, 6900.0, 7000.0, 7000.0, 6900.0, 6800.0, 6700.0, 6600.0, 6500.0, 6400.0, 6300.0, 6200.0, 6100.0, 6000.0, 5900.0, 5800.0, 5700.0, 5600.0, 5500.0, 5400.0, 5300.0, 5200.0, 5100.0, 5000.0, 4900.0, 4800.0, 4700.0, 4600.0, 4500.0, 4400.0, 4300.0, 4200.0, 4100.0, 4000.0, 3900.0, 3800.0, 3700.0, 3600.0, 3500.0, 3400.0, 3300.0, 3200.0, 3100.0, 3000.0, 2900.0, 2800.0, 2700.0, 2600.0, 2500.0, 2400.0, 2300.0, 2200.0, 2100.0, 2000.0, 1900.0, 1800.0, 1700.0, 1600.0, 1500.0])
xs_exp_limits_1sigma = array('d', [2.72099, 2.30468, 2.10604, 1.77963, 1.79304, 1.65048, 1.38915, 1.23582, 1.12073, 0.905697, 0.868187, 0.780696, 0.619416, 0.587901, 0.53608, 0.49426, 0.435342, 0.381676, 0.332729, 0.322793, 0.300883, 0.265258, 0.24951, 0.23737, 0.223226, 0.209224, 0.200152, 0.187904, 0.170091, 0.163758, 0.154413, 0.145216, 0.135368, 0.129995, 0.122716, 0.12094, 0.11541, 0.115365, 0.10853, 0.104359, 0.103945, 0.100959, 0.100754, 0.0979252, 0.0958495, 0.0945738, 0.0989364, 0.100455, 0.103605, 0.105169, 0.105504, 0.107319, 0.110305, 0.114939, 0.118541, 0.122665, 0.164408, 0.159636, 0.156013, 0.152365, 0.14989, 0.147368, 0.164102, 0.158119, 0.160589, 0.1566, 0.14864, 0.151814, 0.160147, 0.164057, 0.172679, 0.171964, 0.177414, 0.183014, 0.195492, 0.206018, 0.218164, 0.225981, 0.242863, 0.26778, 0.273349, 0.3039, 0.322213, 0.347268, 0.388073, 0.411427, 0.421363, 0.472292, 0.531281, 0.526219, 0.572379, 0.667547, 0.74036, 0.771543, 0.894017, 1.06962, 1.14546, 1.28919, 1.41492, 1.58375, 1.81677, 2.11757, 2.4642, 2.73558, 3.26609, 3.87645, 4.5795, 5.18275, 6.40938, 7.68245, 8.46029, 11.8433])
xs_exp_limits_2sigma = array('d', [1.68421, 1.47921, 1.16785, 1.10874, 1.15351, 1.08594, 0.92911, 0.815137, 0.701933, 0.630023, 0.556618, 0.501437, 0.431643, 0.414038, 0.392379, 0.375155, 0.281253, 0.279494, 0.244061, 0.23595, 0.238075, 0.210867, 0.199967, 0.197631, 0.174599, 0.169588, 0.154408, 0.147103, 0.143242, 0.139044, 0.128663, 0.118225, 0.115909, 0.112849, 0.103446, 0.098143, 0.0953756, 0.0948135, 0.0917908, 0.0871054, 0.0889806, 0.0858828, 0.0873832, 0.0830129, 0.0849501, 0.0851479, 0.0871004, 0.0903385, 0.0915161, 0.0927306, 0.0935436, 0.0961725, 0.0989607, 0.101967, 0.104974, 0.108406, 0.244023, 0.236121, 0.228941, 0.222843, 0.218629, 0.215568, 0.226613, 0.211089, 0.224442, 0.217954, 0.209072, 0.216288, 0.215651, 0.215907, 0.237953, 0.240575, 0.252386, 0.265721, 0.282413, 0.298958, 0.311585, 0.304404, 0.337496, 0.40571, 0.387257, 0.455812, 0.460431, 0.518067, 0.537458, 0.596184, 0.643834, 0.698191, 0.794256, 0.79037, 0.851925, 1.02384, 1.1563, 1.13569, 1.29354, 1.58176, 1.5959, 1.82151, 2.01927, 2.34276, 2.62979, 3.04345, 3.51409, 3.90442, 4.70601, 5.83211, 6.60658, 8.1892, 9.64807, 12.2614, 13.0381, 17.8233])

if syst:
  masses = array('d', [1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4100.0, 4200.0, 4300.0, 4400.0, 4500.0, 4600.0, 4700.0, 4800.0, 4900.0, 5000.0, 5100.0, 5200.0, 5300.0, 5400.0, 5500.0, 5600.0, 5700.0, 5800.0, 5900.0, 6000.0, 6100.0, 6200.0, 6300.0, 6400.0, 6500.0, 6600.0, 6700.0, 6800.0, 6900.0, 7000.0])
  xs_obs_limits = array('d', [18.0287, 15.6733, 8.6325, 3.91811, 2.1875, 1.69301, 2.13894, 2.80253, 2.79607, 2.63993, 2.65454, 2.58143, 2.36525, 1.83277, 1.27788, 1.03022, 1.11398, 1.13528, 1.05868, 0.910854, 0.720537, 0.592423, 0.492657, 0.397243, 0.311835, 0.251862, 0.207095, 0.18806, 0.184561, 0.177655, 0.169964, 0.166488, 0.155208, 0.159438, 0.162678, 0.164746, 0.166951, 0.167498, 0.164833, 0.162225, 0.156879, 0.153625, 0.146906, 0.139942, 0.13422, 0.128718, 0.125957, 0.125876, 0.124731, 0.125308, 0.132913, 0.135618, 0.13851, 0.142256, 0.145583, 0.149747])
  xs_exp_limits = array('d', [10.4422, 8.9131, 7.47655, 6.2181, 5.2968, 4.500395, 3.855925, 3.167, 2.69755, 2.292435, 1.940255, 1.683285, 1.418775, 1.24041, 1.11487, 0.9766635, 0.844834, 0.7089375, 0.625544, 0.5524985, 0.5503275, 0.4784735, 0.4144995, 0.402687, 0.3619335, 0.3407565, 0.3199655, 0.2868715, 0.260819, 0.241752, 0.219856, 0.2151445, 0.202777, 0.1877995, 0.1729915, 0.1606085, 0.1550125, 0.144495, 0.141409, 0.137229, 0.1342635, 0.131153, 0.127747, 0.12197, 0.1202775, 0.1174895, 0.116965, 0.122172, 0.121244, 0.1215555, 0.1223685, 0.1248045, 0.1276105, 0.130358, 0.1346525, 0.139314])

  masses_exp = array('d', [1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4100.0, 4200.0, 4300.0, 4400.0, 4500.0, 4600.0, 4700.0, 4800.0, 4900.0, 5000.0, 5100.0, 5200.0, 5300.0, 5400.0, 5500.0, 5600.0, 5700.0, 5800.0, 5900.0, 6000.0, 6100.0, 6200.0, 6300.0, 6400.0, 6500.0, 6600.0, 6700.0, 6800.0, 6900.0, 7000.0, 7000.0, 6900.0, 6800.0, 6700.0, 6600.0, 6500.0, 6400.0, 6300.0, 6200.0, 6100.0, 6000.0, 5900.0, 5800.0, 5700.0, 5600.0, 5500.0, 5400.0, 5300.0, 5200.0, 5100.0, 5000.0, 4900.0, 4800.0, 4700.0, 4600.0, 4500.0, 4400.0, 4300.0, 4200.0, 4100.0, 4000.0, 3900.0, 3800.0, 3700.0, 3600.0, 3500.0, 3400.0, 3300.0, 3200.0, 3100.0, 3000.0, 2900.0, 2800.0, 2700.0, 2600.0, 2500.0, 2400.0, 2300.0, 2200.0, 2100.0, 2000.0, 1900.0, 1800.0, 1700.0, 1600.0, 1500.0])
  xs_exp_limits_1sigma = array('d', [6.21123476, 5.26774792, 4.36130257, 3.92517088, 3.62367304, 3.1688113, 2.71086825, 2.22266038, 1.87066821, 1.6134789, 1.35538591, 1.14366417, 0.973090906, 0.880815864, 0.780716373, 0.672944018, 0.583737785, 0.486137268, 0.436473526, 0.391914933, 0.375144287, 0.334171995, 0.295714159, 0.277061038, 0.263978496, 0.24036933, 0.218494429, 0.210549895, 0.1860362, 0.175329411, 0.164290302, 0.15017127, 0.15097111, 0.139251541, 0.129000335, 0.121852994, 0.114884839, 0.112090308, 0.107497497, 0.104425647, 0.101918181, 0.0985768604, 0.0967240176, 0.0980416221, 0.095948516, 0.0949250467, 0.0953759724, 0.100206435, 0.10092792, 0.104190573, 0.103037659, 0.105800909, 0.108548293, 0.111889628, 0.114588734, 0.118852025, 0.17316646, 0.167086506, 0.164254097, 0.159900792, 0.156215415, 0.154398651, 0.165078838, 0.163019218, 0.160267459, 0.157527738, 0.152001972, 0.155495314, 0.166548133, 0.172389747, 0.178661832, 0.183550924, 0.193918855, 0.198610202, 0.197859598, 0.227741346, 0.235231649, 0.248077328, 0.262762694, 0.308964994, 0.302282313, 0.322546232, 0.364378886, 0.375145427, 0.412668625, 0.469653668, 0.504513639, 0.539266796, 0.594023462, 0.588069243, 0.687031341, 0.784097076, 0.832520944, 0.923402771, 1.08663353, 1.25484349, 1.45501727, 1.65018378, 1.86366904, 2.09552459, 2.45080602, 2.89172908, 3.36528267, 3.76500412, 4.43536148, 5.56642359, 6.57651434, 7.48619724, 9.20909846, 11.7407675, 13.4752294, 18.1688591])
  xs_exp_limits_2sigma = array('d', [4.13138985, 3.21887024, 2.74955129, 2.70920042, 2.34549972, 2.0751619, 1.76364209, 1.66353852, 1.35870571, 1.19483766, 1.02480137, 0.839703034, 0.699227499, 0.656588448, 0.556879603, 0.501896998, 0.435314986, 0.368385357, 0.312124235, 0.310869604, 0.289678626, 0.255802094, 0.238445697, 0.214639598, 0.198199573, 0.184097747, 0.165507971, 0.161417087, 0.150125485, 0.132436442, 0.129053316, 0.127601918, 0.120263858, 0.10776226, 0.104534027, 0.0966922096, 0.0953319424, 0.0933798708, 0.0896073309, 0.0885899154, 0.0884077286, 0.0871315166, 0.0864900831, 0.0858222999, 0.084434173, 0.0852307461, 0.0861213143, 0.0882715819, 0.089939739, 0.0939455176, 0.0934549111, 0.0956070408, 0.0986325466, 0.101375669, 0.104947137, 0.10850885, 0.242563867, 0.235649719, 0.231115816, 0.226199685, 0.223434103, 0.219643088, 0.23770357, 0.226604366, 0.230483558, 0.215268437, 0.209815919, 0.220304471, 0.233581698, 0.24534997, 0.248604114, 0.256775158, 0.259767017, 0.268449538, 0.278327136, 0.318409261, 0.316953385, 0.358192821, 0.370259557, 0.427721484, 0.453463059, 0.454163746, 0.49550195, 0.518073945, 0.614585016, 0.655984169, 0.692087759, 0.727687211, 0.80751574, 0.808281262, 0.939624131, 1.03679852, 1.19514181, 1.32925097, 1.4809772, 1.75900633, 1.94401271, 2.19141083, 2.7067759, 2.81269465, 3.17864731, 3.93668574, 4.45634077, 4.99311173, 6.16222264, 8.22243635, 9.26108307, 10.6994382, 13.016748, 17.0977239, 21.9691376, 24.3170575])

##
########################################################

massesS8 = array('d', [1000.0,1100.0,1200.0,1300.0,1400.0,1500.0,1600.0,1700.0,1800.0,1900.0,2000.0,2100.0,2200.0,2300.0,2400.0,2500.0,2600.0,2700.0,2800.0,2900.0,3000.0,3100.0,3200.0,3300.0,3400.0,3500.0,3600.0,3700.0,3800.0,3900.0,4000.0,4100.0,4200.0,4300.0,4400.0,4500.0,4600.0,4700.0,4800.0,4900.0,5000.0,5100.0,5200.0,5300.0,5400.0,5500.0,5600.0,5700.0,5800.0,5900.0,6000.0])
xsS8 = array('d', [5.46E+02,3.12E+02,1.85E+02,1.12E+02,7.19E+01,4.59E+01,3.02E+01,2.01E+01,1.37E+01,9.46E+00,6.55E+00,4.64E+00,3.27E+00,2.36E+00,1.70E+00,1.24E+00,9.11E-01,6.69E-01,4.97E-01,3.71E-01,2.78E-01,2.07E-01,1.55E-01,1.19E-01,9.26E-02,7.08E-02,5.43E-02,4.15E-02,3.22E-02,2.50E-02,1.92E-02,1.51E-02,1.19E-02,9.25E-03,7.35E-03,5.86E-03,4.53E-03,3.66E-03,2.91E-03,2.33E-03,1.86E-03,1.45E-03,1.12E-03,8.75E-04,6.90E-04,5.55E-04,4.47E-04,3.63E-04,2.92E-04,2.37E-04,1.97E-04])

xs_max = 3.5e+01
idx = 0

for i, xs in enumerate(xsS8):
  if xs < xs_max:
    idx = i
    break

graph_xsS8 = TGraph(len(massesS8[idx:-1]),massesS8[idx:-1],xsS8[idx:-1])
graph_xsS8.SetLineWidth(3)
graph_xsS8.SetLineStyle(8)
graph_xsS8.SetLineColor(6)

graph_exp_2sigma = TGraph(len(masses_exp),masses_exp,xs_exp_limits_2sigma)
graph_exp_2sigma.SetFillColor(kYellow)
graph_exp_2sigma.GetXaxis().SetTitle("gg resonance mass [GeV]")
graph_exp_2sigma.GetYaxis().SetTitle("#sigma #times #it{B} #times #it{A} [pb]")
graph_exp_2sigma.GetYaxis().SetTitleOffset(1.1)
graph_exp_2sigma.GetYaxis().SetRangeUser(4e-02,1e+02)
#graph_exp_2sigma.GetXaxis().SetNdivisions(1005)

graph_exp_1sigma = TGraph(len(masses_exp),masses_exp,xs_exp_limits_1sigma)
graph_exp_1sigma.SetFillColor(kGreen+1)

graph_exp = TGraph(len(masses),masses,xs_exp_limits)
#graph_exp.SetMarkerStyle(24)
graph_exp.SetLineWidth(3)
graph_exp.SetLineStyle(2)
graph_exp.SetLineColor(4)

graph_obs = TGraph(len(masses),masses,xs_obs_limits)
graph_obs.SetMarkerStyle(20)
graph_obs.SetLineWidth(3)
#graph_obs.SetLineStyle(1)
graph_obs.SetLineColor(1)


c = TCanvas("c", "",800,800)
c.cd()

graph_exp_2sigma.Draw("AF")
graph_exp_1sigma.Draw("F")
graph_exp.Draw("L")
graph_obs.Draw("LP")
graph_xsS8.Draw("L")

legend = TLegend(.55,.50,.90,.70)
legend.SetBorderSize(0)
legend.SetFillColor(0)
legend.SetFillStyle(0)
legend.SetTextFont(42)
legend.SetTextSize(0.035)
legend.SetHeader('95% CL upper limits')
legend.AddEntry(graph_obs,"Observed","lp")
legend.AddEntry(graph_exp,"Expected","lp")
legend.AddEntry(graph_exp_1sigma,"#pm 1#sigma","F")
legend.AddEntry(graph_exp_2sigma,"#pm 2#sigma","F")
legend.Draw()

legendTh = TLegend(.55,.80,.90,.84)
legendTh.SetBorderSize(0)
legendTh.SetFillColor(0)
legendTh.SetFillStyle(0)
legendTh.SetTextFont(42)
legendTh.SetTextSize(0.035)
legendTh.AddEntry(graph_xsS8,"S8","l")
legendTh.Draw()

#l1 = TLatex()
#l1.SetTextAlign(12)
#l1.SetTextFont(42)
#l1.SetNDC()
#l1.SetTextSize(0.04)
#l1.SetTextSize(0.04)
#l1.DrawLatex(0.18,0.40, "CMS Preliminary")
#l1.DrawLatex(0.18,0.32, "#intLdt = 1 fb^{-1}")
#l1.DrawLatex(0.19,0.27, "#sqrt{s} = 13 TeV")

#draw the lumi text on the canvas
CMS_lumi.extraText = "Preliminary"
CMS_lumi.lumi_sqrtS = "65 pb^{-1} (13 TeV)" # used with iPeriod = 0, e.g. for simulation-only plots (default is an empty string)
iPos = 11
if( iPos==0 ): CMS_lumi.relPosX = 0.15
iPeriod = 0

CMS_lumi.CMS_lumi(c, iPeriod, iPos)

gPad.RedrawAxis()

c.SetLogy()
c.SaveAs('xs_limit_DijetLimitCode_gg' + ('_NoSyst' if not syst else '') + '_Run2_13TeV_DATA_65_invpb.eps')
