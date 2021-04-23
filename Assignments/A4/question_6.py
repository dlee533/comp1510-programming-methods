"""
The first unit test will be done to test the return value for parallel lines. ex. [[3.0, 5.0], [1.0, 3.0]]
and [[0.0, 0.0], [1.0, 3.0]]. It is an exceptional case and thus needs to be tested on a separate unit test.

The second unit test will be on coincident line, by asserting that the first argument returns. This is also
an exceptional case and needs to be tested on a separate unit test.

The third unit test will be to test that the function raises error when a pair of points have same
coordinates. It is again, an exceptional case and needs to be tested

The fourth unit test will be to test that the function raises error when the argument passed is not of correct
data structure. It is a possible error a user can make, and needs to be tested

The fifth unit test will be to test for intersection with negative coordinates. This is tested to see if the correct
return value is returned and if it works properly. It is the standard use case of the users and so must be tested

The sixth unit test will be to test for intersection with positive coordinates. This is tested to see if the correct
return value is returned and if it works properly. It is the standard use case of the users and so must be tested
"""