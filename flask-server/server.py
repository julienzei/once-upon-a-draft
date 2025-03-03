from flask import Flask, request, send_file
from flask_cors import CORS
import tempfile
import os

app = Flask(__name__)
CORS(app)

@app.route('/process-pdf', methods=['POST'])
def process_pdf():
    if 'pdf' not in request.files:
        return 'No PDF file uploaded', 400

    pdf_file = request.files['pdf']
    
    
    with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as temp_input:
        pdf_file.save(temp_input.name)
        input_path = temp_input.name

    
    with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as temp_output:
        output_path = temp_output.name

    # CHANGE "input_path" to the processed pdf (i.e. the outputted notes). In other words, you can put the whole function here, or call it from another file.
    # u can also add it to output_file, (and change "input_file" in send_file to "output_file")
    
    return send_file(input_path, as_attachment=True, download_name='processed.pdf')

def process_pdf_file(input_path, output_path):
    # Replace this with your actual PDF processing logic
    # For now, we'll just copy the input file to the output file
    import shutil
    shutil.copy(input_path, output_path)

if __name__ == '__main__':
    app.run(debug=True)