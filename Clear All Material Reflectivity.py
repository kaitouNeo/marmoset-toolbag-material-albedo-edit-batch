# Quick turn the reflectivity of all materials into zero in Marmoset Toolbag 4.
# Import the libraries of Marmoset Toolbag.
import mset

# Get all of materials.
sceneMaterials = mset.getAllMaterials()

# Iterate all of the materials.
for material in sceneMaterials:
    # Get a field name of the material, the field name is reflectivity.
    materialFieldNames = material.reflectivity.getFieldNames()
    # If the field name is type of "Specular Map".
    if "Specular Map" in materialFieldNames:
            material.reflectivity.setField("Intensity", 0)
            material.reflectivity.setField("Color", [1, 1, 1])
            material.reflectivity.setField("Fresnel", 0)
            material.reflectivity.setField("Color;fresnel", [1, 1, 1])
    # If the field name is type of "Metalness Map".
    if "Metalness Map" in materialFieldNames:
            material.reflectivity.setField("Metalness", 0)
    else:
            continue
