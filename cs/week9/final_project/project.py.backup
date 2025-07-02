# project.py
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TextAnalyzer Ultimate - An Optimized Intelligent Text Analysis Tool
"""
import re
from collections import Counter
from typing import Dict, List, Optional

# ===============================================================
# TOP-LEVEL FUNCTIONS AS PER REQUIREMENTS
# ===============================================================

def preprocess_text(text):
    import re

    # Normalize tabs and carriage returns to spaces
    text = re.sub(r'[\t\r]', ' ', text)

    # Check if the original text contains double newlines (before removing leading/trailing whitespace)
    has_double_newline = '\n\n' in text

    # Remove leading and trailing whitespace
    text = text.strip()

    # If the original text has double newlines and there's content after removing leading/trailing whitespace
    if has_double_newline and text:
        # Extract all non-whitespace character sequences (words)
        words = re.findall(r'\S+', text)
        # Join all words with double newlines
        return '\n\n'.join(words)
    else:
        # Process according to normal logic
        # Replace multiple consecutive newlines with double newlines
        text = re.sub(r'\n{2,}', '\n\n', text)
        # Protect double newlines with special markers
        text = text.replace('\n\n', '<<DOUBLE_NEWLINE>>')
        # Replace remaining single newlines with spaces
        text = text.replace('\n', ' ')
        # Restore double newlines
        text = text.replace('<<DOUBLE_NEWLINE>>', '\n\n')
        # Merge multiple spaces into single spaces
        text = re.sub(r' +', ' ', text)
        return text

def get_top_words(text: str, stop_words: set, top_n: int = 10) -> List[tuple[str, int]]:
    """
    Analyzes text to extract the top N most frequent words.
    This function attempts to use jieba for Chinese word segmentation and filters out stop words.
    """
    try:
        import jieba
        # Separate and process Chinese and English text
        chinese_text = ''.join(re.findall(r'[\u4e00-\u9fff]+', text))
        english_text = ' '.join(re.findall(r'[a-zA-Z]+', text.lower()))

        words = []
        if chinese_text:
            # Use precise mode for segmentation, keeping only words with length > 1
            words.extend([word for word in jieba.cut(chinese_text) if len(word) > 1])
        if english_text:
            words.extend(english_text.split())

        # Filter out stop words
        filtered_words = [word for word in words if word not in stop_words]
        return Counter(filtered_words).most_common(top_n)

    except ImportError:
        # If jieba is not available, perform simple English word frequency analysis
        words = re.findall(r'[a-zA-Z]+', text.lower())
        filtered_words = [word for word in words if word not in stop_words]
        return Counter(filtered_words).most_common(top_n)

def calculate_lexical_diversity(words: List[str]) -> float:
    """
    Calculates the Type-Token Ratio (TTR).
    TTR = (Number of unique words / Total number of words)
    Returns 0.0 if the total number of words is zero.
    """
    if not words:
        return 0.0
    return len(set(words)) / len(words)

# ===============================================================
# PRIMARY CLASSES
# ===============================================================

class TextAnalyzer:
    """A class that encapsulates the core text analysis logic."""
    def __init__(self):
        self.stop_words = {
            # Chinese stop words
            '的', '了', '在', '是', '我', '有', '和', '就', '不', '人', '都', '一', '個', '也', '會', '要', '可以', '這個',
            # English stop words
            'the', 'a', 'an', 'is', 'are', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 'this', 'that', 'it', 'we'
        }

    def analyze(self, text: str) -> Dict:
        """
        Performs a comprehensive analysis on a single piece of text.
        """
        processed_text = preprocess_text(text)
        if not processed_text:
            return {}

        all_words = re.findall(r'\b[a-zA-Z]+\b|[\u4e00-\u9fff]', processed_text)
        english_words = re.findall(r'\b[a-zA-Z]+\b', processed_text)
        sentences = re.split(r'[.!?。！？]+', processed_text)
        sentences = [s for s in sentences if s.strip()]

        # Call top-level functions for analysis
        top_words = get_top_words(processed_text, self.stop_words)
        lexical_diversity = calculate_lexical_diversity(all_words)

        return {
            "stats": {
                "char_count": len(processed_text),
                "word_count": len(all_words),
                "english_word_count": len(english_words),
                "chinese_char_count": len(re.findall(r'[\u4e00-\u9fff]', processed_text)),
                "sentence_count": len(sentences),
                "avg_sentence_length": round(len(all_words) / len(sentences), 2) if sentences else 0,
            },
            "top_words": top_words,
            "complexity": {
                "lexical_diversity": round(lexical_diversity, 3)
            }
        }

class AppInterface:
    """A class to handle user interaction, input, and output."""
    def __init__(self):
        self.analyzer = TextAnalyzer()

    def run(self):
        """The main application loop."""
        self.show_header()
        while True:
            text = self.get_input()
            if not text:
                print("\n👋 Thank you for using TextAnalyzer Ultimate!")
                break

            print("\n🔍 Analyzing...")
            results = self.analyzer.analyze(text)
            self.display_results(results)

            if not self.ask_continue():
                print("\n👋 Thank you for using TextAnalyzer Ultimate!")
                break

    def show_header(self):
        print("\n" + "="*65)
        print("TextAnalyzer Ultimate - An Optimized Intelligent Text Analysis Tool".center(65))
        print("="*65)

    def get_input(self) -> str:
        print("\n📝 Please enter or paste the text you want to analyze (press Enter twice to start analysis):")
        lines = []
        while True:
            try:
                line = input()
                if not line:
                    break
                lines.append(line)
            except EOFError:
                break
        return "\n".join(lines)

    def display_results(self, results: Dict):
        if not results:
            print("⚠️ Input is empty, cannot analyze.")
            return

        print("\n" + "📊 Analysis Report " + "="*50)

        # Basic Statistics
        stats = results.get("stats", {})
        print("\n📈 Basic Statistics:")
        print(f"   - Total Characters: {stats.get('char_count', 0):,}")
        print(f"   - Total Words: {stats.get('word_count', 0):,}")
        print(f"   - Sentence Count: {stats.get('sentence_count', 0):,}")
        print(f"   - Avg. Sentence Length: {stats.get('avg_sentence_length', 0)} words")

        # Top Words
        top_words = results.get("top_words", [])
        print("\n🔥 Top 5 Frequent Words:")
        if not top_words:
            print("   (Not enough words to analyze)")
        else:
            for i, (word, count) in enumerate(top_words[:5]):
                print(f"   {i+1}. {word} ({count} times)")

        # Complexity
        complexity = results.get("complexity", {})
        diversity = complexity.get('lexical_diversity', 0)
        rating = "High" if diversity > 0.8 else "Medium" if diversity > 0.5 else "Low"
        print("\n🧠 Lexical Diversity (TTR):")
        print(f"   - Diversity Score: {diversity} ({rating})")

        print("\n" + "="*65)

    def ask_continue(self) -> bool:
        choice = input("\n🔄 Analyze another text? (Y/n): ").strip().lower()
        return choice != 'n'

def main():
    """Main entry point of the program."""
    app = AppInterface()
    app.run()

if __name__ == "__main__":
    main()
