from json_parser import parse_json
from logic_processor import process_logic
# If you have a GUI, you would also import it here
# from gui import start_gui

def main():
    # Example of parsing JSON data
    json_file_path = 'data/example_data.json'
    data = parse_json(json_file_path)
    print("Parsed data:", data)
    
    # Processing the parsed data with your logic
    processed_data = process_logic(data)
    print("Processed data:", processed_data)
    
    # If you have a GUI, you might start it here
    # start_gui(processed_data)

if __name__ == "__main__":
    main()
