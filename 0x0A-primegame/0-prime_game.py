#!/usr/bin/python3
"""Prime game module.
"""


def is_prime(n):
    """ Check if the given input is a prime numeber
    """
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def primepicker(numlist):
    """ Picks a prime number from the given list numlist
    """
    picked_prime = 0
    for ele in numlist:
        if is_prime(ele):
            picked_prime = ele
            break
    return picked_prime


def isWinner(x, nums):
    """Determines the winner of a prime game session with `x` rounds.
    """
    if x < 1 or not nums:
        return None
    b = 0
    m = 0

    for index in range(x):
        numlist = list(range(1, nums[index] + 1))

        while numlist:
            m_primepick = primepicker(numlist)
            if m_primepick != 0:
                for ele in numlist:
                    if ele % m_primepick == 0:
                        numlist.remove(ele)
            else:
                break

            b_primepick = primepicker(numlist)
            if b_primepick != 0:
                for ele in numlist:
                    if ele % b_primepick == 0:
                        numlist.remove(ele)
            else:
                break

        if m_primepick == 0:
            b += 1
        elif b_primepick == 0:
            m += 1

    if b > m:
        return "Ben"
    elif m > b:
        return "Maria"
    else:
        return None
