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
