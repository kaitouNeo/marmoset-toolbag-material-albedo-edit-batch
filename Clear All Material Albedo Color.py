# Quick turn the albedo of all materials into pure white in Marmoset Toolbag 4.
# Import the libraries of Marmoset Toolbag.
import mset

# Get all of materials.
sceneMaterials = mset.getAllMaterials()

# Iterate all of the materials.
for material in sceneMaterials:
    # Get a field name of the material, the field name is albedo.
    materialFieldNames = material.albedo.getFieldNames()
     # If the field name is type of "Albedo" rather than the type of "vertext color". 
    if "Albedo Map" in materialFieldNames:
        # Turn the value of albedo into pure white (RGB = 1,1,1).
        material.albedo.setField("Color", [1, 1, 1])
    else:
        continue
