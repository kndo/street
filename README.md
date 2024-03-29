# street
Scrape earnings history from StreetInsider.com


## Installation
```
$ pip install street
```


## Quickstart
To display the help menu:
```
$ street
Usage: street [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  setup   Set request headers to bypass bot blocker
  ticker  Get earnings history for ticker symbol
```


In order to scrape the earnings history of a company from StreetInsider.com, the `street` CLI must look like it's making an HTTP request from a browser. Otherwise, the request will get blocked by the site. So, first visit the site from a browser and grab the `user-agent` and `cookie` parameters from the request header.

To set the `user-agent` and `cookie` parameters for our CLI, use `street setup`, which will prompt you to enter the values. You can find these values, for example, by visiting `https://www.streetinsider.com/ec_earnings.php?q={TICKER_SYMBOL}` in a browser and checking the network tab of the developer tools inspector. Afterwards, the parameters are written to `.street.ini` in your `$HOME` directory. You can also set these values by editing the INI file manually.
```
$ street setup
User agent:
Cookie:
```


The `.street.ini` file looks like this:
```ini
[browser]
user_agent = YOUR_USER_AGENT
cookie = YOUR_COOKIE
```


Now, to get the earnings history of a company such as `AMZN` (case-insensitive), use the following command:
```
$ street ticker amzn
         DATE   QTR     EPS EPS_CONSENSUS SURPRISE  REVENUE REVENUE_CONSENSUS
0  2019-04-25  Q119   $7.09         $4.72   +$2.37   $59.7B           $59.65B
1  2019-01-31  Q418   $6.04         $5.67   +$0.37   $72.4B           $71.87B
2  2018-10-25  Q318   $5.75         $3.14   +$2.61   $56.6B            $57.1B
3  2018-07-26  Q218   $5.07         $2.50   +$2.57   $52.9B           $53.27B
4  2018-04-26  Q118   $3.27         $1.27   +$2.00     $51B           $49.87B
5  2018-02-01  Q417   $3.75         $1.85   +$1.90   $60.5B           $59.83B
6  2017-10-26  Q317   $0.52         $0.03   +$0.49   $43.7B           $42.14B
7  2017-07-27  Q217   $0.40         $1.42   -$1.02     $38B           $37.18B
8  2017-04-27  Q117   $1.48         $1.13   +$0.35   $35.7B           $35.31B
9  2017-02-02  Q416   $1.54         $1.35   +$0.19   $43.7B           $44.68B
10 2016-10-27  Q316   $0.52         $0.78   -$0.26   $32.7B           $32.69B
11 2016-07-28  Q216   $1.78         $1.11   +$0.67   $30.4B           $29.55B
12 2016-04-28  Q116   $1.07         $0.58   +$0.49   $29.1B           $27.97B
13 2016-01-28  Q415   $1.00         $1.56   -$0.56  $35.75B           $35.93B
14 2015-10-22  Q315   $0.17        -$0.13   +$0.30   $25.4B           $24.91B
15 2015-07-23  Q215   $0.19        -$0.14   +$0.33  $23.18B           $22.39B
16 2015-04-23  Q115  -$0.12        -$0.13   +$0.01  $22.72B           $22.39B
17 2015-01-29  Q414   $0.45         $0.17   +$0.28  $29.33B            $29.7B
18 2014-10-23  Q314  -$0.95        -$0.74   -$0.21  $20.58B           $20.85B
19 2014-07-24  Q214  -$0.24        -$0.15   -$0.09  $19.34B           $19.32B
20 2014-04-24  Q114   $0.23         $0.23    $0.00  $19.74B           $19.42B
21 2014-01-30  Q413   $0.51         $0.66   -$0.15  $25.59B           $26.06B
22 2013-10-24  Q313  -$0.09        -$0.09    $0.00  $17.09B           $16.77B
23 2013-07-25  Q213  -$0.08         $0.05   -$0.13   $15.7B           $15.73B
24 2013-04-25  Q113   $0.18         $0.09   +$0.09  $16.07B           $16.17B
25 2013-01-29  Q412   $0.21         $0.27   -$0.06  $21.27B           $22.27B
26 2012-10-25  Q312  -$0.60        -$0.08   -$0.52  $13.81B           $13.92B
27 2012-07-26  Q212   $0.01         $0.02   -$0.01  $12.83B           $12.89B
28 2012-04-26  Q112   $0.28         $0.07   +$0.21   $13.2B            $12.9B
29 2012-01-31  Q411   $0.38         $0.19   +$0.19   $17.4B            $18.2B
30 2011-10-25  Q311   $0.14         $0.24   -$0.10   $10.9B           $10.93B
31 2011-07-26  Q211   $0.41         $0.35   +$0.06    $9.9B            $9.37B
32 2011-04-26  Q111   $0.44         $0.61   -$0.17   $9.86B            $9.52B
33 2011-01-27  Q410   $0.91         $0.88   +$0.03   $12.9B           $12.98B
34 2010-10-21  Q310   $0.51         $0.48   +$0.03      N/A               N/A
```


To save the earnings history to a CSV file, include the `-o/--outfile` option:
```
$ street ticker -o amzn.csv amzn
```