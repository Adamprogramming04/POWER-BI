# Power BI AI Insights Generator

This project connects Power BI to OpenAI's GPT model to automatically generate natural-language insights, trend summaries, and business recommendations from your data.

## Features

- Automatically summarizes trends and patterns from your data
- Highlights anomalies, risks, and performance shifts
- Provides plain-language business recommendations
- Integrates directly into Power BI through a Python script
- Uses OpenAI's GPT (ChatGPT) via API

## How It Works

1. Power BI loads your dataset and passes it to a Python visual
2. The Python script sends a sample of your data to OpenAI
3. GPT returns a natural-language summary of what it finds
4. The insight appears directly in your Power BI report

## OpenAI Setup

To use this project, you need an OpenAI API key.

### Steps to Get Your API Key:

1. Visit: https://platform.openai.com/account/api-keys
2. Log in or sign up for an OpenAI account
3. Click "Create new secret key"
4. Copy the key (it will look like `sk-...`)
5. Create a `.env` file in your project folder to store the key

### Example `.env` file:

