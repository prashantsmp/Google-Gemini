import os
import time
import streamlit as st
from google import genai
from google.genai import types
from dotenv import load_dotenv
import tempfile

load_dotenv()

# --- API Key ---
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    st.error("GOOGLE_API_KEY environment variable not set.")
    st.stop()

client = genai.Client(api_key=GOOGLE_API_KEY)

# --- Safety Settings ---
safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_NONE",
    },
]

# --- System Prompt ---
system_prompt = "You should provide a quick 4 or 5 sentence summary of what is happening in the video."

# --- Streamlit App ---
st.title("Video Summarization with Gemini")

uploaded_file = st.file_uploader("Upload a video", type=["mp4", "mov", "avi"])

if uploaded_file is not None:
    st.video(uploaded_file)

    # Save the uploaded file to a temporary location
    with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[1]) as tmp_file:
        tmp_file.write(uploaded_file.getvalue())
        temp_file_path = tmp_file.name

    if st.button("Summarize"):
        with st.spinner("Processing video..."):
            try:
                # Upload video to Gemini API
                video_file = client.files.upload(file=temp_file_path)

                # Wait until the uploaded video is available
                while video_file.state.name == "PROCESSING":
                    st.write('.', end='')
                    time.sleep(5)
                    video_file = client.files.get(name=video_file.name)

                if video_file.state.name == "FAILED":
                    raise ValueError(video_file.state.name)

                # Generate content
                MODEL_ID = "gemini-2.0-flash"
                response = client.models.generate_content(
                    model=f"models/{MODEL_ID}",
                    contents=[
                        "Summarise this video please.",
                        video_file
                    ],
                    config=types.GenerateContentConfig(
                        system_instruction=system_prompt,
                        safety_settings=safety_settings,
                    ),
                )

                st.subheader("Summary:")
                st.write(response.text)

            except Exception as e:
                st.error(f"An error occurred: {e}")
            finally:
                # Clean up the temporary file
                os.remove(temp_file_path)
