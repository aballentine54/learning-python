input_prompt = "what is your height, in feet and inches? (separate with a space)"

usr_ft, usr_inch = map(int, input(input_prompt).split())

tot_in_inch = (usr_ft*12) + usr_inch
print("you are",tot_in_inch,"inches tall.")

giraffe = 192 # giraffes are 192 inches tall, on average

ratio = giraffe / tot_in_inch

print(f"the average giraffe is: {ratio:.2f} times taller than you.")