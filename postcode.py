#!/usr/bin/python
import re
import pprint
REGULAR_PINCODE_REGEX = re.compile(r'^[A-Z]{1,2}[0-9][A-Z0-9]? ?[0-9][A-Z]{2}$')
SPECIAL_PINCODE_REGEX = re.compile(r'^(([A-Z]{1,2}[0-9][A-Z0-9]?|ASCN|STHL|TDCU|BBND|[BFS]IQQ|PCRN|TKCA) ?[0-9][A-Z]{2}|BFPO ?[0-9]{1,4}|(KY[0-9]|MSR|VG|AI)[ -]?[0-9]{4}|[A-Z]{2} ?[0-9]{2}|GE ?CX|GIR ?0A{2}|SAN ?TA1)$')

    
class UKPostcode(object):
    '''
    This class responsible for validating and formating UK postcodes.
    This class accepts postcode as a strings, validates it and set different parts of postcode
    as its attributes. If an invalid postcode is provided, it raises ValueError
    This class has two public methods for accessing various segments of postcode.
    E.g
    try:
        postCodeObj = UKPostcode('B1 1HQ')
    except ValueError:
        print('Invalid postcode')
    else:
        # printing out postcode various segments
        postCodeObj.printDetails()
        --------Output---------------
        >>
        Postcode             : B1 1HQ
        Outward code         : B1
         - Postcode area     : B
         - Postcode district : 1
        Inward code          : 1HQ
         - Postcode sector   : 1
         - Postcode unit     : HQ
        Is Special Case      : False
        
        # printing available attributes of postcode
        postCodeObj.printlistOfAttributes()
        --------Output---------------
        >>
        ['postcode', 'isValid', 'outwardCode', 'postcodeArea', 
        'postcodeDistrict', 'inwardCode', 'postcodeSector', 'postcodeUnit', 
        'isSpecialCase']
        

        # accessing individual attribute
        print(postCodeObj.outwardCode)
        print(postCodeObj.isValid)
        print(postCodeObj.isSpecialCase)
        --------Output---------------
        >> B1
        >> True
        >> False
    '''

    # Since all the properties of a postcode are fixed __slots__ will enfore the limitation.
    __slots__ = ['postcode', 'isValid', 'outwardCode', 'postcodeArea', 'postcodeDistrict',
                'inwardCode', 'postcodeSector', 'postcodeUnit', 'isSpecialCase'
                ]
    def __init__(self, postcode):
        self.postcode = postcode
        self.isValid  = False
        self.outwardCode = None
        self.postcodeArea = None
        self.postcodeDistrict = None
        self.inwardCode = None
        self.postcodeSector = None
        self.postcodeUnit = None
        self.isSpecialCase = False

        # Validating postcode automatically on UKPostcode class object initialization.
        self._validatePincodeAndSetSpecialCase()

        # Formating various postcode atttibutes and setting them as class attributes.
        self._setPostcodeAttributes()


    def _validatePincodeAndSetSpecialCase(self):
        '''
        This method is responsible for validating postcode and also identifying 
        whether this postcode is a special case postcode or not.
        If an invalid postcode is supplied function raises ValueError.
        Param: self
        Return: None
        Note: This is a private method
        '''
        if not REGULAR_PINCODE_REGEX.match(self.postcode):
            if not SPECIAL_PINCODE_REGEX.match(self.postcode):
                raise ValueError('Invalid UK postcode provided!!')
            else:
                self.isSpecialCase = True
        self.isValid = True

    def _setPostcodeAttributes(self):
        '''
        This method is responsible for setting class attributes related to
        various segments of postcode.
        Param: self
        Return: None
        Note: This is a private method
        '''
        self._setOutwardCodeDetails()
        self._setInwardCodeDetails()
    
    def _setOutwardCodeDetails(self):
        '''
        This method sets outward code and its segment details.
        There are two outward segments:
        1) postcode area
        2) postcode district
        Param: self
        Return: None
        Note: This is a private method
        '''
        # First half of postcode i.e set of charactes before spaces in postcode represents outward code.
        self.outwardCode = self.postcode.split(' ')[0]
        
        # If outward segment's length is 4 then postcode area is represented by two characters of  outward code
        # and remaining charactes represents postcode district
        if len(self.outwardCode) == 4:
            self.postcodeArea = self.outwardCode[0:2]
            self.postcodeDistrict = self.outwardCode[2:]
        
        # If outward segment's length is less than 4 then postcode area is represented by first characters of outward code
        # and remaining charactes represents postcode district
        else:
            self.postcodeArea = self.outwardCode[0]
            self.postcodeDistrict = self.outwardCode[1:]

    def _setInwardCodeDetails(self):
        '''
        This method sets inward code and its segment details.
        There are two outward segments:
        1) postcode sector
        2) postcode unit
        Param: self
        Return: None
        Note: This is a private method
        '''
        # Second half of postcode i.e set of charactes after spaces in postcode represents outward code.
        self.inwardCode = self.postcode.split(' ')[1]

        # First character of inwardcode represents postcode sector
        self.postcodeSector = self.inwardCode[0]
        # Remaining characters after postcode sector represents postcode unit.
        self.postcodeUnit = self.inwardCode[1:]
    
    def printDetails(self):
        '''
        This methods prints out various components of postcode.
        Param: self
        Return: None
        '''
        print('''
        Postcode             : {0}
        Outward code         : {1}
         - Postcode area     : {2}
         - Postcode district : {3}
        Inward code          : {4}
         - Postcode sector   : {5}
         - Postcode unit     : {6}
        Is Special Case      : {7}
        '''.format(self.postcode, self.outwardCode, self.postcodeArea, self.postcodeDistrict, 
        self.inwardCode, self.postcodeSector, self.postcodeUnit, self.isSpecialCase))

    def printListOfAttributes(self):
        '''
        This methods prints out available attribues of UKPostcode class.
        Param: self
        Return: None
        '''
        pprint.pprint(self.__slots__)
