# python data assignments mission list

## Assignment 0 -- Bridging assignment for language efficiency

Deadline: **Oct 24, 2018 (Wed)**

- [x] Read all the `.txt` files in folder `assignment0/`. (consider `open().read()`; You can use a `list` to store the relative paths of the files first)
- [x] For every file, extract the English words from the file content. (consider `str.split()`)
- [x] For every word extracted above, count how many times each one appears. (consider to use `dict`; keys are keywords; values are word count)
- [x] Rank the keywords from higher frequency to lower frequency. Only `print` the top 15 keywords on Terminal. (consider `sorted()` and list slicing)
- [x] Output the full keyword frequency list into a CSV file. The table headers are `keyword,frequency`. (consider to use `csv`)

### Bonus: Handle the stop words
- [x] Can you remove the stop words from above Terminal output, as well as the CSV file?
- [x] Can you further enrich this `stop_words` list to make the output more meaningful?

### Bonus: Discussion or demo

To address following questions, you can choose to simply discuss the solution in your `README.md` file or give a working demo using codes:

- [x] If you spotted one interesting keyword from the top list, how do you locate this keyword in articles? i.e. Find which article and which paragraph contains the keyword.
- [ ] Can you further organise your code for future reuse? One example of reusable piece is the keyword extraction from one string. Another example is the keyword extraction from one file. You can consider to put those in functions.
- [ ] There are two ways to approach the above problem: 1) assemble the content of all 5 files and extract keyword list for one string; 2) extract keyword-frequency list for all 5 files first and then merge the keyword-frequency (may need to sum the count for the same keyword). Which did you use? Which way is better? And Why?

### further plans
- [ ] I must write something in readme
- [ ] learn visualisation to make data organised
- [ ] I can try text analysis
- [ ] learn how to use 'try' in case some input problems
