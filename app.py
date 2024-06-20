import streamlit as st
import os
import openai
from openai import OpenAI
client = OpenAI()

# Function to read player files and return their names
def get_player_files(directory):
    return [f for f in os.listdir(directory) if f.endswith('.txt')]

# Function to read the content of a selected file
def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# Streamlit app
st.title("Batsman Analysis with GPT-4o")

# Directory containing player files
player_directory = 'players'  # Make sure this directory exists and contains .txt files

# Get player files
player_files = get_player_files(player_directory)

# Sidebar for player selection
selected_file = st.sidebar.selectbox("Select a player file", player_files)
def remove_extension(filename):
    return filename.rsplit('.', 1)[0]
# Remove the .txt extension to get the batsman's name
BATSMAN_NAME = remove_extension(selected_file)

# Text area for custom prompt
default_prompt = f""" I am a cricket analyst for the Indian National cricket team
1. Devise a ball-by-ball strategy that the Indian team can execute to get the batsman {BATSMAN_NAME} out in a T20 game
2. Provide details on bowler names and field placements
3. Provide evidence for why this strategy will work
4. Choose a few from the bowlers Jasprit Bumrah, Siraj , Yuzvendra Chahal, Arshdeep Singh, Hardik Pandya, Kuldeep Yadav and Axar Patel
"""

# Text box for custom prompt

prompt = st.text_area("Enter your Custom Prompt (if you want to override)", value=default_prompt,height=250)


# Text box for OpenAI API key
##api_key = st.text_input("Enter your OpenAI API key", type="password")


def analyze_player(text):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are an efficient Cricket Coach, Strategist and Analyst. You are supposed to develop a detailed ball by ball strategy and field placement understanding a batsman's stength, weakness. Always provide evidence and FOLLOW RULES OF CRICKET. For example, multiple bowlers cannot bowl the same over ."},
            {"role": "user", "content": text}
        ])
    return response.choices[0].message.content


# Button to trigger the analysis
if st.button("Go!!"):
    if selected_file and prompt:
        # Read the content of the selected player file
        player_content = read_file(os.path.join(player_directory, selected_file))        
        # Concatenate player content and custom prompt
        final_prompt = prompt + "\n Recent history:\n" + player_content  
        
        # Make API call to OpenAI
        try:
            # Stream response back to the user
            response_text = analyze_player(final_prompt)
            st.write(response_text)
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.error("Please select a file, enter a prompt, and provide your OpenAI API key.")

st.markdown("Scraped cricinfo to develop a dataset based on ball by ball commentary of cricinfo of each batsman's last several matches")
st.markdown("API Link example: https://hs-consumer-api.espncricinfo.com/v1/pages/match/comments?seriesId=1411166&matchId=1415725&inningNumber=2&commentType=ALL&fromInningOver=1")
st.markdown("GPT does not have information on the latest form of individual players, this might help")
st.markdown(f"<font color=red> Hallucinations happen as this is based on LLMs</font>", unsafe_allow_html=True)


