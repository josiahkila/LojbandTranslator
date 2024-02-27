import tkinter as tk
from tkinter import scrolledtext
from src.logic_processor import count_characters, count_words, simple_translate

class TranslatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Processor and Translator")

        # Text input
        self.txt_input = scrolledtext.ScrolledText(root, height=10)
        self.txt_input.pack(pady=10)

        # Character count button
        self.btn_char_count = tk.Button(root, text="Count Characters", command=self.display_char_count)
        self.btn_char_count.pack(pady=5)

        # Word count button
        self.btn_word_count = tk.Button(root, text="Count Words", command=self.display_word_count)
        self.btn_word_count.pack(pady=5)

        # Translate button
        self.btn_translate = tk.Button(root, text="Translate", command=self.display_translation)
        self.btn_translate.pack(pady=5)

        # Display results
        self.lbl_result = tk.Label(root, text="", font=("Arial", 12))
        self.lbl_result.pack(pady=10)

    def display_char_count(self):
        text = self.txt_input.get("1.0", "end-1c")
        chars = count_characters(text)
        self.lbl_result.config(text=f"Character Count: {chars}")

    def display_word_count(self):
        text = self.txt_input.get("1.0", "end-1c")
        words = count_words(text)
        self.lbl_result.config(text=f"Word Count: {words}")

    def display_translation(self):
        text = self.txt_input.get("1.0", "end-1c")
        # Assuming translation_dict is defined within your logic_processor.py
        translation_dict = {
            'hello': 'hola',
            'world': 'mundo',
            # Add your translations here
        }
        translated_text = simple_translate(text, translation_dict)
        self.lbl_result.config(text=f"Translated Text: {translated_text}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TranslatorApp(root)
    root.mainloop()
