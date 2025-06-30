import streamlit as st
import random
from datetime import datetime
from streamlit_drawable_canvas import st_canvas

# --- PAGE SETUP ---
st.set_page_config(page_title="The NORMAD Game", page_icon="❤️", layout="centered")

st.title("💖 The NORMAD Game")
st.write("Choose a game mode below and let's play something sweet...")

# --- GAME MODE SELECTION ---
game_mode = st.selectbox("Pick a mode", [
    "-- Select --",
    "Compliment Generator",
    "Guess the Memory",
    "Love Letter",
    "Draw a my artist"
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
        "miss perfection"
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
    st.write("Let's test your memory! ")

    memories = [
        {"hint": "May 5th, 2023", "answer": "The first text"},
        {"hint": "Nov 19th 2024", "answer": "the first meeting"},
        {"hint": "Dec 20th 2024", "answer": "Becoming official"},
        {"hint": "6", "answer": "the number of times we met"},
        {"hint": "My fav thing about you", "answer": " La, Kolech"},
        {"hint": "My favorite TV SHOW to watch", "answer": "Admiring you a chabaa, wow im good"},
        {"hint": "How did i start the conversation the first time", "answer": "Whats the best way to start a conversation"},
    ]

    selected = st.selectbox("Pick a memory to guess", [m["hint"] for m in memories])
    user_guess = st.text_input("What's your guess?")

    memory = next((m for m in memories if m["hint"] == selected), None)

    if st.button("Reveal the memory"):
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
        st.markdown(f"""
        <div style="padding: 1rem; margin: 1rem 0; background: #fff0f5; border-left: 5px solid #ff69b4; border-radius: 10px;">
            <strong style="color:#c71585;">Your Love Note:</strong><br>{user_note}
        </div>
        """, unsafe_allow_html=True)
        st.write("That’s so sweet! Want to write another or switch to another mode?")

# --- DRAW MY LOVE MODE ---
elif game_mode == "Draw a my artist":
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
                st.success("That’s a true love home ")
                st.image(canvas_result.image_data, caption="Our future house", use_column_width=True)
                st.markdown("> I’d move in right")
            else:
                st.warning("Looks like the canvas is empty! Try drawing something first.")
    with col2:
        if st.button("Erase Drawing ❌"):
            erase_drawing()
