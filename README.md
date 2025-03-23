# Video Summarization with Gemini AI

This project is a Streamlit application that leverages Google's Gemini AI to automatically summarize video content. Users can upload videos (MP4, MOV, AVI), and the application will generate a concise summary of the video's content.

## Features

*   **Video Upload:** Users can upload video files directly through the Streamlit interface.
*   **Gemini AI Integration:** Utilizes Google's Gemini AI for intelligent video summarization.
*   **Concise Summaries:** Generates 4-5 sentence summaries of the video content.
*   **Safety Settings:** Includes customizable safety settings to filter potentially harmful content.
*   **User-Friendly Interface:** Simple and intuitive Streamlit interface for easy interaction.
*   **Progress Indicator:** Shows a loading animation while the video is being processed.
*   **Error Handling:** Handles potential errors gracefully and displays error messages to the user.

## Prerequisites

*   **Python 3.8+**
*   **Google Gemini API Key:** You'll need a Google Gemini API key to use this application.
*   **Environment Variables:** Set the `GOOGLE_API_KEY` environment variable with your API key.

## Installation

1.  **Clone the repository (if applicable):**
    ```bash
    git clone https://github.com/prashantsmp/Google-Gemini.git
    cd Google-Gemini
    ```

2.  **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set the `GOOGLE_API_KEY` environment variable:**

    *   Create a file named `.env` in the same directory as `app.py`.
    *   Add the following line to the `.env` file:
        ```
        GOOGLE_API_KEY="your_api_key_here"
        ```
        (Replace `"your_api_key_here"` with your actual API key.)

## Usage

1.  **Run the Streamlit application:**
    ```bash
    streamlit run app.py
    ```

2.  **Open the application in your browser:**
    *   Streamlit will provide a local URL (usually `http://localhost:8501`) where you can access the application.

3.  **Upload a video:**
    *   Click the "Browse files" button to select a video file (MP4, MOV, or AVI) from your computer.

4.  **Summarize the video:**
    *   Click the "Summarize" button.
    *   The application will process the video and display a summary in a few moments.
    *   A loading animation will be shown while the video is being processed.

## Code Structure

*   **`app.py`:** The main Python file containing the Streamlit application code.
    *   **API Key Handling:** Loads the Google Gemini API key from environment variables.
    *   **Safety Settings:** Defines safety settings for content filtering.
    *   **System Prompt:** Sets the system prompt for the Gemini AI model.
    *   **Streamlit UI:** Creates the user interface for video upload and summarization.
    *   **Video Processing:** Handles video uploads, temporary file storage, and interaction with the Gemini API.
    *   **Error Handling:** Includes error handling for API issues and other potential problems.

## Dependencies

*   **streamlit:** For creating the web application interface.
*   **google-generativeai:** For interacting with the Google Gemini API.
*   **python-dotenv:** For loading environment variables from a `.env` file.
*   **tempfile:** For creating temporary files.
