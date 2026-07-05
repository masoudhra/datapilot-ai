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

def validate_sql_query(query: str) -> dict:
    """Performs a basic syntax check on a SQL query.

    Args:
        query: The SQL query string to validate.

    Returns:
        A dict with 'status' (either 'success' or 'error') and 'message' describing the result.
    """
    query_clean = query.strip().upper()
    if not query_clean.startswith("SELECT"):
        return {
            "status": "error",
            "message": "SQL query must start with a SELECT statement."
        }
    if "FROM" not in query_clean:
        return {
            "status": "error",
            "message": "SQL query is missing the FROM clause."
        }
    return {
        "status": "success",
        "message": "Basic syntax check passed (SELECT and FROM clauses found)."
    }
