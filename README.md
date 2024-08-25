# No AI Summary

This project provides a simple text summarization tool that doesn't rely on AI or machine learning algorithms. Instead, it uses a rule-based approach to extract key sections from the input text.

## Features

- Summarizes text of various lengths
- Adapts the summary length based on the input text length
- Web-based interface for easy use
- Backend API for text summarization

## How it works

The summarization process follows these steps:

1. Split the input text into paragraphs
2. Based on the number of paragraphs, select key sections:
   - For very short texts (5 paragraphs or less): Return all paragraphs
   - For short texts (6-10 paragraphs): Return first, middle, and last paragraphs
   - For medium-length texts (11-20 paragraphs): Return five evenly distributed sections
   - For long texts (more than 20 paragraphs): Return seven evenly distributed sections

## Project Structure

- `summarize.py`: Contains the Flask backend with the summarization logic
- `front-end/index.html`: The web interface for the summarization tool

## Setup and Usage

1. Install the required Python packages:
   ```
   pip install flask flask-cors
   ```

2. Run the Flask backend:
   ```
   python summarize.py
   ```

3. Open `front-end/index.html` in a web browser

4. Enter or paste your text into the textarea and click "Summarize"

## Limitations

- This method doesn't understand the semantic meaning of the text
- It may not always capture the most important information
- The quality of the summary depends on how well the key information is distributed in the original text