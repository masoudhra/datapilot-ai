# DataPilot AI

DataPilot AI is an AI-powered SQL Interview Preparation Agent built with **Google ADK 2.0** and **Gemini 2.5 Flash**.

The agent helps aspiring Data Analysts practice SQL interview questions by generating realistic interview scenarios, evaluating SQL answers, and providing structured interview feedback.

---

## Features

- 🎯 Generate realistic SQL interview questions
- 🗂️ Provide business scenarios and table schemas
- 🧠 Evaluate SQL answers
- ✅ Validate SQL syntax using a custom Python tool
- 📊 Give an interview score
- 💡 Highlight strengths and areas for improvement
- 📚 Recommend the next learning topic

---

## Tech Stack

- Google ADK 2.0
- Gemini 2.5 Flash
- Python
- Agents CLI
- Local ADK Playground

---

## Agent Workflow

```
User
      ↓
DataPilot AI
      ↓
Generate SQL Interview Question
      ↓
User submits SQL Answer
      ↓
validate_sql_query Tool
      ↓
Interview Feedback
      ↓
Interview Score
      ↓
Learning Recommendation
```

---

## Example Prompt

```text
Start my Data Analyst SQL interview.
```

---

## Example SQL Answer

```sql
SELECT
    c.customer_id,
    c.first_name,
    c.last_name,
    SUM(o.total_amount) AS total_spent,
    COUNT(o.order_id) AS number_of_orders
FROM Customers c
JOIN Orders o
    ON c.customer_id = o.customer_id
GROUP BY
    c.customer_id,
    c.first_name,
    c.last_name
ORDER BY total_spent DESC
LIMIT 5;
```

---

## Example Feedback

```
Interview Score: 9/10

Strengths
• Correct JOIN
• Proper aggregation
• Good use of GROUP BY

Areas for Improvement
• Consider handling customers without orders using LEFT JOIN.

Learning Recommendation
Review OUTER JOINs and Window Functions.
```

---

## Security

- API keys are stored locally in `.env`
- `.env` is excluded from Git using `.gitignore`
- `.env.example` is provided as a safe template

---

## Run Locally

Install dependencies:

```bash
agents-cli install
```

Run the local playground:

```bash
agents-cli playground
```

Then open:

```
http://127.0.0.1:8080
```

---

## Future Improvements

- Multiple interview difficulty levels
- Advanced SQL validation
- Personalized learning plans
- Python interview mode
- Power BI interview mode

---

## Capstone Project

This project was developed for the **Kaggle 5-Day AI Agents: Intensive Vibe Coding Course with Google** Capstone Project.

Built with ❤️ using Google ADK 2.0 and Gemini.