#!/usr/bin/python3

"""
plotLog.py:  This python script is used plot
a timestamped log file.  It assumes a log files
of the form:

2020-09-12 00:07:12,737 INFO 20.10
2020-09-12 00:08:12,884 INFO 28.3
2020-09-12 00:09:13,085 INFO 26.7

These log files may be produced by the python Logging
library and are in a form typical of Linux system
logs. The only items recognized fo plotting are "INFO"
log items and the only data is a single numeric value.

The companion python application Logger may be used
to conveniently produce logs used as input by this
plotting script.
"""

__author__    = "Steven A. Guccione"
__date__      = "September 14, 2020"
__copyright__ = "Copyright (c) 2020 by Steven A. Guccione"

import matplotlib.pyplot as plotter
import matplotlib.dates as mdates
import argparse
import datetime
import time
  
if __name__ == '__main__':

   # Parse command line parameters
   parser = argparse.ArgumentParser()
   parser.add_argument("infile", nargs="*", help="input log files")
   parser.add_argument("--title", help="plot title")
   parser.add_argument("--xlabel", help="x axis label")
   parser.add_argument("--ylabel", help="y axis label")
   parser.add_argument("--debug", help="debug flag", action='store_true')
   args = parser.parse_args()

   # opening the log files
   infileData = []
   for infile in args.infile:
      with open(infile, mode ='r') as input: 
         for line in input:
            infileData.append(input.readline())
         if args.debug:
            for line in infileData:
               print(line)

   # Convert to time / data
   x = []
   y = []
   for line in infileData:
      try:
         line = line.split()
         if args.debug:
            print(line)
         # Skip blank lines
         if line == []:
            continue
         # Only use INFO log entries
         if line[2] != "INFO":
            print("Non-INFO data entry ignored: " + str(line))
            continue
         t = datetime.datetime.strptime(line[0] + " " + line[1], "%Y-%m-%d %H:%M:%S,%f")
         x.append(t)
         # Single float data item (use 0.0 otherwise)
         try:
            y.append(float(line[3]))
         except Exception as de:
            print("Missing data in input file: " + str(line) + ".  Using 0.0")
            y.append(float(0.0))
            if args.debug:
               print(de)
      except Exception as e:
         # Skip bad data in log file
         print("Ignoring badly formed line in input file: " + str(line))
         if args.debug:
            print(e)

   # Plot graph 
   if args.title:
      plotter.title(args.title)
   if args.xlabel:
      plotter.xlabel(args.xlabel)
   if args.ylabel:
      plotter.ylabel(args.ylabel)

   plotter.gca().xaxis.set_minor_locator(mdates.HourLocator(interval=6))   # every 6 hours
   plotter.gca().xaxis.set_minor_formatter(mdates.DateFormatter('%H:%M'))  # hours and minutes
   plotter.gca().xaxis.set_major_locator(mdates.DayLocator(interval=1))    # every day
   plotter.gca().xaxis.set_major_formatter(mdates.DateFormatter('\n%m-%d-%Y')) 
   
   plotter.plot(x,y)
   plotter.show()

   if args.debug:
      print("Done.")
   
   SystemExit(0)
