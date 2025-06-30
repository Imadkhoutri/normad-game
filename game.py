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
        st.write("That’s so sweet! Want to write another or switch to another mode?")

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

            