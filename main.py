def main():
    workhours = int(input('Enter your work hours: '))
    # overtime = workhours - reg_hours
    # overtime_wage = overtime * ov_rate
    # regular_wage = reg_hours * reg_rate
    # total_wage = regular_wage + overtime_wage
    regular_rate = 18.25
    regular_hours = 40
    overtime_rate = 27.78

    regular_wage = (regular_rate) * (regular_hours)
    overtime_wage = (overtime_rate) * (workhours - regular_hours) 
    total_wage =  regular_wage + overtime_wage


    print("Regular Charge: ", regular_wage)
    print("Overtime Charge: " , overtime_wage)
    print("Total Wage: ", total_wage)

# =======
#     regular_hours = 50
#     overtime_rate = 27.78

#     regular_rate = (regular_rate) * (regular_hours)
#     overtime_hours = (regular_hours) + (overtime_rate) * 1.5
#     total_wage = (regular_rate) + (regular_hours) + (overtime_hours)


    print("Regular Charge: ", regular_rate)
    print("Overtime Charge: " , overtime_hours)
    print("Total Wage: ", total_wage)

# >>>>>>> main
#     # print(f"Regular hours: {reg_hours} Regular Charge: {regular_wage}")
#     # print(f"Overtime hours: {overtime} Overtime Charge: {overtime_wage:.2f}")
#     # print(f"Total wage : {total_wage:.2f}")

   ##################################################
   # Do not delete the return statement
   ##################################################
    return regular_wage, overtime_wage, total_wage


if __name__ == '__main__':
    main()
