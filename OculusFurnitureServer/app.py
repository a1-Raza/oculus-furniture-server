from flask import Flask, jsonify, request, send_from_directory
import os
import json

#from convertmodel import convert_usdz_to_usd, convert_usd_to_gltf, fix_material_bindings

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

@app.route('/get/convertusdz', methods=['GET'])
def get_convertusdz():
    usdz_url = request.args.get('url')
    if not usdz_url:
        return jsonify({"error": "No URL provided"}), 400

    #convert_usdz_to_usd("convert/input/dresser.usdz","convert/intermediate/dresser.usd")
    #fix_material_bindings("convert/intermediate/dresser.usd")
    #convert_usd_to_gltf("convert/intermediate/dresser.usd","convert/output/dresser.gltf")

    return "Url provided"

@app.route('/download/<foldername>/<filename>')
def download_file(foldername, filename):
    return send_from_directory("glb", str(foldername)+"/"+str(filename), as_attachment=True)

@app.route('/get/all_models_json')
def get_models_json():
    glb_dir = os.path.join(os.getcwd(), 'glb')
    
    folders_info = []
    
    # Walk through the 'glb' directory
    for foldername in os.listdir(glb_dir):
        folder_path = os.path.join(glb_dir, foldername)
        
        if os.path.isdir(folder_path):
            models = []
            
            for filename in os.listdir(folder_path):
                if filename.endswith('.glb'):
                    # Construct the model info
                    model_info = {
                        "id": filename.replace(".glb",""),
                        "download_url": request.host_url + 'download/' + foldername + '/' + filename
                    }
                    
                    models.append(model_info)
            
            folder_info = {
                "name": foldername,
                "models": models
            }
            
            folders_info.append(folder_info)
    
    return jsonify(folders_info)

@app.route('/get/poc2/templates/bedroom')
def get_poc2_template_bedroom():

    # Define the path to the JSON file
    json_file_path = os.path.join(os.getcwd(), 'poc2', 'templates', 'bedroom.json')
    
    # Read the JSON file
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
    
    # Return the data as a JSON response
    return jsonify(data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
