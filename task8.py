import openpyxl
from datetime import datetime, timedelta
data_path = 'C:/Users/Dhanush N INT-214/Desktop/attendance.xlsx'  
workbook = openpyxl.load_workbook(data_path)
worksheet = workbook.active
data = list(worksheet.iter_rows(values_only=True))
# Extract column headers and data rows
headers = data[0]
rows = data[1:]
# Convert headers to a dictionary index for easy access
header_index = {header: idx for idx, header in enumerate(headers)}
# Calculate current date and previous 5 dates
current_date = datetime.today().strftime('%b %d')
previous_dates = [(datetime.today() - timedelta(days=i)).strftime('%b %d') for i in range(1, 6)]
# Find column indices for current date and previous dates
current_date_index = header_index.get(current_date)
previous_date_indices = [header_index.get(date) for date in previous_dates]
today_wfh_count = 0
today_wfo_count = 0
previous_wfh_count = 0
previous_wfo_count = 0
for row in rows:
    if current_date_index is not None:
        if row[current_date_index] == 'WFH':
            today_wfh_count += 1
        elif row[current_date_index] == 'WFO':
            today_wfo_count += 1
    
    if all(previous_date_indices) and any(row[i] in ['WFH', 'WFO'] for i in previous_date_indices):
        for i in previous_date_indices:
            if row[i] == 'WFH':
                previous_wfh_count += 1
            elif row[i] == 'WFO':
                previous_wfo_count += 1
result = []
for row in rows:
    if any(cell is None or cell == '' for cell in row):
        result.append(row[0])  # Append the value from the first column
print("Today's WFH Count:", today_wfh_count)
print("Today's WFO Count:", today_wfo_count)
print("Previous 5 days WFH Count:", previous_wfh_count)
print("Previous 5 days WFO Count:", previous_wfo_count)
print("Employees with Missing Attendance:", result)
workbook.close()
