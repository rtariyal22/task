#!/usr/bin/python
'''
Testing UKPostcode class
python test_postcode.py

We should use pytest for running and maintaing test suits. Since it requires pytest to be installed for the purpose of this task
I have written custom tests.
'''
STANDARD_POSTCODE_FORMATS = ['AA9A 9AA', 'A9A 9AA', 'A9 9AA', 'A99 9AA', 'AA9 9AA','AA99 9AA']
SPECIAL_POSTCODE_FORMATS = ['ASCN 1ZZ','BBND 1ZZ','BIQQ 1ZZ','FIQQ 1ZZ','GX11 1AA','PCRN 1ZZ','SIQQ 1ZZ','STHL 1ZZ',
'TDCU 1ZZ','TKCA 1ZZ']

from pincode import UKPostcode


def test_standard_postcodes():
    '''
    Validates all standard postcode formats
    '''
    for eachPostcode in STANDARD_POSTCODE_FORMATS:
        try:
            UKPostcode(eachPostcode)
        except ValueError:
            assert False, 'Invalidating valid postcode'
        else:
            assert True

def test_special_postcode():
    '''
    Validates all special postcode formats
    '''
    for eachPostcode in SPECIAL_POSTCODE_FORMATS:
        try:
            UKPostcode(eachPostcode)
        except ValueError:
            assert False, 'Invalidating valid special postcodes'
        else:
            assert True


def test_invalid_postcode():
    '''
    Checks if UKPostcode is invalidating invalid postcode correctly.
    '''
    try:
        UKPostcode('UK12 22')
    except ValueError:
        assert True
    else:
        assert False, 'Invalidating valid postcode'

def test_postcode_isstandard():
    '''
    Checks if UKPostcode is identifying a standard postcode correctly.
    '''
    try:
        postCodeObj = UKPostcode('AA9A 9AA')
    except ValueError:
        assert False, 'Invalidating valid postcode'
    else:
        assert postCodeObj.isSpecialCase == False


def test_postcode_isspecial():
    '''
    Checks if UKPostcode is identifying a special postcode correctly.
    '''
    try:
        postCodeObj = UKPostcode('ASCN 1ZZ')
    except ValueError:
        assert False, 'Invalidating valid postcode'
    else:
        assert postCodeObj.isSpecialCase == True


def test_postcode_outwardcode_details():
    '''
    Checks all outword code details of UKPostcode 
    '''
    try:
        postCodeObj = UKPostcode('AA9A 9AA')
    except ValueError:
        assert False, 'Invalidating valid postcode'
    else:
        assert postCodeObj.outwardCode == 'AA9A'
        assert postCodeObj.postcodeArea == 'AA'
        assert postCodeObj.postcodeDistrict == '9A'


def test_postcode_inwardcode_details():
    '''
    Checks all inward code details of UKPostcode 
    '''
    try:
        postCodeObj = UKPostcode('AA9A 9AA')
    except ValueError:
        assert False, 'Invalidating valid postcode'
    else:
        assert postCodeObj.inwardCode == '9AA'
        assert postCodeObj.postcodeSector == '9'
        assert postCodeObj.postcodeUnit == 'AA'

    
if __name__ == '__main__':
    test_standard_postcodes()
    test_special_postcode()
    test_invalid_postcode()
    test_postcode_isstandard()
    test_postcode_isspecial()
    test_postcode_outwardcode_details()
    test_postcode_inwardcode_details()

