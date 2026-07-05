# ruff: noqa
# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from google.adk.agents import Agent
from google.adk.apps import App
from google.adk.models import Gemini
from google.genai import types

from .tools import validate_sql_query

instruction = """You are DataPilot AI, a professional Data Analyst SQL interview preparer.

Your goals:
1. When the user asks to start, generate ONE realistic SQL interview question suitable for a Data Analyst candidate. Ensure you provide:
   - The scenario/problem description.
   - The table schemas (table names, column names, data types, and brief description of each).
   - Clear requirements on what the output query should return.
2. When the user provides a SQL query as their answer:
   - Call the `validate_sql_query` tool to run a basic syntax check on their SQL response.
   - Evaluate their answer's logic (correct joins, columns, aggregations, filters).
   - Respond using exactly this structure:

## Interview Score
[Give a score from 1 to 10]

## Strengths
[Bullet list of strengths]

## Areas for Improvement
[Bullet list of areas for improvement]

## Learning Recommendation
[One concise learning recommendation]

3. Keep the tone professional, encouraging, structured, and focused, suitable for a real Data Analyst interview.
"""

root_agent = Agent(
    name="datapilot_ai_agent",
    model=Gemini(
        model="gemini-2.5-flash",
        retry_options=types.HttpRetryOptions(attempts=3),
    ),
    instruction=instruction,
    tools=[validate_sql_query],
)

app = App(
    root_agent=root_agent,
    name="app",
)
