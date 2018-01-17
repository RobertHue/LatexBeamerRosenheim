#to add support for Python 3.x
from __future__ import division
from __future__ import print_function

import os, sys

import matplotlib
import gtk
# gtk.set_interactive(False)
matplotlib.use('TkAgg')     # use WXAgg for smoother graphs; GTKAgg is faster

import matplotlib.pyplot as plt
import numpy as np
import xml.etree.ElementTree as ET
from collections import OrderedDict
from pprint import pprint

pltFont = {'fontname':'Vera Sans'}

colors = ['b', 'r', 'g', 'y']
styles = ['', '', '', '']
markers = ['', '', '', '']
last_color_index=0
last_style_index=0
last_marker_index=0

cafont = {'fontname':'Cambria'}

def debug_list_comprehension(x):
    x = x.strip()   # remove trailing and ending white spaces
    try:
        result = float(x)   # try to convert
    except ValueError:
        print("ValueError: could not convert string to float: ")
        print(x)
    return result

def iter_color():
    global last_color_index, colors
    last_color_index = (last_color_index + 1) % len(colors)
    return colors[last_color_index]

def iter_style():
    global last_style_index, styles
    last_style_index = (last_style_index + 1) % len(styles)
    return styles[last_style_index]

def iter_markers():
    global last_marker_index, markers
    last_marker_index = (last_marker_index + 1) % len(markers)
    return markers[last_marker_index]


# execute this if py interpreter is running this module as the main program (interpreter will set name to "main")
if __name__ == "__main__":
    print("Number of arguments: ", len(sys.argv))
    print("Argument List:", str(sys.argv))

    if len(sys.argv) >= 2:
        os.chdir(sys.argv[1])
    else:
        os.chdir(".")

    ######## READ DATA FROM LOGFILE ########
    # os.listdir will get everything that's inside specified directory
    # str.endswith(suffix [, start, end]) - returns True if the string ends with the specified suffix
    stat_files = [ f for f in os.listdir(".") if f.endswith(".stats") ]
    data = {}

    # go through all the log files found in the current directory
    for stat_file in stat_files:
        print("loading", stat_file)

        # go through the lines of the current stat file
        #for line in file(stat_file):
        #    splittedDatasets = [x for x in line.split(';') if x]
        #    print("amount of splitted data sets: ", str(len(splittedDatasets)))

        file = open(stat_file, 'r')
        curDataset = file.read()
        file.close()

        # go through all the data field seperated by '\n'
        # for curDataset in file(stat_file):
        print("content: ", curDataset[0:400])

        TITLE, SLOTNUMBER,  X_LABEL, Y_LABEL, DATASET_NAME, COLOR, LINESTYLE, MARKER, XY_TAG, DATA_LIST = curDataset.split('\n', 9)    # -> log dateiformat: TITEL | X_LABEL | Y_LABEL | DATASET_NAME | XY_TAG | DATA_LIST
        TITLE = (TITLE.split('|', 1))[1].strip()
        SLOTNUMBER = (SLOTNUMBER.split('|', 1))[1].strip()
        X_LABEL = (X_LABEL.split('|', 1))[1].strip()
        Y_LABEL = (Y_LABEL.split('|', 1))[1].strip()
        DATASET_NAME = (DATASET_NAME.split('|', 1))[1].strip()
        COLOR = (COLOR.split('|', 1))[1].strip()
        LINESTYLE = (LINESTYLE.split('|', 1))[1].strip()
        MARKER = (MARKER.split('|', 1))[1].strip()
        XY_TAG = (XY_TAG.split('|', 1))[1].strip()
        DATA_LIST = (DATA_LIST.split('|', 1))[1].strip()

        #TITLE  = TITLE.strip()		# -> strip returns a copy of the string in which all white spaces have been stripped of

        #if not stat_file in data.keys():
        #    print("new name: " + stat_file)
        #    data[stat_file] = []
        #    data[stat_file].append( (name, amount, iTimestamps) )
        # print(infoData)

        slotNumber = int(SLOTNUMBER)

        print("----------------")
        print("dataset_name: ", DATASET_NAME)
        print("slotnumber: ", slotNumber)

        if TITLE not in data.keys():
            # print("new name: " + titlename)
            data[TITLE] = {}

        #slot = data[titlename]
        if slotNumber not in data[TITLE].keys():
            data[TITLE][slotNumber] = []

        if COLOR == "":
            COLOR = iter_color()

        if LINESTYLE == "":
            LINESTYLE = iter_style()

        if MARKER == "":
            MARKER = iter_markers()

        data[TITLE][slotNumber].append((X_LABEL, Y_LABEL, DATASET_NAME, COLOR, LINESTYLE, MARKER, XY_TAG, DATA_LIST)) # DATA_LIST is alternating between x and y
        #print("DATA::::::::", data)

    ######## PLOT ONE FIGURE ########
    print("data_len: ",str(len(data)))
    for titlename, innerDict in data.items():		#data.items() returns a list of ditc's (key,value) tuple pairs; neu: titlename  vorher: stat_file_name
        print("############################")
        fig = plt.figure('Figure of ' + titlename)
        fig.set_size_inches(15, 10, forward=True)
        fig.suptitle(r'' + titlename + r'', fontsize=20, verticalalignment='top', horizontalalignment='center') # titlename.replace('_', '\_')
        fig.subplots_adjust(top=0.2)

        for slotNumber, datasets in innerDict.items():  # data.items() returns a list of ditc's (key,value) tuple pairs; neu: titlename  vorher: stat_file_name
            print("############################")
            #::::::::plot:::::::::
            print("plotting ", titlename, " with slotNumber ", slotNumber)
            print("datasets_len: ",str(len(datasets)))

            for dataset in datasets:
                print("dataset_len: ",str(len(dataset)))
                xAxisDescription, yAxisDescription, dataset_name, color, linestyle, marker, XY_TAG, values = dataset[0], dataset[1], dataset[2], dataset[3], dataset[4], dataset[5], dataset[6], dataset[7]

                print("plotting ", dataset_name)
                print("slotNumber: ", slotNumber)
                print("XY_TAG: ", XY_TAG)

                plt.hold(True)  # hold to add elements without first clearing the figure; used to add more than one plot on the same graph
                #  cur_axes = plt.subplot(len(datasets), 1, slotNumber)
                # adding a subplot
                if slotNumber == 1:
                    cur_axes = plt.subplot(len(innerDict), 1, slotNumber)
                else:
                    cur_axes = plt.subplot(len(innerDict), 1, slotNumber, sharex=cur_axes)


                # configure the labels
                #matplotlib.rcParams.update({'fontname':'Cambria'})
                # fig.title   (r'' + titlename.replace('_', '\_') + r'')  # title above the graph
                #plt.rcParams["font.family"] = pltFont
                plt.xlabel  (r'' + xAxisDescription.replace('_', '\_') + r'', fontsize=14, fontweight='medium')  # xlabel of the current graph
                yLabelHandle = plt.ylabel  (r'' + yAxisDescription.replace('_', '\_') + r'', fontsize=14, horizontalalignment='left', fontweight='medium')  # ylabel of the current graph
                yLabelHandle.set_rotation(0)
                cur_axes.yaxis.set_label_coords(-0.1, 1.1)
                cur_axes.ticklabel_format(useOffset=False, style='plain') # disable scientific notation on both axis (useOffset for x, style for y axis)
                # plt.xticks(rotation=70)  # You can specify a rotation for the tick labels in degrees or with keywords.

                cur_axes.xaxis.grid(True)
                cur_axes.yaxis.grid(True)

                print("prepare data values and plot them")
                print("values: ", values[0:300])
                values = values.strip()
                if XY_TAG == 'x':
                    fxvals = np.fromstring(values, dtype='float', sep=' ')
                    for ax in fxvals:
                        cur_axes.axvline(x=ax, color=color, linestyle=linestyle, marker=marker, alpha=0.7, zorder=5) # , label=dataset_name)
                elif XY_TAG == 'y':
                    fyvals = np.fromstring(values, dtype='float', sep=' ')
                    for ay in fyvals:
                        cur_axes.axhline(y=ay, color=color, linestyle=linestyle, marker=marker, alpha=0.7, zorder=4, label=dataset_name)
                elif XY_TAG == 'xy':
                    fValueList = [float(x) for x in values.split(' ')]      # use of list comprehension to convert strings from split func
                    #print("fValueList: ", fValueList)
                    fxvals = np.array(fValueList[0::2], dtype='float')    # get all the even   indexed elements inside the log after :
                    fyvals = np.array(fValueList[1::2], dtype='float')    # get all the uneven indexed elements inside the log after :
  
                    print("fxvals: ", fxvals)
                    print("fyvals: ", fyvals)
                    print("len of fxvals: ", str(len(fxvals)))
                    print("len of fyvals: ", str(len(fyvals)))

                    #print("...........DEBUG.................");
                    #print("dataset_name: ", dataset_name);
                    #print("datavalues: ", fyvals[0:100]);
                    #print(".................................");
                    cur_axes.plot(fxvals, fyvals, color=color, linestyle=linestyle, marker=marker, label=dataset_name)
                else:
                    print("skipping because of undefined plotOnAxis value...")
                    continue 


                # Put a legend below current axis
                legend = plt.legend(loc='best', fancybox=True, shadow=False, ncol=1, fontsize=12) #bbox_to_anchor=(0, 0),
                legend.get_frame().set_alpha(0.5)
                fig.tight_layout(h_pad=0.7)  # add some padding between the subplots (left, bottom, right, top)
        fig.savefig(titlename + '_stats.png', bbox_inches='tight', transparent=False)
    print("############################")
    plt.show()
