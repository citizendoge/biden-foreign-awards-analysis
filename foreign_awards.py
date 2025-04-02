import pandas as pd
from datetime import datetime, timedelta

# Load the CSV file
file_path = 'foreign_awards.csv'
data = pd.read_csv(file_path)

# Convert date columns to datetime
date_columns = [
    'period_of_performance_start_date',
    'period_of_performance_current_end_date',
    'award_base_action_date'
]
for column in date_columns:
    data[column] = pd.to_datetime(data[column], errors='coerce')

# Create flag_low_outlay column
data['flag_low_outlay'] = (data['total_obligated_amount'] > 1_000_000) & (data['total_outlayed_amount'] < 100_000)

# Create risk_score column based only on flag_low_outlay
data['risk_score'] = data['flag_low_outlay'].astype(int)

# Filter rows where recipient_name contains "undisclosed" (case-insensitive)
filtered_data = data[data['recipient_name'].str.contains('undisclosed', case=False, na=False)]

# Create unspent_amount column
filtered_data['unspent_amount'] = filtered_data['total_obligated_amount'] - filtered_data['total_outlayed_amount']

# Further filter where unspent_amount is greater than 0
final_filtered_data = filtered_data[filtered_data['unspent_amount'] > 0]

# Calculate the sum of numeric columns
totals = final_filtered_data[['total_obligated_amount', 'total_outlayed_amount', 'unspent_amount']].sum()

# Create a total row
total_row = pd.DataFrame({
    'contract_award_unique_key': [''],
    'recipient_name': ['TOTAL'],
    'total_obligated_amount': [totals['total_obligated_amount']],
    'total_outlayed_amount': [totals['total_outlayed_amount']],
    'unspent_amount': [totals['unspent_amount']]
})

# Append the total row to the DataFrame
final_output = pd.concat([final_filtered_data, total_row], ignore_index=True)

# Print the final output
print(final_output[[
    'contract_award_unique_key',
    'recipient_name',
    'total_obligated_amount',
    'total_outlayed_amount',
    'unspent_amount'
]])

# Print the total number of rows in the filtered DataFrame
print("Total number of rows with 'undisclosed' in recipient_name:", len(filtered_data))

# List all available column names
print("\nColumn names:")
print(data.columns.tolist())

# Select and rename columns for export
final_output = final_filtered_data[[
    'contract_award_unique_key',
    'recipient_name',
    'total_obligated_amount',
    'total_outlayed_amount',
    'unspent_amount',
    'award_base_action_date'
]].rename(columns={
    'contract_award_unique_key': 'Contract Award Key',
    'recipient_name': 'Recipient Name',
    'total_obligated_amount': 'Total Obligated Amount',
    'total_outlayed_amount': 'Total Outlayed Amount',
    'unspent_amount': 'Unspent Amount',
    'award_base_action_date': 'Award Base Action Date'
})

# Round numeric columns to two decimal places
final_output[['Total Obligated Amount', 'Total Outlayed Amount', 'Unspent Amount']] = final_output[[
    'Total Obligated Amount', 'Total Outlayed Amount', 'Unspent Amount'
]].round(2)

# Calculate totals for numeric columns
totals = final_output[['Total Obligated Amount', 'Total Outlayed Amount', 'Unspent Amount']].sum()

# Create a total row
total_row = pd.DataFrame({
    'Contract Award Key': [''],
    'Recipient Name': ['TOTAL'],
    'Total Obligated Amount': [totals['Total Obligated Amount']],
    'Total Outlayed Amount': [totals['Total Outlayed Amount']],
    'Unspent Amount': [totals['Unspent Amount']],
    'Award Base Action Date': ['']
})

# Append the total row to the DataFrame
final_output_with_total = pd.concat([final_output, total_row], ignore_index=True)

# Export to CSV
final_output_with_total.to_csv('top_undisclosed_unspent.csv', index=False)
