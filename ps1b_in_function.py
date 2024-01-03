def part_b(annual_salary, percent_saved, total_cost_of_home, semi_annual_raise):
	#########################################################################
	percent_down_payment = 0.12
	amount_saved = 0.0
	r = 0.06
	months = 0
	
	###############################################################################################
	## Determine how many months it would take to get the down payment for your dream home below ## 
	###############################################################################################
	down_payment_cost = total_cost_of_home * percent_down_payment
	monthly_salary = annual_salary / 12
	
	def saving_funds(current_saved_amount):
	    """
	    Assumes: current_saved_amount, a float number
	    Returns the additional funds accumulated in the savings account due to the annual rate of return
	    """
	    return current_saved_amount * (r / 12)
	
	while (amount_saved < down_payment_cost):
	    # if months is a product of 6, update monthly salary 
	    if (months % 6 == 0 and months != 0):
	        monthly_salary += (monthly_salary * semi_annual_raise)
	    # update amount_saved per month with an addition of the saved amount of the monthly salary and the additional funds created by returns in the saving account
	    amount_saved += (monthly_salary * percent_saved) + saving_funds(amount_saved)
	    months += 1
	
	print(f"Number of months: {months}")
	return months