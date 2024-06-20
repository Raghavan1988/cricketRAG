# CricRAG: Batsman Analysis with GPT-4o

## Overview

CricRAG is a Streamlit application that leverages OpenAI's GPT-4o to provide detailed ball-by-ball strategies and field placements for cricket batsmen. Using Cricinfo's API, we have built specific dataset for many batsmen. The application reads recent ball by ball commentary from the dataset text files and allows users to input custom prompts to generate tailored strategies, ensuring up-to-date analyses.

## Features

- **Player File Selection**: Choose from a list of player files containing their recent performances and profiles.
- **Custom Prompt Input**: Enter a custom prompt to refine the strategy generation.
- **OpenAI GPT-4o Integration**: Utilizes GPT-4o to analyze player data and generate strategies.
- **Latest Player Information**: Scrapes Cricinfo for the most recent data on over 500 players from their national team's last 10 matches.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Raghavan1988/cricketRAG
   cd cricgpt
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure you have a directory named `players` with player profile `.txt` files in the same directory as the script.

## Usage

1. **Run the Streamlit App**:
   ```bash
   streamlit run app.py
   ```

2. **Interface**:
   - **Select a Player File**: Choose a player file from the sidebar.
   - **Enter a Custom Prompt**: (Optional) Provide a custom prompt for more specific analysis.
   - **Get Strategy**: Click the "Go! Get Strategy" button to generate and display the strategy.

## Explanation of CricGPT's Data Source

CricRAG maintains the latest player information by scraping ball-by-ball commentary from Cricinfo. This data includes detailed performance metrics for each batsman's last several matches. By using this real-time data, CricRAG can provide the most relevant and up-to-date strategies, ensuring that users receive accurate and actionable insights.

### Example API Link for Cricinfo Scraping

CricRAG utilizes the following type of API link to fetch ball-by-ball commentary and built a dataset for 500+ players
```
https://hs-consumer-api.espncricinfo.com/v1/pages/match/comments?seriesId=1411166&matchId=1415725&inningNumber=2&commentType=ALL&fromInningOver=1
```

This API link retrieves detailed commentary for specific matches and innings, allowing CricGPT to analyze each player's recent form and performance.

## Disclaimer

**Note**: While CricGPT aims to provide accurate and insightful strategies, it is based on large language models (LLMs) which may sometimes produce hallucinations or errors. Users should validate the generated strategies before implementation.

## Conclusion

CricRAG offers a powerful tool for cricket coaches, analysts, and enthusiasts to develop effective strategies against various batsmen. By integrating the latest data from Cricinfo and leveraging the capabilities of GPT-4o, CricRAG ensures up-to-date and comprehensive analysis.
