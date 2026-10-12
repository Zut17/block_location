def _assign_block_group_to_existing_users(cr, registry):
    """Coche la case 'Bloquer la modification des emplacements de stock'
    pour tous les utilisateurs internes existants au moment de l'installation."""
    from odoo import api, SUPERUSER_ID
    env = api.Environment(cr, SUPERUSER_ID, {})
    group = env.ref('block_location.group_stock_location_editor')
    internal_users = env['res.users'].search([('share', '=', False)])
    group.write({'users': [(4, u.id) for u in internal_users]})
