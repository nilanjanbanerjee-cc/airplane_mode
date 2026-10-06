// Copyright (c) 2026, Nilanjan Banerjee and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Airplane Ticket", {
// 	refresh(frm) {

// 	},
// });
// Copyright (c) 2026, Nilanjan Banerjee and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Airplane", {
// 	refresh(frm) {

// 	},
// });
frappe.ui.form.on("Airplane Ticket", {
    status(frm) {
        set_seat_read_only(frm);
    },

    refresh(frm) {
        frm.add_custom_button(__("Assign Seat"), () => {
            let d = new frappe.ui.Dialog({
                title: __("Select Seat"),
                fields: [
                    {
                        label: __("Seat Number"),
                        fieldname: "seat_number",
                        fieldtype: "Data",
                        reqd: 1,
                        default: frm.doc.seat
                    }
                ],
                primary_action_label: __("Set"),
                primary_action(values) {
                    frm.set_value("seat", values.seat_number);
                    d.hide();
                }
            });
            d.show();
        });
    }
});
function set_seat_read_only(frm) {
    if (frm.doc.status === "Boarded") {
        console.log("Setting seat field to read-only because status is 'Boarded'");
        frm.set_df_property("seat", "read_only", 1);
    } else {
        frm.set_df_property("seat", "read_only", 0);
    }
}
       