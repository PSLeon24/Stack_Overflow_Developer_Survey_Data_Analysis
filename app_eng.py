import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import squarify
import re

sns.set(style="whitegrid", palette="pastel")


def add_commas(s):
    return re.sub(r"(?<=\d)(?=(\d{3})+(?!\d))", ",", s)


# Streamlit 페이지 설정
st.set_page_config(
    page_title="Developer Survey Analysis",  # 페이지 타이틀 설정
    layout="wide",  # 전체 페이지 레이아웃 설정
)

st.set_option("deprecation.showPyplotGlobalUse", False)
st.markdown(
    """
    <style>
        .css-1t42vgf {
            overflow-y: hidden !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Import Data
df = pd.read_csv("./data/survey_results_public.csv")

# Data Preprocessing
# Country 변수의 결측값을 최빈값으로 대체
most_frequent_country = df["Country"].mode()[0]
df["Country"].fillna(most_frequent_country, inplace=True)

# LanguageHaveWorkedWith 변수의 결측값을 최빈값으로 대체
most_frequent_have_worked_with = df["LanguageHaveWorkedWith"].mode()[0]
df["LanguageHaveWorkedWith"].fillna(most_frequent_have_worked_with, inplace=True)

# LanguageWantToWorkWith 변수의 결측값을 최빈값으로 대체
most_frequent_want_to_work_with = df["LanguageWantToWorkWith"].mode()[0]
df["LanguageWantToWorkWith"].fillna(most_frequent_want_to_work_with, inplace=True)

# EdLevel 변수의 결측값을 최빈값으로 대체
most_frequent_ed_level = df["EdLevel"].mode()[0]
df["EdLevel"].fillna(most_frequent_ed_level, inplace=True)

# LearnCode 변수의 결측값을 최빈값으로 대체
most_frequent_learn_code = df["LearnCode"].mode()[0]
df["LearnCode"].fillna(most_frequent_learn_code, inplace=True)

revised_df = df[
    [
        "Age",
        "Country",
        "LanguageHaveWorkedWith",
        "LearnCode",
        "LearnCodeOnline",
        "LanguageWantToWorkWith",
        "EdLevel",
        "DevType",
        "WorkExp",
    ]
]


st.header("2023 Developer Survey Data Analysis")
st.subheader("Stack Overflow")

question_title = st.subheader("")  # Question Title

st.sidebar.markdown(
    "<h1 style='text-align: center;'>Data Information</h1>", unsafe_allow_html=True
)
st.sidebar.info(f"데이터셋의 행의 개수: {add_commas(str(df.shape[0]))}개")
st.sidebar.info(f"데이터셋의 열의 개수: {add_commas(str(df.shape[1]))}개")
columns_to_check = [
    "Employment",
    "RemoteWork",
    "CodingActivities",
    "EdLevel",
    "LearnCode",
    "LearnCodeOnline",
    "LearnCodeCoursesCert",
    "YearsCode",
    "YearsCodePro",
    "DevType",
    "OrgSize",
    "PurchaseInfluence",
    "TechList",
    "BuyNewTool",
    "Country",
    "Currency",
    "CompTotal",
    "LanguageHaveWorkedWith",
    "LanguageWantToWorkWith",
    "DatabaseHaveWorkedWith",
    "DatabaseWantToWorkWith",
    "PlatformHaveWorkedWith",
    "PlatformWantToWorkWith",
    "WebframeHaveWorkedWith",
    "WebframeWantToWorkWith",
    "MiscTechHaveWorkedWith",
    "MiscTechWantToWorkWith",
    "ToolsTechHaveWorkedWith",
    "ToolsTechWantToWorkWith",
    "NEWCollabToolsHaveWorkedWith",
    "NEWCollabToolsWantToWorkWith",
    "OpSysPersonal use",
    "OpSysProfessional use",
    "OfficeStackAsyncHaveWorkedWith",
    "OfficeStackAsyncWantToWorkWith",
    "OfficeStackSyncHaveWorkedWith",
    "OfficeStackSyncWantToWorkWith",
    "AISearchHaveWorkedWith",
    "AISearchWantToWorkWith",
    "AIDevHaveWorkedWith",
    "AIDevWantToWorkWith",
    "NEWSOSites",
    "SOVisitFreq",
    "SOAccount",
    "SOPartFreq",
    "SOComm",
    "SOAI",
    "AISelect",
    "AISent",
    "AIAcc",
    "AIBen",
    "AIToolInterested in Using",
    "AIToolCurrently Using",
    "AIToolNot interested in Using",
    "AINextVery different",
    "AINextNeither different nor similar",
    "AINextSomewhat similar",
    "AINextVery similar",
    "AINextSomewhat different",
    "TBranch",
    "ICorPM",
    "WorkExp",
    "Knowledge_1",
    "Knowledge_2",
    "Knowledge_3",
    "Knowledge_4",
    "Knowledge_5",
    "Knowledge_6",
    "Knowledge_7",
    "Knowledge_8",
    "Frequency_1",
    "Frequency_2",
    "Frequency_3",
    "TimeSearching",
    "TimeAnswering",
    "ProfessionalTech",
    "Industry",
    "SurveyLength",
    "SurveyEase",
    "ConvertedCompYearly",
]
selected_column_check = st.sidebar.selectbox("결측치 확인", columns_to_check)

missing_ratio = (df[selected_column_check].isna().sum() / len(df)) * 100
if missing_ratio == 0:
    st.sidebar.info(f"{selected_column_check} 변수의 결측값 비율: {missing_ratio:.2f}%")
else:
    st.sidebar.error(f"{selected_column_check} 변수의 결측값 비율: {missing_ratio:.2f}%")
st.sidebar.markdown("---")

# Sidebar
st.sidebar.markdown(
    "<h1 style='text-align: center;'>Question</h1>", unsafe_allow_html=True
)

questions = [
    "질문을 선택해주세요",
    "데이터셋 상위 10개 확인하기",
    "데이터셋 요약 통계량 확인하기",
    "연령에 따른 응답자 수는 어떠할까?",
    "응답 수 상위 10개 국가는 어디일까?",
    "프로그래밍 언어 사용 현황은 어떠할까?",
    "25~34세의 응답자들이 가장 많이 사용하는 언어는 무엇일까?",
    "프로그래밍 학습 희망 언어는 어떤 언어일까?",
    "25~34세의 응답자들이 가장 학습하기 희망하는 언어는 무엇일까?",
    "프로그래밍을 학습하는 방법에는 어떤 것들이 있을까?",
    "온라인 학습 자료로는 어떤 것들을 활용할까?",
    "응답자들의 학위 분포는 어떠한가?",
    "학사 학위 보유자의 직업 분포는 어떠한가?",
    "석사 학위 보유자의 직업 분포는 어떠한가?",
    "박사 학위 보유자의 직업 분포는 어떠한가?",
    "학위별 직업 분포는 어떤 차이가 있을까?",
    "상위 3개 직업군의 경력 분포는 어떠한가?",
]

select_question = st.sidebar.selectbox("확인하고 싶은 질문을 선택하세요.", questions)

st.sidebar.markdown("---")

st.sidebar.text("Developed by Yeongmin Ko")

# Main
if select_question == "데이터셋 상위 10개 확인하기":
    question_title.subheader(select_question)
    st.dataframe(df.head(10))

elif select_question == "데이터셋 요약 통계량 확인하기":
    question_title.subheader(select_question)
    st.dataframe(df.describe(include="all"))

elif select_question == "연령에 따른 응답자 수는 어떠할까?":
    question_title.subheader(select_question)
    # 데이터프레임에서 연령대별 응답자 수를 시각화
    size_by_age = revised_df.groupby(["Age"]).size()
    size_by_age = size_by_age.reindex(
        index=[
            "Under 18 years old",
            "18-24 years old",
            "25-34 years old",
            "35-44 years old",
            "45-54 years old",
            "55-64 years old",
            "65 years or older",
            "Prefer not to say",
        ]
    )
    translated_age_index = {
        "Under 18 years old": "Under 18 years old",
        "18-24 years old": "18-24 years old",
        "25-34 years old": "25-34 years old",
        "35-44 years old": "35-44 years old",
        "45-54 years old": "45-54 years old",
        "55-64 years old": "55-64 years old",
        "65 years or older": "65 years or older",
        "Prefer not to say": "Prefer not to say",
    }
    size_by_age.index = size_by_age.index.map(translated_age_index)

    fig, ax = plt.subplots()
    sns.barplot(
        x=size_by_age.values,
        y=size_by_age.index,
        palette="viridis",
        ax=ax,
    )
    plt.xticks(rotation=45)
    plt.title("Number of respondents by age group", fontsize=16)
    plt.xlabel("number of respondents", fontsize=10)
    plt.ylabel("age", fontsize=10)

    st.pyplot(fig)

elif select_question == "응답 수 상위 10개 국가는 어디일까?":
    question_title.subheader(select_question)
    # 국가별 응답 숫자 상위 10개국 확인
    size_by_country_top10 = (
        revised_df.groupby(["Country"]).size().sort_values(ascending=False)[:10]
    )
    new_index = [
        "United States",
        "Germany",
        "India",
        "United Kingdom",
        "Canada",
        "France",
        "Poland",
        "Netherlands",
        "Australia",
        "Brazil",
    ]
    size_by_country_top10.index = new_index

    plt.figure(figsize=(10, 6))
    sns.set_palette("pastel")

    squarify.plot(
        sizes=size_by_country_top10,
        label=size_by_country_top10.index,
        color=sns.color_palette("pastel"),
        alpha=0.7,
    )

    plt.title("Tree Map of responses from top 10 countries", fontsize=16)
    plt.axis("off")
    st.pyplot()

elif select_question == "프로그래밍 언어 사용 현황은 어떠할까?":
    question_title.subheader(select_question)
    languages = revised_df["LanguageHaveWorkedWith"]
    languages = languages.str.split(";")  # 단일 객체를 리스트로 변환
    exploded_languages = languages.explode()
    size_by_languages = (
        exploded_languages.groupby(exploded_languages)
        .size()
        .sort_values(ascending=False)
    )
    fig, axes = plt.subplots(1, 2, figsize=(18, 8))

    # 첫 번째 subplot (원형 파이 차트)
    axes[0].pie(
        x=size_by_languages[:10],
        labels=size_by_languages[:10].index,
        autopct="%1.1f%%",
        startangle=140,
    )
    axes[0].set_title("Programming Language Usage (Pie Chart)", fontsize=16)

    # 두 번째 subplot (Treemap)
    squarify.plot(
        sizes=size_by_languages[:10],
        label=size_by_languages[:10].index,
        color=sns.color_palette("pastel"),
        alpha=0.7,
        ax=axes[1],
    )
    axes[1].set_title("Programming Language Usage (Tree Map)", fontsize=16)
    axes[1].axis("off")

    st.pyplot(fig)

elif select_question == "25~34세의 응답자들이 가장 많이 사용하는 언어는 무엇일까?":
    question_title.subheader(select_question)
    languages_for_25_34 = (
        revised_df[revised_df.Age == "25-34 years old"]["LanguageHaveWorkedWith"]
        .str.split(";")
        .explode()
        .value_counts()
        .sort_values(ascending=False)
    )
    fig, axes = plt.subplots(1, 2, figsize=(18, 8))
    # 첫 번째 서브플롯 (원형 파이 차트)
    axes[0].pie(
        x=languages_for_25_34[:10],
        labels=languages_for_25_34[:10].index,
        autopct="%1.1f%%",
        startangle=140,
    )
    axes[0].set_title(
        "Programming language usage among 25-34 year olds (Pie Chart)", fontsize=16
    )

    # 두 번째 서브플롯 (트리맵)
    squarify.plot(
        sizes=languages_for_25_34[:10],
        label=languages_for_25_34[:10].index,
        color=sns.color_palette("pastel"),
        alpha=0.7,
        ax=axes[1],
    )
    axes[1].set_title(
        "Programming language usage among 25-34 year olds (Tree Map)", fontsize=16
    )
    axes[1].axis("off")

    st.pyplot(fig)

elif select_question == "프로그래밍 학습 희망 언어는 어떤 언어일까?":
    question_title.subheader(select_question)
    languages_want = (
        revised_df["LanguageWantToWorkWith"]
        .str.split(";")
        .explode()
        .value_counts()
        .sort_values(ascending=False)
    )
    fig, axes = plt.subplots(1, 2, figsize=(18, 8))

    # 첫 번째 서브 플롯 (원형 파이 차트)
    axes[0].pie(
        x=languages_want[:10],
        labels=languages_want[:10].index,
        autopct="%1.1f%%",
        startangle=140,
    )
    axes[0].set_title(
        "Programming language learning desire status (Pie Chart)", fontsize=16
    )

    # 두 번째 서브플롯 (트리맵)
    squarify.plot(
        sizes=languages_want[:10],
        label=languages_want[:10].index,
        color=sns.color_palette("pastel"),
        alpha=0.7,
        ax=axes[1],
    )
    axes[1].set_title(
        "Programming language learning desire status (Tree Map)", fontsize=16
    )
    axes[1].axis("off")

    st.pyplot(fig)

elif select_question == "25~34세의 응답자들이 가장 학습하기 희망하는 언어는 무엇일까?":
    question_title.subheader(select_question)
    languages_want_for_25_34 = (
        revised_df[revised_df.Age == "25-34 years old"]["LanguageWantToWorkWith"]
        .str.split(";")
        .explode()
        .value_counts()
        .sort_values(ascending=False)
    )
    fig, axes = plt.subplots(1, 2, figsize=(18, 8))
    # 첫 번째 서브플롯 (원형 파이 차트)
    axes[0].pie(
        x=languages_want_for_25_34[:10],
        labels=languages_want_for_25_34[:10].index,
        autopct="%1.1f%%",
        startangle=140,
    )
    axes[0].set_title(
        "Current status of programming language learning desires among 25-34 year olds (Pie Chart)",
        fontsize=16,
    )

    # 두 번째 서브플롯 (트리맵)
    squarify.plot(
        sizes=languages_want_for_25_34[:10],
        label=languages_want_for_25_34[:10].index,
        color=sns.color_palette("pastel"),
        alpha=0.7,
        ax=axes[1],
    )
    axes[1].set_title(
        "Current status of programming language learning desires among 25-34 year olds (Tree Map)",
        fontsize=16,
    )
    axes[1].axis("off")

    st.pyplot(fig)

elif select_question == "프로그래밍을 학습하는 방법에는 어떤 것들이 있을까?":
    question_title.subheader(select_question)
    learnCode = revised_df["LearnCode"].str.split(";")
    exploded_learnCode = learnCode.explode()
    translated_dict = {
        "Other online resources (e.g., videos, blogs, forum)": "Other online resources (e.g., videos, blogs, forum)",
        "Books / Physical media": "Books / Physical media",
        "School (i.e., University, College, etc)": "School (i.e., University, College, etc)",
        "Online Courses or Certification": "Online Courses or Certification",
        "On the job training": "On the job training",
        "Colleague": "Colleague",
        "Friend or family member": "Friend or family member",
        "Coding Bootcamp": "Coding Bootcamp",
        "Hackathons (virtual or in-person)": "Hackathons (virtual or in-person)",
        "Other (please specify):": "Other",
    }

    exploded_learnCode = exploded_learnCode.map(translated_dict)
    exploded_learnCode.value_counts().plot.pie(autopct="%1.01f%%")
    plt.title("Learning method distribution", fontsize=16)
    st.pyplot()

elif select_question == "온라인 학습 자료로는 어떤 것들을 활용할까?":
    question_title.subheader(select_question)
    learnCodeOnline = revised_df["LearnCodeOnline"].str.split(";")
    exploded_learnCodeOnline = learnCodeOnline.explode()
    unique_values = exploded_learnCodeOnline.unique()
    translated_index = {
        "Formal documentation provided by the owner of the tech": "Formal documentation provided by the owner of the tech",
        "Stack Overflow": "Stack Overflow",
        "Blogs with tips and tricks": "Blog resources",
        "How-to videos": "How-to videos",
        "Written Tutorials": "Written Tutorials",
        "Video-based Online Courses": "Video-based Online Courses",
        "Books": "Books",
        "Click to write Choice 20": "Click to write Choice 20",
        "Written-based Online Courses": "Written-based Online Courses",
        "Recorded coding sessions": "Recorded coding sessions",
        "Interactive tutorial": "Interactive tutorial",
        "Online challenges (e.g., daily or weekly coding challenges)": "Online challenges (e.g., daily or weekly coding challenges)",
        "Certification videos": "Certification videos",
        "Auditory material (e.g., podcasts)": "Auditory material (e.g., podcasts)",
        "Programming Games": "Programming Games",
        "Other (Please specify):": "Other",
    }

    exploded_learnCodeOnline = exploded_learnCodeOnline.value_counts().rename(
        index=translated_index
    )
    exploded_learnCodeOnline.sort_values(ascending=True).plot.barh()

    plt.title("online learning resources", fontsize=16)
    plt.xlabel("Number of people (persons)")
    st.pyplot()

elif select_question == "응답자들의 학위 분포는 어떠한가?":
    question_title.subheader(select_question)
    ed_level_counts = revised_df["EdLevel"].value_counts()
    # 인덱스명을 한글로 변경
    ed_level_counts.index = [
        "Bachelor's degree",
        "master degree",
        "Completion of college courses without a degree",
        "Secondary education (middle school and high school graduate)",
        "Ph.D. degree (JD, MD, Ph.D, Ed.D, etc.)",
        "Professional Bachelor’s Degree (A.A., A.S., etc.)",
        "Graduated from elementary school",
        "etc",
    ]

    sns.barplot(x=ed_level_counts, y=ed_level_counts.index)
    plt.xlabel("Number of people (persons)")
    plt.title("Education level distribution", fontsize=16)

    st.pyplot()

elif select_question == "학사 학위 보유자의 직업 분포는 어떠한가?":
    question_title.subheader(select_question)

    # 학사 학위를 가진 사람들의 직업 유형 Top10
    bachelor_data = revised_df[
        revised_df["EdLevel"] == "Bachelor’s degree (B.A., B.S., B.Eng., etc.)"
    ]
    bachelor_job_counts = bachelor_data["DevType"].value_counts()

    bachelor_data["DevType"].value_counts().head(10)
    # 학사 학위를 가진 사람들의 데이터 추출
    bachelor_data = revised_df[
        revised_df["EdLevel"] == "Bachelor’s degree (B.A., B.S., B.Eng., etc.)"
    ]

    # 학사 학위를 가진 사람들의 직업 빈도수 계산
    bachelor_job_counts = bachelor_data["DevType"].value_counts().head(10)

    translated_index = {
        "Developer, full-stack": "full-stack developer",
        "Developer, back-end": "Backend developer",
        "Developer, front-end": "Front-end developer",
        "Developer, desktop or enterprise applications": "Desktop or enterprise application developer",
        "Developer, mobile": "Mobile developer",
        "Other (please specify):": "Other ",
        "Engineering manager": "Engineering manager",
        "Developer, embedded applications or devices": "Embedded developer",
        "DevOps specialist": "DevOps specialist",
        "Engineer, data": "data engineer",
    }

    bachelor_job_counts.index = bachelor_job_counts.index.map(translated_index)

    plt.figure(figsize=(12, 8))

    sns.barplot(x=bachelor_job_counts, y=bachelor_job_counts.index, palette="viridis")

    plt.title("Occupation distribution of bachelor's degree holders", fontsize=16)

    plt.xlabel("Number of people (people)")
    plt.ylabel("Occupation")
    st.pyplot()

elif select_question == "석사 학위 보유자의 직업 분포는 어떠한가?":
    question_title.subheader(select_question)

    # 석사 학위를 가진 사람들의 직업 유형 Top10
    master_data = revised_df[
        revised_df["EdLevel"] == "Master’s degree (M.A., M.S., M.Eng., MBA, etc.)"
    ]
    master_job_counts = master_data["DevType"].value_counts()

    translated_index = {
        "Developer, full-stack": "full-stack developer",
        "Developer, back-end": "Backend developer",
        "Developer, desktop or enterprise applications": "Desktop or enterprise application developer",
        "Developer, front-end": "Front-end developer",
        "Other (please specify):": "Other",
        "Data scientist or machine learning specialist": "Data scientist or machine learning specialist",
        "Developer, mobile": "Mobile developer",
        "Engineering manager": "Engineering manager",
        "Developer, embedded applications or devices": "Embedded developer",
        "Academic researcher": "academic researcher",
    }

    master_job_counts.index = master_job_counts.index.map(translated_index)
    plt.figure(figsize=(12, 8))

    sns.barplot(x=master_job_counts, y=master_job_counts.index, palette="viridis")

    plt.title("Occupation distribution of master's degree holders", fontsize=16)

    plt.xlabel("Number of people (people)")
    plt.ylabel("Occupation")
    st.pyplot()

elif select_question == "박사 학위 보유자의 직업 분포는 어떠한가?":
    question_title.subheader(select_question)

    # 박사 학위를 가진 사람들의 직업 유형 Top10
    professional_data = revised_df[
        revised_df["EdLevel"] == "Professional degree (JD, MD, Ph.D, Ed.D, etc.)"
    ]
    professional_job_counts = professional_data["DevType"].value_counts()

    # 주어진 인덱스와 대응할 한글 인덱스 딕셔너리
    translated_index = {
        "Developer, full-stack": "full-stack developer",
        "Academic researcher": "academic researcher",
        "Developer, back-end": "Backend developer",
        "Data scientist or machine learning specialist": "Data scientist or machine learning specialist",
        "Research & Development role": "Researcher and developer",
        "Scientist": "scientist",
        "Other (please specify):": "Other",
        "Developer, desktop or enterprise applications": "Desktop or enterprise application developer",
        "Senior Executive (C-Suite, VP, etc.)": "Senior Executive (CEO, VP, etc.)",
        "Educator": "Educator",
    }

    professional_job_counts.index = professional_job_counts.index.map(
        translated_index
    )  # 데이터프레임의 인덱스를 한글로 변경
    plt.figure(figsize=(12, 8))

    sns.barplot(
        x=professional_job_counts, y=professional_job_counts.index, palette="viridis"
    )

    plt.title("Occupation distribution of PhD holders", fontsize=16)

    plt.xlabel("Number of people (people)")
    plt.ylabel("Occupation")

    st.pyplot()

elif select_question == "학위별 직업 분포는 어떤 차이가 있을까?":
    question_title.subheader(select_question)

    plt.figure(figsize=(10, 18))

    # 학사 학위를 가진 사람들의 직업 유형 Top10
    bachelor_data = revised_df[
        revised_df["EdLevel"] == "Bachelor’s degree (B.A., B.S., B.Eng., etc.)"
    ]
    bachelor_job_counts = bachelor_data["DevType"].value_counts()

    bachelor_data["DevType"].value_counts().head(10)
    # 학사 학위를 가진 사람들의 데이터 추출
    bachelor_data = revised_df[
        revised_df["EdLevel"] == "Bachelor’s degree (B.A., B.S., B.Eng., etc.)"
    ]

    # 학사 학위를 가진 사람들의 직업 빈도수 계산
    bachelor_job_counts = bachelor_data["DevType"].value_counts().head(10)

    translated_index = {
        "Developer, full-stack": "full-stack developer",
        "Developer, back-end": "Backend developer",
        "Developer, front-end": "Front-end developer",
        "Developer, desktop or enterprise applications": "Desktop or enterprise application developer",
        "Developer, mobile": "Mobile developer",
        "Other (please specify):": "Other ",
        "Engineering manager": "Engineering manager",
        "Developer, embedded applications or devices": "Embedded developer",
        "DevOps specialist": "DevOps specialist",
        "Engineer, data": "data engineer",
    }

    bachelor_job_counts.index = bachelor_job_counts.index.map(translated_index)

    # 첫 번째 subplot: 학사 학위자의 직업 분포
    plt.subplot(3, 1, 1)
    sns.barplot(x=bachelor_job_counts, y=bachelor_job_counts.index, palette="viridis")
    plt.title("Occupation distribution of bachelor's degree holders", fontsize=16)
    plt.xlabel("Number of people (people)")
    plt.ylabel("Occupation")
    max_count = bachelor_job_counts.max() + 1000
    plt.xlim(0, max_count)

    # 석사 학위를 가진 사람들의 직업 유형 Top10
    master_data = revised_df[
        revised_df["EdLevel"] == "Master’s degree (M.A., M.S., M.Eng., MBA, etc.)"
    ]
    master_job_counts = master_data["DevType"].value_counts()

    translated_index = {
        "Developer, full-stack": "full-stack developer",
        "Developer, back-end": "Backend developer",
        "Developer, desktop or enterprise applications": "Desktop or enterprise application developer",
        "Developer, front-end": "Front-end developer",
        "Other (please specify):": "Other",
        "Data scientist or machine learning specialist": "Data scientist or machine learning specialist",
        "Developer, mobile": "Mobile developer",
        "Engineering manager": "Engineering manager",
        "Developer, embedded applications or devices": "Embedded developer",
        "Academic researcher": "academic researcher",
    }

    master_job_counts.index = master_job_counts.index.map(
        translated_index
    )  # 데이터프레임의 인덱스를 한글로 변경

    # 두 번째 subplot: 석사 학위자의 직업 분포
    plt.subplot(3, 1, 2)
    sns.barplot(x=master_job_counts, y=master_job_counts.index, palette="viridis")
    plt.title("Occupation distribution of master's degree holders", fontsize=16)
    plt.xlabel("Number of people (people)")
    plt.ylabel("Occupation")
    max_count = (
        max(
            bachelor_job_counts.max(),
            master_job_counts.max(),
        )
        + 1000
    )
    plt.xlim(0, max_count)

    # 박사 학위를 가진 사람들의 직업 유형 Top10
    professional_data = revised_df[
        revised_df["EdLevel"] == "Professional degree (JD, MD, Ph.D, Ed.D, etc.)"
    ]
    professional_job_counts = professional_data["DevType"].value_counts()

    # 주어진 인덱스와 대응할 한글 인덱스 딕셔너리
    translated_index = {
        "Developer, full-stack": "full-stack developer",
        "Academic researcher": "academic researcher",
        "Developer, back-end": "Backend developer",
        "Data scientist or machine learning specialist": "Data scientist or machine learning specialist",
        "Research & Development role": "Researcher and developer",
        "Scientist": "scientist",
        "Other (please specify):": "Other",
        "Developer, desktop or enterprise applications": "Desktop or enterprise application developer",
        "Senior Executive (C-Suite, VP, etc.)": "Senior Executive (CEO, VP, etc.)",
        "Educator": "Educator",
    }

    professional_job_counts.index = professional_job_counts.index.map(translated_index)

    # 세 번째 subplot: 박사 학위자의 직업 분포
    plt.subplot(3, 1, 3)
    sns.barplot(
        x=professional_job_counts, y=professional_job_counts.index, palette="viridis"
    )
    plt.title("Occupation distribution of PhD holders", fontsize=16)
    plt.xlabel("Number of people (people)")
    plt.ylabel("Occupation")

    max_count = (
        max(
            bachelor_job_counts.max(),
            master_job_counts.max(),
            professional_job_counts.max(),
        )
        + 1000
    )
    plt.xlim(0, max_count)

    st.pyplot()

elif select_question == "상위 3개 직업군의 경력 분포는 어떠한가?":
    question_title.subheader(select_question)
    # 상위 3개의 개발 유형을 추출
    top_devtypes = revised_df["DevType"].value_counts().head(3).index

    # 개발 유형을 기준으로 그룹화 (상위 3개만 선택)
    grouped_by_devtype = revised_df[revised_df["DevType"].isin(top_devtypes)].groupby(
        "DevType"
    )

    # 색상 리스트 정의
    colors = ["blue", "white", "orange"]

    # 각 DevType에 대한 경력 분포 시각화
    plt.figure(figsize=(12, 8))
    for i, (devtype, data) in enumerate(grouped_by_devtype):
        sns.histplot(
            data=data,
            x="WorkExp",
            label=devtype,
            kde=True,
            bins=20,
            alpha=0.5,
            color=colors[i],
        )

    plt.title("Experience distribution by top 3 job types", fontsize=16)
    plt.xlabel("Experience (years)")
    plt.ylabel("Number of people (people)")
    plt.legend(title="DevType", bbox_to_anchor=(1.05, 1), loc="upper right")

    st.pyplot()
