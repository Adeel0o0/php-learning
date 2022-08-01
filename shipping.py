weight = 80
# Ground shipping

if weight <= 2:
 cost_ground_shipping = weight * 1.5 + 20
elif weight <= 6:
 cost_ground_shipping = weight * 3 + 20
elif weight <= 10:
  cost_ground_shipping = weight * 4 + 20
else:
  cost_ground_shipping = weight * 4.75 + 20

print("Ground shipping $", cost_ground_shipping)