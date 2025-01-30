import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo14-addons-akretion-dilicom",
    description="Meta package for akretion-dilicom Odoo addons",
    version=version,
    install_requires=[
        'odoo14-addon-product_chasse_aux_livres',
        'odoo14-addon-purchase_chasse_aux_livres',
        'odoo14-addon-purchase_dilicom_csv',
        'odoo14-addon-purchase_interforum_xlsx',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 14.0',
    ]
)
