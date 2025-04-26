import streamlit as st
import pandas as pd
import plotly.express as px
import sqlite3
import hashlib
import matplotlib.pyplot as plt

st.markdown(
    """
    <style>
    * {
        font-family: "Constantia", sans-serif; 
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Database setup
def init_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users_1 (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT
        )
    """)
    conn.commit()
    conn.close()

# Hash passwords for security
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Register a new user
def register_user(username, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users_1 (username, password) VALUES (?, ?)", (username, hash_password(password)))
        conn.commit()
        conn.close()
        return True
    except sqlite3.IntegrityError:
        return False  # Username already exists

# Authenticate user
def authenticate(username, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM users_1 WHERE username = ?", (username,))
    stored_password = cursor.fetchone()
    conn.close()
    
    if stored_password and stored_password[0] == hash_password(password):
        return True
    return False

# Logout function
def logout():
    st.session_state.authenticated = False
    st.session_state.username = None
    # st.experimental_rerun()
    st.rerun()

# Initialize database
init_db()

# Session state initialization
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "username" not in st.session_state:
    st.session_state.username = None

# Authentication flow
if not st.session_state.authenticated:
    st.title("🔐 Login / Register")

    tab1, tab2 = st.tabs(["🔑Login", "🆕Sign Up"])

    with tab1:  # Login tab
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            if authenticate(username, password):
                st.session_state.authenticated = True
                st.session_state.username = username
                st.success(f"✅ Logged in as {username}")
                # st.experimental_rerun()
                st.rerun()
            else:
                st.error("❌ Invalid username or password")

    with tab2:  # Sign Up tab
        new_username = st.text_input("New Username")
        new_password = st.text_input("New Password", type="password")
        if st.button("Sign Up"):
            if register_user(new_username, new_password):
                st.success("✅ Account created! You can now log in.")
            else:
                st.error("⚠️ Username already taken. Choose a different one.")

else:
    # User Dashboard
    st.sidebar.write(f"👤 Logged in as: **{st.session_state.username}**")
    st.sidebar.button("🚪Logout", on_click=logout)

    # Example: Show users in the database (admin feature)
    if st.session_state.username == "admin":
        st.subheader("🔧 Admin Panel")
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id, username FROM users_1")
        users = cursor.fetchall()
        conn.close()

        st.write("📜 Registered Users:")
        for user in users:
            st.write(f"🆔 {user[0]} | 👤 {user[1]}")


    df = px.data.tips()
    column_descriptions = {
        "total_bill": "Общая сумма счета (в долларах)",
        "tip": "Сумма чаевых (в долларах)",
        "sex": "Пол (Male - мужчина, Female - женщина)",
        "smoker": "Курящий ли посетитель (Yes - да, No - нет)",
        "day": "День недели (Thur - Четверг, Fri - Пятница, Sat - Суббота, Sun - Воскресенье)",
        "time": "Время дня (Lunch - обед, Dinner - ужин)",
        "size": "Размер компании (количество человек за столом)"
    }
    
    st.markdown("<h1>Анализ данных о чаевых<br>(Tips Dataset)</h1>", unsafe_allow_html=True)
    
        
    if st.checkbox("Показать/Скрыть исходные данные."):
        st.dataframe(df)
    tab1, tab2, tab3 = st.tabs(["📊 Анализ данных", "📊 Визуализация данных", "🔍 Матрица корреляций"])
    



    with tab1:
        st.sidebar.header("Фильтр данных")
        day_filter = st.sidebar.multiselect("📅 Выберите день", list(df["day"].astype(str).unique()), default=list(df["day"].astype(str).unique()))
        gender_filter = st.sidebar.multiselect("🚻 Выберите пол", df["sex"].unique(), default=df["sex"].unique())

        filtered_data = df[(df["day"].isin(day_filter)) & (df["sex"].isin(gender_filter))]

        st.subheader("Описание столбцов")
        for col, desc in column_descriptions.items():
            st.write(f"**{col}** - {desc}")
    

        st.subheader("📋 Отфильтрованные данные")
        st.write(filtered_data)
        
        st.markdown(
            f"### 🔢 Всего строк: <span style='color:red;'>{df.shape[0]}</span>, всего столбцов: <span style='color:red;'>{df.shape[1]}</span>", 
            unsafe_allow_html=True
        )

        

        st.subheader("🔝 Первые 5 строк данных:")
        st.write(df.head())

        st.subheader("🔍 Общая информация о данных:")
        st.dataframe(df.describe())
        
        st.subheader("📈 Распределение чаевых по полу")
        st.write(df["sex"].value_counts(dropna = False))

        st.subheader("💰 Средние чаевые в зависимости от пола")
        avg_tips = df.groupby('sex')['tip'].mean().reset_index()
        st.write(avg_tips)

        
    with tab2:
        

        st.subheader("📉 Гистограмма распределения чаевых")
        fig1 = px.histogram(df, x='tip', nbins=20, title='Распределение чаевых')
        st.plotly_chart(fig1)

        st.subheader("💲 График зависимости чаевых от суммы счета")
        fig2 = px.scatter(df, x='total_bill', y='tip', color='sex', title='Чаевые vs Сумма счета',color_discrete_sequence=["red", "blue"])
        st.plotly_chart(fig2)

        st.subheader("📆 График зависимости чаевых от дня недели")
        fig3 = px.box(df, x='day', y='tip', color='day', title='Чаевые по дням недели')
        st.plotly_chart(fig3)

        st.subheader("👥 Зависимость суммы счета от размера компании")
        fig4 = px.bar(df, x='size', y='total_bill', title='Сумма счета vs Размер компании',color_discrete_sequence=["blue", "red"])
        st.plotly_chart(fig4)

        st.subheader("📊 Средний размер чаевых по дням недели")
        avg_tips = filtered_data.groupby("day")["tip"].mean()
        st.bar_chart(avg_tips)

        

    with tab3:
# Корреляционная матрица
        st.subheader("Матрица корреляции")
        corr_matrix = df.corr(numeric_only=True)
        st.write(corr_matrix.style.background_gradient(cmap='coolwarm'))

