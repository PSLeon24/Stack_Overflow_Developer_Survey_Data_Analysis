import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import squarify
import re

sns.set(style="whitegrid", font="AppleGothic", palette="pastel")


def add_commas(s):
    return re.sub(r"(?<=\d)(?=(\d{3})+(?!\d))", ",", s)


# Streamlit 페이지 설정
st.set_page_config(
    page_title="Developer Survey Analysis",  # 페이지 타이틀 설정
    layout="wide",  # 전체 페이지 레이아웃 설정
)
st.set_option("deprecation.showPyplotGlobalUse", False)

# Import Data
df = pd.read_csv("./data/survey_results_public.csv")

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

# 대체 후 결측값 비율 재확인
missing_country_percentage_after_fillna = (
    df["Country"].isna().sum() / len(df["Country"])
) * 100
missing_have_worked_with_percentage_after_fillna = (
    df["LanguageHaveWorkedWith"].isna().sum() / len(df["LanguageHaveWorkedWith"])
) * 100
missing_want_to_work_with_percentage_after_fillna = (
    df["LanguageWantToWorkWith"].isna().sum() / len(df["LanguageWantToWorkWith"])
) * 100
missing_ed_level_percentage_after_fillna = (
    df["EdLevel"].isna().sum() / len(df["EdLevel"])
) * 100
missing_learn_code_percentage_after_fillna = (
    df["LearnCode"].isna().sum() / len(df["LearnCode"])
) * 100

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

st.sidebar.markdown(
    "<h1 style='text-align: center;'>Data Information</h1>", unsafe_allow_html=True
)
st.sidebar.text(f"데이터셋의 행의 개수: {add_commas(str(df.shape[0]))}개")
st.sidebar.text(f"데이터셋의 열의 개수: {add_commas(str(df.shape[1]))}개")
st.sidebar.selectbox("컬럼명 확인", df.columns.tolist())
st.sidebar.markdown("---")

# Sidebar
st.sidebar.markdown(
    "<h1 style='text-align: center;'>Question</h1>", unsafe_allow_html=True
)

questions = [
    "질문을 선택해주세요",
    "데이터셋 상위 10개 확인하기",
    "데이터셋 요약통계량 확인하기",
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
    "상위 10개 직업군의 경력 분포는 어떠한가?",
]

select_question = st.sidebar.selectbox("확인하고 싶은 질문을 선택하세요.", questions)

st.sidebar.markdown("---")

st.sidebar.text("Made by Yeongmin Ko")

# Main
if select_question == "데이터셋 상위 10개 확인하기":
    st.dataframe(df.head(10))

elif select_question == "데이터셋 요약통계량 확인하기":
    st.dataframe(df.describe(include="all"))

elif select_question == "연령에 따른 응답자 수는 어떠할까?":
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
        "Under 18 years old": "18세 미만",
        "18-24 years old": "18-24세",
        "25-34 years old": "25-34세",
        "35-44 years old": "35-44세",
        "45-54 years old": "45-54세",
        "55-64 years old": "55-64세",
        "65 years or older": "65세 이상",
        "Prefer not to say": "응답하지 않음",
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
    plt.title("연령대별 응답자 수", fontsize=16)
    plt.xlabel("응답자 수", fontsize=10)
    plt.ylabel("연령", fontsize=10)

    st.pyplot(fig)

elif select_question == "응답 수 상위 10개 국가는 어디일까?":
    # 국가별 응답 숫자 상위 10개국 확인
    size_by_country_top10 = (
        revised_df.groupby(["Country"]).size().sort_values(ascending=False)[:10]
    )
    new_index = ["미국", "독일", "인도", "영국", "캐나다", "프랑스", "폴란드", "네덜란드", "호주", "브라질"]
    size_by_country_top10.index = new_index

    plt.figure(figsize=(10, 6))
    sns.set_palette("pastel")

    ax = squarify.plot(
        sizes=size_by_country_top10,
        label=size_by_country_top10.index,
        color=sns.color_palette("pastel"),
        alpha=0.7,
    )

    plt.title("상위 10개 국가의 응답 수 트리맵", fontsize=16)
    plt.axis("off")
    st.pyplot()

elif select_question == "프로그래밍 언어 사용 현황은 어떠할까?":
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
    axes[0].set_title("프로그래밍 언어 사용 현황 (파이 차트)", fontsize=16)

    # 두 번째 subplot (Treemap)
    squarify.plot(
        sizes=size_by_languages[:10],
        label=size_by_languages[:10].index,
        color=sns.color_palette("pastel"),
        alpha=0.7,
        ax=axes[1],
    )
    axes[1].set_title("프로그래밍 언어 사용 현황 (트리맵)", fontsize=16)
    axes[1].axis("off")

    st.pyplot(fig)

elif select_question == "25~34세의 응답자들이 가장 많이 사용하는 언어는 무엇일까?":
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
    axes[0].set_title("25~34세의 프로그래밍 언어 사용 현황 (파이차트)", fontsize=16)

    # 두 번째 서브플롯 (트리맵)
    squarify.plot(
        sizes=languages_for_25_34[:10],
        label=languages_for_25_34[:10].index,
        color=sns.color_palette("pastel"),
        alpha=0.7,
        ax=axes[1],
    )
    axes[1].set_title("25~34세의 프로그래밍 언어 사용 현황 (트리맵)", fontsize=16)
    axes[1].axis("off")

    st.pyplot(fig)

elif select_question == "프로그래밍 학습 희망 언어는 어떤 언어일까?":
    languages_want = (
        revised_df["LanguageWantToWorkWith"]
        .str.split(";")
        .explode()
        .value_counts()
        .sort_values(ascending=False)
    )
    fig, axes = plt.subplots(1, 2, figsize=(18, 8))

    # 첫 번째 subplot (원형 파이 차트)
    axes[0].pie(
        x=languages_want[:10],
        labels=languages_want[:10].index,
        autopct="%1.1f%%",
        startangle=140,
    )
    axes[0].set_title("프로그래밍 언어 학습 희망 현황 (파이 차트)", fontsize=16)

    # 두 번째 subplot (Treemap)
    squarify.plot(
        sizes=languages_want[:10],
        label=languages_want[:10].index,
        color=sns.color_palette("pastel"),
        alpha=0.7,
        ax=axes[1],
    )
    axes[1].set_title("프로그래밍 언어 학습 희망 현황 (트리맵)", fontsize=16)
    axes[1].axis("off")

    st.pyplot(fig)
