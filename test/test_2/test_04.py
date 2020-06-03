# 身高
height = 168

# 体重
weight = height - 105

# 胸围＝身高（厘米）×0.535
bust = height * 0.535

# 腰围＝身高（厘米）×0.365
the_waist = height * 0.365

# 臀围＝身高（厘米）×0.565
hipline = height * 0.565

print(f'身高:{height}cm\n'
      f'体重:{weight}KG\n'
      f'胸围:{round(bust,2)}cm\n'
      f'腰围:{round(the_waist,2)}cm\n'
      f'臀围:{round(hipline,2)}cm')