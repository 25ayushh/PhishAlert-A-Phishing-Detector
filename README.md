# PhishAlert: A Phishing Detector

## Overview

PhishAlert is a lightweight desktop application designed to detect phishing attempts in URLs using machine learning algorithms. The project leverages Logistic Regression and Count Vectorization to identify and classify phishing websites. The goal of PhishAlert is to provide a user-friendly platform that enhances cybersecurity by proactively detecting and mitigating phishing threats.

## Features

- **Phishing Website Detection:** The system analyzes website URLs to identify phishing attempts using a trained machine learning pipeline.
- **User-Friendly Desktop Interface:** PhishAlert offers an intuitive Tkinter-based desktop interface where users can submit URLs for analysis without needing a web browser or command line.
- **Feature Importance Analysis:** The included Jupyter Notebook explores the importance of individual features in distinguishing between phishing and legitimate content, providing insights into key indicators of phishing behavior.

## How It Works

1. **Data Collection:** The system gathered a diverse dataset of both phishing and legitimate website URLs.
2. **Preprocessing:** The raw data underwent preprocessing, including cleaning and custom tokenization using Regular Expressions and Snowball Stemmer.
3. **Feature Extraction:** Informative features such as linguistic patterns were extracted using Count Vectorization.
4. **Model Training:** The system trained a Logistic Regression model to recognize patterns indicative of phishing behavior, achieving 98% accuracy.
5. **Deployment:** The trained model is saved as a serialized pipeline and loaded into a standalone Python GUI (`PhishAlert_App.pyw`) for easy user testing.

## Technical Specifications

- **Frontend:** Developed using **Tkinter** for a native, fast, and simple desktop window.
- **Backend/ML:** Python scripts handle text preprocessing, feature extraction, and model integration. Libraries like NLTK, scikit-learn, and pickle are used for natural language processing, machine learning, and model serialization.

## Installment Steps:
1. Run the following command to install the required packages:
    ```bash
    pip install -r requirements.txt
    ```
2. To use the PhishAlert Detector, simply double-click the desktop application file:
    ```
    PhishAlert_App.pyw
    ```
    *(Alternatively, you can run `python PhishAlert_App.pyw` in your terminal)*
