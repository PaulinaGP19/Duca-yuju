# -*- coding: utf-8 -*-
{
    'name': "Yuju Multi Images Product",

    'summary': """
        Integration with Yuju's platform, handle multiple images per product""",

    'description': """
        Module integration with Yuju's software platform.
        - Create and Update Products with multiple images.
    """,

    'author': "Gerardo A Lopez Vega",
    'website': "https://yuju.io/",
    'category': 'Sales',
    'version': '0.0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'website_sale',
        'madkting'
    ],
    # always loaded
    'data': [
        # 'views/views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
    "cloc_exclude": [
        # "lib/common.py", # exclude a single file
        # "data/*.xml",    # exclude all XML files in a specific folder
        "controllers/**/*",  # exclude all files in a folder hierarchy recursively
        "log/**/*",  # exclude all files in a folder hierarchy recursively
        "models/**/*",  # exclude all files in a folder hierarchy recursively
        "notifier/**/*",  # exclude all files in a folder hierarchy recursively
        "requirements/**/*",  # exclude all files in a folder hierarchy recursively
        "responses/**/*",  # exclude all files in a folder hierarchy recursively
        "security/**/*",  # exclude all files in a folder hierarchy recursively
        "views/**/*",  # exclude all files in a folder hierarchy recursively
    ]
}