def part_c(initial_deposit):
	#########################################################################
	total_cost_of_home = 800000.0
	percent_down_payment = 0.12
	months = 36
	r_max = 1.00
	r_min = 0.00
	r_mid = 0.00
	r = 0.00
	steps = 0
	
	##################################################################################################
	## Determine the lowest rate of return needed to get the down payment for your dream home below ##
	##################################################################################################
	down_payment_cost = total_cost_of_home * percent_down_payment
	down_payment_cost_bottom_range = down_payment_cost - 100
	down_payment_cost_top_range = down_payment_cost + 100
	r_lowest = False
	
	def amount_saved_formula(r):
	    """
	    Assumes: r, a float number
	    Returns the amount saved
	    """
	    return(initial_deposit * (1 + r/12)**months)
	
	while(r_lowest == False):
	    # Fail safe for if initial deposit is too small for it to be possible
	    if (amount_saved_formula(r_max) < down_payment_cost_bottom_range):
	        r = None
	        break
	
	    if (initial_deposit > down_payment_cost_bottom_range):
	        r = 0.0
	        break
	
	    # Set r_mid equal to new mid value for bisection search
	    r_mid = (r_max + r_min) / 2
	
	    amount_saved = amount_saved_formula(r_mid)
	    
	    # perform bisection search
	    if (amount_saved > down_payment_cost_top_range):
	        r_max = r_mid
	    elif(amount_saved < down_payment_cost_bottom_range): 
	        r_min = r_mid
	    elif(amount_saved < down_payment_cost_top_range and amount_saved > down_payment_cost_bottom_range):
	        r = r_mid
	        r_lowest = True
	    steps += 1
	
	print(f"Best savings rate: {r} [or very close to this number]")
	print(f"Steps in bisection search: {steps}")
	return r, steps