import pandas as pd

# Load the CSV file
file_path = 'foreign_awards.csv'
data = pd.read_csv(file_path)

# Convert date columns to datetime
data['award_base_action_date'] = pd.to_datetime(data['award_base_action_date'], errors='coerce')

# Filter rows where recipient_name contains "undisclosed" (case-insensitive)
filtered_data = data[data['recipient_name'].str.contains('undisclosed', case=False, na=False)]

# Create unspent_amount column
filtered_data['unspent_amount'] = filtered_data['total_obligated_amount'] - filtered_data['total_outlayed_amount']

# Further filter where unspent_amount is greater than 0
final_filtered_data = filtered_data[filtered_data['unspent_amount'] > 0]

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

# Sort by Award Base Action Date in reverse chronological order
final_output = final_output.sort_values(by='Award Base Action Date', ascending=False)

# Calculate totals for numeric columns
totals = final_output[['Total Obligated Amount', 'Total Outlayed Amount', 'Unspent Amount']].sum().round(2)

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
