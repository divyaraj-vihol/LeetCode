import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    # Handle invalid input (negative or non-positive N)
    if N <= 0:
        return pd.DataFrame({f"getNthHighestSalary({N})": [None]})
    
    # Get distinct salaries sorted in descending order
    distinct_salaries = employee['salary'].drop_duplicates().sort_values(ascending=False)
    
    # Check if N is greater than the number of distinct salaries
    if N > len(distinct_salaries):
        return pd.DataFrame({f"getNthHighestSalary({N})": [None]})
    
    # Get the N-th highest salary
    nth_salary = distinct_salaries.iloc[N - 1]
    
    return pd.DataFrame({f"getNthHighestSalary({N})": [nth_salary]})

# Example usage with the given input:
df = pd.DataFrame({'id': [1, 2, 3], 'salary': [100, 200, 300]})
print(nth_highest_salary(df, -1))  # This should output 'null' or None
