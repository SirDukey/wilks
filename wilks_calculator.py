import argparse


# Values for calculation
A = -216.0475144
B = 16.2606339
C = -0.002388645
D = -0.00113732
E = 7.01863E-06
F = -1.291E-08


# configuration for the argument parser
text = 'This is a program to calculate your wilks score.'
parser = argparse.ArgumentParser(description=text)
parser.add_argument('--weight', '-w', help='body weight')
parser.add_argument('--total', '-t', help='total weight lifted')
args = parser.parse_args()

# getting the variables from the arguments
body_weight = int(args.weight)
total_lifted = int(args.total)

# do the calculation
coeff = 500 / (A + B * body_weight + C * (body_weight**2) + D * (body_weight**3) + E * (body_weight**4) + F * (body_weight**5))
score = round(total_lifted * coeff, 2) 

# print out the score
print(f'Your wilks score is: {score}')
