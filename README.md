# PlotLog
Simple Python Log Plotter

PlotLog is a simple Python logfile plotter.  It takes files in the standard Linux log file format as below.  The first element is the timestamp, the second is the logfile line type (DEBUG, INFO, ERROR, etc.).  Only INFO items are plotted.  The third element is the numeric value being plotted.  All other items in the file are ignored.  Below is an example of the typical plottable log file format:

```
2020-09-12 00:07:12,737 INFO 20.10
2020-09-12 00:08:12,884 INFO 28.3
2020-09-12 00:09:13,085 INFO 26.7
```

The command line parameters for PlotLog are:

```
$ ./plotLog.py --help
usage: plotLog.py [-h] [--title TITLE] [--xlabel XLABEL] [--ylabel YLABEL] [--debug]
                  [infile [infile ...]]

positional arguments:
  infile           input log files

optional arguments:
  -h, --help       show this help message and exit
  --title TITLE    plot title
  --xlabel XLABEL  x axis label
  --ylabel YLABEL  y axis label
  --debug          debug flag
```

Note that multiple files can be specified with wildcards or as a list.  The graph below was generated with the included data files and the following command line:

'''
./plotLog.py pingLog.* --title="Spectrum Ping" --ylabel="milliseconds"
'''

![sample plot](/SpectrumPingSept15_2020.png)
