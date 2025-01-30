import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo10-addons-akretion-dilicom",
    description="Meta package for akretion-dilicom Odoo addons",
    version=version,
    install_requires=[
        'odoo10-addon-purchase_dilicom_csv',
        'odoo10-addon-purchase_interforum_xlsx',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 10.0',
    ]
)
