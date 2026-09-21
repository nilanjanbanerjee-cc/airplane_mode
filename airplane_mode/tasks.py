import frappe


def send_rent_due_reminders():
    settings = frappe.get_single("Airport Shop Settings")

    if not settings.enable_rent_reminders:
        return

    contracts = frappe.get_all(
        "Contract",
        filters={
            "status": "Active"
        },
        fields=[
            "name",
            "shop",
            "tenant",
            "monthly_rent"
        ]
    )

    for contract in contracts:
        tenant = frappe.get_doc("Tenant", contract.tenant)

        if not tenant.contact_email:
            continue

        frappe.sendmail(
            recipients=[tenant.contact_email],
            subject=f"Rent Due Reminder - {contract.shop}",
            message=f"""
                <p>Dear {tenant.tenant_name},</p>

                <p>This is a reminder that the monthly rent of
                <strong>₹{contract.monthly_rent}</strong>
                is due for shop <strong>{contract.shop}</strong>.</p>

                <p>Thank you.</p>
            """
        )