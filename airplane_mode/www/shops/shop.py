import frappe

def get_context(context):
    shop_name = frappe.form_dict.name
    context.shop = frappe.get_doc("Shop", shop_name)
    return context