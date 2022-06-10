# Marmoset Toolbag 4 全部材质的Reflectivity通道批量改成0
# 导入 Marmoset 的程序库
import mset

# 获取所有的材质
sceneMaterials = mset.getAllMaterials()

# 遍历所有的材质
for material in sceneMaterials:
    # 获取 reflectivity 通道的类型名称
    materialFieldNames = material.reflectivity.getFieldNames()
    # 如果 reflectivity 通道的类型名称是 "Specular Map" 的类型
    if "Specular Map" in materialFieldNames:
            material.reflectivity.setField("Intensity", 0)
            material.reflectivity.setField("Color", [1, 1, 1])
            material.reflectivity.setField("Fresnel", 0)
            material.reflectivity.setField("Color;fresnel", [1, 1, 1])
    # 如果 reflectivity 通道的类型名称是 "Metalness Map" 的类型
    if "Metalness Map" in materialFieldNames:
            material.reflectivity.setField("Metalness", 0)
    else:
            continue