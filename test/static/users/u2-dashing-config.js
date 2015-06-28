var dashboard = new Dashboard();

dashboard.addWidget('current_valuation_widget', 'Number', {
	getData: function () {
	    var self = this;
	    $.extend(this.scope, {
		    title: 'Users\' Sensors',
			updatedAt: 'Last updated at 14:10',
			value: '78',
			detail: "Humidity",
			});
	},
	interval:5000
    });

