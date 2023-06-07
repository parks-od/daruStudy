# :calendar: WEEK 2-1
### 1. ChatGPT 업무자동화 엑셀 더미 데이터 생성
#### 1. 구글 코랩 활용
- 온라인으로 파이썬 데이터분석 및 파이썬을 활용한 프로그램을 할 수 있는 도구
#### 2. [ChatGPT]에게 프롬프트 명령을 통한 결과 값
프롬프트 명령어 : 내 엑셀 데이터는 고객에 대한 데이터를 담고있는 시트 한개로 구성되어 있어. 엑셀 데이터는 고객의 [name. age, e-mail, login count, purchase count, total purchase amount]으로 각각의 컬럼이 구성되어 있어. 임의의 100명에 대한 데이터를 생성해서 파일로 저장하는 python zhemfmf openpyxl 라이브러리를 사용해서 만들어 줄  수 있어?
```
import random
from openpyxl import Workbook

# 랜덤한 고객 데이터 생성
def generate_customer_data():
    names = ["John", "Jane", "Mike", "Emily", "David"]
    ages = [25, 30, 35, 40, 45]
    domains = ["gmail.com", "yahoo.com", "hotmail.com"]
    
    customers = []
    for _ in range(100):
        name = random.choice(names)
        age = random.choice(ages)
        email = f"{name.lower()}_{random.randint(100, 999)}@{random.choice(domains)}"
        login_count = random.randint(1, 100)
        purchase_count = random.randint(1, 10)
        total_purchase_amount = random.randint(100, 1000)
        
        customers.append([name, age, email, login_count, purchase_count, total_purchase_amount])
    
    return customers

# 데이터를 엑셀 파일로 저장
def save_to_excel(data):
    wb = Workbook()
    ws = wb.active
    
    headers = ["Name", "Age", "E-mail", "Login Count", "Purchase Count", "Total Purchase Amount"]
    
    ws.append(headers)
    for row in data:
        ws.append(row)
    
    wb.save("customer_data.xlsx")
    print("데이터가 성공적으로 저장되었습니다.")

# 데이터 생성 및 저장
customer_data = generate_customer_data()
save_to_excel(customer_data)

```
- 팁 : 조건을 구체적으로 제시한다, 열린 질문형 보다 닫힌 지시문으로 프롬프트 작성, 쓸데없는 미사여구 사용 X

#### 3. VBA란 
Visual Basic for Application Excel과 함께 제공되며 Excel의 기능중 자동화 기능을 활용하거나 별도의 기능을 사용할 수 있는 것
Excel에 포함되어 있으므로 별도 다운로드가 필요하지 않음

프롬프트 명령어 :  login count가 10회 미만인 고객의 name과 e-mail만을 데이터로 추려내어 새로운 시트에 남길 수 있는 자동화 방법이 필요해. VBA를 통해 매크로 형식으로 만든다면 어떻게 해야할까?
```
ExtractCustomers 매크로 함수 참조
```
프롬프트 명령어 :  total purchase amount이 500000 이상인 고객의 name과 e-mail 만을 데이터로 추려내어 새로운 시트에 남길 수 있는 자동화 방법이 필요해. VBA를 통해 매크로 형식으로 만든다면 어떻게 해야할까?
```
ExtractCustomers2 매크로 함수 참조
```

# :calendar: WEEK 2-2
### 1. ChatGPT 업무자동화 메일 발송 자동
#### 1. 구글 코랩 활용
- 온라인으로 파이썬 데이터분석 및 파이썬을 활용한 프로그램을 할 수 있는 도구
#### 2. [ChatGPT]에게 프롬프트 명령을 통한 결과 값

## ⚙️ 개발 환경
- `Git & GitHub`
- **IDE** : 구글 코랩 (Colab)
- **노트북** :  macBook Air m1 (2020) 
