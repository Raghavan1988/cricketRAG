# Cricket Analysis with GPT-4

## Overview
This Streamlit application leverages OpenAI's GPT-4 model to provide advanced cricket analysis and generate engaging commentary. It offers two main features:

1. **Batsman Strategy Analysis:** Generates detailed, ball-by-ball strategies to dismiss specific batsmen in T20 cricket.
2. **Live Match Commentary:** Produces witty, personality-driven commentary for live cricket matches.

## Features

### Batsman Strategy Analysis
- Select a batsman from a dropdown list
- View or customize a prompt for strategy generation
- Receive a detailed strategy including:
  - Ball-by-ball plans
  - Bowler recommendations
  - Field placements
  - Evidence-based justifications

### Live Match Commentary
- Input a Cricinfo URL for live match data
- Receive ball-by-ball commentary in various commentator styles
- Enjoy witty remarks and strategic insights

## Setup and Installation

1. Clone this repository
2. Install required dependencies:
   ```
   pip install streamlit openai requests
   ```
3. Set up your OpenAI API key as an environment variable or in the app
4. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

## Usage

1. **Batsman Analysis:**
   - Select a batsman from the sidebar
   - Review or modify the strategy prompt
   - Click "Get Strategy!!" to generate analysis

2. **Live Commentary:**
   - Enter a Cricinfo URL in the text area
   - Click "Get Commentary" to start receiving live, stylized commentary

## Note
- Ensure you have the necessary player data files in a 'players' directory
- The app uses GPT-4, which may produce hallucinations or inaccuracies
- Data is scraped from Cricinfo for recent player performances

## Disclaimer
This application is for entertainment and analytical purposes. Always verify critical information and strategies with professional cricket analysts and coaches.

## Acknowledgements
Thanks to Cricinfo for the data used in this application.
