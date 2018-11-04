# python-data-assignments
## Assignment 0 -- Bridging assignment for language efficiency

### Indroduction
  - I finish this assignment with this functions os.listdir,pandas,csv,string.punctuation. The keywords_frequency.ipynb is the mainstream and the keywords_location.ipynb is to locate a keyword. You can check the codes and outputs in the hyperlinks below.

- The integrated codes
  - [keywords.py](https://github.com/FLYSTEPHEN/python-data-assignments/blob/master/assignment0/keywords.py)

- Output:
  - [keywords_frequency.ipynb](https://github.com/FLYSTEPHEN/python-data-assignments/blob/master/assignment0/keywords_frequency.ipynb)
  - [keywords_frequency.csv](https://github.com/FLYSTEPHEN/python-data-assignments/blob/master/assignment0/keywords_frequency.csv)
  - [keywords_location.ipynb](https://github.com/FLYSTEPHEN/python-data-assignments/blob/master/assignment0/keywords_location.ipynb)
  - [keywords_location.csv](https://github.com/FLYSTEPHEN/python-data-assignments/blob/master/assignment0/keywords_location.csv)


### Mission List
- [x] Read all the `.txt` files in folder `assignment0/`.
  - Use `os.listdir` function to read all the file path firstly. Then it will be easy to use `str.find(.txt)` to locate all the txt files. Remember to remove `stoplist.txt`
  
- [x] For every file, extract the English words from the file content. 
  - Just use `.split()` function to transfer the text into a list of words.

- [x] For every word extracted above, count how many times each one appears. 
  ```bash
  for m in list:
      dict_words_frequency[m]=list.count(m)
  ```
  - Use the lines above to solve this question.
  
- [x] Rank the keywords from higher frequency to lower frequency.
  ```bash
  def rank_frequency(dict): #根據frequency排序，也可以最後用print(s.sort_values(ascending=False))，但是不方便寫cvs
      dict_frequency_rank={}
      rank = sorted(dict.items(), key=lambda item: item[1], reverse=True) 
      #將字典轉化爲二元數組，並根據字典中value排序
      for m in range(0,len(rank)):
          dict_frequency_rank.update({rank[m][0]:rank[m][1]})
      #再將字典重新整合起來
      return dict_frequency_rank
   ```
  - It transfers the dictionary into a list of two-element arrays, then we can sort the list by the second element of each item. Afterwards, we can combine the ranked list into dictionary again.
   
- [x] Output the full keyword frequency list into a CSV file. The table headers are `keyword,frequency`. 

- [x] Only `print` the top 15 keywords on Terminal.
  - use `.head(15)`
  
### Bonus: Handle the stop words
- [x] Can you remove the stop words from above Terminal output, as well as the CSV file?
  - I wrote a txt file containing the stopwords I defined. Then I can read the txt and use this line: `if m not in list_stop_words` with a for loop to check if the words being counted in the stopwords list. 
  
- [x] Can you further enrich this `stop_words` list to make the output more meaningful?
  - Enriching the list is easy since it is in a form of txt file that we just need to add some common prep. or num. or pron. into the file. The question is although a stoplist of words has been created, it is still difficult to expel some punctuations, Capitals, and words with 's. I defined a function to address this problem, where I used str.translator, str.lower and str.replace("’s","").
  
### Bonus: Discussion or demo

- [x] To address following questions, you can choose to simply discuss the solution in your `README.md` file or give a working demo using codes:

- [x] If you spotted one interesting keyword from the top list, how do you locate this keyword in articles? i.e. Find which article and which paragraph contains the keyword.
  - [keywords_location.ipynb](https://github.com/FLYSTEPHEN/python-data-assignments/blob/master/assignment0/keywords_location.ipynb)

- [ ] Can you further organise your code for future reuse? One example of reusable piece is the keyword extraction from one string. Another example is the keyword extraction from one file. You can consider to put those in functions.

- [x] There are two ways to approach the above problem: 1) assemble the content of all 5 files and extract keyword list for one string; 2) extract keyword-frequency list for all 5 files first and then merge the keyword-frequency (may need to sum the count for the same keyword). Which did you use? Which way is better? And Why?
  - I think the first one is better since we can use the unmerged data to do further analysis.

### Future
- [ ] I can try text analysis
- [ ] learn how to use 'try' in case some input problems
- [ ] use class

## Assignment 1 -- Data collection and ideation

Deadline: **Nov 9, 2018 (Fri)**

- [x] Collect your **original** data by one of the following two ways:

- Scraping static website (requests + beautiful soup)
- Scraping a dynamic website (selenium/ splinter)

Requirement:

- [x] The dataset needs to contain more than **100** entries and more than **5** fields.
- [x] In the `README.md` file, give information about your dataset, so people can quickly understand the content without looking into your CSV file. You can include those sections: 1) topic ; 2) data source; 3) data fields (type, sample data); 4) data volume; 5) **license**.

### Bonus: Enrich your dataset

enrich your dataset:

- You can download data set from [gov open data portals](https://data.gov.hk/en/), [research institutes](https://ourworldindata.org/), or [any collection](https://github.com/awesomedata/awesome-public-datasets) that you can verify. You don't have to actually download the data in this bonus question, because some dataset is too large to be put onto GitHub repo. Simply give pointers to the database you are considering and briefly describe how they can be incorporated into the dataset you just scraped or how they can assist your articulation.
- You can get some related data via [HTTP based API](https://earthquake.usgs.gov/fdsnws/event/1/). Please tell us what is the API, give a few (truncated) sample responses, and discuss how that data can potentially help your data-driven report.
