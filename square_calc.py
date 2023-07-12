def main():
	num_case = (input("Insert the number of cases: "))
	try:
		(int(num_case))
	except:
		print("Error! Input should be a valid number between 1 and 100.")
		return main()
	num_case = int(num_case)
	if (num_case > 100) or (num_case < 1):
		print("Number of cases should be between 1 and 100. Try Again!")
		return main()
	result = cases_counter(0, num_case, 0, 0)
	print("Here are the results: ")
	print(result)
	
def cases_counter(result, num_case, case_count, index):
	if case_count == num_case:
		return (result)
	
	num_int = (input("Insert the ammount of numbers you wish to insert: "))
	try:
		(int(num_int))
	except:
		print("Error! Input should be a valid number between 1 and 100.")
		return cases_counter(result, num_case, case_count, index)
	
	num_int = int(num_int)
	if (num_int > 100) or (num_int < 1) or (num_int == ''):
		print("Ammount of numbers should be between 1 and 100. Try Again!")
		return cases_counter(result, num_case, case_count, index)
	
	num_tuple = tuple(input("Insert the number(s) separated by spaces: ").split())
	if (len(num_tuple) > num_int):
		print("Error! Incorrect ammount of integers inserted.")
		return cases_counter(result, num_case, case_count, index)
	try:
		(int(num_tuple[index]))		
	except:
		print("Error! Input should be a valid number")
		return cases_counter(result, num_case, case_count, index + 1)

	value = str(calc_square(0, num_int, 0, num_tuple))

	if result == 0:
			result = value
	else:
		result = str(result + '\n' + value)
	return cases_counter(result, num_case, case_count + 1, index)

def calc_square(result, num_int, index, num_tuple):
	if index == num_int:
		return (result)

	num = int(num_tuple[index])
	if num >= 1:
		result = result + num ** 2
	return(calc_square(result, num_int, index + 1, num_tuple))

if __name__ == "__main__":
		main()