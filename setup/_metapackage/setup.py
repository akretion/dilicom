import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo-addons-akretion-dilicom",
    description="Meta package for akretion-dilicom Odoo addons",
    version=version,
    install_requires=[
        'odoo-addon-product_chasse_aux_livres>=16.0dev,<16.1dev',
        'odoo-addon-purchase_chasse_aux_livres>=16.0dev,<16.1dev',
        'odoo-addon-purchase_dilicom_csv>=16.0dev,<16.1dev',
        'odoo-addon-purchase_interforum_xlsx>=16.0dev,<16.1dev',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 16.0',
    ]
)
