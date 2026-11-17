
# NovaRetail Q2 2026 Executive QBR Deck

## Overview

This project automates the generation of a 5-slide executive business review deck for NovaRetail using Python, PowerPoint automation, and Google ADK.

The solution analyzes business performance, customer experience, and operational risk data, generates insights and charts, and creates a presentation-ready PowerPoint deck.

## Problem Statement
Leadership requires a concise executive review deck generated directly from raw business data.

The solution should:

Analyze performance data
Generate business insights
Create charts automatically
Populate a fixed PowerPoint template
Generate an executive-ready presentation
Features
Core Features
Dynamic KPI generation
Dynamic executive summary
Dynamic business insights
Dynamic recommendations
Automated chart generation
Automated PowerPoint generation
Template placeholder replacement
ADK Enhancements
Google ADK Agent integration
Business Story Tool
Executive Deck Generation Tool
Agent-driven report generation
Session state support for business story and generated deck information
Project Structure
NovaRetail-Executive-Deck-Generator/
charts/
data/
icons/
output/
template/
tools/
business_story.py
chart_generator.py
customer_chart_generator.py
data_loader.py
ppt_generator.py
risk_chart_generator.py
.gitignore
agent.py
README.md
requirements.txt

## Installation
1. Clone the Repository
Clone the repository and navigate to the project directory.

2. Create a Virtual Environment
python -m venv venv
3. Activate the Virtual Environment
For Windows:

venv\Scripts\activate
4. Install Dependencies
pip install -r requirements.txt
Environment Variable Setup
Create a .env file in the project root directory.

Add your Google API key:

GOOGLE_API_KEY=your_google_api_key_here
Replace your_google_api_key_here with your actual Google API key.

Do not commit the .env file or your actual API key to GitHub.

Running the Application
Make sure the virtual environment is activated and the required environment variable is configured.

## Start the Google ADK web interface:

adk web
Open the ADK web interface and select the novaretail_agent.

Get the Business Story
Use a prompt such as:

What is the NovaRetail business story?
The agent uses the Business Story Tool to analyze the NovaRetail dataset and return dataset-based business insights.

## Generate the Executive Deck
Use the following prompt:

Generate the NovaRetail executive deck.
The agent calls the Executive Deck Generation Tool and generates the PowerPoint presentation.

The generated presentation is saved to:

output/NovaRetail_Q2_2026_Executive_QBR_Final.pptx
Output
The final output is a 5-slide NovaRetail Quarterly Business Review presentation containing:

Executive Summary and KPIs
Business Performance
Customer Experience
Operational Risk
Recommended Actions and Next Steps
The KPIs, insights, recommendations, charts, and executive story are generated from the underlying NovaRetail business data.