// Copyright (c) 2016, SBK and contributors
// For license information, please see license.txt

frappe.ui.form.on('Book', {
	refresh: function(frm) {
		//
		//
		//
		//
	},
	onload: function(frm){
		//code for onload
		var next_7day = frappe.datetime.add_days(get_today(),7)
		cur_frm.set_value("publishing_date",next_7day)
		// msgprint("hello");
	}

});
