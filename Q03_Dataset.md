# Dataset
## Q01) How would you nomalized (parsing, pre-processing, grouping) this data to simplify it’s processing into a database?

I'll nomalized data and insert into DB table as follows


| Product_id | Product | Country | Variety | Grades         | Region                        | Week       | Score |
| ---------- | ------- | ------- | ------- | -------------- | ----------------------------- | ---------- | ----- |
| INT        | VARCHAR | VARCAHR | VARCAHR | VARCAHR        | VARCHAR                       | DATE       | FLOAT |
| 99         | Avocado | Chile   | Hass    | Second Quality | Pedro Aguirre Cerda, Santiago | 2020-11-16 | 4.15  |

### 1. Product ID
I add the Product_id column. cus When extractig Data, It is less expensive to extract INT type data than VARCHAR type data.   
Product_id can be extract as a regex from the `#number` of the raw dataset   

```
product_id = re.sub(r'[^0-9]', '', string)
```
### 2. Product
Extract product using regex like product_id

```
product = re.findall(r'[A-Za-z]+', s)[0]
```
### 3. Country
Insert country column data without any preprocessing

### 4. Variety
```
Avocado / Variety / Hass
```
Among the raw data, the data corresponding Variety is Hass.   
preprocessing the data corresponding to Variety and insert in to DB.   
```
raw_variety = split "Avocado / Variety / Hass"
variety = raw_variety[2]
```
### 5. Grades
```
Avocado / Grade / Second Quality
```
Among the raw data, the data corresponding Grades is Second Quality.   
preprocessing the data corresponding to Grades and insert in to DB. 
```
raw_grades = split "Avocado / Grade / Second Quality"
grades = raw_grades[2]
```
### 6. Region
Remove the double quotes(") before and after the Region. And insert into DB

```
region = re.sub(r'["]', '', string)
```
### 7. Week
The dates scattered in several columns are gathered into one column for structural and convenient analysis.

If it is RDBMS, I'll indexing this column for analysis
### 8. Score
Honestly, I don't have a clear idea of what these numbers meant for each date.
However, considering that it is a positive float of 0 < n < 10, it is estimated that **price(dollar) or yield data**   
But I named "Score" for its versatility
## Q02) What additional value can you extract from this dataset ? If you find any please explain how would you collect it (pseudo-algorithm)
### additional column
- average annual rate
```
result <- List
for row in dataset do
    data <- Dict
    total = 0
    num = 0
    for key, value in row do
        if key is datetime
            total += value
            num ++
        else
            data[key] = value
    avg = total / num++
    data['avg'] = avg
    add data into result
``` 
And It will be able to extract various statistics from weekly score data(mothly, yearly, ovarall, .. etc)

## Q03) How would you approach the script of putting this information into a database ?(Concurrency, Scale, Prerequisites, etc..)
- Judging from the columns by the week, It is assumed that the data is not real-time data.
- Therefore, It is confirmed that data should be processed in **batch** rather than streaming
- After reading File Data using Spark(or pandas... for using dataframe for preprocessing), pre-processing and nomalizing the data, And will Bulk Upload the file type Data