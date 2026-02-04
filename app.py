from flask import Flask, render_template
import os
import re

app = Flask(__name__)

def parse_bill_file():
    """Parse the bill_for_claude.txt file and extract structured data."""
    file_path = os.path.join(os.path.dirname(__file__), 'bill_for_claude.txt')
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract title, name, and class
    title_match = re.search(r'Title:\s*(.+)', content)
    name_match = re.search(r'Name:\s*(.+)', content)
    class_match = re.search(r'Class:\s*(.+)', content)
    
    bill_data = {
        'title': title_match.group(1).strip() if title_match else 'The Student-Centered Bill of Rights',
        'name': name_match.group(1).strip() if name_match else 'Student',
        'class': class_match.group(1).strip() if class_match else 'US History',
        'rights': [],
        'reflection': ''
    }
    
    # Extract each right (Right 1, Right 2, etc.)
    right_pattern = r'Right (\d+)\s*—\s*(.+?)\nExplanation:\s*(.+?)\nReal-life example:\s*(.+?)(?=\n\nRight \d+|Reflection|$)'
    rights = re.finditer(right_pattern, content, re.DOTALL)
    
    for match in rights:
        right_num = int(match.group(1))
        title = match.group(2).strip()
        explanation = match.group(3).strip()
        example = match.group(4).strip()
        
        bill_data['rights'].append({
            'number': right_num,
            'title': title,
            'explanation': explanation,
            'example': example
        })
    
    # Extract reflection
    reflection_match = re.search(r'Reflection.*?\n(.+?)(?=Submit as|$)', content, re.DOTALL)
    if reflection_match:
        bill_data['reflection'] = reflection_match.group(1).strip()
    
    return bill_data

@app.route('/')
def home():
    bill_data = parse_bill_file()
    return render_template('index.html', bill=bill_data)

if __name__ == '__main__':
    app.run(debug=True)
