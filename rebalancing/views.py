from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from demosite.views import convert_to_standard_date_format
import time
from runs.models import Run
from datetime import datetime, timedelta
import re
from urllib.parse import quote
from .rebalancing_result import table_output, sector_hex_colors, chart_historical, chart_recommend, chart_current, table_output_new, portfolio_value_historical, portfolio_value_recommended, portfolio_value_current, index_value

# Create your views here.
def process_f1_input_form(rq):
    # Fetch form data
    purchase_date = convert_to_standard_date_format(rq.POST.get('purchase_date'))
    tracking_period = rq.POST.get('tracking_period')
    rebalancing_period = rq.POST.get('rebalancing_period')
    invested_amount = float(rq.POST.get('invested_amount', 0))
    display_name = rq.POST.get('display_name')
    index = rq.POST.get('index')
    
    
    # Ticker data - 
    historical_symbols = rq.POST.getlist('historical_symbols[]')
    historical_target_allocations = rq.POST.getlist('historical_target_allocations[]')

    recommendation_symbols = rq.POST.getlist('recommendation_symbols[]')
    recommendation_target_allocations = rq.POST.getlist('recommendation_target_allocations[]')

    current_symbols = rq.POST.getlist('current_symbols[]')
    current_target_allocations = rq.POST.getlist('current_target_allocations[]')  

    # Create the ticker data structure
    historical_data = []
    for i in range(len(historical_symbols)):
        historical_data.append({
            "symbol": historical_symbols[i],
            "target_allocation": historical_target_allocations[i],
            
        })
    
    recommendation_data = []
    for i in range(len(recommendation_symbols)):
        recommendation_data.append({
            "symbol": recommendation_symbols[i],
            "target_allocation": recommendation_target_allocations[i],
            
        })
    
    current_data = []
    for i in range(len(current_symbols)):
        current_data.append({
            "symbol": current_symbols[i],
            "target_allocation": current_target_allocations[i],
            
        })
    
    
    # Construct final JSON structure
    form_data = {
        "purchase_date": purchase_date,
        "tracking_period": tracking_period,
        "rebalancing_period": rebalancing_period,
        "invested_amount": invested_amount,
        "display_name": display_name,
        "index": index,
        "historical_data": historical_data,
        "recommendation_data": recommendation_data,
        "current_data": current_data
    }

    return form_data


def format_table_values(value):
    html = ''
    if isinstance(value, (float, int)):
        formatted_value = f"{value:,.2f}" if isinstance(value, float) else f"{value:,}"
        html_output = (
            f'<span class="formatted-value">{formatted_value}</span>'
            f'<span class="original-value">{value}</span>'
        )
    html += f"<td class='p-2 table-value-cell'>{html_output}</td>"
    return html


def format_table_values_2(value, row_color):
    html = ''
    if isinstance(value, (float, int)):
        formatted_value = f"{value:,.2f}" if isinstance(value, float) else f"{value:,}"
        html_output = (
            f'<span class="formatted-value">{formatted_value}</span>'
            f'<span class="original-value">{value}</span>'
        )
    html += f"<td class='p-2 fixed-columns table-value-cell' style='background-color: {row_color}'>{html_output}</td>"
    return html


def format_table_header(th_text):

    # Replace underscores with spaces for better readability
    formatted_text = th_text.replace('_', ' ')

    # Replace substrings with user-friendly symbols
    formatted_text = formatted_text.replace('perc', '%')
    formatted_text = formatted_text.replace('Alloc', 'A')
    formatted_text = formatted_text.replace('Shares', 'S')
    formatted_text = formatted_text.replace('Value', 'V')
    formatted_text = formatted_text.replace('Price', 'P')

    # Regex to remove patterns like Q1/Q2/Q3/Q4 or dates like '2023' or 'Jan 02 2020'
    formatted_text = re.sub(r'\b\d{4}\b', '', formatted_text)  # Remove just years like "2023", "2022"
    formatted_text = re.sub(r'\bQ[1-4]\b', '', formatted_text)  # Remove Q1, Q2, Q3, Q4
    formatted_text = re.sub(r'\b\d{1,2}\s*[A-Za-z]+\s*\d{2,4}\b', '', formatted_text)  # Remove "Jan 02 2020"
    formatted_text = re.sub(r'\b\d{1,2}\s*\d{4}\b', '', formatted_text)  # Remove combinations like "02 2023"
    formatted_text = re.sub(r'\b\d{4}\s*Q\d+\b', '', formatted_text)  # Remove patterns like "2023 Q2"
    
    # Remove extraneous spaces after regex replacements
    formatted_text = re.sub(r'\s+', ' ', formatted_text).strip()

    # Handle Δ (delta) replacements
    words = formatted_text.split()
    formatted_words = [
        word.capitalize() if word.lower() != 'delta' else 'Δ' for word in words
    ]

    # Join back transformed words
    new_formatted_text = ' '.join(formatted_words)

    # Combine original text in the secondary span for context
    original_text = th_text.replace('_', ' ').title()
    new_th = f'<span class="formatted-value">{new_formatted_text}</span><span class="original-value">{original_text}</span>'

    return new_th


# def generate_f1_data_table_old(table_data, sector_color, table_name):
#     # Define the predefined columns that always come first
#     predefined_columns = ["Symbol", "Company Name", "Sector", "Industry", "Market Cap"]

#     # Create a list to collect all columns in order
#     all_columns = predefined_columns[:]

#     # Collect all columns from the data
#     columns_from_data = set()
#     for symbol_data in table_data.values():
#         for column in symbol_data.keys():
#             if column not in predefined_columns and column not in columns_from_data:
#                 columns_from_data.add(column)
#                 all_columns.append(column)

#     # Group columns by their dates
#     date_groups = {}
#     for column in all_columns:
#         if re.search(r'\d{4}', column):  # Check if the column contains a year
#             column_name, date_part = column.rsplit(" ", 1)
#             date_groups[date_part] = date_groups.get(date_part, 0) + 1

#     date_values = list(date_groups.keys())
#     yesterday_date = (datetime.now() - timedelta(days=1)).strftime("%Y-%b-%d")

    
#     # Start creating the HTML for the carousel of date buttons
#     carousel_html = f'<div id="{table_name}-dateCarousel" class="carousel slide" data-ride="carousel" style="overflow: hidden;">'
#     carousel_html += '<div class="carousel-inner">'

#     # Create a chunk of buttons for each carousel item
#     button_chunk_size = 10  # Define how many buttons will fit per slide (adjust based on your layout)
#     total_buttons = len(date_values)
#     num_chunks = (total_buttons // button_chunk_size) + (1 if total_buttons % button_chunk_size != 0 else 0)

#     for chunk_index in range(num_chunks):
#         # Start a new carousel item
#         carousel_html += f'<div class="carousel-item {"active" if chunk_index == 0 else ""}">'

#         # Create buttons for this chunk
#         carousel_html += '<div class="btn-group" style="white-space: nowrap; display: flex; overflow-x: auto;">'
#         for i in range(chunk_index * button_chunk_size, min((chunk_index + 1) * button_chunk_size, total_buttons)):
#             date = date_values[i]
#             active_class = "active" if i == 0 else ""  # Make the first button in the carousel chunk active
#             button_text = date  # Default to the original date text

#             # If it's the first button, replace the text with yesterday's date
#             if i == 0:
#                 button_text = yesterday_date  # Change the button text to yesterday's date

#             carousel_html += f'<button class="btn btn-inverse-info btn-fw btn-sm date-button {active_class}" id="{table_name}-date-{date}" data-date="{table_name}-{date}" style="display: inline-block; margin-right: 5px;">{button_text}</button>'
#         carousel_html += '</div></div>'  # Close the btn-group and carousel-item

#     carousel_html += '</div>'  # Close carousel-inner

#     # Add the carousel controls (prev/next)
#     carousel_html += f'''
#     <a class="carousel-control-prev" href="#{table_name}-dateCarousel" role="button" data-slide="prev">
#         <span class="carousel-control-prev-icon" aria-hidden="true"></span>
#         <span class="sr-only">Previous</span>
#     </a>
#     <a class="carousel-control-next" href="#{table_name}-dateCarousel" role="button" data-slide="next">
#         <span class="carousel-control-next-icon" aria-hidden="true"></span>
#         <span class="sr-only">Next</span>
#     </a>
#     </div>'''  # Close carousel div

#     # Start creating the HTML table
#     table_html = f'<div class="table-responsive pb-3 custom-scrollbar-container"><table class="table" id="{table_name}-data-table">'

#     # Generate table headers
#     table_html += '<thead>'

#     # First header row with dates
#     table_html += '<tr class="date-header">'
#     first_date_replaced = False  # Flag to track if the first date is replaced
#     second_date_found = False  # Flag for the second date
#     first_date_column = None
#     second_date_column = None

#     for column in all_columns:
#         if column in predefined_columns:
#             table_html += '<th class="p-2"></th>'  # Empty cell for predefined columns
#         else:
#             column_name, date_part = column.rsplit(" ", 1)
#             if date_part in date_groups:
#                 colspan = date_groups[date_part]

#                 # Replace the first date with yesterday's date in the header
#                 if not first_date_replaced:
#                     table_html += f'<th class="p-2" colspan="{colspan}" data-date="{table_name}-{date_part}">{yesterday_date}</th>'
#                     first_date_column = date_part  # Track the first date
#                     first_date_replaced = True
#                 elif not second_date_found:
#                     table_html += f'<th class="p-2" colspan="{colspan}" data-date="{table_name}-{date_part}">{date_part}</th>'
#                     second_date_column = date_part  # Track the second date
#                     second_date_found = True
#                 else:
#                     # Add 'hidden-col' class for date columns beyond the first two dates
#                     hidden_class = "hidden-col"
#                     table_html += f'<th class="p-2 {hidden_class}" colspan="{colspan}" data-date="{table_name}-{date_part}">{date_part}</th>'

#                 del date_groups[date_part]  # Remove to avoid repeating
#     table_html += '</tr>'

#     # Second header row with all column names
#     table_html += '<tr>'
#     for column in all_columns:
#         class_name = ""

#         # Add the 'highlighted' class to the first and second date columns
#         if column.endswith(first_date_column):
#             class_name = "highlighted"
#         elif column.endswith(second_date_column):
#             class_name = ""
#         # Add the 'hidden-col' class for other date-related columns
#         elif column not in predefined_columns and first_date_column and second_date_column:
#             class_name = "hidden-col"

#         if column in predefined_columns:
#             table_html += f'<th class="p-2 {class_name}">{format_table_header(column)}</th>'
#         else:
#             column_name, date_part = column.rsplit(" ", 1)
#             table_html += f'<th class="p-2 {class_name}" data-date="{table_name}-{date_part}">{format_table_header(column_name)}</th>'
#     table_html += '</tr>'
#     table_html += '</thead>'

#     # Generate table rows
#     table_html += '<tbody>'
#     for symbol, data in table_data.items():
#         row_color = sector_color.get(data.get("Sector", ""), "#FFFFFF")  # Default to white if no sector

#         # Insert symbol and company name in the first two columns
#         company_name = data.get("Company Name", "-")  # Fallback to "-" if company name is missing
#         table_html += f'<tr style="background-color: {row_color};">'

#         # Symbol in the first column
#         table_html += f'<td class="p-2">{symbol}</td>'
        
#         # Company Name in the second column
#         table_html += f'<td class="p-2">{company_name}</td>'

#         # Insert other columns (after Symbol and Company Name)
#         for column in all_columns[2:]:  # Skip 'Symbol' and 'Company Name' since they're already added
#             cell_value = data.get(column, "-")  # Use "-" for missing values

#             class_name = ""
#             if re.search(r'\d{4}', column):  # If the column is date-related
#                 _, date_part = column.rsplit(" ", 1)
#                 data_date_attr = f' data-date="{table_name}-{date_part}"'

#                 # Add the 'hidden-col' class for columns beyond the first two dates
#                 if date_part not in {first_date_column, second_date_column}:
#                     class_name = "hidden-col"

#                 if date_part in {first_date_column}:
#                     class_name += " highlighted"
#             else:
#                 data_date_attr = ""

#             if isinstance(cell_value, (float, int)):
#                 formatted_value = f"{cell_value:,.2f}" if isinstance(cell_value, float) else f"{cell_value:,}"
#                 html_output = (
#                     f'<span class="formatted-value">{formatted_value}</span>'
#                     f'<span class="original-value">{cell_value}</span>'
#                 )
#                 table_html += f'<td class="p-2 table-value-cell {class_name}"{data_date_attr}>{html_output}</td>'
#             else:
#                 table_html += f'<td class="p-2 {class_name}"{data_date_attr}>{cell_value}</td>'

#         table_html += '</tr>'
#     table_html += '</tbody></table></div>'  # Close table

#     return carousel_html + table_html


# def generate_f1_data_table(table_data, sector_color, table_name):
#     # Define the predefined columns that always come first
#     predefined_columns = ["Symbol", "CompanyName", "Sector", "Industry", "MarketCap"]

#     # Create a list to collect all columns in order
#     all_columns = predefined_columns[:]

#     # Collect all columns from the data
#     columns_from_data = set()
#     for symbol_data in table_data.values():
#         for column in symbol_data.keys():
#             if column not in predefined_columns and column not in columns_from_data:
#                 columns_from_data.add(column)
#                 all_columns.append(column)

#     # Parse all years and quarters dynamically from column names
#     quarter_counts = {}
#     for column in all_columns:
#         match = re.search(r'(\d{4})\s+Q(\d+)', column)  # Match patterns like "2020 Q1"
#         if match:
#             year, quarter = match.groups()
#             # Initialize the dictionary with counts
#             if year not in quarter_counts:
#                 quarter_counts[year] = {}
#             if quarter not in quarter_counts[year]:
#                 quarter_counts[year][quarter] = 0
#             # Count how many times this quarter appears
#             quarter_counts[year][quarter] += 1

#     # Extract years and quarters for table rendering
#     years = sorted(quarter_counts.keys())
#     quarters_per_year = {year: quarter_counts[year] for year in years}

#     # Start creating the HTML for the carousel of date buttons
#     carousel_html = f'<div class="carousel-container"><button type="button" class="btn btn-secondary btn-icon tbl-back-to-start-btn" data-table="{table_name}"><i class="typcn typcn-home-outline"></i></button>'
#     carousel_html += f'<div id="{table_name}-dateCarousel" class="carousel slide" data-ride="carousel" style="overflow: hidden;">'
#     carousel_html += '<div class="carousel-inner">'

#     # Create a chunk of buttons for each carousel item
#     button_chunk_size = 5  # Define how many buttons will fit per slide
#     total_buttons = len(years)  # Total number of years
#     num_chunks = (total_buttons // button_chunk_size) + (1 if total_buttons % button_chunk_size != 0 else 0)

#     for chunk_index in range(num_chunks):
#         # Start a new carousel item
#         carousel_html += f'<div class="carousel-item {"active" if chunk_index == 0 else ""}">'

#         # Create buttons for this chunk
#         carousel_html += '<div class="btn-group" style="white-space: nowrap; display: flex; overflow-x: auto;">'
#         for i in range(chunk_index * button_chunk_size, min((chunk_index + 1) * button_chunk_size, total_buttons)):
#             year = years[i]  # Use extracted years here
#             active_class = "active" if i == 0 else ""  # Make the first button in the carousel chunk active

#             carousel_html += f'<button class="btn btn-inverse-info btn-fw btn-sm date-button {active_class}" id="{table_name}-{year}" data-date="{table_name}-{year}" style="display: inline-block; margin-right: 5px;">{year}</button>'
#         carousel_html += '</div></div>'  # Close the btn-group and carousel-item

#     carousel_html += '</div>'  # Close carousel-inner

#     # Add the carousel controls (prev/next)
#     carousel_html += f'''
#     <a class="carousel-control-prev" href="#{table_name}-dateCarousel" role="button" data-slide="prev">
#         <span class="carousel-control-prev-icon" aria-hidden="true"></span>
#         <span class="sr-only">Previous</span>
#     </a>
#     <a class="carousel-control-next" href="#{table_name}-dateCarousel" role="button" data-slide="next">
#         <span class="carousel-control-next-icon" aria-hidden="true"></span>
#         <span class="sr-only">Next</span>
#     </a>
#     </div></div>'''   # Close carousel div

#     # Start creating the HTML table
#     table_html = f'<div class="table-responsive pb-3 custom-scrollbar-container table-responsive-{table_name}"><table class="table" id="{table_name}-data-table">'

#     # Add the three rows in table headers dynamically
#     table_html += "<thead>"

#     # Row 1: Header for years with correct colspan logic
#     table_html += '<tr class="date-header">'
#     for _ in range(len(predefined_columns)):
#         table_html += '<th class="p-2"></th>'
#     for year in years:
#         colspan_sum = sum(quarters_per_year[year].values())  # Calculate total number of quarters for the year
#         table_html += f'<th class="p-2" colspan="{colspan_sum}" data-date="{table_name}-{year}">{year}</th>'
#     table_html += "</tr>"

#     # Row 2: Header for quarters under each year with the correct colspan
#     table_html += '<tr class="quarter-header">'
#     # Add 5 empty <th> for the initial fixed columns
#     for _ in range(len(predefined_columns)):
#         table_html += '<th class="p-2"></th>'
#     # Now add the quarters with their respective colspan
#     for year in years:
#         for quarter, count in quarters_per_year[year].items():
#             table_html += f'''
#             <th class="p-2 q-{quarter} quarter-data-fetch-btn" 
#                 data-date="{table_name}-{year}" 
#                 data-date-q="{table_name}-{year}-{quarter}" 
#                 colspan="{count}">
#                 <button 
#                     hx-get="/rebalancing/fetch-quarterly-data/?date={table_name}-{year}-q{quarter}"
#                     hx-target="#f1-quarter-data-modal .card-body" 
#                     hx-trigger="click" 
#                     data-bs-toggle="modal" 
#                     data-bs-target="#f1-quarter-data-modal" 
#                     type="button" 
#                     class="btn btn-secondary btn-sm">
#                     Q{quarter}
#                 </button>
#             </th>
#             '''
#     table_html += "</tr>"



#     # Row 3: Data column headers
#     table_html += '<tr>'
#     for column in predefined_columns:
#         table_html += f'<th class="p-2">{column}</th>'
#     # Dynamically add the data headers
#     for column in all_columns:
#         if column not in predefined_columns:
#             table_html += f'<th class="p-2" data-date="{table_name}-{year}">{format_table_header(column)}</th>'
#     table_html += "</tr>"
#     table_html += "</thead>"

#     # Body of the table
#     table_html += "<tbody>"
#     for symbol, data in table_data.items():
#         row_color = sector_color.get(data.get("Sector", ""), "#FFFFFF")  # Default to white if no sector
#         company_name = data.get("CompanyName", "-")
#         table_html += f'<tr style="background-color: {row_color}">'
#         # Render the predefined fixed columns first
#         table_html += f'<td class="p-2">{symbol}</td>'
#         table_html += f'<td class="p-2">{company_name}</td>'
#         table_html += f'<td class="p-2">{data.get("Sector", "-")}</td>'
#         table_html += f'<td class="p-2">{data.get("Industry", "-")}</td>'
#         # table_html += f'<td class="p-2">{data.get("MarketCap", "-")}</td>'
#         table_html += format_table_values(data.get("MarketCap", "-"))

#         # Dynamically add data values beyond the predefined ones
#         for column in all_columns:
#             if column not in predefined_columns:
#                 cell_value = data.get(column, "-")
#                 class_name = ""
                
#                 # Check if column represents a date (like 2024, 2023 Q1, etc.)
#                 if re.search(r'\d{4}', column):  # Matches patterns like '2023', '2024', or similar years
#                     # Extract only the date/quarter part
#                     date_match = re.search(r'(\d{4})(?:\s+Q(\d+))?', column)
#                     if date_match:
#                         year_part = date_match.group(1)  # Extract year
#                         quarter_part = date_match.group(2)  # Extract quarter (if available)
                        
#                         # Dynamically generate the data-date attribute
#                         data_date_attr = f'data-date="{table_name}-{year_part}"'
                        
#                     else:
#                         data_date_attr = ""
#                 else:
#                     data_date_attr = ""
                
#                 # Handle number formatting for integers and floats
#                 if isinstance(cell_value, (float, int)):
#                     formatted_value = f"{cell_value:,.2f}" if isinstance(cell_value, float) else f"{cell_value:,}"
#                     table_html += f'<td class="p-2 {class_name}" {data_date_attr}>{formatted_value}</td>'
#                 else:
#                     table_html += f'<td class="p-2 {class_name}" {data_date_attr}>{cell_value}</td>'

#         table_html += '</tr>'
#     table_html += '</tbody></table></div>'

#     return carousel_html + table_html


def generate_f1_data_table(table_data, sector_color, table_name, saved_or_session, run_id):
    # Define the predefined columns that always come first
    predefined_columns = ["Symbol", "CompanyName", "Sector", "Industry", "MarketCap"]

    initial_col_num = 4
    current_col_num = 4
    # Create a list to collect all columns in order
    all_columns = predefined_columns[:]

    # Collect all columns from the data
    columns_from_data = set()
    for symbol_data in table_data.values():
        for column in symbol_data.keys():
            if column not in predefined_columns and column not in columns_from_data:
                columns_from_data.add(column)
                all_columns.append(column)

    # print(all_columns)

    # Parse all years and quarters dynamically from column names
    quarter_counts = {}
    additional_columns_count = 0  # Count additional dynamic columns

    for column in all_columns:
        # print(f"Checking column: {column}")  # Debugging
        # Match patterns like "2020 Q1"
        match_quarter = re.search(r'(\d{4})\s+Q(\d+)', column)
        # Match patterns like "Shares Jan 02 2020"
        match_date = re.search(r'\b[A-Za-z]+\s+(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+\d{1,2}\s+\d{4}\b', column)

        if match_quarter:
            # print(f"Quarter match: {match_quarter.group()}")  # Debugging
            year, quarter = match_quarter.groups()
            # Initialize the dictionary with counts
            if year not in quarter_counts:
                quarter_counts[year] = {}
            if quarter not in quarter_counts[year]:
                quarter_counts[year][quarter] = 0
            # Count how many times this quarter appears
            quarter_counts[year][quarter] += 1
        elif match_date:  # For dynamic date-like column matches
            # print(f"Date match: {match_date.group()}")  # Debugging
            additional_columns_count += 1

    # Extract years and quarters for table rendering
    years = sorted(quarter_counts.keys())
    quarters_per_year = {year: quarter_counts[year] for year in years}

    # Start creating the HTML for the carousel of date buttons
    carousel_html = f'<div class="carousel-container"><button type="button" class="btn btn-secondary btn-icon tbl-back-to-start-btn" data-table="{table_name}"><i class="typcn typcn-home-outline"></i></button>'
    carousel_html += f'<div id="{table_name}-dateCarousel" class="carousel slide" data-ride="carousel" style="overflow: hidden;">'
    carousel_html += '<div class="carousel-inner">'

    # Create a chunk of buttons for each carousel item
    button_chunk_size = 5  # Define how many buttons will fit per slide
    total_buttons = len(years)  # Total number of years
    num_chunks = (total_buttons // button_chunk_size) + (1 if total_buttons % button_chunk_size != 0 else 0)

    for chunk_index in range(num_chunks):
        # Start a new carousel item
        carousel_html += f'<div class="carousel-item {"active" if chunk_index == 0 else ""}">'

        # Create buttons for this chunk
        carousel_html += '<div class="btn-group" style="white-space: nowrap; display: flex; overflow-x: auto;">'
        for i in range(chunk_index * button_chunk_size, min((chunk_index + 1) * button_chunk_size, total_buttons)):
            year = years[i]  # Use extracted years here
            active_class = "active" if i == 0 else ""  # Make the first button in the carousel chunk active

            carousel_html += f'<button class="btn btn-inverse-info btn-fw btn-sm date-button {active_class}" id="{table_name}-{year}" data-date="{table_name}-{year}" style="display: inline-block; margin-right: 5px;">{year}</button>'
        carousel_html += '</div></div>'  # Close the btn-group and carousel-item

    carousel_html += '</div>'  # Close carousel-inner

    # Add the carousel controls (prev/next)
    carousel_html += f'''
    <a class="carousel-control-prev" href="#{table_name}-dateCarousel" role="button" data-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="sr-only">Previous</span>
    </a>
    <a class="carousel-control-next" href="#{table_name}-dateCarousel" role="button" data-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="sr-only">Next</span>
    </a>
    </div></div>'''   # Close carousel div

    # Start creating the HTML table
    table_html = f'<div class="table-responsive pb-3 custom-scrollbar-container table-responsive-{table_name}"><table class="table" id="{table_name}-data-table">'

    # Add the three rows in table headers dynamically
    table_html += "<thead>"

    # Row 1: Header for years with correct colspan logic
    table_html += '<tr class="date-header">'
    for _ in range(len(predefined_columns)):
        table_html += '<th class="p-2 fixed-columns"></th>'
    for _ in range(initial_col_num + current_col_num):
        table_html += '<th class="p-2"></th>'
    for year in years:
        colspan_sum = sum(quarters_per_year[year].values())  # Calculate total number of quarters for the year
        table_html += f'<th class="p-2" colspan="{colspan_sum}" data-date="{table_name}-{year}">{year}</th>'
    table_html += "</tr>"

    # Row 2: Header for quarters under each year with the correct colspan
    table_html += '<tr class="quarter-header">'
    # Add 5 empty <th> for the initial fixed columns
    for _ in range(len(predefined_columns)):
        table_html += '<th class="p-2 fixed-columns"></th>'
    
    table_html += f'<th class="p-2" colspan="{initial_col_num}">Initials</th>'
    table_html += f'<th class="p-2" colspan="{current_col_num}">Current</th>'
    # Now add the quarters with their respective colspan
    for year in years:
        for quarter, count in quarters_per_year[year].items():
            if saved_or_session == 'session':
                table_html += f'''
                <th class="p-2 q-{quarter} quarter-data-fetch-btn" 
                    data-date="{table_name}-{year}" 
                    data-date-q="{table_name}-{year}-{quarter}" 
                    colspan="{count}">
                    <button 
                        hx-get="/rebalancing/fetch-quarterly-data/?date={table_name}-{year}-q{quarter}"
                        hx-target="#f1-quarter-data-modal .card-body" 
                        hx-trigger="click" 
                        data-bs-toggle="modal" 
                        data-bs-target="#f1-quarter-data-modal" 
                        type="button" 
                        class="btn btn-secondary btn-sm">
                        Q{quarter}
                    </button>
                </th>
                '''
            else:
                table_html += f'''
                <th class="p-2 q-{quarter} quarter-data-fetch-btn" 
                    data-date="{table_name}-{year}" 
                    data-date-q="{table_name}-{year}-{quarter}" 
                    colspan="{count}">
                    <button 
                        hx-get="/rebalancing/fetch-saved-quarterly-data/?date={table_name}-{year}-q{quarter}&run_id={run_id}"
                        hx-target="#f1-quarter-data-modal .card-body" 
                        hx-trigger="click" 
                        data-bs-toggle="modal" 
                        data-bs-target="#f1-quarter-data-modal" 
                        type="button" 
                        class="btn btn-secondary btn-sm">
                        Q{quarter}
                    </button>
                </th>
                '''

    table_html += "</tr>"



    # Row 3: Data column headers
    table_html += '<tr class="data-key-row">'
    for column in predefined_columns:
        table_html += f'<th class="p-2 fixed-columns">{column}</th>'
    # Dynamically add the data headers
    for column in all_columns:
        if column not in predefined_columns:
            table_html += f'<th class="p-2" data-date="{table_name}-{year}">{format_table_header(column)}</th>'
    table_html += "</tr>"
    table_html += "</thead>"

    # Body of the table
    table_html += "<tbody>"
    for symbol, data in table_data.items():
        row_color = sector_color.get(data.get("Sector", ""), "#FFFFFF")  # Default to white if no sector
        company_name = data.get("CompanyName", "-")
        table_html += f'<tr style="background-color: {row_color}">'
        # Render the predefined fixed columns first
        table_html += f'<td class="p-2 fixed-columns"  style="background-color: {row_color}">{symbol}</td>'
        table_html += f'<td class="p-2 fixed-columns"  style="background-color: {row_color}">{company_name}</td>'
        table_html += f'<td class="p-2 fixed-columns"  style="background-color: {row_color}">{data.get("Sector", "-")}</td>'
        table_html += f'<td class="p-2 fixed-columns"  style="background-color: {row_color}">{data.get("Industry", "-")}</td>'
        # table_html += f'<td class="p-2">{data.get("MarketCap", "-")}</td>'
        table_html += format_table_values_2(data.get("MarketCap", "-"), row_color)

        # Dynamically add data values beyond the predefined ones
        for column in all_columns:
            if column not in predefined_columns:
                cell_value = data.get(column, "-")
                class_name = ""
                
                # Check if column represents a date (like 2024, 2023 Q1, etc.)
                if re.search(r'\d{4}', column):  # Matches patterns like '2023', '2024', or similar years
                    # Extract only the date/quarter part
                    date_match = re.search(r'(\d{4})(?:\s+Q(\d+))?', column)
                    if date_match:
                        year_part = date_match.group(1)  # Extract year
                        quarter_part = date_match.group(2)  # Extract quarter (if available)
                        
                        # Dynamically generate the data-date attribute
                        data_date_attr = f'data-date="{table_name}-{year_part}"'
                        
                    else:
                        data_date_attr = ""
                else:
                    data_date_attr = ""
                
                # Handle number formatting for integers and floats
                if isinstance(cell_value, (float, int)):
                    formatted_value = f"{cell_value:,.2f}" if isinstance(cell_value, float) else f"{cell_value:,}"
                    table_html += f'<td class="p-2 {class_name}" {data_date_attr}>{formatted_value}</td>'
                else:
                    table_html += f'<td class="p-2 {class_name}" {data_date_attr}>{cell_value}</td>'

        table_html += '</tr>'
    table_html += '</tbody></table></div>'

    return carousel_html + table_html


@login_required(login_url='/login/')
def input_form_view(request):

    # if request.user.userprofile.role == 'admin':
    #     runs = Run.objects.all()
    # else:
    #     runs = Run.objects.filter(user=request.user.id)

    context = {}

    return render(request, 'f1/index.html', context)


@login_required(login_url='/login/')
def rebalancing_dashboard(request):
    is_f1_run_exist = 1 if 'f1_runs' in request.session and request.session['f1_runs'] else 0

    context = {
        'page_title': 'Welcome to the template home page',
        'is_f1_run_exist': is_f1_run_exist
    }
    

    return render(request, 'rebalancing/dashboard.html', context)


@login_required(login_url='/login/')
def run_rebalancing_f1_view(request):
    # Process form
    form_data = process_f1_input_form(request)
    output_data = table_output_new

    f1_runs = request.session.get('f1_runs', [])
    new_f1_run = {
        'run_id': len(f1_runs) + 1,  
        'title': 'F1 Run ' + str(len(f1_runs) + 1),
        'form_data': form_data,
        'output': output_data
    }
    f1_runs.append(new_f1_run)
    request.session['f1_runs'] = f1_runs

    historical_chart_data = portfolio_value_historical
    recommend_chart_data = portfolio_value_recommended
    current_chart_data = portfolio_value_current
    index_chart_data = index_value

    context = {
        'historical_data': historical_chart_data,
        'recommend_data': recommend_chart_data,
        'current_data': current_chart_data,
        'index_chart_data': index_chart_data,
    }

    return render(request, 'f1/summary_result.html', context)


@login_required(login_url='/login/')
def current_f1_result_view(request):
    f1_runs = request.session.get('f1_runs', [])

    # Get the last run if available, or None if f1_h_runs is empty
    last_run = f1_runs[-1] if f1_runs else None


    chart_data = last_run.get('output').get('quarterly')
    table_output_3 = last_run.get('output').get('quarterly')
    sector_color = sector_hex_colors

    historical_chart_data = portfolio_value_historical
    recommend_chart_data = portfolio_value_recommended
    current_chart_data = portfolio_value_current
    index_chart_data = index_value

    historical_table_html = generate_f1_data_table(table_output_3, sector_color, 'historical', 'session', '')
    recommend_table_html = generate_f1_data_table(table_output_3, sector_color, 'recommend', 'session', '')
    current_table_html = generate_f1_data_table(table_output_3, sector_color, 'current', 'session', '')

    # Pass the generated HTML to the template
    context = {
        'historical_table_html': historical_table_html,
        'recommend_table_html': recommend_table_html,
        'current_table_html': current_table_html,
        'chart_data': chart_data,
        'historical_chart_data': historical_chart_data,
        'recommend_chart_data': recommend_chart_data,
        'current_chart_data': current_chart_data,
        'index_chart_data': index_chart_data,
    }

    return render(request, 'f1/f1_output.html', context)


@login_required(login_url='/login/')
def saved_f1_run_output_view(request, id):
    saved_run = Run.objects.get(id=id)
    saved_output_data = saved_run.output_data

    chart_data = saved_output_data.get('quarterly')
    table_output_3 = saved_output_data.get('quarterly')
    sector_color = sector_hex_colors


    historical_table_html = generate_f1_data_table(table_output_3, sector_color, 'historical', 'saved', id)
    recommend_table_html = generate_f1_data_table(table_output_3, sector_color, 'recommend', 'saved', id)
    current_table_html = generate_f1_data_table(table_output_3, sector_color, 'current', 'saved', id)

    # Pass the generated HTML to the template
    context = {
        'historical_table_html': historical_table_html,
        'recommend_table_html': recommend_table_html,
        'current_table_html': current_table_html,
        'chart_data': chart_data
    }

    return render(request, 'f1/f1_output.html', context)


def fetch_quarterly_data(table_output):
    quarterly_data = []
    for ticker, timeframes in table_output.items():
        if "quarterly" in timeframes:
            quarterly = timeframes["quarterly"]
            # Ensure 'quarterly' is a dictionary
            if isinstance(quarterly, dict):
                for key, value in quarterly.items():
                    if "202" in key:  # Filter keys belonging to specific quarters
                        quarter = key.split(" ")[-1]  # Extract the quarter/year
                        metric_name = " ".join(key.split(" ")[:-1])  # Metric name
                        # Check if the quarter entry exists in the list
                        existing_entry = next(
                            (entry for entry in quarterly_data if entry["Quarter"] == quarter),
                            None,
                        )
                        if not existing_entry:
                            existing_entry = {"Quarter": quarter}
                            quarterly_data.append(existing_entry)
                        # Add data to the corresponding entry
                        existing_entry[metric_name] = value
            elif isinstance(quarterly, list):
                # Handle cases where 'quarterly' is a list
                for entry in quarterly:
                    # Assuming each entry in the list has a structure like {'Quarter': ..., 'Metric': ...}
                    if isinstance(entry, dict) and "Quarter" in entry:
                        quarterly_data.append(entry)
    return quarterly_data


@login_required(login_url='/login/')
def output_view(request):
    form_data = process_f1_input_form(request)
    output_data = table_output_new

    f1_runs = request.session.get('f1_runs', [])
    new_f1_run = {
        'run_id': len(f1_runs) + 1,  
        'title': 'F1 Run ' + str(len(f1_runs) + 1),
        'form_data': form_data,
        'output': output_data
    }
    f1_runs.append(new_f1_run)
    request.session['f1_runs'] = f1_runs

    chart_data = output_data.get('quarterly')
    table_output_3 = output_data.get('quarterly')
    sector_color = sector_hex_colors

    historical_chart_data = portfolio_value_historical
    recommend_chart_data = portfolio_value_recommended
    current_chart_data = portfolio_value_current
    index_chart_data = index_value

    historical_table_html = generate_f1_data_table(table_output_3, sector_color, 'historical', 'session', '')
    recommend_table_html = generate_f1_data_table(table_output_3, sector_color, 'recommend', 'session', '')
    current_table_html = generate_f1_data_table(table_output_3, sector_color, 'current', 'session', '')

    # Pass the generated HTML to the template
    context = {
        'historical_table_html': historical_table_html,
        'recommend_table_html': recommend_table_html,
        'current_table_html': current_table_html,
        'chart_data': chart_data,
        'historical_chart_data': historical_chart_data,
        'recommend_chart_data': recommend_chart_data,
        'current_chart_data': current_chart_data,
        'index_chart_data': index_chart_data,
    }

    return render(request, 'f1/f1_output.html', context)


def fetch_f1_ticker_view(request):

    ticker_data = [
        {
            "ticker": "AAPL",
            "name": "Apple Inc.",
            "sector": "Technology",
            "beta": "1.25",
            "current_price": "$226.05",
            "pe_ratio": "34.46",
            "eps_data": [
                {"quarter": "Q1 24", "status": "Beat", "eps_change": "+0.03"},
                {"quarter": "Q2 24", "status": "Beat", "eps_change": "+0.05"},
                {"quarter": "Q3 24", "status": "Beat", "eps_change": "+0.04"},
                {"quarter": "Q4 24", "status": "-", "eps_change": "+0.03"},
            ],
            "analyst_data": [
                {"month": "Aug", "analyst_num": 42, "strong_buy": 10, "buy": 24, "hold": 7, "underperform": 1, "sell": 0},
                {"month": "Sep", "analyst_num": 50, "strong_buy": 12, "buy": 28, "hold": 8, "underperform": 1, "sell": 1},
                {"month": "Oct", "analyst_num": 38, "strong_buy": 8, "buy": 20, "hold": 7, "underperform": 2, "sell": 1},
                {"month": "Nov", "analyst_num": 45, "strong_buy": 15, "buy": 20, "hold": 5, "underperform": 3, "sell": 2},
            ],
            "price_targets":{
                "low": "183.86",
                "current": "183.86",
                "average": "183.86",
                "high": "300.00"
            },
        },
        {
            "ticker": "GOOGL",
            "name": "Alphabet Inc.",
            "sector": "Technology",
            "beta": "1.10",
            "current_price": "$2,745.00",
            "pe_ratio": "28.50",
            "eps_data": [
                {"quarter": "Q1 24", "status": "Beat", "eps_change": "+0.10"},
                {"quarter": "Q2 24", "status": "Beat", "eps_change": "+0.12"},
                {"quarter": "Q3 24", "status": "Miss", "eps_change": "-0.02"},
                {"quarter": "Q4 24", "status": "-", "eps_change": "+0.08"},
            ],
            "analyst_data": [
                {"month": "Aug", "analyst_num": 40, "strong_buy": 15, "buy": 20, "hold": 4, "underperform": 1, "sell": 0},
                {"month": "Sep", "analyst_num": 48, "strong_buy": 18, "buy": 22, "hold": 5, "underperform": 2, "sell": 1},
                {"month": "Oct", "analyst_num": 35, "strong_buy": 10, "buy": 18, "hold": 6, "underperform": 0, "sell": 1},
                {"month": "Nov", "analyst_num": 50, "strong_buy": 20, "buy": 25, "hold": 4, "underperform": 1, "sell": 0},
            ],
            "price_targets": [
                {"low": "183.86"},
                {"current": "183.86"},
                {"average": "183.86"},
                {"high": "300.00"}
            ],
        },
        {
            "ticker": "AAPL",
            "name": "Apple Inc.",
            "sector": "Technology",
            "beta": "1.25",
            "current_price": "$226.05",
            "pe_ratio": "34.46",
            "eps_data": [
                {"quarter": "Q1 24", "status": "Beat", "eps_change": "+0.03"},
                {"quarter": "Q2 24", "status": "Beat", "eps_change": "+0.05"},
                {"quarter": "Q3 24", "status": "Beat", "eps_change": "+0.04"},
                {"quarter": "Q4 24", "status": "-", "eps_change": "+0.03"},
            ],
            "analyst_data": [
                {"month": "Aug", "analyst_num": 42, "strong_buy": 10, "buy": 24, "hold": 7, "underperform": 1, "sell": 0},
                {"month": "Sep", "analyst_num": 50, "strong_buy": 12, "buy": 28, "hold": 8, "underperform": 1, "sell": 1},
                {"month": "Oct", "analyst_num": 38, "strong_buy": 8, "buy": 20, "hold": 7, "underperform": 2, "sell": 1},
                {"month": "Nov", "analyst_num": 45, "strong_buy": 15, "buy": 20, "hold": 5, "underperform": 3, "sell": 2},
            ],
            "price_targets":{
                "low": "183.86",
                "current": "183.86",
                "average": "183.86",
                "high": "300.00"
            },
        },
        {
            "ticker": "GOOGL",
            "name": "Alphabet Inc.",
            "sector": "Technology",
            "beta": "1.10",
            "current_price": "$2,745.00",
            "pe_ratio": "28.50",
            "eps_data": [
                {"quarter": "Q1 24", "status": "Beat", "eps_change": "+0.10"},
                {"quarter": "Q2 24", "status": "Beat", "eps_change": "+0.12"},
                {"quarter": "Q3 24", "status": "Miss", "eps_change": "-0.02"},
                {"quarter": "Q4 24", "status": "-", "eps_change": "+0.08"},
            ],
            "analyst_data": [
                {"month": "Aug", "analyst_num": 40, "strong_buy": 15, "buy": 20, "hold": 4, "underperform": 1, "sell": 0},
                {"month": "Sep", "analyst_num": 48, "strong_buy": 18, "buy": 22, "hold": 5, "underperform": 2, "sell": 1},
                {"month": "Oct", "analyst_num": 35, "strong_buy": 10, "buy": 18, "hold": 6, "underperform": 0, "sell": 1},
                {"month": "Nov", "analyst_num": 50, "strong_buy": 20, "buy": 25, "hold": 4, "underperform": 1, "sell": 0},
            ],
            "price_targets": [
                {"low": "183.86"},
                {"current": "183.86"},
                {"average": "183.86"},
                {"high": "300.00"}
            ],
        },
        {
            "ticker": "AAPL",
            "name": "Apple Inc.",
            "sector": "Technology",
            "beta": "1.25",
            "current_price": "$226.05",
            "pe_ratio": "34.46",
            "eps_data": [
                {"quarter": "Q1 24", "status": "Beat", "eps_change": "+0.03"},
                {"quarter": "Q2 24", "status": "Beat", "eps_change": "+0.05"},
                {"quarter": "Q3 24", "status": "Beat", "eps_change": "+0.04"},
                {"quarter": "Q4 24", "status": "-", "eps_change": "+0.03"},
            ],
            "analyst_data": [
                {"month": "Aug", "analyst_num": 42, "strong_buy": 10, "buy": 24, "hold": 7, "underperform": 1, "sell": 0},
                {"month": "Sep", "analyst_num": 50, "strong_buy": 12, "buy": 28, "hold": 8, "underperform": 1, "sell": 1},
                {"month": "Oct", "analyst_num": 38, "strong_buy": 8, "buy": 20, "hold": 7, "underperform": 2, "sell": 1},
                {"month": "Nov", "analyst_num": 45, "strong_buy": 15, "buy": 20, "hold": 5, "underperform": 3, "sell": 2},
            ],
            "price_targets":{
                "low": "183.86",
                "current": "183.86",
                "average": "183.86",
                "high": "300.00"
            },
        },
        {
            "ticker": "GOOGL",
            "name": "Alphabet Inc.",
            "sector": "Technology",
            "beta": "1.10",
            "current_price": "$2,745.00",
            "pe_ratio": "28.50",
            "eps_data": [
                {"quarter": "Q1 24", "status": "Beat", "eps_change": "+0.10"},
                {"quarter": "Q2 24", "status": "Beat", "eps_change": "+0.12"},
                {"quarter": "Q3 24", "status": "Miss", "eps_change": "-0.02"},
                {"quarter": "Q4 24", "status": "-", "eps_change": "+0.08"},
            ],
            "analyst_data": [
                {"month": "Aug", "analyst_num": 40, "strong_buy": 15, "buy": 20, "hold": 4, "underperform": 1, "sell": 0},
                {"month": "Sep", "analyst_num": 48, "strong_buy": 18, "buy": 22, "hold": 5, "underperform": 2, "sell": 1},
                {"month": "Oct", "analyst_num": 35, "strong_buy": 10, "buy": 18, "hold": 6, "underperform": 0, "sell": 1},
                {"month": "Nov", "analyst_num": 50, "strong_buy": 20, "buy": 25, "hold": 4, "underperform": 1, "sell": 0},
            ],
            "price_targets": [
                {"low": "183.86"},
                {"current": "183.86"},
                {"average": "183.86"},
                {"high": "300.00"}
            ],
        },
        
    ]

    error_context = {
        'ticker_data': ticker_data
    }
    
    error_html = render_to_string('template-parts/yfinance-ticker-data.html', error_context, request=request)
    return HttpResponse(error_html)


def fetch_f1_error_view(request):

    f1_runs = request.session.get('f1_runs', [])
    # Get the last run if available, or None if mvoh_runs is empty
    last_run = f1_runs[-1] if f1_runs else None

    print(last_run)
    
    if last_run:
        # output = last_run.get('output')
        # error = output.get('stacktraces')
        error = 'There is an error from output'
    else:
        error = 'There is no error'
 
    error_context = {
        'error': error
    }
    error_html = render_to_string('f1/error.html', error_context, request=request)
    return HttpResponse(error_html)


def remove_month_names(column_name):
    # Regex to match month names like Dec, Nov, Oct, etc.
    return re.sub(r'\b(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\b', '', column_name).strip()


def generate_quarter_html_table(data, year, quarter_months):
    # Define the month sequence for correct sorting
    month_order = [
        "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
    ]
    
    # Sort the given quarters in descending chronological order
    sorted_months = sorted(quarter_months, key=lambda month: month_order.index(month), reverse=True)


    # Extract all possible column headers dynamically
    columns = set()
    for company_data in data.values():
        for key in company_data.keys():
            # Include only the relevant month columns from the latest months
            if any(f"{year} {month}" in key for month in sorted_months):
                columns.add(key)

    # Group columns by their respective months to ensure the table's correct dynamic rendering
    grouped_columns = {month: [] for month in sorted_months}
    for column in columns:
        for month in sorted_months:
            if f"{year} {month}" in column:
                grouped_columns[month].append(column)

    # Ensure no misalignment by sorting individual columns for rendering
    for month in grouped_columns:
        grouped_columns[month].sort()

    # Start the HTML table structure
    html = """
    <div class="table-responsive custom-scrollbar-container">
        <table class="table">
            <thead>
                <tr class="modal-month-row">
                    <th></th> <!-- Placeholder for alignment -->
                    <th colspan="4"></th>"""

    # Dynamically generate month headers with colspan
    for month, month_columns in grouped_columns.items():
        html += f'<th class="p-2" colspan="{len(month_columns)}">{month}</th>'

    html += """
                </tr>
                <tr>
                    <th class="p-2">Ticker</th>
                    <th class="p-2">Company Name</th>
                    <th class="p-2">Sector</th>
                    <th class="p-2">Industry</th>
                    <th class="p-2">Market Cap</th>"""

    # Add sub-column headers for each month dynamically
    for month_columns in grouped_columns.values():
        for column in month_columns:
            cleaned_column = remove_month_names(format_table_header(column))  # Clean the month names
            html += f"<th class='p-2'>{cleaned_column}</th>"

    html += """
                </tr>
            </thead>
            <tbody>"""

    # Dynamically generate rows for each company
    for ticker, company_data in data.items():
        sector = company_data.get("Sector", "")
        background_color = sector_hex_colors.get(sector, "#ffffff")  # Default to white if no color found

        html += f"""
            <tr style="background-color: {background_color};">
                <td class="p-2">{ticker}</td>
                <td class="p-2">{company_data.get("CompanyName", "")}</td>
                <td class="p-2">{sector}</td>
                <td class="p-2">{company_data.get("Industry", "")}</td>
                <td class="p-2">{company_data.get("MarketCap", 0):,}</td>"""

        # Dynamically add each month's data in their respective columns
        for month_columns in grouped_columns.values():
            for column in month_columns:
                value = company_data.get(column, "")
                html += f"{format_table_values(value)}</td>"

        html += """
            </tr>"""

    html += """
            </tbody>
        </table>
    </div>"""

    return html


def fetch_f1_quarterly_data_view(request):
    quarter_mapping = {
        "q1": ["Jan", "Feb", "Mar"],
        "q2": ["Apr", "May", "Jun"],
        "q3": ["Jul", "Aug", "Sep"],
        "q4": ["Oct", "Nov", "Dec"]
    }
    # Extract the date query string from GET request
    quarter = request.GET.get('date')  # Example: "historical-2020-q1"

    
    if not quarter:
        return HttpResponse("Invalid request. No date provided.")

    # Parse the year and quarter from the string
    try:
        # Split the string to extract year and quarter
        _, year, q_str = quarter.split('-')  # Split string like "historical-2020-q1"
        quarter_months = quarter_mapping.get(q_str)
        
        if not quarter_months:
            return HttpResponse("Invalid quarter specified in request.")

        # Get the table data dynamically
        f1_runs = request.session.get('f1_runs', [])
        # Get the last run if available, or None if f1_h_runs is empty
        last_run = f1_runs[-1] if f1_runs else None
        table_output_3 = last_run.get('output').get('monthly')

        # Call the HTML table generation with the extracted year and months
        html_table = generate_quarter_html_table(table_output_3, year, quarter_months)

        title = quarter.replace('-', ' ').title()

        # Prepare context for rendering
        context = {
            'title': title,
            'html_table': html_table
        }

        # Render the response
        html = render_to_string('f1/quarterly_data.html', context, request=request)
        return HttpResponse(html)

    except ValueError:
        return HttpResponse("Error parsing the date parameter. Ensure the format is correct.")


def fetch_saved_f1_quarterly_data_view(request):
    quarter_mapping = {
        "q1": ["Jan", "Feb", "Mar"],
        "q2": ["Apr", "May", "Jun"],
        "q3": ["Jul", "Aug", "Sep"],
        "q4": ["Oct", "Nov", "Dec"]
    }
    # Extract the date query string from GET request
    quarter = request.GET.get('date')  # Example: "historical-2020-q1"
    run_id = request.GET.get('run_id')

    
    if not quarter:
        return HttpResponse("Invalid request. No date provided.")

    # Parse the year and quarter from the string
    try:
        # Split the string to extract year and quarter
        _, year, q_str = quarter.split('-')  # Split string like "historical-2020-q1"
        quarter_months = quarter_mapping.get(q_str)
        
        if not quarter_months:
            return HttpResponse("Invalid quarter specified in request.")


        saved_run = Run.objects.get(id=run_id)
        saved_output_data = saved_run.output_data
        table_output_3 = saved_output_data.get('monthly')

        # Call the HTML table generation with the extracted year and months
        html_table = generate_quarter_html_table(table_output_3, year, quarter_months)

        title = quarter.replace('-', ' ').title()

        # Prepare context for rendering
        context = {
            'title': title,
            'html_table': html_table
        }

        # Render the response
        html = render_to_string('f1/quarterly_data.html', context, request=request)
        return HttpResponse(html)

    except ValueError:
        return HttpResponse("Error parsing the date parameter. Ensure the format is correct.")