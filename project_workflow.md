# PhishAlert Project Workflow

Here is a complete, step-by-step breakdown of how the **PhishAlert** project works, tracking the workflow from data gathering to the final Machine Learning deployment.

### 1. Data Collection & Consolidation
The project relies on compiling a massive amount of URL data to teach the machine learning model the difference between legitimate and malicious websites.
* **Datasets Used:** The system begins by loading three separate CSV files containing different sets of URLs (`phishing_urls.csv`, `phishing_data.csv`, and `phishing_data2.csv`). 
* **Merging:** These files are unified into a single primary dataset (`phishing_site_urls.csv`), resulting in a robust dataset of over **549,000 unique URLs**.
* **Labels:** Each URL in the dataset is labeled as either **`good`** (a safe, legitimate site) or **`bad`** (a phishing or malicious site).

### 2. Data Preprocessing (NLP)
Machine Learning models cannot understand raw text or URLs directly. The URLs need to be broken down into words and standardized.
* **Tokenization (`RegexpTokenizer`):** The URLs are stripped of symbols (like `/`, `.`, `?`, `=`) and split into purely alphabetical words using Regular Expressions.
* **Stemming (`SnowballStemmer`):** The extracted words are passed through a stemmer, which reduces words to their root or base form (e.g., "running" becomes "run", "updating" becomes "updat"). This reduces the complexity of the data.
* **Reconstruction:** These root words are joined back together into a space-separated string (a "sentence" of root words) that represents the core components of the URL.

*(Note: During this phase, the developer also generated **Word Clouds** to visualize which words are most commonly used by hackers to disguise bad URLs compared to legitimate ones.)*

### 3. Feature Extraction (Vectorization)
* **Count Vectorization (`CountVectorizer`):** The text generated in the previous step is passed through a Count Vectorizer. This technique converts the "sentences" of root words into a large sparse mathematical matrix of token counts. Essentially, it transforms the text data into numerical arrays that the ML algorithms can process mathematically.

### 4. Machine Learning Model Training & Evaluation
The numerical data is split into a **Training Set** (to teach the model) and a **Testing Set** (to evaluate its performance on unseen data).
* **Model Selection:** The developer tested two primary classification algorithms:
  1. **Logistic Regression:** A statistical model that predicts the probability of a binary outcome (e.g., 0 or 1, Good or Bad). It achieved **~96% accuracy**.
  2. **Multinomial Naive Bayes (MultinomialNB):** A probabilistic algorithm widely used for Natural Language Processing. It achieved **~95% accuracy**.
* **Finalizing the Pipeline:** Because **Logistic Regression** performed the best, the developer created a unified Sklearn **Pipeline** (`make_pipeline`) that chains together the Custom Tokenization, the CountVectorizer, and the Logistic Regression model into a single step. 
* **Exporting the Model (`pickle`):** This final pipeline achieved **98% accuracy**. It is then saved to the local disk as a serialized file named **`phishing.pkl`**. This ensures the model doesn't need to be retrained every time the app starts.

### 5. Desktop Application Integration (Tkinter GUI)
Once the model is trained and saved, it is integrated into a lightweight, standalone Desktop Application.
* **Frontend Framework:** The project uses **Tkinter**, Python's standard GUI library, inside `PhishAlert_App.pyw` to create a simple, native window without needing a terminal or web browser.
* **Loading the Model:** When the application is launched, it uses the `pickle` library to securely load the pre-trained `phishing.pkl` pipeline into memory. It also includes an automatic patch to ensure compatibility with modern versions of `scikit-learn`.
* **Live Predictions:** When a user pastes a URL into the application's text box and clicks "Check URL", the string is passed directly to the loaded pipeline. The pipeline automatically applies the exact same Tokenization, Stemming, Vectorization, and Logistic Regression prediction process it learned during training.
* **Output:** If the model predicts the URL is "bad", it displays a prominent red warning: **"🚨 This is a Phishing Site!"**. Otherwise, it displays a green confirmation: **"✅ This is a safe (good) site."**
