def computepay(hours, rate):
  # print("In computepay", hours, rate)
  if hours > 40 :
  # print("Overtime")
    reg = rate * hours
    otp = (hours - 40.0) * (rate * 0.5)
  # print(reg, otp)
    pay = reg + otp
  else:
  # print("regular")
    pay = hours * rate
  # print("Returning", pay)
  return pay
  
# read two values
sh = input("Enter Hours: ")
sr = input("Enter Rate: ")
# converting to floating point numbers
fh = float(sh)
fr = float(sr)

xp =computepay(fh,fr)

print("Pay: ", xp)