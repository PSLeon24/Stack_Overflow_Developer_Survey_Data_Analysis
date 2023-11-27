# Stack_Overflow_Developer_Survey_Data_Analysis

- <b>Description</b>: This repo is the 2023 Developer Survey Data Analysis Project.

## Introduction to myself
|Selfie|Name|Interests|
|:--:|:--:|:--:|
|<img height="180" src="https://github.com/PSLeon24/CEM_Community/assets/59058869/1c4a75a2-fa44-4bde-ba6f-1b9b6868de0b">|Yeong-Min Ko|AI, Computer Vision, Data Analysis|

### Data Description
![image](https://github.com/PSLeon24/Stack_Overflow_Developer_Survey_Data_Analysis/assets/59058869/367a11ea-113b-4147-898b-6a52ff3adc90)

### Schedule
|date|objective|status|
|:--:|:--:|:--:|
|23.11.18 ~ 23.11.18|Data Acquisition and Understand acquired data|O|
|23.11.19 ~ 23.11.19|Write Worksheets|O|
|23.11.20 ~ 23.11.20|Data Preprocessing|O|
|23.11.21 ~ 23.11.23|Data Visualization|O|
|23.11.24 ~ 23.12.01|Configure the Dashboard|O|
|23.12.02 ~ 23.12.08|Finish Project / Prepare a presentation|in progress|

### How To Use
Open your terminal in mac, linux or your command prompt in Windows. Then, type "Streamlit run app.py".
<img width="571" alt="스크린샷 2023-11-27 오후 11 28 31" src="https://github.com/PSLeon24/Stack_Overflow_Developer_Survey_Data_Analysis/assets/59058869/a5ce9aad-8fb9-4a3a-a7f3-236b8245bd6d">


### My Approach
- <b>Step1. Understand Data</b>
   
- <b>Step2. How to preprocess missing value</b>
<img width="504" alt="스크린샷 2023-11-28 오전 12 28 01" src="https://github.com/PSLeon24/Stack_Overflow_Developer_Survey_Data_Analysis/assets/59058869/c73d11e0-ce7e-47f5-a98e-e98ec0fdf2cb">

- <b>Step3. Write Worksheets</b>
  |No|Question|
  |:--:|:--|
  |1|해당 설문조사 응답자의 연령대와 국적은 어디가 많은가?|
  |2|설문 응답자 중 프로그래밍 언어 사용 현황과 학습 희망 프로그래밍 언어의 현황은 어떻게 되는가?|
  |3|위 질문과 마찬가지로 25~34세의 경우는 어떠한가?|
  |4|학습 자료는 어떠한 자료들을 활용할까?|
  |5|온라인 학습 자료 중에서는 어떤 자료를 가장 많이 활용할까?|
  |6|교육 수준 분포는 어떻게 될까?|
  |7|학사, 석사, 박사 학위별로 현재의 직업 분포가 어떻게 다를까?|
  |8|전체 설문 응답자의 직업 TOP3의 유형별 경력 분포는 어떻게 될까?|

- <b>Step4. Data Preprocessing</b>

|Country|LanguageHaveWorkedWith|LanguageWantToWorkWith|EdLevel|LearnCode|
|--|--|--|--|--|
|<img width="527" alt="스크린샷 2023-11-28 오전 12 30 02" src="https://github.com/PSLeon24/Stack_Overflow_Developer_Survey_Data_Analysis/assets/59058869/8afada6d-895d-4f5a-b46e-dacfbfc60427">|<img width="525" alt="스크린샷 2023-11-28 오전 12 30 16" src="https://github.com/PSLeon24/Stack_Overflow_Developer_Survey_Data_Analysis/assets/59058869/5dda4734-4192-4b6c-b3e4-e8a4ccb801f1">|<img width="531" alt="스크린샷 2023-11-28 오전 12 30 27" src="https://github.com/PSLeon24/Stack_Overflow_Developer_Survey_Data_Analysis/assets/59058869/8f878179-df54-4e71-8ec1-12f869b75953">|<img width="521" alt="스크린샷 2023-11-28 오전 12 30 41" src="https://github.com/PSLeon24/Stack_Overflow_Developer_Survey_Data_Analysis/assets/59058869/4ac36120-b747-4f54-9cf0-18fa3fcdda74">|<img width="533" alt="스크린샷 2023-11-28 오전 12 30 50" src="https://github.com/PSLeon24/Stack_Overflow_Developer_Survey_Data_Analysis/assets/59058869/5b312f31-c4dc-4a90-a3a2-9897c18b6e11">|

- <b>Step5. Configuring Dashboard using Streamlit(Data Visualization)</b>
<img src="https://github.com/PSLeon24/Stack_Overflow_Developer_Survey_Data_Analysis/blob/main/imgs/%EB%8D%B0%EC%9D%B4%ED%84%B0%EC%85%8B%20%EC%83%81%EC%9C%84%2010%EA%B0%9C%20%ED%99%95%EC%9D%B8%ED%95%98%EA%B8%B0.png"/>
<img src="https://github.com/PSLeon24/Stack_Overflow_Developer_Survey_Data_Analysis/blob/main/imgs/%EB%8D%B0%EC%9D%B4%ED%84%B0%EC%85%8B%20%EC%9A%94%EC%95%BD%20%ED%86%B5%EA%B3%84%EB%9F%89%20%ED%99%95%EC%9D%B8%ED%95%98%EA%B8%B0.png"/>
<img src="https://github.com/PSLeon24/Stack_Overflow_Developer_Survey_Data_Analysis/blob/main/imgs/%EC%97%B0%EB%A0%B9%EC%97%90%20%EB%94%B0%EB%A5%B8%20%EC%9D%91%EB%8B%B5%EC%9E%90%20%EC%88%98%EB%8A%94%20%EC%96%B4%EB%96%A0%ED%95%A0%EA%B9%8C%3F.png"/>
<img src="https://github.com/PSLeon24/Stack_Overflow_Developer_Survey_Data_Analysis/blob/main/imgs/%EC%9D%91%EB%8B%B5%20%EC%88%98%20%EC%83%81%EC%9C%84%2010%EA%B0%9C%20%EA%B5%AD%EA%B0%80%EB%8A%94%20%EC%96%B4%EB%94%94%EC%9D%BC%EA%B9%8C%3F.png"/>
<img src="https://github.com/PSLeon24/Stack_Overflow_Developer_Survey_Data_Analysis/blob/main/imgs/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D%20%EC%96%B8%EC%96%B4%20%EC%82%AC%EC%9A%A9%20%ED%98%84%ED%99%A9%EC%9D%80%20%EC%96%B4%EB%96%A0%ED%95%A0%EA%B9%8C%3F.png"/>
<img src="https://github.com/PSLeon24/Stack_Overflow_Developer_Survey_Data_Analysis/blob/main/imgs/25~34%EC%84%B8%EC%9D%98%20%EC%9D%91%EB%8B%B5%EC%9E%90%EB%93%A4%EC%9D%B4%20%EA%B0%80%EC%9E%A5%20%EB%A7%8E%EC%9D%B4%20%EC%82%AC%EC%9A%A9%ED%95%98%EB%8A%94%20%EC%96%B8%EC%96%B4%EB%8A%94%20%EB%AC%B4%EC%97%87%EC%9D%BC%EA%B9%8C%3F.png"/>
<img src="https://github.com/PSLeon24/Stack_Overflow_Developer_Survey_Data_Analysis/blob/main/imgs/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D%20%ED%95%99%EC%8A%B5%20%ED%9D%AC%EB%A7%9D%20%EC%96%B8%EC%96%B4%EB%8A%94%20%EC%96%B4%EB%96%A4%20%EC%96%B8%EC%96%B4%EC%9D%BC%EA%B9%8C%3F.png"/>
<img src="https://github.com/PSLeon24/Stack_Overflow_Developer_Survey_Data_Analysis/blob/main/imgs/25~34%EC%84%B8%EC%9D%98%20%EC%9D%91%EB%8B%B5%EC%9E%90%EB%93%A4%EC%9D%B4%20%EA%B0%80%EC%9E%A5%20%ED%95%99%EC%8A%B5%ED%95%98%EA%B8%B0%20%ED%9D%AC%EB%A7%9D%ED%95%98%EB%8A%94%20%EC%96%B8%EC%96%B4%EB%8A%94%20%EB%AC%B4%EC%97%87%EC%9D%BC%EA%B9%8C%3F.png"/>
<img src="https://github.com/PSLeon24/Stack_Overflow_Developer_Survey_Data_Analysis/blob/main/imgs/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D%EC%9D%84%20%ED%95%99%EC%8A%B5%ED%95%98%EB%8A%94%20%EB%B0%A9%EB%B2%95%EC%97%90%EB%8A%94%20%EC%96%B4%EB%96%A4%20%EA%B2%83%EB%93%A4%EC%9D%B4%20%EC%9E%88%EC%9D%84%EA%B9%8C%3F.png"/>
<img src="https://github.com/PSLeon24/Stack_Overflow_Developer_Survey_Data_Analysis/blob/main/imgs/%EC%98%A8%EB%9D%BC%EC%9D%B8%20%ED%95%99%EC%8A%B5%20%EC%9E%90%EB%A3%8C%EB%A1%9C%EB%8A%94%20%EC%96%B4%EB%96%A4%20%EA%B2%83%EB%93%A4%EC%9D%84%20%ED%99%9C%EC%9A%A9%ED%95%A0%EA%B9%8C%3F.png"/>
<img src="https://github.com/PSLeon24/Stack_Overflow_Developer_Survey_Data_Analysis/blob/main/imgs/%EC%9D%91%EB%8B%B5%EC%9E%90%EB%93%A4%EC%9D%98%20%ED%95%99%EC%9C%84%20%EB%B6%84%ED%8F%AC%EB%8A%94%20%EC%96%B4%EB%96%A0%ED%95%9C%EA%B0%80%3F.png"/>
<img src="https://github.com/PSLeon24/Stack_Overflow_Developer_Survey_Data_Analysis/blob/main/imgs/%ED%95%99%EC%82%AC%20%ED%95%99%EC%9C%84%20%EB%B3%B4%EC%9C%A0%EC%9E%90%EC%9D%98%20%EC%A7%81%EC%97%85%20%EB%B6%84%ED%8F%AC%EB%8A%94%20%EC%96%B4%EB%96%A0%ED%95%9C%EA%B0%80%3F.png"/>
<img src="https://github.com/PSLeon24/Stack_Overflow_Developer_Survey_Data_Analysis/blob/main/imgs/%EC%84%9D%EC%82%AC%20%ED%95%99%EC%9C%84%20%EB%B3%B4%EC%9C%A0%EC%9E%90%EC%9D%98%20%EC%A7%81%EC%97%85%20%EB%B6%84%ED%8F%AC%EB%8A%94%20%EC%96%B4%EB%96%A0%ED%95%9C%EA%B0%80%3F.png"/>
<img src="https://github.com/PSLeon24/Stack_Overflow_Developer_Survey_Data_Analysis/blob/main/imgs/%EB%B0%95%EC%82%AC%20%ED%95%99%EC%9C%84%20%EB%B3%B4%EC%9C%A0%EC%9E%90%EC%9D%98%20%EC%A7%81%EC%97%85%20%EB%B6%84%ED%8F%AC%EB%8A%94%20%EC%96%B4%EB%96%A0%ED%95%9C%EA%B0%80%3F.png"/>
<img src="https://github.com/PSLeon24/Stack_Overflow_Developer_Survey_Data_Analysis/blob/main/imgs/%ED%95%99%EC%9C%84%EB%B3%84%20%EC%A7%81%EC%97%85%20%EB%B6%84%ED%8F%AC%EB%8A%94%20%EC%96%B4%EB%96%A4%20%EC%B0%A8%EC%9D%B4%EA%B0%80%20%EC%9E%88%EC%9D%84%EA%B9%8C%3F_1.png"/>
<img src="https://github.com/PSLeon24/Stack_Overflow_Developer_Survey_Data_Analysis/blob/main/imgs/%ED%95%99%EC%9C%84%EB%B3%84%20%EC%A7%81%EC%97%85%20%EB%B6%84%ED%8F%AC%EB%8A%94%20%EC%96%B4%EB%96%A4%20%EC%B0%A8%EC%9D%B4%EA%B0%80%20%EC%9E%88%EC%9D%84%EA%B9%8C%3F_2.png"/>
<img src="https://github.com/PSLeon24/Stack_Overflow_Developer_Survey_Data_Analysis/blob/main/imgs/%EC%83%81%EC%9C%84%203%EA%B0%9C%20%EC%A7%81%EC%97%85%EA%B5%B0%EC%9D%98%20%EA%B2%BD%EB%A0%A5%20%EB%B6%84%ED%8F%AC%EB%8A%94%20%EC%96%B4%EB%96%A0%ED%95%9C%EA%B0%80%3F.png"/>

  
### Work Records
|date|main work|
|:--:|:--|
|23.11.18(Sat)|I created this repo.|
|23.11.18(Sat)|I acquired datasets in stack overflow.|
|23.11.19(Sun)|I writed worksheets and preprossed data.|
|23.11.20(Mon)|I created presentation resource.|
|23.11.25(Sat)|I analyzed the dataset for visualization.|
|23.11.27(Mon)|I configured the dashboard using Streamlit.|

### References
- [1] Dataset: https://insights.stackoverflow.com/survey
- [2] Streamlit: https://docs.streamlit.io/
