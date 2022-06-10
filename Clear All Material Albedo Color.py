# Marmoset Toolbag 4 全部材质的Albedo通道批量改成白色
# 导入 Marmoset 的程序库
import mset

# 获取所有的材质
sceneMaterials = mset.getAllMaterials()

# 遍历所有的材质，然后把颜色改成白色
for material in sceneMaterials:
    # 获取 albedo 通道的类型名称
    materialFieldNames = material.albedo.getFieldNames()
     # 如果 albedo 通道的类型名称是 "albedo" 的类型(而不是vertext color类型)
    if "Albedo Map" in materialFieldNames:
        # 把"albedo"的数值改成白色
        material.albedo.setField("Color", [1, 1, 1])
    else:
        continue