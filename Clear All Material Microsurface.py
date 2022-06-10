# Marmoset Toolbag 4 全部材质的Microsurface通道批量改成完全粗糙
# 导入 Marmoset 的程序库
import mset

# 获取所有的材质
sceneMaterials = mset.getAllMaterials()

# 遍历所有的材质
for material in sceneMaterials:
    # 获取microsurface通道的类型名称
   materialFieldNames = material.microsurface.getFieldNames()
   # 如果microsurface通道的类型名称是 "Gloss" 的类型
   if "Gloss" in materialFieldNames:
    # 把"Gloss"的数值改成0
    material.microsurface.setField("Gloss", 0)
   # 如果microsurface通道的类型名称是 "Roughness" 的类型
   if "Roughness" in materialFieldNames:
    # 把 "Roughness" 的数值改成1，这个刚好和"Gloss"相反的
    material.microsurface.setField("Roughness", 1)
   if "Microsurface Map" in materialFieldNames:
    material.microsurface.setField("Mode", 0)
    material.microsurface.setField("Maximum", 0)
    material.microsurface.setField("Minimum", 0)
    material.microsurface.setField("Exponent", 0)
    material.microsurface.setField("Horizon Smoothing", 0)
   else:
    continue