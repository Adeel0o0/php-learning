train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1



def f_to_c(temp):
  c_temp = (temp - 32) * 5/9
  return c_temp

f100_in_celcius = f_to_c(100)
print(f100_in_celcius)

def c_to_f(temp):
  f_temp = temp * (9/5) + 32
  return f_temp

c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit)

