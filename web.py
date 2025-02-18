import streamlit as st
import random
import emoji

custom_css = """
<style>
body {
    font-family: 'Inter', sans-serif;
    background-color: #f9fafb;
    margin: 0;
    padding: 0;
}

.navbar {
    font-size: 20px;
    font-weight: bold;
    position: fixed;
    top: 0;
    width: 100vw;
    background: #78a1a1 ;
    color: white;
    padding: 15px;
    text-align: center;
    left: 0;
    z-index: 1000;
}

.footer {
    background: #78a1a1 ;
    color: white;
    padding: 15px 0;
    text-align: center;
    font-size: 16px;
    width: 100vw;
    position: fixed;
    bottom: 0;
    left: 0;
    z-index: 1000;
}

.stApp {
    padding-top: 60px;
    padding-bottom: 60px;
}

.quote-box {
    font-size: 18px;
    font-weight: 600;
    animation: fadeIn 1s ease-in-out;
    background: #cff4f5;
    padding: 20px;
    border-radius: 8px;
    text-align: center;
    color: #b45309;
}

.challenge-text {
    border-radius: 8px;
    text-align: center;
    font-size: 16px;
    font-weight: 500;
    color: #92400e;
    background: #fffbeb;
    padding: 15px;
    margin-top: 10px;
}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)
st.markdown("<div class='navbar'>🚀 Growth Mindset App</div>", unsafe_allow_html=True)

if "page" not in st.session_state:
    st.session_state.page = "home"

quotes = [
    emoji.emojize("💡 Mistakes are proof that you are trying."),
    emoji.emojize("💪 Challenges help you grow stronger."),
    emoji.emojize("🚀 Believe you can, and you're halfway there."),
    emoji.emojize("📖 Every day is a new opportunity to learn."),
    emoji.emojize("💡 Mistakes are proof that you are trying."), 
emoji.emojize("💪 Challenges help you grow stronger."),  
emoji.emojize("🚀 Believe you can, and you're halfway there."),  
emoji.emojize("📖 Every day is a new opportunity to learn."),  
emoji.emojize("🔥 Don't be afraid to fail. Be afraid not to try."),  
emoji.emojize("🌟 Small steps lead to big success. Keep going!"),  
emoji.emojize("🏋‍♂ Your comfort zone will never let you grow. Step out!"),  
emoji.emojize("🎯 Focus on progress, not perfection."),  
emoji.emojize("⏳ Patience and persistence conquer everything."),  
emoji.emojize("🛠 Your mindset shapes your reality. Think positively!"),  
emoji.emojize("💭 If you can dream it, you can achieve it."),  
emoji.emojize("🌍 Opportunities don’t happen, you create them."),  
emoji.emojize("⚡ Energy flows where focus goes."),  
emoji.emojize("🏆 Success is a series of small wins."),  
emoji.emojize("🛤 The road to success is always under construction."),  
emoji.emojize("🧠 A strong mind leads to a strong life."),  
emoji.emojize("🔄 Every failure is a lesson, not an endpoint."),  
emoji.emojize("🏃‍♂ Stay consistent. Small actions build great habits."),  
emoji.emojize("🕰 Your future depends on what you do today."),  
emoji.emojize("💖 Believe in yourself, even when no one else does."),
]

challenges = [
    "Write down one thing you struggled with today and how you handled it.",
    "Learn a new skill today, no matter how small.",
    "Give constructive feedback to someone and help them improve.",
    "Practice gratitude: List three things you're grateful for today.",
    "Step outside your comfort zone: Try something new today.",
    "Spend 15 minutes reading a book or article on self-improvement.",
    "Teach someone something new today.",
    "Identify a mistake you made recently and what you learned from it.",
    "Do something today that scares you a little.",
    "Avoid complaining for a whole day—focus on solutions instead!",
]

if st.session_state.page == "home":
    st.title("Growth Mindset Challenge")
    name = st.text_input("Enter your name:")
    email = st.text_input("Enter your email:")

    if st.button("🚀 Get The Challenge"):
        if name and email:
            st.session_state.name = name
            st.session_state.email = email
            st.session_state.page = "welcome"
            st.rerun()
        else:
            st.warning("Please enter both your name and email.")

elif st.session_state.page == "welcome":
    st.header(f"🚀 Welcome, {st.session_state.name}!")
    st.write("Let's embrace a growth mindset together.")

    if st.button("🎯 Get Quote", key="get_quote"):
        st.session_state.page = "challenge"
        st.session_state.quote = random.choice(quotes)
        st.session_state.daily_challenge = random.choice(challenges)
        st.rerun()

    st.markdown(
        """
        <div class='challenge-text'>
        By clicking "Get Quote," you will receive an inspirational quote and a daily challenge.  
        Promise yourself to embrace these challenges and work towards personal growth! 💡💪🚀  
        </div>
        """,
        unsafe_allow_html=True
    )
elif st.session_state.page == "challenge":
    st.header("💡 Growth Challenge")
    st.markdown(f"<p class='quote-box'>{st.session_state.quote}</p>", unsafe_allow_html=True)

    st.subheader("🎯 Today's Challenge")
    st.markdown(f"<p class='challenge-text'>{st.session_state.daily_challenge}</p>", unsafe_allow_html=True)

    reflection = st.text_area("📝 Reflect on today's challenge and what you learned:")

    if reflection:
        st.success("🌟 Great! Keep learning from your experiences.")

    if st.button("🏠 Go to Home"):
        st.session_state.page = "home"
        st.rerun()

st.markdown("<div class='footer'>📧 Contact: sairanasir853@gmail.com | 🌍 03492608035</div>", unsafe_allow_html=True)