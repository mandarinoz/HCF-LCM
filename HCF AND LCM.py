# github: mandarinoz
# HCF and LCM of two numbers

x, y = int(input("Enter x: ")), int(input("Enter y: "))        # Let two nums are x and y
if (x < 0) or (y < 0):
    print("Number is negative")                      #if any one num is -ve
else:
    if x > y:
        smallest = y                         # finding smallest of two nums
    else:
        smallest = x
    for i in range(1, smallest + 1):                  #1st loop  for finding HCF but it shows only 1st common multiple
        if (x % i == 0) and (y % i == 0):
            HCF = i
            for j in range(i, smallest + 1):            #2nd loop for finding HCF it shows highest common multiple
                if (x % j == 0) and (y % j == 0):
                    HCF = j
                    break                                #break to exit from loop
    LCM = (x * y) / (HCF)              #Formula for finding LCM
    LCM = int(LCM)
    print("HCF =", HCF)
    print("LCM =", LCM)

#Done :)
