{
    'name': "hr_hospital",
    'summary': "Module for odoo-course",
    'license': 'LGPL-3',
    'author': "Dicantnik",
    'website': "https://example.com",
    'category': 'Uncategorized',
    'version': '17.0.1.0.0',
    'depends': [],
    'external_dependencies': {'python': ['dateutil'], },
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/hr_hospital_menus.xml',
        'views/hospital_doctor_views.xml',
        'views/hospital_illness_views.xml',
        'views/hospital_patient_views.xml',
        'views/hospital_visit_patient_views.xml',
        'views/hospital_diagnosis_views.xml',
        'wizard/hospital_override_doctor_views.xml',
        'wizard/hospital_list_diagnosis_views.xml',
        'data/hospital_illness_data.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/hospital_doctor_demo.xml',
        'demo/hospital_patient_demo.xml',
        'demo/hospital_illness_demo.xml',
    ],
    'images': [],
    'live_test_url': 'https://demo.example.com',
    'price': 0.0,
    'currency': 'EUR',
    'support': 'support@example.com',
    'application': False,
    'installable': True,
    'auto_install': False,

}
