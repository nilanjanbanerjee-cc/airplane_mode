// Copyright (c) 2026, Nilanjan Banerjee and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Shop", {
// 	refresh(frm) {

// 	},
// });
frappe.ui.form.on("Shop", {
    setup(frm) {
        frm.set_query("shop_type", () => {
            return {
                filters: {
                    enabled: 1
                }
            };
        });
    }
});