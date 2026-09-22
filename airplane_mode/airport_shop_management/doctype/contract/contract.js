// Copyright (c) 2026, Nilanjan Banerjee and contributors
// For license information, please see license.txt

frappe.ui.form.on("Contract", {
    onload(frm) {
        if (frm.is_new() && !frm.doc.monthly_rent) {
            frappe.db.get_single_value(
                "Airport Shop Settings",
                "default_rent_amount"
            ).then(value => {
                if (value) {
                    frm.set_value("monthly_rent", value);
                }
            });
        }
    }
});
