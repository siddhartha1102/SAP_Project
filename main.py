from replace_image_text import image_to_text
from excel_date import date_conversion
#from combine import generate_summary
from highlight import hihglight
import os
from remove import remove
import json
output_directory = r"C:\SAP Project\Reports\Dec 2025"
input_directory = r"C:\SAP Project\raw files\Dec 2025"
input_file = 'Process_chain_01_Nov_2025.xlsx'
output_filename = 'Process_chain_01_Nov_2025_final.xlsx'


try:

    image_to_text(os.path.join(input_directory, input_file), os.path.join(input_directory, output_filename))
    date_conversion(os.path.join(input_directory, output_filename), os.path.join(output_directory , output_filename))
    #generate_summary(output_directory)
    hihglight(output_directory, output_filename)
    remove(input_directory)
except Exception as e:
    print(e)