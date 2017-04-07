"""Module defining currencies and currency utilities"""

from enum import Enum

#pylint: disable=too-many-lines

class Currency(Enum):
    """Enumerates all supported currencies"""

    AED = 'AED'
    AFN = 'AFN'
    ALL = 'ALL'
    AMD = 'AMD'
    ANG = 'ANG'
    AOA = 'AOA'
    ARS = 'ARS'
    AUD = 'AUD'
    AWG = 'AWG'
    AZN = 'AZN'
    BAM = 'BAM'
    BBD = 'BBD'
    BDT = 'BDT'
    BGN = 'BGN'
    BHD = 'BHD'
    BIF = 'BIF'
    BMD = 'BMD'
    BND = 'BND'
    BOB = 'BOB'
    BOV = 'BOV'
    BRL = 'BRL'
    BSD = 'BSD'
    BTN = 'BTN'
    BWP = 'BWP'
    BYR = 'BYR'
    BZD = 'BZD'
    CAD = 'CAD'
    CDF = 'CDF'
    CHE = 'CHE'
    CHF = 'CHF'
    CHW = 'CHW'
    CLF = 'CLF'
    CLP = 'CLP'
    CNY = 'CNY'
    COP = 'COP'
    COU = 'COU'
    CRC = 'CRC'
    CUC = 'CUC'
    CUP = 'CUP'
    CVE = 'CVE'
    CZK = 'CZK'
    DJF = 'DJF'
    DKK = 'DKK'
    DOP = 'DOP'
    DZD = 'DZD'
    EGP = 'EGP'
    ERN = 'ERN'
    ETB = 'ETB'
    EUR = 'EUR'
    FJD = 'FJD'
    FKP = 'FKP'
    GBP = 'GBP'
    GEL = 'GEL'
    GHS = 'GHS'
    GIP = 'GIP'
    GMD = 'GMD'
    GNF = 'GNF'
    GTQ = 'GTQ'
    GYD = 'GYD'
    HKD = 'HKD'
    HNL = 'HNL'
    HRK = 'HRK'
    HTG = 'HTG'
    HUF = 'HUF'
    IDR = 'IDR'
    ILS = 'ILS'
    INR = 'INR'
    IQD = 'IQD'
    IRR = 'IRR'
    ISK = 'ISK'
    JMD = 'JMD'
    JOD = 'JOD'
    JPY = 'JPY'
    KES = 'KES'
    KGS = 'KGS'
    KHR = 'KHR'
    KMF = 'KMF'
    KPW = 'KPW'
    KRW = 'KRW'
    KWD = 'KWD'
    KYD = 'KYD'
    KZT = 'KZT'
    LAK = 'LAK'
    LBP = 'LBP'
    LKR = 'LKR'
    LRD = 'LRD'
    LSL = 'LSL'
    LTL = 'LTL'
    LVL = 'LVL'
    LYD = 'LYD'
    MAD = 'MAD'
    MDL = 'MDL'
    MGA = 'MGA'
    MKD = 'MKD'
    MMK = 'MMK'
    MNT = 'MNT'
    MOP = 'MOP'
    MRO = 'MRO'
    MUR = 'MUR'
    MVR = 'MVR'
    MWK = 'MWK'
    MXN = 'MXN'
    MXV = 'MXV'
    MYR = 'MYR'
    MZN = 'MZN'
    NAD = 'NAD'
    NGN = 'NGN'
    NIO = 'NIO'
    NOK = 'NOK'
    NPR = 'NPR'
    NZD = 'NZD'
    OMR = 'OMR'
    PAB = 'PAB'
    PEN = 'PEN'
    PGK = 'PGK'
    PHP = 'PHP'
    PKR = 'PKR'
    PLN = 'PLN'
    PYG = 'PYG'
    QAR = 'QAR'
    RON = 'RON'
    RSD = 'RSD'
    RUB = 'RUB'
    RWF = 'RWF'
    SAR = 'SAR'
    SBD = 'SBD'
    SCR = 'SCR'
    SDG = 'SDG'
    SEK = 'SEK'
    SGD = 'SGD'
    SHP = 'SHP'
    SLL = 'SLL'
    SOS = 'SOS'
    SRD = 'SRD'
    SSP = 'SSP'
    STD = 'STD'
    SVC = 'SVC'
    SYP = 'SYP'
    SZL = 'SZL'
    THB = 'THB'
    TJS = 'TJS'
    TMT = 'TMT'
    TND = 'TND'
    TOP = 'TOP'
    TRY = 'TRY'
    TTD = 'TTD'
    TWD = 'TWD'
    TZS = 'TZS'
    UAH = 'UAH'
    UGX = 'UGX'
    USD = 'USD'
    USN = 'USN'
    USS = 'USS'
    UYI = 'UYI'
    UYU = 'UYU'
    UZS = 'UZS'
    VEF = 'VEF'
    VND = 'VND'
    VUV = 'VUV'
    WST = 'WST'
    XAF = 'XAF'
    XAG = 'XAG'
    XAU = 'XAU'
    XBA = 'XBA'
    XBB = 'XBB'
    XBC = 'XBC'
    XBD = 'XBD'
    XCD = 'XCD'
    XDR = 'XDR'
    XFU = 'XFU'
    XOF = 'XOF'
    XPD = 'XPD'
    XPF = 'XPF'
    XPT = 'XPT'
    XSU = 'XSU'
    XTS = 'XTS'
    XUA = 'XUA'
    YER = 'YER'
    ZAR = 'ZAR'
    ZMW = 'ZMW'
    ZWL = 'ZWL'

class CurrencyHelper:
    """Utilities for currencies"""

    _CURRENCY_DATA = {
        Currency.AED: {
            'display_name': 'UAE Dirham',
            'numeric_code': 784,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.AFN: {
            'display_name': 'Afghani',
            'numeric_code': 971,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.ALL: {
            'display_name': 'Lek',
            'numeric_code': 8,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.AMD: {
            'display_name': 'Armenian Dram',
            'numeric_code': 51,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.ANG: {
            'display_name': 'Netherlands Antillean Guilder',
            'numeric_code': 532,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.AOA: {
            'display_name': 'Kwanza',
            'numeric_code': 973,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.ARS: {
            'display_name': 'Argentine Peso',
            'numeric_code': 32,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.AUD: {
            'display_name': 'Australian Dollar',
            'numeric_code': 36,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.AWG: {
            'display_name': 'Aruban Florin',
            'numeric_code': 533,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.AZN: {
            'display_name': 'Azerbaijanian Manat',
            'numeric_code': 944,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.BAM: {
            'display_name': 'Convertible Mark',
            'numeric_code': 977,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.BBD: {
            'display_name': 'Barbados Dollar',
            'numeric_code': 52,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.BDT: {
            'display_name': 'Taka',
            'numeric_code': 50,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.BGN: {
            'display_name': 'Bulgarian Lev',
            'numeric_code': 975,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.BHD: {
            'display_name': 'Bahraini Dinar',
            'numeric_code': 48,
            'default_fraction_digits': 3,
            'sub_unit': 1000,
        },
        Currency.BIF: {
            'display_name': 'Burundi Franc',
            'numeric_code': 108,
            'default_fraction_digits': 0,
            'sub_unit': 100,
        },
        Currency.BMD: {
            'display_name': 'Bermudian Dollar',
            'numeric_code': 60,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.BND: {
            'display_name': 'Brunei Dollar',
            'numeric_code': 96,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.BOB: {
            'display_name': 'Boliviano',
            'numeric_code': 68,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.BOV: {
            'display_name': 'Mvdol',
            'numeric_code': 984,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.BRL: {
            'display_name': 'Brazilian Real',
            'numeric_code': 986,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.BSD: {
            'display_name': 'Bahamian Dollar',
            'numeric_code': 44,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.BTN: {
            'display_name': 'Ngultrum',
            'numeric_code': 64,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.BWP: {
            'display_name': 'Pula',
            'numeric_code': 72,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.BYR: {
            'display_name': 'Belarussian Ruble',
            'numeric_code': 974,
            'default_fraction_digits': 0,
            'sub_unit': 100,
        },
        Currency.BZD: {
            'display_name': 'Belize Dollar',
            'numeric_code': 84,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.CAD: {
            'display_name': 'Canadian Dollar',
            'numeric_code': 124,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.CDF: {
            'display_name': 'Congolese Franc',
            'numeric_code': 976,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.CHE: {
            'display_name': 'WIR Euro',
            'numeric_code': 947,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.CHF: {
            'display_name': 'Swiss Franc',
            'numeric_code': 756,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.CHW: {
            'display_name': 'WIR Franc',
            'numeric_code': 948,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.CLF: {
            'display_name': 'Unidades de fomento',
            'numeric_code': 990,
            'default_fraction_digits': 0,
            'sub_unit': 100,
        },
        Currency.CLP: {
            'display_name': 'Chilean Peso',
            'numeric_code': 152,
            'default_fraction_digits': 0,
            'sub_unit': 100,
        },
        Currency.CNY: {
            'display_name': 'Yuan Renminbi',
            'numeric_code': 156,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.COP: {
            'display_name': 'Colombian Peso',
            'numeric_code': 170,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.COU: {
            'display_name': 'Unidad de Valor Real',
            'numeric_code': 970,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.CRC: {
            'display_name': 'Costa Rican Colon',
            'numeric_code': 188,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.CUC: {
            'display_name': 'Peso Convertible',
            'numeric_code': 931,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.CUP: {
            'display_name': 'Cuban Peso',
            'numeric_code': 192,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.CVE: {
            'display_name': 'Cape Verde Escudo',
            'numeric_code': 132,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.CZK: {
            'display_name': 'Czech Koruna',
            'numeric_code': 203,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.DJF: {
            'display_name': 'Djibouti Franc',
            'numeric_code': 262,
            'default_fraction_digits': 0,
            'sub_unit': 100,
        },
        Currency.DKK: {
            'display_name': 'Danish Krone',
            'numeric_code': 208,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.DOP: {
            'display_name': 'Dominican Peso',
            'numeric_code': 214,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.DZD: {
            'display_name': 'Algerian Dinar',
            'numeric_code': 12,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.EGP: {
            'display_name': 'Egyptian Pound',
            'numeric_code': 818,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.ERN: {
            'display_name': 'Nakfa',
            'numeric_code': 232,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.ETB: {
            'display_name': 'Ethiopian Birr',
            'numeric_code': 230,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.EUR: {
            'display_name': 'Euro',
            'numeric_code': 978,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.FJD: {
            'display_name': 'Fiji Dollar',
            'numeric_code': 242,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.FKP: {
            'display_name': 'Falkland Islands Pound',
            'numeric_code': 238,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.GBP: {
            'display_name': 'Pound Sterling',
            'numeric_code': 826,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.GEL: {
            'display_name': 'Lari',
            'numeric_code': 981,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.GHS: {
            'display_name': 'Ghana Cedi',
            'numeric_code': 936,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.GIP: {
            'display_name': 'Gibraltar Pound',
            'numeric_code': 292,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.GMD: {
            'display_name': 'Dalasi',
            'numeric_code': 270,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.GNF: {
            'display_name': 'Guinea Franc',
            'numeric_code': 324,
            'default_fraction_digits': 0,
            'sub_unit': 100,
        },
        Currency.GTQ: {
            'display_name': 'Quetzal',
            'numeric_code': 320,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.GYD: {
            'display_name': 'Guyana Dollar',
            'numeric_code': 328,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.HKD: {
            'display_name': 'Hong Kong Dollar',
            'numeric_code': 344,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.HNL: {
            'display_name': 'Lempira',
            'numeric_code': 340,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.HRK: {
            'display_name': 'Croatian Kuna',
            'numeric_code': 191,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.HTG: {
            'display_name': 'Gourde',
            'numeric_code': 332,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.HUF: {
            'display_name': 'Forint',
            'numeric_code': 348,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.IDR: {
            'display_name': 'Rupiah',
            'numeric_code': 360,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.ILS: {
            'display_name': 'New Israeli Sheqel',
            'numeric_code': 376,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.INR: {
            'display_name': 'Indian Rupee',
            'numeric_code': 356,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.IQD: {
            'display_name': 'Iraqi Dinar',
            'numeric_code': 368,
            'default_fraction_digits': 3,
            'sub_unit': 1000,
        },
        Currency.IRR: {
            'display_name': 'Iranian Rial',
            'numeric_code': 364,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.ISK: {
            'display_name': 'Iceland Krona',
            'numeric_code': 352,
            'default_fraction_digits': 0,
            'sub_unit': 100,
        },
        Currency.JMD: {
            'display_name': 'Jamaican Dollar',
            'numeric_code': 388,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.JOD: {
            'display_name': 'Jordanian Dinar',
            'numeric_code': 400,
            'default_fraction_digits': 3,
            'sub_unit': 1000,
        },
        Currency.JPY: {
            'display_name': 'Yen',
            'numeric_code': 392,
            'default_fraction_digits': 0,
            'sub_unit': 1,
        },
        Currency.KES: {
            'display_name': 'Kenyan Shilling',
            'numeric_code': 404,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.KGS: {
            'display_name': 'Som',
            'numeric_code': 417,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.KHR: {
            'display_name': 'Riel',
            'numeric_code': 116,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.KMF: {
            'display_name': 'Comoro Franc',
            'numeric_code': 174,
            'default_fraction_digits': 0,
            'sub_unit': 100,
        },
        Currency.KPW: {
            'display_name': 'North Korean Won',
            'numeric_code': 408,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.KRW: {
            'display_name': 'Won',
            'numeric_code': 410,
            'default_fraction_digits': 0,
            'sub_unit': 100,
        },
        Currency.KWD: {
            'display_name': 'Kuwaiti Dinar',
            'numeric_code': 414,
            'default_fraction_digits': 3,
            'sub_unit': 1000,
        },
        Currency.KYD: {
            'display_name': 'Cayman Islands Dollar',
            'numeric_code': 136,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.KZT: {
            'display_name': 'Tenge',
            'numeric_code': 398,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.LAK: {
            'display_name': 'Kip',
            'numeric_code': 418,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.LBP: {
            'display_name': 'Lebanese Pound',
            'numeric_code': 422,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.LKR: {
            'display_name': 'Sri Lanka Rupee',
            'numeric_code': 144,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.LRD: {
            'display_name': 'Liberian Dollar',
            'numeric_code': 430,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.LSL: {
            'display_name': 'Loti',
            'numeric_code': 426,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.LTL: {
            'display_name': 'Lithuanian Litas',
            'numeric_code': 440,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.LVL: {
            'display_name': 'Latvian Lats',
            'numeric_code': 428,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.LYD: {
            'display_name': 'Libyan Dinar',
            'numeric_code': 434,
            'default_fraction_digits': 3,
            'sub_unit': 1000,
        },
        Currency.MAD: {
            'display_name': 'Moroccan Dirham',
            'numeric_code': 504,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.MDL: {
            'display_name': 'Moldovan Leu',
            'numeric_code': 498,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.MGA: {
            'display_name': 'Malagasy Ariary',
            'numeric_code': 969,
            'default_fraction_digits': 2,
            'sub_unit': 5,
        },
        Currency.MKD: {
            'display_name': 'Denar',
            'numeric_code': 807,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.MMK: {
            'display_name': 'Kyat',
            'numeric_code': 104,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.MNT: {
            'display_name': 'Tugrik',
            'numeric_code': 496,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.MOP: {
            'display_name': 'Pataca',
            'numeric_code': 446,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.MRO: {
            'display_name': 'Ouguiya',
            'numeric_code': 478,
            'default_fraction_digits': 2,
            'sub_unit': 5,
        },
        Currency.MUR: {
            'display_name': 'Mauritius Rupee',
            'numeric_code': 480,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.MVR: {
            'display_name': 'Rufiyaa',
            'numeric_code': 462,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.MWK: {
            'display_name': 'Kwacha',
            'numeric_code': 454,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.MXN: {
            'display_name': 'Mexican Peso',
            'numeric_code': 484,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.MXV: {
            'display_name': 'Mexican Unidad de Inversion (UDI)',
            'numeric_code': 979,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.MYR: {
            'display_name': 'Malaysian Ringgit',
            'numeric_code': 458,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.MZN: {
            'display_name': 'Mozambique Metical',
            'numeric_code': 943,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.NAD: {
            'display_name': 'Namibia Dollar',
            'numeric_code': 516,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.NGN: {
            'display_name': 'Naira',
            'numeric_code': 566,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.NIO: {
            'display_name': 'Cordoba Oro',
            'numeric_code': 558,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.NOK: {
            'display_name': 'Norwegian Krone',
            'numeric_code': 578,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.NPR: {
            'display_name': 'Nepalese Rupee',
            'numeric_code': 524,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.NZD: {
            'display_name': 'New Zealand Dollar',
            'numeric_code': 554,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.OMR: {
            'display_name': 'Rial Omani',
            'numeric_code': 512,
            'default_fraction_digits': 3,
            'sub_unit': 1000,
        },
        Currency.PAB: {
            'display_name': 'Balboa',
            'numeric_code': 590,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.PEN: {
            'display_name': 'Nuevo Sol',
            'numeric_code': 604,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.PGK: {
            'display_name': 'Kina',
            'numeric_code': 598,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.PHP: {
            'display_name': 'Philippine Peso',
            'numeric_code': 608,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.PKR: {
            'display_name': 'Pakistan Rupee',
            'numeric_code': 586,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.PLN: {
            'display_name': 'Zloty',
            'numeric_code': 985,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.PYG: {
            'display_name': 'Guarani',
            'numeric_code': 600,
            'default_fraction_digits': 0,
            'sub_unit': 100,
        },
        Currency.QAR: {
            'display_name': 'Qatari Rial',
            'numeric_code': 634,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.RON: {
            'display_name': 'New Romanian Leu',
            'numeric_code': 946,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.RSD: {
            'display_name': 'Serbian Dinar',
            'numeric_code': 941,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.RUB: {
            'display_name': 'Russian Ruble',
            'numeric_code': 643,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.RWF: {
            'display_name': 'Rwanda Franc',
            'numeric_code': 646,
            'default_fraction_digits': 0,
            'sub_unit': 100,
        },
        Currency.SAR: {
            'display_name': 'Saudi Riyal',
            'numeric_code': 682,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.SBD: {
            'display_name': 'Solomon Islands Dollar',
            'numeric_code': 90,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.SCR: {
            'display_name': 'Seychelles Rupee',
            'numeric_code': 690,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.SDG: {
            'display_name': 'Sudanese Pound',
            'numeric_code': 938,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.SEK: {
            'display_name': 'Swedish Krona',
            'numeric_code': 752,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.SGD: {
            'display_name': 'Singapore Dollar',
            'numeric_code': 702,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.SHP: {
            'display_name': 'Saint Helena Pound',
            'numeric_code': 654,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.SLL: {
            'display_name': 'Leone',
            'numeric_code': 694,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.SOS: {
            'display_name': 'Somali Shilling',
            'numeric_code': 706,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.SRD: {
            'display_name': 'Surinam Dollar',
            'numeric_code': 968,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.SSP: {
            'display_name': 'South Sudanese Pound',
            'numeric_code': 728,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.STD: {
            'display_name': 'Dobra',
            'numeric_code': 678,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.SVC: {
            'display_name': 'El Salvador Colon',
            'numeric_code': 222,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.SYP: {
            'display_name': 'Syrian Pound',
            'numeric_code': 760,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.SZL: {
            'display_name': 'Lilangeni',
            'numeric_code': 748,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.THB: {
            'display_name': 'Baht',
            'numeric_code': 764,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.TJS: {
            'display_name': 'Somoni',
            'numeric_code': 972,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.TMT: {
            'display_name': 'Turkmenistan New Manat',
            'numeric_code': 934,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.TND: {
            'display_name': 'Tunisian Dinar',
            'numeric_code': 788,
            'default_fraction_digits': 3,
            'sub_unit': 1000,
        },
        Currency.TOP: {
            'display_name': 'Pa’anga',
            'numeric_code': 776,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.TRY: {
            'display_name': 'Turkish Lira',
            'numeric_code': 949,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.TTD: {
            'display_name': 'Trinidad and Tobago Dollar',
            'numeric_code': 780,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.TWD: {
            'display_name': 'New Taiwan Dollar',
            'numeric_code': 901,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.TZS: {
            'display_name': 'Tanzanian Shilling',
            'numeric_code': 834,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.UAH: {
            'display_name': 'Hryvnia',
            'numeric_code': 980,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.UGX: {
            'display_name': 'Uganda Shilling',
            'numeric_code': 800,
            'default_fraction_digits': 0,
            'sub_unit': 100,
        },
        Currency.USD: {
            'display_name': 'US Dollar',
            'numeric_code': 840,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.USN: {
            'display_name': 'US Dollar (Next day)',
            'numeric_code': 997,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.USS: {
            'display_name': 'US Dollar (Same day)',
            'numeric_code': 998,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.UYI: {
            'display_name': 'Uruguay Peso en Unidades Indexadas (URUIURUI)',
            'numeric_code': 940,
            'default_fraction_digits': 0,
            'sub_unit': 100,
        },
        Currency.UYU: {
            'display_name': 'Peso Uruguayo',
            'numeric_code': 858,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.UZS: {
            'display_name': 'Uzbekistan Sum',
            'numeric_code': 860,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.VEF: {
            'display_name': 'Bolivar',
            'numeric_code': 937,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.VND: {
            'display_name': 'Dong',
            'numeric_code': 704,
            'default_fraction_digits': 0,
            'sub_unit': 10,
        },
        Currency.VUV: {
            'display_name': 'Vatu',
            'numeric_code': 548,
            'default_fraction_digits': 0,
            'sub_unit': 1,
        },
        Currency.WST: {
            'display_name': 'Tala',
            'numeric_code': 882,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.XAF: {
            'display_name': 'CFA Franc BEAC',
            'numeric_code': 950,
            'default_fraction_digits': 0,
            'sub_unit': 100,
        },
        Currency.XAG: {
            'display_name': 'Silver',
            'numeric_code': 961,
            'default_fraction_digits': 0,
            'sub_unit': 100,
        },
        Currency.XAU: {
            'display_name': 'Gold',
            'numeric_code': 959,
            'default_fraction_digits': 0,
            'sub_unit': 100,
        },
        Currency.XBA: {
            'display_name': 'Bond Markets Unit European Composite Unit (EURCO)',
            'numeric_code': 955,
            'default_fraction_digits': 0,
            'sub_unit': 100,
        },
        Currency.XBB: {
            'display_name': 'Bond Markets Unit European Monetary Unit (E.M.U.-6)',
            'numeric_code': 956,
            'default_fraction_digits': 0,
            'sub_unit': 100,
        },
        Currency.XBC: {
            'display_name': 'Bond Markets Unit European Unit of Account 9 (E.U.A.-9)',
            'numeric_code': 957,
            'default_fraction_digits': 0,
            'sub_unit': 100,
        },
        Currency.XBD: {
            'display_name': 'Bond Markets Unit European Unit of Account 17 (E.U.A.-17)',
            'numeric_code': 958,
            'default_fraction_digits': 0,
            'sub_unit': 100,
        },
        Currency.XCD: {
            'display_name': 'East Caribbean Dollar',
            'numeric_code': 951,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.XDR: {
            'display_name': 'SDR (Special Drawing Right)',
            'numeric_code': 960,
            'default_fraction_digits': 0,
            'sub_unit': 100,
        },
        Currency.XFU: {
            'display_name': 'UIC-Franc',
            'numeric_code': 958,
            'default_fraction_digits': 0,
            'sub_unit': 100,
        },
        Currency.XOF: {
            'display_name': 'CFA Franc BCEAO',
            'numeric_code': 952,
            'default_fraction_digits': 0,
            'sub_unit': 100,
        },
        Currency.XPD: {
            'display_name': 'Palladium',
            'numeric_code': 964,
            'default_fraction_digits': 0,
            'sub_unit': 100,
        },
        Currency.XPF: {
            'display_name': 'CFP Franc',
            'numeric_code': 953,
            'default_fraction_digits': 0,
            'sub_unit': 100,
        },
        Currency.XPT: {
            'display_name': 'Platinum',
            'numeric_code': 962,
            'default_fraction_digits': 0,
            'sub_unit': 100,
        },
        Currency.XSU: {
            'display_name': 'Sucre',
            'numeric_code': 994,
            'default_fraction_digits': 0,
            'sub_unit': 100,
        },
        Currency.XTS: {
            'display_name': 'Codes specifically reserved for testing purposes',
            'numeric_code': 963,
            'default_fraction_digits': 0,
            'sub_unit': 100,
        },
        Currency.XUA: {
            'display_name': 'ADB Unit of Account',
            'numeric_code': 965,
            'default_fraction_digits': 0,
            'sub_unit': 100,
        },
        Currency.YER: {
            'display_name': 'Yemeni Rial',
            'numeric_code': 886,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.ZAR: {
            'display_name': 'Rand',
            'numeric_code': 710,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.ZMW: {
            'display_name': 'Zambian Kwacha',
            'numeric_code': 967,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        },
        Currency.ZWL: {
            'display_name': 'Zimbabwe Dollar',
            'numeric_code': 932,
            'default_fraction_digits': 2,
            'sub_unit': 100,
        }
    }
    """Data about currencies.

    Taken from https://github.com/sebastianbergmann/money

    """

    @classmethod
    def decimal_precision_for_currency(cls, currency: Currency) -> int:
        """Returns the decimal precision for a currency (number of digits after the decimal)"""

        return cls._CURRENCY_DATA[currency]['default_fraction_digits']

    @classmethod
    def sub_unit_for_currency(cls, currency: Currency) -> int:
        """Returns the sub unit for a currency.
        (eg, the subunit for USD is 100 because there are 100 cents in a dollar)

        """
        return cls._CURRENCY_DATA[currency]['sub_unit']
