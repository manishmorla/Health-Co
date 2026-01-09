# Health & Co 🩺

An AI-powered personalized nutrition advisor that provides tailored nutrition recommendations based on your BMI, age, gender, health conditions, and dietary habits.

## Features

- **BMI Calculation**: Automatically calculates your Body Mass Index
- **Personalized Nutrition Advice**: Get AI-powered recommendations tailored to your specific needs
- **Dietary Analysis**: Analyzes your dietary habits and identifies potential issues
- **Health Condition Consideration**: Takes into account your health conditions for personalized advice
- **Interactive Q&A**: Ask general nutrition questions to the AI assistant
- **Multiple Interfaces**: Available as both a web app (Streamlit) and CLI tool

## Tech Stack

- **Python 3.8+**
- **Streamlit** - Web interface framework
- **Google Gemini AI** - AI-powered nutrition advice
- **python-dotenv** - Environment variable management

## Project Structure

```
Health-Co/
├── src/
│   ├── app.py          # Streamlit web application
│   ├── cli.py          # Command-line interface
│   └── utils.py        # Shared utility functions
├── assets/
│   ├── background.png  # Background image for web app
│   └── logo.png        # Logo image
├── .env.example        # Example environment variables file
├── .gitignore          # Git ignore file
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/Health-Co.git
   cd Health-Co
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   - Copy `.env.example` to `.env`
   ```bash
   cp .env.example .env
   ```
   - Edit `.env` and add your Google Gemini API key:
     ```
     GEMINI_API_KEY=your_actual_api_key_here
     ```
   - Get your API key from [Google AI Studio](https://makersuite.google.com/app/apikey)

## Usage

### Web Application (Recommended)

Run the Streamlit web application:

```bash
streamlit run src/app.py
```

The application will open in your default web browser at `http://localhost:8501`

### Command-Line Interface

Run the CLI version:

```bash
python src/cli.py
```

Follow the prompts to enter your information and get personalized nutrition advice.

## How It Works

1. **Input Collection**: Enter your age, gender, weight, height, health conditions, and dietary habits
2. **BMI Calculation**: The system calculates your Body Mass Index
3. **Problem Identification**: Identifies potential nutrition problems based on BMI and dietary habits
4. **AI Analysis**: Uses Google Gemini AI to generate personalized nutrition advice
5. **Recommendations**: Provides tailored recommendations specific to your needs

## Nutrition Problem Categories

The system can identify and provide advice for:

- **Malnutrition (underweight)**: BMI < 18.5
- **Healthy weight**: BMI 18.5-24.9
- **Overweight**: BMI 25-29.9
- **Obesity**: BMI ≥ 30
- **Age-related malnutrition**: For individuals 65+
- **Poor dietary diversity**: Insufficient variety in diet
- **Micronutrient deficiency**: Specific nutrient deficiencies

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

## Disclaimer

This application provides general nutrition information and should not replace professional medical advice. Always consult with a healthcare provider or registered dietitian for personalized medical and nutrition advice.

## Acknowledgments

- Powered by [Google Gemini AI](https://deepmind.google/technologies/gemini/)
- Built with [Streamlit](https://streamlit.io/)

## Support

If you encounter any issues or have questions, please open an issue on GitHub.

---

Made with ❤️ for better health and nutrition
