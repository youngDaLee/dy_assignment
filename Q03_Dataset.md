# Dataset
## Q01) How would you nomalized (parsing, pre-processing, grouping) this data to simplify it’s processing into a database?

아래와 같은 형식으로 DB에 데이터를 정규화 할 것 입니다.

| Product_id | Product | Country | Variety | Grades         | Region                        | Week       | Score |
| ---------- | ------- | ------- | ------- | -------------- | ----------------------------- | ---------- | ----- |
| INT        | VARCHAR | VARCAHR | VARCAHR | VARCAHR        | VARCHAR                       | DATE       | FLOAT |
| 99         | Avocado | Chile   | Hass    | Second Quality | Pedro Aguirre Cerda, Santiago | 2020-11-16 | 4.15  |

### 1. Product ID
데이터 추출 시, VARCHAR 형태 보다는 INT형 데이터를 추출하는 것이 비용이 적기 때문에, Product ID 컬럼을 추가했습니다.   
Product ID는 raw 데이터셋의 #number 에서 정규식으로 추출 가능합니다.

```
product_id = re.sub(r'[^0-9]', '', string)
```
### 2. Product
product_id와 마찬가지로, 정규식을 사용해 product name을 추출 가능합니다.

```
product = re.findall(r'[A-Za-z]+', s)[0]
```
### 3. Country
특별한 전처리 과정 없이 기존 column raw 데이터를 인서트 해 줍니다

### 4. Variety
```
Avocado / Variety / Hass
```

위의 raw 데이터 중 실제 Variety 에 해당하는 데이터는 Hass 입니다. Variety에 해당하는 데이터를 pre-processing 하여 데이터 인서트를 합니다. 아래는 psudo-code 입니다.
```
raw_variety = split "Avocado / Variety / Hass"
variety = raw_variety[2]
```
### 5. Grades
```
Avocado / Grade / Second Quality
```

Variety와 마찬가지로 위의 raw 데이터 중 실제 Grade 에 해당하는 데이터는 Second Quality 입니다. Grade 해당하는 데이터를 pre-processing 하여 데이터 인서트를 합니다. 아래는 psudo-code 입니다.
```
raw_grades = split "Avocado / Grade / Second Quality"
grades = raw_grades[2]
```
### 6. Region
Region 앞뒤의 큰따옴표를 제거하여 데이터 인서트 해 줍니다.

```
region = re.sub(r'["]', '', string)
```
### 7. Week
날짜별 분석을 위해 인덱스를 걸 것 같습니다.

### 8. Score
사실 이 각 날짜에 대한 이 숫자가 어떤 것을 의미하는지에 대해서는 명확하게 파악하기 못했습니다.
다만 0이상 10미만의 양수 float인 것으로 보아, 가격(달러) 혹은 수확량 데이터 일 것으로 추측합니다.

## Q02) What additional value can you extract from this dataset ? If you find any please explain how would you collect it (pseudo-algorithm)
- 

## Q03) How would you approach the script of putting this information into a database ?(Concurrency, Scale, Prerequisites, etc..)
- 일주일 단위로 나뉘어진 컬럼으로 추측해 봤을 때, 해당 데이터는 실시간으로 변동되는 데이터는 아닐 것으로 추측됩니다.
- 따라서 스트리밍 처리 보다는 배치 형식으로 데이터를 처리해야 할 것으로 확인됩니다.
- 파일 데이터를 spark 등을 이용하여 읽어들인 뒤, 적절하게 데이터 pre-processing 및 nomalizing을 한 뒤, 파일 형식 데이터를 bulk upload 할 것 입니다.
