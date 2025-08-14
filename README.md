# Writing Prompt Generator
This Python project uses the **DeepSeek V3 model** via OpenRouter to generate unique and creative writing prompts based on a theme provided by the user. The generated prompts are saved into a text file `prompt.txt`, one line per line.

---

## **Libraries Required**

Make sure you have Python installed. Then install the following library:

```bash
pip install openai
```

## How It Works

1. **Main Function**

```python
def main():
    story_theme = input("Enter a theme for your writing prompt: ")
    reply = generate_prompt(story_theme)
    
    with open("prompt.txt", "w") as file:
        lines = reply.splitlines()
        for line in lines:
            file.write(line + "\n")
```
* Prompts the user for input to enter a theme.
* Calls generate_prompt() to get the AI-generated text.
* Saves the text into prompt.txt.

2. **Generating a Writing Prompt**

```python
def generate_prompt(theme):
    response = client.chat.completions.create(
        model="deepseek/deepseek-chat-v3-0324:free",
        messages=[
            {"role": "system", "content": "You are a Professor of English at a prestigious university that writes creative and unique writing prompts."},
            {"role": "user", "content": theme}
        ]
    )
    return response.choices[0].message.content
```
* theme: Input (string format) provided by the user.
* role (system and user): defines how the system should operate and the user's role for the system
* Return value: The AI response according to the user's theme (String format).
