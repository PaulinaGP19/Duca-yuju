# -*- coding: utf-8 -*-
{
    'name': "Yuju",

    'summary': """
        Integration with Yuju's platform""",

    'description': """
        Module integration with Yuju's software platform.
        - Create orders into your odoo software from marketplaces like Mercado Libre, Amazon, etc..
        - Create products from Yuju platform into odoo
        - Update your stock from odoo to your Yuju account.
    """,

    'author': "Israel Calderón Aguilar, Gerardo A Lopez Vega",
    'website': "https://yuju.io/",
    'category': 'Sales',
    'version': '0.3.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'sale_management',
        'stock',
        'component_event'
    ],
    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        # 'views/templates.xml',
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

# Version 0.2.0
# *** Agrega parametros a la configuracion para poder customizar el flujo de dropship
#       - Define una ruta default
#       - Define una ruta para cuando es dropship
#       - Define una ruta para cuando es MTO
#       - Agrega un campo en el producto para indicar si se procesara como dropship o MTO

# Version 0.2.1
# *** Envia proveedor al activar producto

# Version 0.2.2
# *** Actualizar nombre cliente venta configuracion

# Version 0.2.3
# *** Actualizacion de metodo deliver, corrige problemas de duplicados debido a que tenia conflicto 
# al definir reglas de almacen que generan mas de 1 movimiento al confirmar la venta

# Version 0.2.4
# *** Estatus venta se deja como draft (default) debido a que genera conflictos con movimientos 
# de productos configurados como Kits y Reglas de Inventario.

# Version 0.2.5
# *** Modifica metodo get_data_with_variations, valores id, default_code se dejan de tomar de la 
# variante ligada al producto

# Version 0.2.6
# *** Actualiza las vistas y agrega descripcion a modelos para evitar warnings en la instalacion debido 
# a problemas de deprecacion

# Version 0.2.7
# *** Actualiza campos misma descripcion Marketplace Fee

# Version 0.3.0
# *** Mapeo de campos custom Odoo - Yuju

# Version 0.3.1
# *** Agrega validacion para buscar rfc cliente antes de crearlo.
