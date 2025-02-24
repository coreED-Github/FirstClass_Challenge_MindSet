import streamlit as st
import random
import emoji
import datetime
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
from database import create_table, save_challenge, get_user_challenges, delete_reflection  
from  PIL import Image
create_table()

if "page" not in st.session_state:
    st.session_state.page = "home"
if "prev_page" not in st.session_state:
    st.session_state.prev_page = None

# Sidebar
with st.sidebar:
    st.markdown("<h2 style='text-align: center;'>🌱 Growth Mindset Challenges</h2>", unsafe_allow_html=True)
    
    if st.button("🏠 Home", key="sidebar_home"):
        st.session_state.prev_page = st.session_state.page
        st.session_state.page = "home"
        st.rerun()
    

    if st.session_state.page != "home" and st.button("📜 View Previous Challenges", key="view previous challenges"):
            st.session_state.prev_page = "challenge"
            st.session_state.page = "previous_challenges"
            st.rerun()

    if st.session_state.page != "home" and st.button("📊View your progress tracker", key="progress_tracker"):
         st.session_state.page = "Progress"
         st.rerun()

    
    if st.session_state.page != "home" and st.button("⬅ Back", key="sidebar_back"):
        st.session_state.page = st.session_state.prev_page if st.session_state.prev_page else "home"
        st.rerun()
    

quotes = [
  emoji.emojize("💡 Mistakes are proof that you are trying."),
  emoji.emojize("💪 Challenges help you grow stronger."),
  emoji.emojize("🚀 Believe you can, and you're halfway there."),
  emoji.emojize("💡 Mistakes are proof that you are trying."),
  emoji.emojize("💪 Challenges help you grow stronger."),
  emoji.emojize("🚀 Believe you can, and you're halfway there."),
  emoji.emojize("🔥 Growth begins outside your comfort zone."),
  emoji.emojize("🌱 Small daily improvements lead to big results."),
  emoji.emojize("🎯 Set goals, stay focused, and never give up."),
  emoji.emojize("🛠 Work on yourself like you would build a masterpiece."),
  emoji.emojize("⏳ Patience and persistence create lasting success."),
  emoji.emojize("🌟 Be the best version of yourself every day."),
  emoji.emojize("🔄 Learn from failures; they are your stepping stones."),
  emoji.emojize("📝 Your mindset shapes your reality."),
  emoji.emojize("🌍 Kindness and positivity can change the world."),
  emoji.emojize("🔗 Self-discipline is the bridge between goals and success."),
  emoji.emojize("🧩 Every challenge is an opportunity for growth."),
  emoji.emojize("📌 Progress, not perfection, leads to true success."),
  emoji.emojize("🚦 Keep moving forward, even if it’s just one step."),
  emoji.emojize("🔑 Your attitude determines your altitude."),
  emoji.emojize("🎶 A peaceful mind leads to a happy life."),
  emoji.emojize("🛑 Stop doubting yourself and start believing."),
  emoji.emojize("💭 Your thoughts shape your destiny."),
  emoji.emojize("📖 Read, learn, and grow every single day."),
  emoji.emojize("🌐 Surround yourself with positive energy."),
  emoji.emojize("🔬 Self-awareness is the first step to self-improvement."),
  emoji.emojize("⚡ Take action—dreams don’t work unless you do."),
  emoji.emojize("🧠 Feed your mind with knowledge and positivity."),
  emoji.emojize("📊 Measure your progress, not your failures."),
  emoji.emojize("🤝 Treat yourself with kindness and patience."),
  emoji.emojize("💎 Your value does not decrease based on others’ opinions."),
  emoji.emojize("🛤 Life is a journey—make it meaningful."),


]

challenges = [
    
  "📝 Write down one thing you struggled with today and how you handled it.",
  "📚 Learn a new skill today, no matter how small.",
  "🙏 Practice gratitude: List three things you're grateful for today.",
  "🌱 Step out of your comfort zone and try something new.",
  "💡 Read an article or book that expands your knowledge.",
  "🔄 Replace one negative thought with a positive one.",
  "🤝 Perform a random act of kindness for someone.",
  "🎯 Set a small, achievable goal and accomplish it today.",
  "🛠 Fix one bad habit by replacing it with a good one.",
  "⏳ Spend at least 30 minutes today working on self-improvement.",
  "🎶 Take a break and do something that brings you joy.",
  "💭 Reflect on your past mistakes and write down what you learned.",
  "🚀 Challenge yourself to do something you've been avoiding.",
  "🔍 Observe your thoughts and practice mindfulness for 10 minutes.",
  "📖 Write down three things you love about yourself.",
  "🌍 Reduce distractions and focus deeply on one task today.",
  "🧩 Solve a problem creatively instead of the usual way.",
  "📌 Organize a small part of your workspace or home.",
  "🔗 Strengthen a relationship by reaching out to someone you care about.",
  "🚦 Take a small step towards a big dream you have.",
  "💎 Speak kindly to yourself and challenge negative self-talk.",
  "🛑 Identify one bad habit and take action to reduce it today.",
  "⚡ Spend time learning something outside your comfort zone.",
   "🔑 Identify your strengths and find ways to use them more.",
  "🧠 Take 10 minutes to plan your day before starting work.",
  "📊 Track your progress on a goal you've been working on.",
  "🌐 Do something to help the environment, no matter how small.",
  "🤝 Compliment or appreciate someone genuinely today.",
  "🛤 End your day with a moment of reflection and self-care.",


]

# Home Page
if st.session_state.page == "home":
    st.title("🌱Growth Mindset Challenge")

    name = st.text_input("Enter your name:")
    st.warning("🔒 If you want to keep your challenge days continuous, use the same password every time ")
    email = st.text_input("Enter your Password:")

    if st.button("🚀 Start Now", key="get_challenge"):
        if name and email:
            st.session_state.prev_page = "home"
            st.session_state.name = name
            st.session_state.email = email
            st.session_state.page = "welcome"
            st.rerun()
        else:
            st.warning("Please enter both your Name and Password.")

# Wellcome page
elif st.session_state.page == "welcome":
    
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

 @keyframes blink {
            0% { color: red; }
            50% { color: yellow; }
            100% { color: red; }
  }
        
        .highlight {
            font-size: 24px;
            font-weight: bold;
            animation: blink 1s infinite;
            padding-bottom:20px;
            border-radius: 10px;
        }

            .welcome-container {
                text-align: left;
                animation: fadeIn 1.5s ease-in-out;
                color: #50cac6 ;
                font-size: 50px;
                
                padding-bottom:20px;
                font-weight: bold;
                text-shadow: 2px 2px 5px black;
            }

            .background {
                animation: backgroundAnimation 5s infinite alternate;
                padding: 30px;
                border-radius: 15px;
 text-align: left;
            }

            .motivation-text {
                font-size: 18px;
                margin-top: 10px
                margin-bottom: 10px
                color: #20f2e7 ;
                font-weight: bold;
                padding-bottom:20px;
                text-align: left;
                border-radius: 10px;
                animation: fadeIn 2s ease-in-out;
            }

            
        </style>
 """,

        unsafe_allow_html=True
    )

    st.markdown(f"<div class='welcome-container'>Welcome,{st.session_state.name}! ✨</div>", unsafe_allow_html=True)
    today = datetime.date.today() 
    st.write(f'<p class="highlight">📅 Today\'s Date: {today.strftime('%A, %d %B %Y')}</p>', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="motivation-text">

           🌟 Unlock Your Potential! 🌟

This is a golden opportunity for you to bring positive growth to your personality! 🌱 Through this challenge, you can enhance your mindset 🧠, develop productive habits, and engage in activities that bring happiness and peace 😊.

Are you ready to embrace a better version of yourself? 💪 
Click "Get Challenge" button and begin your journey today! 
        </div>
        """,
        unsafe_allow_html=True
    )
    col1, col2 = st.columns([1, 1])

    with col1:
        if st.button("Get Challenge", key="welcome_get_challenge"):
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

# challenge
st.markdown("""
    <style>
        .challenge-text {
            font-size: 22px;
            font-weight: bold;
            color: black;
            text-align: center;
            background: linear-gradient(90deg, yellow, #ff5e62);
            padding: 10px;
            border-radius: 8px;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
            animation: fadeInScale 1.5s ease-in-out;
        }
        .quote-box {
            font-size: 20px;
            font-style: italic;
            font-weight: bold;
            background-color: #f8f9fa;
            color: #333;
            padding: 10px;
            border-left: 5px solid #ff5e62;
            border-radius: 5px;
            text-align: center;
        }
        h1, h2, h3, h4, h5, h6 {
            color: #ff5e62;
        }
        @keyframes fadeInScale {
            0% { opacity: 0; transform: scale(0.9); }
            100% { opacity: 1; transform: scale(1); }
        }
    </style>
""", unsafe_allow_html=True)

if st.session_state.page == "challenge":
    st.subheader("Your Mindset Path to Growth! 📚")
    st.markdown("<span style='color: #50cac6  ;'>This is a new lesson for you today. By following this lesson, you will complete your challenge.</span>", unsafe_allow_html=True)
    st.markdown(f"<p class='quote-box'>{st.session_state.quote}</p>", unsafe_allow_html=True)
    
    st.subheader("Today's Challenge! 🎯 ")
    st.markdown("<span style='color: #50cac6 ;'>Finally, here is your new challenge for today. Hope you complete it with honesty.</span>", unsafe_allow_html=True)
    st.markdown(f"<p class='challenge-text'>{st.session_state.daily_challenge}</p>", unsafe_allow_html=True)
    if st.button("⚔ Accept Challenge ⚔", key="challenge_back"):
        st.session_state.page = "Reflection"
        st.rerun()

    if st.button("⬅ Back", key="welcome_back"):
            st.session_state.page = "welcome"
            st.rerun()


# reflection page
if st.session_state.page == "Reflection":
    
    st.subheader("Mission Accomplished! Share Your Learnings ✍")
    st.markdown("<span style='color: #50cac6 ;'>After completing your task, fill out this reflection.</span>", unsafe_allow_html=True)
    st.text("Using the lesson given above, how did you complete your task? Were you successful? What challenges did you face? Where is improvement needed? Define these aspects as well.")
    reflection = st.text_area("📝 Reflect on today's challenge and what you learned:")

    col1, col2 , col3 = st.columns(3)
    if "progress" not in st.session_state:
        st.session_state.progress =0

    with col1:
        if st.button("💾 Save your Reflection", key="save_reflection"):
            if not reflection.strip():
                st.warning("⚠ Please write your reflection before saving!")
            else:
                today_date = datetime.date.today().strftime("%Y-%m-%d")
                save_challenge(st.session_state.email, today_date, st.session_state.daily_challenge, reflection)
                st.session_state.progress += 1
                st.session_state.graph_update = True
                st.session_state.user_challenges = get_user_challenges(st.session_state.email) or []
                st.session_state.page = "congratulations"
                st.rerun()
    
    with col2:
        if st.button("📜 View Previous Challenges", key="view_previous_challenges"):
            st.session_state.prev_page = "challenge"
            st.session_state.page = "previous_challenges"
            st.rerun()
    with col3:
        if st.button("📊View your progress tracker", key="challenge_back"):
         st.session_state.page = "Progress"
         st.rerun()
    
# Progress tracker
if st.session_state.page == "Progress":
       
       st.subheader("📊 Your Challenges Progress")
       st.markdown("<span style='color: #50cac6;'>This is your progress tracking graph. Every time you accept a challenge and click the Save Reflection button, you will see your progress increasing in the graph. If you achieve 100%, you will successfully bring a positive change to your personality with a strong and growth-oriented mindset.</span>", unsafe_allow_html=True)
       fig, ax = plt.subplots()
       ax.bar(["Progress"], [st.session_state.progress], color= "#50cac6")
       ax.set_ylim(0 ,100 )
       st.pyplot(fig)
       
       if st.button("⬅ Back", key="challenge_backs"):
        st.session_state.page = "welcome"
        st.rerun()


    


# congratulation page
if st.session_state.page == "congratulations":
    st.markdown("""
        <style>
            @keyframes fadeInScale {
                0% { opacity: 0; transform: scale(0.8); }
                100% { opacity: 1; transform: scale(1); }
            }
            .congrats-box {
                padding: 20px;
                font-size: 25px;
                font-weight: bold;
                color: #d6c32b ;
                text-align: center;
                background: white;
                border-radius: 10px;
                box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.3);
                animation: fadeInScale 1.5s ease-in-out;
            }
            body {
                background-color: #f0f8ff;
                text-align: center;
            }
        </style>
    """, unsafe_allow_html=True)
    
    
    image= Image.open("congrats.jpg")
    resized_image = image.resize((800,300))
    st.image(resized_image)
    st.markdown(f"<div class='congrats-box'>🎉Welldone, {st.session_state.name.split('@')[0]}! 🎉<br> You successfully completed today's challenge! Keep growing! 🚀</div>", unsafe_allow_html=True)
    
    st.markdown("<br><br>" , unsafe_allow_html=True)
    if st.button("⬅ Back", key="back_to_challenges"):
        st.session_state.page = "Reflection"
        st.rerun()
# privous challenge
elif st.session_state.page == "previous_challenges":
    
    st.title("📜 Your Previous Challenges")
    st.write("Here, you can view a complete record of all the challenges you have completed. You can also revisit the challenges you have successfully achieved and see how you overcame them. This will help you reflect on your progress and boost your confidence.")

    user_challenges = get_user_challenges(st.session_state.email)

    if user_challenges:
        df = pd.DataFrame(user_challenges, columns=["Date", "Challenge", "Reflection"])
        df["Date"] = pd.to_datetime(df["Date"])
        df = df.sort_values(by="Date", ascending=False)

        for idx, row in df.iterrows():
            col1, col2, col3 = st.columns([4, 1, 1])  
            with col1:
                st.subheader(f"📅 {row['Date'].strftime('%A, %d %B %Y')}")
                st.markdown(f"🎯 Challenge: {row['Challenge']}")
                st.markdown(f"📝 Reflection: {row['Reflection'] if row['Reflection'] else 'No reflection added.'}")
                st.markdown("---")
            
            with col3:
                if st.button("❌ Delete", key=f"delete_{idx}"):
                    delete_reflection(st.session_state.email, row['Date']
                                      .strftime('%Y-%m-%d'), row['Challenge'])
                    st.success("Reflection deleted successfully!")
                    st.rerun()

    else:
        st.info("You haven't completed any challenges yet. Start now!")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("🏠 Go to Home", key="previous_home"):
            st.session_state.page = "home"
            st.rerun()

    with col2:
        if st.button("⬅ Back", key="challenge_backs"):
         st.session_state.page = "welcome"
        st.rerun()