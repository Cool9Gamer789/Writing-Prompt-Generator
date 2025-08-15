from openai import OpenAI

# Creating the 'Open Router' url so we can use the api from Deepseek
client = OpenAI(
    # YOU MUST CREATE YOUR OWN API KEY
    api_key="",
    base_url="https://openrouter.ai/api/v1",
)

def main():
    story_theme = input("Enter a theme for your writing prompt: ").rstrip()
    # Contains the reply from the Deepseek
    reply = generate_prompt(story_theme)
    
    with open("prompt.txt", "w") as file:
        # Seperates the long string into seperate lines
        lines = reply.splitlines()
        for line in lines:
            file.write(line + "\n")

# Create a model to generate a writing prompt
def generate_prompt(theme):
    response = client.chat.completions.create(
        model="deepseek/deepseek-chat-v3-0324:free",
        messages=[
            {"role": "system", "content": "You are a Professor of English at a prestigous university that writes creative and unique writing prompts."},
            {"role": "user", "content": theme}
        ]
    )

    # Return the response from Deepseek
    return response.choices[0].message.content

if __name__ == "__main__":
    main()

