# VR Furniture Shopping Experience Server / oculus-furniture-server

This Flask server is designed to allow the POC apps to download assets during runtime, get templates, etc. 
This currently works with all POCs completed.

This server can simply be run in a Python virtual environment, and will work automatically with the POC apps. 
NOTE: You need to create a folder named "glb" in the same directory as "app.py", and include subfolders (with the name of the model) with the model's glb files inside. For example, if you have a folder "Leather_Sofa" with files "black_sofa.glb" and "brown_chair.glb".

### Features:
- Download assets - use the URL extension "/download/<foldername>/<filename>" to download the glb file from the folder
- Load template - use the URL extension "/get/poc2/templates/<json_name>" to load the template

### Creating your own templates:
These will be JSON files stored in the "poc2/templates" folder. Each object in a JSON template file represents a model that will appear in a given location in the POC app on the Oculus, and includes the following:
- "description" - the type of furniture that will be placed at the location
- "world_pos" - the location the model will be placed in Unity 3D coords
- "euler_angles" - the rotation of the model in the space
- "valid_models" - a list of objects for other models that you can swap between at the location of the object; each of these objects will have a "name" and a list of "files" (this can be left empty, as app.py fills in all the available files inside the folder of the model)
- "default_model" - the model that will show up when you first open the template in the POC app; it will have a "name" and a "file" (note that this should be set)

You can take a look at bedroom.json in "poc2/templates" as an example. Note that for the name and files, they must match with the folder and file names inside the "glb" folder.

### Current Status
This project has been on hiatus for a while, but I'll be picking it up again soon now that I'm on break!
