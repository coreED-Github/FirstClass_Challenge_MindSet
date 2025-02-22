import streamlit as st
import random
import emoji
import datetime
import pandas as pd
import plotly.express as px
from database import create_table, save_challenge, get_user_challenges, delete_challenge  

# ✅ Ensure the table is created before any operation
create_table()

# Initialize session state
if "page" not in st.session_state:
    st.session_state.page = "home"
if "prev_page" not in st.session_state:
    st.session_state.prev_page = None  # For tracking previous page

# Sidebar
with st.sidebar:
    st.markdown("<h2 style='text-align: center;'>🚀 Growth Mindset Challenges</h2>", unsafe_allow_html=True)
    
    if st.button("🏠 Home", key="sidebar_home"):
        st.session_state.prev_page = st.session_state.page
        st.session_state.page = "home"
        st.rerun()
    
    if st.session_state.page != "home" and st.button("⬅ Back", key="sidebar_back"):
        st.session_state.page = st.session_state.prev_page if st.session_state.prev_page else "home"
        st.rerun()

# Quotes and Challenges
quotes = [
    emoji.emojize("💡 Mistakes are proof that you are trying."),
    emoji.emojize("💪 Challenges help you grow stronger."),
    emoji.emojize("🚀 Believe you can, and you're halfway there."),
]

challenges = [
    "Write down one thing you struggled with today and how you handled it.",
    "Learn a new skill today, no matter how small.",
    "Practice gratitude: List three things you're grateful for today.",
]

# Home Page
if st.session_state.page == "home":
    st.title("Growth Mindset Challenge")
    name = st.text_input("Enter your name:")
    st.warning("If you want to continue your 30-day challenge, it is necessary to keep the same email.")
    email = st.text_input("Enter your email:")

    if st.button("🚀 Get The Challenge", key="get_challenge"):
        if name and email:
            st.session_state.prev_page = "home"
            st.session_state.name = name
            st.session_state.email = email
            st.session_state.page = "welcome"
            st.rerun()
        else:
            st.warning("Please enter both your name and email.")


# Welcome Page with Animation and Styling
elif st.session_state.page == "welcome":
    # Custom CSS for animations and styling
    st.markdown(
        """
        <style>
            @keyframes fadeIn {
                from {opacity: 0; transform: translateY(-20px);}
                to {opacity: 1; transform: translateY(0);}
            }

            @keyframes backgroundAnimation {
                  0% { background-color: #ff9a9e; }
                50% { background-color: #fad0c4; }
                100% { background-color: #ffdde1; }

            }

            .welcome-container {
                text-align: center;
                animation: fadeIn 1.5s ease-in-out;
                color: black;
                font-size: 50px;
                margin-bottom: 20px
                font-weight: bold;
                text-shadow: 2px 2px 5px black;
            }

            .background {
                animation: backgroundAnimation 5s infinite alternate;
                padding: 30px;
                border-radius: 15px;
            }

            .motivation-text {
                font-size: 18px;
                margin-top: 10px
                margin-bottom: 10px
                color: #ffffff;
                font-weight: bold;
                padding: 20px;
                text-align: center;
                border-radius: 10px;
                animation: fadeIn 2s ease-in-out;
            }

            .button-row {
                display: flex;
                justify-content: center;
                gap: 10px;
                margin-top: 20px;
                
                
            }

            .button-row button {
                width: 150px;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Animated Welcome Text
    st.markdown(f"<div class='welcome-container'>🚀 Welcome, {st.session_state.name}!</div>", unsafe_allow_html=True)
    
    # Date Display (Same as Before)
    today = datetime.date.today()
    st.write(f"📅 Today's Date: {today.strftime('%A, %d %B %Y')}")

    
    # Motivational Animated Paragraph
    st.markdown(
        """
        <div class="motivation-text">
            This is a great opportunity for you to bring positive improvement to your personality! 
            Through this challenge, you can enhance your mindset and habits while engaging in 
            various activities that make you feel happy and peaceful. 🌟  
            Are you ready to bring a positive change in yourself?  
            Click Get Challenge and begin your journey! 🚀  
        </div>
        """,
        unsafe_allow_html=True
    )

# Buttons in a Row
    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        if st.button("🎯 Get Challenge", key="welcome_get_challenge"):
            st.session_state.prev_page = "welcome"
            st.session_state.page = "challenge"
            st.session_state.quote = random.choice(quotes)
            st.session_state.daily_challenge = random.choice(challenges)
            save_challenge(st.session_state.email, today.strftime("%Y-%m-%d"), st.session_state.daily_challenge)
            st.rerun()

    with col2:
        if st.button("🚫 Ignore", key="welcome_ignore"):
            st.session_state.page = "home"
            st.rerun()

    with col3:
        if st.button("⬅ Back", key="welcome_back"):
            st.session_state.page = "home"
            st.rerun()












# Challenge Page
elif st.session_state.page == "challenge":
    st.header("💡 Growth Challenge")
    st.markdown(f"<p class='quote-box'>{st.session_state.quote}</p>", unsafe_allow_html=True)

    st.subheader("🎯 Today's Challenge")
    st.markdown(f"<p class='challenge-text'>{st.session_state.daily_challenge}</p>", unsafe_allow_html=True)

    reflection = st.text_area("📝 Reflect on today's challenge and what you learned:")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("💾 Save Reflection", key="save_reflection"):
            if reflection:
                today_date = datetime.date.today().strftime("%Y-%m-%d")
                
                # ✅ Reflection save karna
                save_challenge(st.session_state.email, today_date, st.session_state.daily_challenge, reflection)
                
                # ✅ Graph update trigger
                st.session_state.graph_update = True

                # ✅ UPDATED: Fetch latest challenges to update Pie Chart
                st.session_state.user_challenges = get_user_challenges(st.session_state.email) or []
                
                st.success("Reflection saved successfully! 🚀")
                st.rerun()

    with col2:
        if st.button("📜 View Previous Challenges", key="view_previous_challenges"):
            st.session_state.prev_page = "challenge"
            st.session_state.page = "previous_challenges"
            st.rerun()

    if st.button("⬅ Back", key="challenge_back"):
        st.session_state.page = "welcome"
        st.rerun()

    # ✅ New Feature: Progress Pie Chart
    st.subheader("📊 Your Challenge Completion (Last 31 Days)")

    # ✅ Handle errors gracefully
    if "user_challenges" not in st.session_state:
        st.session_state.user_challenges = get_user_challenges(st.session_state.email) or []

    user_challenges = st.session_state.user_challenges

    today = datetime.date.today()
    start_date = today - datetime.timedelta(days=30)
    total_days = 31  # Last 31 days

    # ✅ Count reflections
    completed_days = len(set([entry[0] for entry in user_challenges]))  # Unique dates in data
    missed_days = total_days - completed_days  # Days without reflection

    # ✅ Ensure percentage calculations are accurate
    completed_percent = (completed_days / total_days) * 100
    missed_percent = (missed_days / total_days) * 100

    # ✅ Create Pie Chart Data
    pie_data = pd.DataFrame({
        "Status": ["Completed Challenges", "Missed Challenges"],
        "Percentage": [completed_percent, missed_percent]
    })

    # ✅ Generate Pie Chart
    fig = px.pie(
        pie_data, 
        names="Status", 
        values="Percentage", 
        title="📊 Challenge Completion Percentage",
        hole=0.3,
        color="Status",
        color_discrete_map={"Completed Challenges": "green", "Missed Challenges": "red"}
    )

    st.plotly_chart(fig)



# Previous Challenges Page
elif st.session_state.page == "previous_challenges":
    
    st.title("📜 Your Previous Challenges")
    st.warning("Remember, if you delete any main challenge, you can delete all challenges, and you will have to complete all challenges again from day 1.")

    user_challenges = get_user_challenges(st.session_state.email)

    if user_challenges:
        df = pd.DataFrame(user_challenges, columns=["Date", "Challenge", "Reflection"])
        df["Date"] = pd.to_datetime(df["Date"])
        df = df.sort_values(by="Date", ascending=False)

        for idx, row in df.iterrows():
            col1, col2 = st.columns([4, 1])  

            with col1:
                st.subheader(f"📅 {row['Date'].strftime('%A, %d %B %Y')} (Challenge #{len(df) - idx})")
                st.markdown(f"🎯 Challenge: {row['Challenge']}")
                st.markdown(f"📝 Reflection: {row['Reflection'] if row['Reflection'] else 'No reflection added.'}")
                st.markdown("---")

            with col2:
                if st.button("🗑 Delete", key=f"delete_{idx}"):  
                    delete_challenge(row["Date"].strftime("%Y-%m-%d"), st.session_state.email)
                    st.rerun()

    else:
        st.info("You haven't completed any challenges yet. Start now!")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("🏠 Go to Home", key="previous_home"):
            st.session_state.page = "home"
            st.rerun()

    with col2:
        if st.button("⬅ Back", key="previous_back"):
            st.session_state.page = st.session_state.prev_page if st.session_state.prev_page else "home"
            st.rerun()