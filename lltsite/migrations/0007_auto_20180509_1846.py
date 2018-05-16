# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-05-09 18:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lltsite', '0006_auto_20170810_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriber',
            name='country',
            field=models.CharField(choices=[(b'', b'-- Select Country --'), (b'USA', b'United States of America'), (b'CAN', b'Canada'), (b'AFG', b'Afghanistan'), (b'ALB', b'Albania'), (b'DZA', b'Algeria'), (b'ASM', b'American Samoa'), (b'AND', b'Andorra'), (b'AGO', b'Angola'), (b'AIA', b'Anguilla'), (b'ATA', b'Antarctica'), (b'ATG', b'Antigua and Barbuda'), (b'ARG', b'Argentina'), (b'ARM', b'Armenia'), (b'ABW', b'Aruba'), (b'AUS', b'Australia'), (b'AUT', b'Austria'), (b'AZE', b'Azerbaijan'), (b'BHS', b'Bahamas'), (b'BHR', b'Bahrain'), (b'BGD', b'Bangladesh'), (b'BRB', b'Barbados'), (b'BLR', b'Belarus'), (b'BEL', b'Belgium'), (b'BLZ', b'Belize'), (b'BEN', b'Benin'), (b'BMU', b'Bermuda'), (b'BTN', b'Bhutan'), (b'BOL', b'Bolivia'), (b'BIH', b'Bosnia and Herzegowina'), (b'BWA', b'Botswana'), (b'BVT', b'Bouvet Island'), (b'BRA', b'Brazil'), (b'IOT', b'British Indian Ocean Territory'), (b'BRN', b'Brunei Darussalam'), (b'BGR', b'Bulgaria'), (b'BFA', b'Burkina Faso'), (b'BDI', b'Burundi'), (b'KHM', b'Cambodia'), (b'CMR', b'Cameroon'), (b'CPV', b'Cape Verde'), (b'CYM', b'Cayman Islands'), (b'CAF', b'Central African Republic'), (b'TCD', b'Chad'), (b'CHL', b'Chile'), (b'CHN', b'China'), (b'CXR', b'Christmas Island'), (b'CCK', b'Cocoa (Keeling) Islands'), (b'COL', b'Colombia'), (b'COM', b'Comoros'), (b'COG', b'Congo'), (b'COK', b'Cook Islands'), (b'CRI', b'Costa Rica'), (b'CIV', b'Cote Divoire'), (b'HRV', b'Croatia (local name: Hrvatska)'), (b'CUB', b'Cuba'), (b'CYP', b'Cyprus'), (b'CZE', b'Czech Republic'), (b'DNK', b'Denmark'), (b'DJI', b'Djibouti'), (b'DMA', b'Dominica'), (b'DOM', b'Dominican Republic'), (b'TMP', b'East Timor'), (b'ECU', b'Ecuador'), (b'EGY', b'Egypt'), (b'SLV', b'El Salvador'), (b'GNQ', b'Equatorial Guinea'), (b'ERI', b'Eritrea'), (b'EST', b'Estonia'), (b'ETH', b'Ethiopia'), (b'FLK', b'Falkland Islands (Malvinas)'), (b'FRO', b'Faroe Islands'), (b'FJI', b'Fiji'), (b'FIN', b'Finland'), (b'FRA', b'France'), (b'FXX', b'France, Metropolitan'), (b'GUF', b'French Guiana'), (b'PYF', b'French Polynesia'), (b'ATF', b'French Southern Territories'), (b'GAB', b'Gabon'), (b'GMB', b'Gambia'), (b'GEO', b'Georgia'), (b'DEU', b'Germany'), (b'GHA', b'Ghana'), (b'GIB', b'Gibraltar'), (b'GRC', b'Greece'), (b'GRL', b'Greenland'), (b'GRD', b'Grenada'), (b'GLP', b'Guadeloupe'), (b'GUM', b'Guam'), (b'GTM', b'Guatemala'), (b'GIN', b'Guinea'), (b'GNB', b'Guinea-Bissau'), (b'GUY', b'Guyana'), (b'HTI', b'Haiti'), (b'HMD', b'Heard and Mc Donald Islands'), (b'HND', b'Honduras'), (b'HKG', b'Hong Kong'), (b'HUN', b'Hungary'), (b'ISL', b'Iceland'), (b'IND', b'India'), (b'IDN', b'Indonesia'), (b'IRN', b'Iran (Islamic Republic of)'), (b'IRQ', b'Iraq'), (b'IRL', b'Ireland'), (b'ISR', b'Israel'), (b'ITA', b'Italy'), (b'JAM', b'Jamaica'), (b'JPN', b'Japan'), (b'JOR', b'Jordan'), (b'KAZ', b'Kazakhstan'), (b'KEN', b'Kenya'), (b'KIR', b'Kiribati'), (b'PRK', b'Korea, Democratic Peoples Republic of'), (b'KOR', b'Korea, Republic of'), (b'KWT', b'Kuwait'), (b'KGZ', b'Kyrgyzstan'), (b'LAO', b'Lao Peoples Democratic Republic'), (b'LVA', b'Latvia'), (b'LBN', b'Lebanon'), (b'LSO', b'Lesotho'), (b'LBR', b'Liberia'), (b'LBY', b'Libyan Arab Jamahiriya'), (b'LIE', b'Liechtenstein'), (b'LTU', b'Lithuania'), (b'LUX', b'Luxembourg'), (b'MAC', b'Macau'), (b'MKD', b'Macedonia, The Former Yugoslav Republic of'), (b'MDG', b'Madagascar'), (b'MWI', b'Malawi'), (b'MYS', b'Malaysia'), (b'MDV', b'Maldives'), (b'MLI', b'Mali'), (b'MLT', b'Malta'), (b'MHL', b'Marshall Islands'), (b'MTQ', b'Martinique'), (b'MRT', b'Mauritania'), (b'MVS', b'Mauritius'), (b'MYT', b'Mayotte'), (b'MEX', b'Mexico'), (b'FSM', b'Micronesia, Federated States of'), (b'MDA', b'Moldova, Republic of'), (b'MCO', b'Monaco'), (b'MNG', b'Mongolia'), (b'MSR', b'Montserrat'), (b'MAR', b'Morocco'), (b'MOZ', b'Mozambique'), (b'MMR', b'Myanmar'), (b'NAM', b'Namibia'), (b'NRU', b'Nauru'), (b'NPL', b'Nepal'), (b'NLD', b'Netherlands'), (b'ANT', b'Netherlands Antilles'), (b'NCL', b'New Caledonia'), (b'NZL', b'New Zealand'), (b'NIC', b'Nicaragua'), (b'NER', b'Niger'), (b'NGA', b'Nigeria'), (b'NIU', b'Niue'), (b'NFK', b'Norfolk Island'), (b'MNP', b'Northern Mariana Islands'), (b'MOR', b'Norway'), (b'OMN', b'Oman'), (b'PAK', b'Pakistan'), (b'PLW', b'Palau'), (b'PAN', b'Panama'), (b'PNG', b'Papua New Guinea'), (b'PRY', b'Paraguay'), (b'PER', b'Peru'), (b'PHL', b'Philippines'), (b'PCN', b'Pitcairn'), (b'POL', b'Poland'), (b'PRT', b'Portugal'), (b'PRI', b'Puerto Rico'), (b'QAT', b'Qatar'), (b'REU', b'Reunion'), (b'ROM', b'Romania'), (b'RUS', b'Russian Federation'), (b'RWA', b'Rwanda'), (b'KNA', b'Saint Kitts and Nevis'), (b'LCA', b'Saint Lucia'), (b'VCT', b'Saint Vincent and the Grenadines'), (b'WSM', b'Samoa'), (b'SMR', b'San Marino'), (b'STP', b'Sao Tome and Principe'), (b'SAU', b'Saudi Arabia'), (b'SEN', b'Senegal'), (b'SYC', b'Seychelles'), (b'SLE', b'Sierra Leone'), (b'SGP', b'Singapore'), (b'SVK', b'Slovakia (Slovak Republic)'), (b'SVN', b'Slovenia'), (b'SLB', b'Solomon Islands'), (b'SOM', b'Somalia'), (b'ZAF', b'South Africa'), (b'SGS', b'South Georgia and the South Sandwich Islands'), (b'ESP', b'Spain'), (b'LKA', b'Sri Lanka'), (b'SHN', b'St. Helena'), (b'SPM', b'St. Pierre and Miquelon'), (b'SDN', b'Sudan'), (b'SUR', b'Suriname'), (b'SJM', b'Svalbard and Jan Mayen Islands'), (b'SWZ', b'Swaziland'), (b'SWE', b'Sweden'), (b'CHE', b'Switzerland'), (b'SYR', b'Syrian Arab Republic'), (b'TWN', b'Taiwan'), (b'TJK', b'Tajikistan'), (b'TZA', b'Tanzania, United Republic of'), (b'THA', b'Thailand'), (b'TGO', b'Togo'), (b'TKL', b'Tokelau'), (b'TON', b'Tonga'), (b'TTO', b'Trinidad and Tobago'), (b'TUN', b'Tunisia'), (b'TUR', b'Turkey'), (b'TKM', b'Turkmenistan'), (b'TCA', b'Turks and Caicos Islands'), (b'TUV', b'Tuvalu'), (b'UGA', b'Uganda'), (b'UKR', b'Ukraine'), (b'ARE', b'United Arab Emirates'), (b'GBR', b'United Kingdom'), (b'UMI', b'United States Minor Outlying Islands'), (b'UNK', b'Unknown Country'), (b'URY', b'Uruguay'), (b'UZB', b'Uzbekistan'), (b'VUT', b'Vanuatu'), (b'VAT', b'Vatican City State (Holy See)'), (b'VEN', b'Venezuela'), (b'VNM', b'Viet Nam'), (b'VGB', b'Virgin Islands (British)'), (b'VIR', b'Virgin Islands (U.S.)'), (b'WLF', b'Wallisw and Futuna Islands'), (b'ESH', b'Western Sahara'), (b'YEM', b'Yeman'), (b'YUG', b'Yugoslavia'), (b'ZAR', b'Zaire'), (b'ZMB', b'Zambia'), (b'ZWE', b'Zimbabwe')], max_length=254),
        ),
    ]
