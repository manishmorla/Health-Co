# Quick Start Guide - How to Run Health & Co

## Prerequisites
- Python 3.7 or higher installed
- Google Gemini API key (get it from [Google AI Studio](https://makersuite.google.com/app/apikey))

## Step-by-Step Instructions

### Step 1: Navigate to Project Directory
Open your terminal/command prompt and navigate to the project folder:
```bash
cd "c:\Users\91703\OneDrive\Desktop\github repositories\Health-Co"
```

### Step 2: Install Dependencies
Install the required Python packages:
```bash
pip install -r requirements.txt
```

Or install individually:
```bash
pip install streamlit python-dotenv requests
```

### Step 3: Set Up API Key
1. Make sure you have a `.env` file in the project root directory
2. If you don't have one, copy from the example:
   ```bash
   # On Windows PowerShell
   Copy-Item .env.example .env
   
   # On Windows CMD
   copy .env.example .env
   
   # On macOS/Linux
   cp .env.example .env
   ```
3. Open the `.env` file and add your Google Gemini API key:
   ```
   GEMINI_API_KEY=your_actual_api_key_here
   ```
   Replace `your_actual_api_key_here` with your actual API key from [Google AI Studio](https://makersuite.google.com/app/apikey)

### Step 4: Run the Application

#### Option A: Web Application (Recommended - Best User Experience)
Run the Streamlit web app:
```bash
streamlit run src/app.py
```

The application will:
- Start a local web server
- Automatically open in your default web browser at `http://localhost:8501`
- If it doesn't open automatically, manually go to `http://localhost:8501` in your browser

**To stop the application:** Press `Ctrl+C` in the terminal

#### Option B: Command-Line Interface (CLI)
Run the command-line version:
```bash
python src/cli.py
```

Follow the prompts to enter your information and get nutrition advice.

## Troubleshooting

### Error: "GEMINI_API_KEY environment variable is not set"
- Make sure you have a `.env` file in the project root
- Check that the `.env` file contains: `GEMINI_API_KEY=your_key_here`
- Ensure there are no extra spaces around the `=` sign

### Error: "ModuleNotFoundError: No module named 'streamlit'"
- Install dependencies: `pip install -r requirements.txt`

### Error: "Connection Error" or API errors
- Check your internet connection
- Verify your API key is correct and active
- Make sure you have API access enabled in Google AI Studio

### Port Already in Use
If port 8501 is already in use:
```bash
streamlit run src/app.py --server.port 8502
```

## Project Structure
```
Health-Co/
├── src/
│   ├── app.py          # Web application (Streamlit)
│   ├── cli.py          # Command-line interface
│   └── utils.py        # Shared functions
├── assets/
│   ├── background.png
│   └── logo.png
├── .env                # Your API key (not in git)
├── requirements.txt    # Dependencies
└── README.md          # Full documentation
```

## Need Help?
- Check the main [README.md](README.md) for detailed documentation
- Make sure all dependencies are installed
- Verify your API key is correct
