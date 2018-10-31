"""
Tests for list_util module
"""

import sermacs_workshop as sermacs
import pytest

def test_title_case():
	test_string = 'thIs Is a test STRING.'
	title_string = sermacs.title_case(test_string)
	
	assert title_string == 'This Is A Test String.'
	
	return True

def test_type_failure():
	test_input = ['This', 'is', 'a', 'list']
	
	with pytest.raises(TypeError):
		sermacs.title_case(test_input)