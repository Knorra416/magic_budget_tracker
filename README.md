## Magic Budget Tracker
I made this function to help track my goal to getting 
toward expensive magic cards. 

![LOTV](liliana.jpeg)

There are two inputs to this file: `-budget_file` and `-card_config`. 
These two arguments are string paths locations to a .csv file where
your savings are stored (a column called `Savings` should be in the file
and a config for the cards you are building towards 
(an example is provided in the repo under `card_file.json`). 

### Example Call
Running this from the command line:
`python magic_budget_tracking.py 
-budget_file budget_saving.csv
-card_config card_file.json`


### Example Output
The output is a string with your percentage status to the goal and
the values used to calculate for each card. 

`You are 20% of the way to your goal! Card Prices: 
{'Liliana of the Veil': 69.36, 'Liliana, the Last Hope': 45.64} and 
Total Cost: $253.72 and Total Saving: $50`

This function uses the excellent `Scrython` library which can be found 
[here](https://github.com/NandaScott/Scrython).

A quick note:

I had some problems with SSL Certifications and had to run some additional setup.
If using Python later than 3.6 on Mac you need to install the basic certificates. 
I found this info [here](https://stackoverflow.com/questions/50236117/scraping-ssl-certificate-verify-failed-error-for-http-en-wikipedia-org) 



