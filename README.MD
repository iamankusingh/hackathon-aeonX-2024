
# hackathon-aeonX-2024
#### 🥈 We got second prize.

## Health Prediction and Caution System

This is the code of a prototype we build in hackathon to predict health and caution near future.
## Organizer

The hackathon was organized by [AeonX Digital](https://www.aeonx.digital/) at Bhuj on 5th september 2024.
## To Run Locally

Clone the project

```bash
  git clone https://github.com/iamankusingh/hackathon-aeonX-2024
```

Go to the project directory

```bash
  cd hackathon-aeonX-2024
```

Create virtual environment

```bash
  python3 -m venv .venv
```

Install libraries

```bash
  pip install requirement.txt
```
#### Setup API

Go to [Gemini Api](https://aistudio.google.com/) and copy the key.

#### Make a .env file in your folder

#### Paste key in the .env file

```
GEMINI_API_KEY=your_key_here
```

Start server

```bash
  streamlit run app.py
```
Some commands my vary according to your system.
## Flow of Program

 - Input what it is asking.
 - Click "Predict Health Risk" button
 - It generate a prompt on the basis of your input and call API.
- And at end, it print future risk and also suggestion to improve health.