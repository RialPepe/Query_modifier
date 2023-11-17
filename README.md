This project provides a simple tool to modify SQL queries by replacing specific keywords and variable names with substitution labels. The tool is useful for anonymizing or pseudonymizing SQL queries.

Key Features:
Lowercasing: Converts the SQL query to lowercase to ensure consistency.
Name Replacement: Substitutes specific variable names and keywords with replacement labels (e.g., x1, x2).
Variable Legend: Provides a legend mapping original names to the substitution labels used in the modified query.
Usage:
Insert your SQL query into the sql_query variable.
Run the script.
The modified SQL query is printed in the console along with a variable legend for replacement.
This project is particularly useful when you need to share SQL queries without revealing sensitive information about specific variable names or keywords. It can be applied in scenarios where you want to transform queries with confidential data into more generic queries suitable for sharing with AI programs without compromising data privacy.

Feel free to adapt and integrate this tool into your workflow to facilitate the safe handling of SQL queries in scenarios involving data sharing or collaboration with AI systems.
