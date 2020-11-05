# Project 5 - SafeZone: Mapping Covid19 and Natural Disasters
---
## What is Your Action Plan during a Federal Emergency?

There seems to be an unprecedented amount of natural disasters in 2020. In addition to the more common seasonal hurricanes, tornadoes and floods, there have been wildfires, earthquakes, civil unrest and even ‘murder hornets’. All of these risks have been magnified by Covid.

Regardless of whether there are more of these instances this year or it just seems that way because of Covid, it is important to have an action plan readily available during a disaster or emergency, especially if you are unfamiliar with a given location or a potential destination.

Our team has developed an application that will alert you when an emergency in your location has occurred and then provide you a plan to “prepare for, respond to and mitigate emergencies, including natural and man-made disasters.” 

---

## Table of Contents 

- API Data Pulls
- Exploratory Data Analysis
- Modeling

---

## Executive Summary

Our three-step process is grounded on sourcing reliable data from government  and research organizations then relaying pertinent information to the user:

- What is the emergency? - access FEMA data to determine if there is anything imminent or ongoing in the user’s location.

- What is the Covid risk? - the Covid Tracking Project (source to Johns Hopkins) provides testing data to calculate the positivity rates/Covid risk levels for the location.

- What is the proper action? - if the application determines there is an emergency or elevated covid risk in the user’s location, relay FEMA’s, Ready.gov, action plan with specific safety instructions and precaution steps. 

---

## Process Detail

- FEMA Data - FEMA has an API that is freely available, and it has a variety of reports that can be pulled. By combining 2-3 FEMA reports from the API pull, over 60 thousand rows of data were collected. The data includes info on all US disasters dated back to 1953, by state (and county, if applicable). The dataset was divided into active and closed disasters. The active disasters dataset was used to give the user disaster info on a given state. Closed disasters data was used to give the user context on what disasters a given state had in the past, hinting at future possibilities but not certainties of disasters in a given state.

- Covid Data - State and City Covid data releases are available on multiple government sites and the Covid Tracking Project aggregates the testing data and provides daily visualizations of the positivity rates for each state. State and city municipalities present the positivity rate as either a 7 or 14-day rolling moving average. We have pulled the raw API data from the Covid Tracking Project and calculated the 7-day moving average consistent with their site visualizations. Different states are using varying degrees of positivity levels to determine whether or not they stay “open”. The WHO recommends a 5% level for at least 14 days. We are using the 5% over 7 days as it is consistent with JHU measures and is more sensitive in the near-term.


## Software Requirements:
- Our analysis required the use of pandas, scikit-learn, numpy, json and requests, and plotting libraries matplotlib and seaborn.
- Our modeling required the use of sktime's sarima model
- Our web app required flask and many submodels of flask, bootstrap, javascript, css, sqlite3



## Sources: 

FEMA
https://www.fema.gov/about/openfema/data-sets

Ready.Gov
https://www.ready.gov/

Positivity Rate Calculation
https://www.cdc.gov/coronavirus/2019-ncov/lab/resources/calculating-percent-positivity.html


WHO guidelines for reopening 
On May 12, 2020 the World Health Organization (WHO) advised governments that before reopening, rates of positivity in testing (ie, out of all tests conducted, how many came back positive for COVID-19) of should remain at 5% or lower for at least 14 days.
https://coronavirus.jhu.edu/testing/testing-positivity

Surgeon General recommended schools reopen with less than 10% in communities back in july 24
https://www.cbsnews.com/news/surgeon-general-jerome-adams-coronavirus-recommends-schools-reopen-with-covid-positivity-rates-less-than-10-in-communities/

CDC with the president released guidelines back in May 20 but they have a lot of “if then’s”. On page 5 of below more related to reopening
https://www.cdc.gov/coronavirus/2019-ncov/downloads/php/CDC-Activities-Initiatives-for-COVID-19-Response.pdf

