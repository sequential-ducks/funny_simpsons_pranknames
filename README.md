
# Prank Call Name Generator 🎉

![Bart Simpson Prank Call Vibes](https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExM3R1dWs4MzR6Z2p2c2R1YjBwMDNtYXhmZGliZmR6cDAzZGszMTBpZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/xT5LMSpdMqGMvQRkFa/giphy.gif)

## Project Description
A whimsical Python script that generates random, hilarious prank call names inspired by Bart Simpson's legendary prank calls to Moe's Bar from *The Simpsons*. Think *"Hugh Jass"*, *"I.P. Freely"*, or *"Amanda Hugnkiss"*. Think there should have been more prank calls made? Now you can create your own!

## Features
- ✨ **Data-Powered Comedy:** Prank names are sourced straight from the Simpsons Wiki.
- 📊 **Data Cleaning with Pandas:** Raw prank name data is polished and split into first and last names.
- 👨‍💼 **Interactive Fun:** Generate as many prank call names as your heart desires!
- ↺ **Repeat or Quit:** Keep the laughs coming or exit anytime.

---

## How It Works 💡
1. The program downloads prank call names using the **`requests`** library.
2. Data is cleaned and organized into lists using **`pandas`**, making it ready for top-notch prank name generation.
3. First and last names are randomly selected and combined into the perfect prank call identities.
4. You decide whether to generate another name or quit.

## Project Highlights 🌐
This project demonstrates:
- **Data Retrieval:** Effective use of `requests` to download external resources.
- **Data Manipulation:** Leveraging `pandas` for data cleaning and preparation.
- **User Interaction:** Designing fun, interactive experiences in Python.

---

## Setup & Requirements
 Clone the repository:  
   ```bash
   git clone https://github.com/sequential-ducks/funny_simpsons_pranknames.git
   cd funny_simpsons_pranknames
   ```
### With Pip
1. Install dependencies:  
   ```bash
   pip install -r requirements.txt  
   ```

2. Run the script:  
   ```bash
   python prank_names_script.py
   ```
## With UV
1. Create venv 
   ```bash
    uv venv
   ```
   Activate venv
   ```bash
   .venv\Scripts\activate
   ```
2. Install dependencies:
       ```bash
   uv sync
   ```
3. Run the script:  
   ```bash
   python prank_names_script.py
   ```
---

## Example Output 🤣
```
Welcome to generating amusing names in the style of prank calls made by Bart Simpson on the classic show The Simpsons!

Press Enter to generate a name or press q to exit:
Emma O'Problem

Press Enter to generate a name or press q to exit:
Milady Jass

Press Enter to generate a name or press q to exit:  q
```

---

## License
This project is licensed under the MIT License.

---

## Contact
Built with 😉 and Python by [Anna Sivula](https://github.com/sequential-ducks).

Have fun — but don't get caught prank-calling!

