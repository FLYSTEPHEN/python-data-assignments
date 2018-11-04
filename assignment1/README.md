## Topic
  - The data journalists' information and their contributions on Github from 2008 to 2018
## Data source
  - http://jplusplus.github.io/global-directory/
## Data fields (type, sample data); 
  - ```name``` - String. e.g. ```Justin Myers```
  - ```institution``` - String. e.g. ```The Associated Press```
  - ```city``` - String. e.g. ```United States, Brooklyn (US-VA)```
  - ```github adress``` - String. e.g. ```http://github.com/myersjustinc```
  - ```github contributions``` - Float. e.g. ```1.0,0.0,12.0,3.0...```
  - The result is in [Result.csv](https://github.com/FLYSTEPHEN/python-data-assignments/blob/master/assignment1/Result.csv)
  - The codes is in [scrape-data-journalist-directory-and-output-github-contributions.ipynb](https://github.com/FLYSTEPHEN/python-data-assignments/blob/master/assignment1/scrape-data-journalist-directory.ipynb)
## Data volume
  - 3967 rows × 81 columns
  - 217 data journalists's information, including their names, institutions, cities, github adress and everyday github contributions(only 81 have a github account) from 2008. 
## License
  - CC 4.0
## Future issues
  - The codes for scraping journalists' twitter accounts, pgps, emails and websites have been written but not operated since there is no needs at this stage
  - We can also get their twitter easily, then we could scrape their twitts.
  - We can analyze the pattern of their contributions by time. we can also do the analysis by geography ， since we have collect their cities.
