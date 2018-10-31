"""
molssi_math.py
Sample repository for MolSSI workshop

Handles the primary functions
"""

def mean(num_list):
	"""
	description -- computes the mean of a list.
	Parameters
	----------
	num_list: list
		A list of numbers whose mean is to be computed
	
	Returns
	-------
	list_mean: float
		Mean of the list of numbers
	"""
	
	# error checking
	
	# check that input is a list
	
	if not isinstance(num_list, list):
		raise TypeError('In mean, input must be a list.')
	
	# check that list length > 0
	
	if len(num_list) == 0:
		raise TypeError('In mean, list must have nonzero length.')
	
	# check that values in list are all numeric
	
	for i in range(len(num_list)):
		if (not isinstance(num_list[i], int)) and (not isinstance(num_list[i], float)):
			raise TypeError('In mean, list must be populated with only numbers.')
	
	list_mean = sum(num_list)/len(num_list)
	
	return list_mean

def mean2(num_list):
	"""
	description -- computes the mean of a list.
	Parameters
	----------
	num_list: list
		A list of numbers whose mean is to be computed
	
	Returns
	-------
	list_mean: float
		Mean of the list of numbers
	"""
	
	s = 0
	
	for i in range(len(num_list)):
		s = s + num_list[i]
	
	list_mean = s/len(num_list)
	
	return list_mean

def canvas(with_attribution=True):
    """
    Placeholder function to show example docstring (NumPy format)

    Replace this function and doc string for your own project

    Parameters
    ----------
    with_attribution : bool, Optional, default: True
        Set whether or not to display who the quote is from

    Returns
    -------
    quote : str
        Compiled string including quote and optional attribution
    """

    quote = "The code is but a canvas to our imagination."
    if with_attribution:
        quote += "\n\t- Adapted from Henry David Thoreau"
    return quote


if __name__ == "__main__":
    # Do something if this file is invoked on its own
    print(canvas())
