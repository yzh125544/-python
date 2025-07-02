# TextAnalyzer Ultimate - An Optimized Intelligent Text Analysis Tool

#### Video Demo:  <[URL HERE](https://youtu.be/E_J3x2HCpdw)>

---

## Project Description

`TextAnalyzer Ultimate` is an advanced command-line text analysis tool designed for writers, students, and language researchers. While traditional word counters are often too simplistic and professional academic software can be overly complex, this project aims to fill the gap by providing a solution that is both powerful and easy to use.

It not only handles standard text statistics but also features a core capability to **efficiently analyze very long texts** and provide quantitative metrics on **lexical diversity**. Users can simply paste text directly into the terminal to receive an instant, multi-dimensional analysis report, helping them to deeply understand and improve their writing.

---

## Key Features

* **Cross-Lingual Support**: Capable of simultaneously processing and providing statistics for both Chinese characters and English words.
* **Intelligent Text Preprocessing**: Automatically cleans and standardizes input text by removing redundant spaces, newlines, and special characters while preserving paragraph structure to ensure analytical accuracy.
* **Basic Data Statistics**: Provides core data points including total character count, total word count, sentence count, and average sentence length.
* **High-Frequency Word Extraction**: Utilizes the `jieba` library for Chinese word segmentation and incorporates a stop-word filter to accurately identify the most significant core vocabulary in the text.
* **Lexical Diversity Analysis**: Calculates the text's Type-Token Ratio (TTR), a key academic metric for measuring how varied an author's vocabulary is and whether they avoid repetition.

---

## Project File Structure

This project follows principles of modularity and testability, primarily consisting of the following three files:

### `project.py`

This is the main executable file for the project, where all functionalities converge.

* **Top-Level Functions**:
    * `preprocess_text()`: Responsible for cleaning and standardizing text, forming the foundation for all subsequent analysis.
    * `get_top_words()`: The core frequency analysis function, encapsulating the logic for segmentation, filtering, and counting.
    * `calculate_lexical_diversity()`: A standalone mathematical function responsible for calculating the TTR metric.
    * These three functions were intentionally designed as top-level functions to meet the CS50P project's structural requirements and to make them easily accessible for unit testing.

* **Classes**:
    * `TextAnalyzer`: This class serves as the analysis engine, encapsulating all core analysis methods and configurations (such as the stop word list). It is responsible for performing the actual computations.
    * `AppInterface`: This class handles all user-facing interactions, including displaying the welcome screen, getting user input, and formatting and beautifully presenting the final analysis report.
    * `main()`: The sole entry point of the program, which initializes the `AppInterface` and starts the main application loop.

### `test_project.py`

The sole purpose of this file is to ensure the correctness and stability of the core functions in `project.py`.

* **Test Scope**: Contains unit tests specifically for the three top-level functions: `preprocess_text`, `get_top_words`, and `calculate_lexical_diversity`.
* **Testing Framework**: Uses the `pytest` framework.
* **Test Coverage**: Each test function covers multiple edge cases, such as handling strings with complex whitespace and newlines, empty inputs, and expected mathematical outcomes, thereby ensuring the robustness of the program.

### `requirements.txt`

A simple text file used to declare the external libraries required for this project to run.

* `jieba`: A powerful Python library for Chinese word segmentation, which is key to the project's ability to accurately analyze Chinese word frequency.
* `pytest`: The standard testing framework for Python, used to execute all tests in `test_project.py`.

---

## Design Choices and Philosophy

During the development of this project, several key design decisions were made:

1.  **Why a Command-Line Interface (CLI)?**
    Compared to a Graphical User Interface (GUI), a CLI application is more lightweight, efficient, and easier to deploy across different platforms. It allows users to quickly interact with the program via simple copy-paste operations without the need to install complex GUI libraries, better suiting the use case of rapid analysis.

2.  **Why an Object-Oriented (OOP) Structure?**
    Although some core functionalities were designed as top-level functions to meet course requirements, the project's main body still adopts an object-oriented design. I separated the "analysis logic" (`TextAnalyzer`) from the "presentation logic" (`AppInterface`). This follows the important software engineering principle of "Separation of Concerns," which makes the code structure clearer and easier to maintain and extend. For example, if I wanted to change the interface from a terminal to a website in the future, I would only need to modify `AppInterface` without touching the core analysis engine.

3.  **Why Preprocess Text?**
    Raw text pasted by users is often full of non-standard formatting, such as extra spaces and different newline characters (Windows' `\r\n` vs. Linux/Mac's `\n`). Without preprocessing, the accuracy of the analysis would be severely compromised. The `preprocess_text` function ensures that no matter how messy the input format is, it is standardized into a clean and consistent state, which is the cornerstone for all subsequent precise analysis.

---

## How to Use

1.  **Install Dependencies**:
    In your terminal, navigate to the project's root directory and run the following command:
    ```bash
    pip install -r requirements.txt
    ```
2.  **Run the Program**:
    ```bash
    python project.py
    ```
3.  **Input Text**:
    After the program starts, simply paste any text you wish to analyze into the terminal.
4.  **Start Analysis**:
    After pasting the text, press the `Enter` key twice in a row, and the analysis report will be displayed immediately.
