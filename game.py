import streamlit as st
import random
from datetime import datetime
from streamlit_drawable_canvas import st_canvas
from PIL import Image
import numpy as np

# --- PAGE SETUP ---
st.set_page_config(page_title="The NORMAD Game", page_icon="❤️", layout="centered")

# --- ROMANTIC PURPLE BACKGROUND CSS ---
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        background-attachment: fixed;
    }
    
    .stApp::before {
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: 
            radial-gradient(circle at 20% 80%, rgba(120, 119, 198, 0.3) 0%, transparent 50%),
            radial-gradient(circle at 80% 20%, rgba(255, 182, 193, 0.3) 0%, transparent 50%),
            radial-gradient(circle at 40% 40%, rgba(138, 43, 226, 0.2) 0%, transparent 50%);
        pointer-events: none;
        z-index: -1;
    }
    
    .main .block-container {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 2rem;
        box-shadow: 0 8px 32px rgba(106, 90, 205, 0.3);
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    h1 {
        color: #4a148c !important;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
        text-align: center;
    }
    
    .stApp p, .stApp div, .stApp span, .stApp label {
        color: #2d1b69 !important;
        font-weight: 500;
    }
    
    .stTextInput label, .stSelectbox label {
        color: #4a148c !important;
        font-weight: bold;
        font-size: 1.1rem !important;
    }
    
    .stSelectbox > div > div, .stTextInput > div > div > input {
        background: rgba(255, 255, 255, 0.9) !important;
        border-radius: 10px;
        border: 2px solid rgba(106, 90, 205, 0.5) !important;
        color: #2d1b69 !important;
        font-weight: bold;
    }
    
    .stTextInput > div > div > input::placeholder {
        color: #6a5acd !important;
    }
    
    .stTextArea > div > div > textarea {
        background: rgba(230, 220, 255, 0.8);
        border-radius: 10px;
        border: 2px solid rgba(106, 90, 205, 0.3);
    }
    
    .stButton > button {
        background: linear-gradient(45deg, #9370db, #ba55d3);
        color: white;
        border-radius: 25px;
        border: none;
        padding: 0.5rem 2rem;
        font-weight: bold;
        box-shadow: 0 4px 15px rgba(147, 112, 219, 0.4);
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(147, 112, 219, 0.6);
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0px) rotate(0deg); }
        50% { transform: translateY(-20px) rotate(180deg); }
    }
    
    .floating-hearts {
        position: fixed;
        top: 10%;
        left: 50%;
        transform: translateX(-50%);
        font-size: 2rem;
        animation: float 6s ease-in-out infinite;
        pointer-events: none;
        z-index: 100;
        color: rgba(255, 182, 193, 0.7);
    }
</style>
""", unsafe_allow_html=True)

# UI components
st.title("Welcome to The NORMAD Game")

# --- Access control ---
password = st.text_input("Dakhli your birthday 💌", type="password")

if password != "29042003":
    st.stop()

st.title("HEY A CHABA 💖")
st.write("Choose a game mode below and let's play something sweet...")

# --- GAME MODE SELECTION ---
game_mode = st.selectbox("Pick a mode", [
    "-- Select --",
    "Compliment Generator",
    "Guess the Memory",
    "Love Letter",
    "Love Letters for You",
    "Draw a CHABA"
])

# --- COMPLIMENT GENERATOR ---
if game_mode == "Compliment Generator":
    compliments = [
        "You're the most beautiful chapter in my story.",
        "The Smartest girl f HEC",
        "Always making me proud",
        "Your smile is my favorite view.",
        "L AZZABIA EZELAA.",
        "You're not just my love. You're my peace.",
        "Your voice is my favorite sound.",
        "Being with you feels like home.",
        "I love you a CHABA",
        "I'd choose you in every lifetime",
        "You're my favorite notification",
        "miss perfection",
        "gorgeous",
        "lucky me!!",
    ]

    if st.button("Give me a compliment"):
        compliment = random.choice(compliments)
        st.markdown(f"""
        <div style="padding: 1rem; margin: 1rem 0; background: #fff0f5; border-left: 5px solid #ff69b4; border-radius: 10px;">
            <strong style="color:#c71585;">{compliment}</strong>
        </div>
        """, unsafe_allow_html=True)

# --- GUESS THE MEMORY GAME ---
elif game_mode == "Guess the Memory":
    st.write("Let's test your memory!")

    memories = [
        {"hint": "May 5th, 2023", "answer": "The first text"},
        {"hint": "Nov 19th 2024", "answer": "the first meeting"},
        {"hint": "Dec 20th 2024", "answer": "Becoming official"},
        {"hint": "6", "answer": "the number of times we met"},
        {"hint": "My fav thing about you", "answer": " La, Kolech"},
        {"hint": "My favorite TV SHOW to watch", "answer": "Admiring you a zela, wow im good"},
        {"hint": "How did i start the conversation the first time", "answer": "Whats the best way to start a conversation"},
    ]

    selected = st.selectbox("Sahlin 3lik i know but choose", [m["hint"] for m in memories])
    user_guess = st.text_input("What's your guess a 3ayniya?")

    memory = next((m for m in memories if m["hint"] == selected), None)

    if st.button("Reveal the memory"):
        # Save her guess
        with open("memory_guesses.txt", "a", encoding="utf-8") as f:
            f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Hint: {memory['hint']}\n")
            f.write(f"Her Guess: {user_guess.strip()}\n")
            f.write(f"Correct Answer: {memory['answer']}\n\n")

        # Show correct answer
        st.markdown(f"""
        <div style="padding: 1rem; margin: 1rem 0; background: #e6f7ff; border-left: 5px solid #1e90ff; border-radius: 10px;">
            <strong style="color:#007acc;">Correct memory:</strong> {memory['answer']}
        </div>
        """, unsafe_allow_html=True)

# --- LOVE LETTERS FOR YOU ---
elif game_mode == "Love Letters for You":
    st.write("Choose how you're feeling, and I'll give you exactly what you need to hear 💌")
    
    mood_options = [
        "-- How are you feeling? --",
        "Sad",
        "Lonely", 
        "Self-doubt",
        "Overthinking",
        "Noor ✨"
    ]
    
    selected_mood = st.selectbox("Pick your current mood", mood_options)
    
    if selected_mood != "-- How are you feeling? --":
        if st.button("Give me my letter 💝"):
            if selected_mood == "Sad":
                letter = """My beautiful CHABA,

I know today feels heavy, but I need you to remember something incredible - you are one of the most precious souls to ever exist in this world. Do you know how lucky I am? How lucky your mom is? How lucky everyone who knows the real you is?

You bring light into spaces that didn't even know they were dark. Your heart, your laugh, your way of caring about others.

The world is brighter because you're in it. I'm a better person because you're in my life. 



Forever yours,"""

            elif selected_mood == "Lonely":
                letter = """My dear,

I know the distance feels overwhelming sometimes, and I know there are moments when you feel alone. But I need you to hear this with your whole heart:

You are NEVER alone. Never.

Your mama is always thinking about you, praying for you, loving you with every breath she takes. And me? even when we're not talking, you're in my thoughts, in my prayers, in every beat of my heart.

We are your team, your support system, your safe place. No matter what you're going through - the good days, the bad days, the confusing days - we are here. We believe in you. We're cheering you on from every corner of our hearts.

You don't have to carry anything alone anymore. We're here, and we're not going anywhere.

With all my love,"""

            elif selected_mood == "Self-doubt":
                letter = """

Stop right there. Before you doubt yourself for even one more second, let me remind you.

You SURVIVED the bac exam. You made it through HEC. You dealt with difficult roommates and still kept it together. You handled bad friends and still chose to have a kind heart. You left your hometown.

Do you see the pattern here? You are UNBREAKABLE.

Every test that seemed impossible? You found a way through. Every moment when you wanted to give up? You chose to keep going.

And through it all, you never stopped trying to become a better person.

You are capable. Trust yourself the way I trust you - completely and without question.

Proudly yours,"""

            elif selected_mood == "Overthinking":
                letter = """My precious,

I can feel your mind racing from here, and I want to wrap you in the most peaceful hug right now.

Take a deep breath with me. Allah SWT is with you. He has always been with you, and He always will be.

That thing you're overthinking? That situation that's keeping you up at night? That decision that feels too big? Allah already knows the outcome, and He has already planned what's best for you.

Every single thing that has happened in your life - the good and the challenging - has led you to exactly where you need to be. Every door that closed made room for a better one to open. Every "no" was protection for a bigger "yes."

Trust in Allah's timing. Trust in His wisdom. Trust that He loves you more than you can imagine and would never give you more than you can handle.

Your future is beautiful. Stop worrying about it and start looking forward to it."""

            elif selected_mood == "Noor ✨":
                letter = """Noor,

NHABEK"""

            # Display the letter in a beautiful format
            st.markdown(f"""
            <div style="padding: 2rem; margin: 1rem 0; background: linear-gradient(135deg, #fff0f5, #e6f3ff); 
                        border-left: 5px solid #ff69b4; border-radius: 15px; 
                        box-shadow: 0 4px 15px rgba(255, 105, 180, 0.2);">
                <div style="white-space: pre-line; color: #2d1b69; font-size: 1.05rem; line-height: 1.6;">
                    {letter}
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # Save the letter with timestamp
            with open("mood_letters.txt", "a", encoding="utf-8") as f:
                f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Mood: {selected_mood}\n")
                f.write(f"Letter sent:\n{letter}\n\n")

# --- LOVE LETTER CHALLENGE ---
elif game_mode == "Love Letter":
    st.write("Write a short love note based on the prompt below, and let's make it unforgettable!")

    prompts = [
        "The moment I knew I loved you...",
        "Our perfect date would be...",
        "One thing I adore about us is...",
        "A dream I have for our future..."
    ]

    selected_prompt = random.choice(prompts)
    st.markdown(f"**Prompt**: *{selected_prompt}*")
    user_note = st.text_area("Your love note", height=100)

    if st.button("Share your note", disabled=not user_note.strip()):
        # Save to file
        with open("love_notes.txt", "a", encoding="utf-8") as f:
            f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Prompt: {selected_prompt}\n")
            f.write(f"Note: {user_note}\n\n")

        # Show back to her
        st.markdown(f"""
        <div style="padding: 1rem; margin: 1rem 0; background: #fff0f5; border-left: 5px solid #ff69b4; border-radius: 10px;">
            <strong style="color:#c71585;">Your Love Note:</strong><br>{user_note}
        </div>
        """, unsafe_allow_html=True)
        st.write("That's so sweet! Want to write another or switch to another mode?")

# --- DRAW MY LOVE MODE ---
elif game_mode == "Draw a CHABA":
    st.markdown("### 🎨 Draw our future house 🏡")
    st.write("Use the canvas below to create your dream house together — cozy, fancy, space-themed, whatever you imagine!")

    with st.expander("🎛️ Drawing Settings"):
        stroke_color = st.color_picker("Pick a pen color", "#FF69B4")
        stroke_width = st.slider("Pen thickness", 1, 10, 3)
        drawing_mode = st.selectbox("Drawing mode", ["freedraw", "transform", "rect", "circle", "line", "point"])
        bg_color = st.color_picker("Canvas background", "#FFFFFF")

    # Initialize/reset canvas key
    if "canvas_key" not in st.session_state:
        st.session_state.canvas_key = "love_canvas"

    def erase_drawing():
        st.session_state.canvas_key = f"love_canvas_{random.randint(0, 10000)}"

    canvas_result = st_canvas(
        fill_color="rgba(255,192,203,0.3)",
        stroke_width=stroke_width,
        stroke_color=stroke_color,
        background_color=bg_color,
        height=400,
        width=600,
        drawing_mode=drawing_mode,
        key=st.session_state.canvas_key
    )

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("Submit Drawing 🖼️"):
            if canvas_result.image_data is not None:
                # Save drawing as image
                img = Image.fromarray((canvas_result.image_data).astype(np.uint8))
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"chaba_drawing_{timestamp}.png"
                img.save(filename)

                st.success("That's a true love home 🏠")
                st.image(canvas_result.image_data, caption="Our future house", use_column_width=True)
                st.markdown("> I'd move in right away.")
            else:
                st.warning("Looks like the canvas is empty! Try drawing something first.")
    with col2:
        if st.button("Erase Drawing ❌"):
            erase_drawing()