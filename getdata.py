from pathlib import Path
import os
file_path = Path(r"C:\rename\10789_DANNY R COCHRAN_20260727_NSFLetter_43.pdf")
file_name = Path(file_path).stem  # Result: "20260729_London_SensorB"

# Split the string by the underscore delimiter
elements = file_name.split("_")

# Unpack elements directly into descriptive variables
memnum, Name, datet, lettern, index1 = elements

print(f"Membernum: {memnum}, Name: {Name}, Date: {datet}, Letter Name: {lettern}, Index: {index1}")

# Build filename using an f-string
filename = f"{Name}^{memnum}^0^{datet}^00000^{lettern}^.pdf"
file_count = sum(1 for item in file_path.iterdir() if item.is_file())


print(f"Number of files: {file_count}")
print(filename)

# Output: report_sales_2026-07-29.csv
# Output: Date: 20260729, City: London, Sensor: SensorB
full_path = file_path + filename


# Save the file
with open(full_path, "w") as new_file:
    new_file.write("Column1,Column2\nValue1,Value2")

print(new_file)
