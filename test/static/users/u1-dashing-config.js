

var dashboard = new Dashboard();

dashboard.addWidget('clock_widget', 'Clock');

dashboard.addWidget('custom_number_widget', 'Number', {
	getData: function () { 
	    var self = this;
	$.get('widgets/custom_number_widget/u1/p1/s1', function(data) { 
		$.extend(self.data, data); 
	    });
	},
    interval:5000
	    });

