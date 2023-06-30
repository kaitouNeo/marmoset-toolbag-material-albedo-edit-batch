# Quick turn the roughness of all materials into most rough in Marmoset Toolbag 4.
# Import the libraries of Marmoset Toolbag.
import mset

# Get all of materials.
sceneMaterials = mset.getAllMaterials()

# Iterate all of the materials.
for material in sceneMaterials:
    # Get a field name of the material, the field name is microsurface.
   materialFieldNames = material.microsurface.getFieldNames()
   # If the field name is type of "Gloss".
   if "Gloss" in materialFieldNames:
    # Turn the value of gloss into 0.
    material.microsurface.setField("Gloss", 0)
   # If the field name is type of "Roughness"(PBR metalness workflow).
   if "Roughness" in materialFieldNames:
    # Turn the value of roughness into 1,  it is reverse to the value of gloss.
    material.microsurface.setField("Roughness", 1)
   if "Microsurface Map" in materialFieldNames:
    material.microsurface.setField("Mode", 0)
    material.microsurface.setField("Maximum", 0)
    material.microsurface.setField("Minimum", 0)
    material.microsurface.setField("Exponent", 0)
    material.microsurface.setField("Horizon Smoothing", 0)
   else:
    continue
