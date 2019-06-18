def overlap_indicator(line1, line2):
    """
    First we will check for +ve and -ve numbers
    :param line1: First line with two points( starting and ending)
    :type line1:
    :param line2: Second line with two points( starting and ending)
    :type line2:
    :return: True for overlap and False for not overlap
    :rtype: String
    """
    if line1[0] and line1[1] < 0 and line2[0] and line2[1] < 0:
        # check out the starting and ending point
        if line1[1] > line2[0]:
            return False
        else:
            return True
    else:
        if line1[1] > line2[0]:
            return True
        else:
            return False


def string_comparison(str1, str2):
    """
    first, we will check out if the strings are convertible to integers or not
    :param str1:
    :type str1:
    :param str2:
    :type str2:
    :return:
    :rtype:
    """
    if str1.isdigit() and str2.isdigit():
        print('Its Integer')
        s1 = int(str1)
        s2 = int(str2)
        if s1 > s2:
            return 'greater then'
        elif s1 < s2:
            return 'less then'
        else:
            return 'equal to '
    # secondly, we will check for floating number
    elif str1.replace('.', '', 1).isdigit() and str1.count('.') < 2:
        print('Its float')
        s1 = float(str1)
        s2 = float(str2)
        if s1 > s2:
            return 'greater then'
        elif s1 < s2:
            return 'less then'
        else:
            return 'equal to'
    # and finally, we will check for strings
    else:
        print('Its is Neither Integer Nor Float! Something else')
        s1 = sorted(str1)
        s2 = sorted(str2)
        if s1 > s2:
            return 'greater then'
        elif s1 < s2:
            return 'less then'
        else:
            return 'equal to'


if __name__ == '__main__':
    l1 = [5, 6]
    l2 = [4, 7]
    l3 = [1, 5]
    l4 = [6, 8]
    str1 = '3.1'
    str2 = '3.9'
    # print(overlap_indicator(l3, l4))
    print(string_comparison(str1, str2))
