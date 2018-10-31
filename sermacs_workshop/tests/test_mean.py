"""
Tests for molssi_math module
"""

import sermacs_workshop as sermacs
import pytest

def test_numeric_input():
	test_input = [1, 2, 3, 'a']
	
	with pytest.raises(TypeError):
		sermacs.mean(test_input)
