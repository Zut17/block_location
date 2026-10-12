{
    'name': 'Block Location',
    'version': '15.0.1.0.0',
    'summary': "Restreint la modification des emplacements de stock",
    'category': 'Inventory',
    'depends': ['stock'],
    'data': [
        'security/security_groups.xml',
        'security/ir_rule.xml',
    ],
    'installable': True,
    'application': False,
    'post_init_hook': '_assign_block_group_to_existing_users',
}