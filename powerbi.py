import openai
import pandas as pd

# --------------------------------------------------------
# INSERT YOUR OPENAI API KEY BELOW
openai.api_key = "YOUR_API_KEY_HERE"
# --------------------------------------------------------

# Get data from Power BI (Power BI assigns dataset to the variable 'dataset')
df = dataset  # This line must not be changed when running in Power BI

# Sample the data if it's large
sample_df = df.sample(min(1000, len(df)), random_state=42)

# Generate a prompt based on a small sample of the dataset
def generate_prompt(dataframe):
    head = dataframe.head(5).to_markdown()
    prompt = f"""
You are a business data analyst.

Analyze the dataset sample below and return a professional insight report including:
1. Key trends or anomalies
2. Descriptive statistics
3. Business recommendations
4. Possible causes for any patterns or shifts
5. Any risks or warnings

Sample data:
{head}
"""
    return prompt

# Query GPT model using the generated prompt
def get_ai_insight(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.5,
            max_tokens=500
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error communicating with OpenAI: {str(e)}"

# Generate prompt and get insight
prompt = generate_prompt(sample_df)
insight = get_ai_insight(prompt)

# Output the result in Power BI visual
print("AI-Generated Business Insight:\n")
print(insight)
