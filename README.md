
# Code Helper App 🤖</>

This is a Python-based **Streamlit** application that allows users to input a query and generate code or responses using **Google Generative AI (Gemini)**.

## Features
- Enter a query or code snippet, and the app generates relevant responses.
- Integrates with **Google Generative AI** to provide AI-generated content.
- The app uses **Streamlit** for a fast and interactive web interface.
- Supports a chat-like interface where the user and the assistant (AI) exchange messages.

## Prerequisites

Before running the application, make sure you have the following installed:

- **Python 3.x** (preferably the latest version)
- **Streamlit** - A Python framework for building interactive apps.
- **Google Generative AI** - The Python client for Google's AI models.

You will also need a **Google API key** to use the generative models.

## Installation

### Step 1: Clone the Repository

Clone this repository to your local machine:

```bash
git clone <repository_url>
cd <repository_name>
```

### Step 2: Set up a Virtual Environment (Optional but Recommended)

It's a good practice to use a virtual environment. Here's how to create and activate one:

#### On Windows:
```bash
python -m venv venv
.\venv\Scripts\activate
```

#### On Mac/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install the Required Packages

Install the necessary dependencies by running the following command in your terminal:

```bash
pip install -r requirements.txt
```

Alternatively, install each package individually:

```bash
pip install streamlit google-generativeai python-dotenv
```

### Step 4: Set Up Environment Variables

1. Create a `.env` file in the root of the project directory.
2. Add your **Gemini API Key** to the `.env` file:

```plaintext
gemini_api_key=YOUR_API_KEY_HERE
```

Replace `YOUR_API_KEY_HERE` with your actual API key from Google.

### Step 5: Run the Application

Start the Streamlit application by running:

```bash
streamlit run app.py
```

This will open the app in your default browser. You can now start using the app to input code queries and generate responses.

## Usage

1. **Enter a Query**: In the input box, type a programming-related question or code snippet. For example: "How do I write a Python function to reverse a string?"
2. **Generate Response**: Click the "Search" button, and the assistant will generate an answer based on the input.
3. **View Chat History**: The assistant's responses will appear in a chat-like interface.
4. **Clear History**: Click the "Clear history" button to reset the conversation.

## Example

For example, if you input:
```
Python code says hello world
```

The assistant might respond with:
```python
print("Hello, World!")
```

## Contributing

If you want to contribute to this project, feel free to fork it, create a branch, and submit a pull request. All contributions are welcome!

## License

This project is licensed under the MIT License.

---
