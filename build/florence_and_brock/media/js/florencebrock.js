/*
*	Florence & Brock
*	Utility functions for florenceandbrock.com
*	
*	Requires jQuery library (http://www.jquery.com), 
*	jQuery Class plug-in
*	
*	Taylan Pince (taylanpince at gmail dot com) - October 25, 2008
*/

$.extend($.namespace("FlorenceBrock"), {
    
    media_path : "",
    
    init_markers : function() {
		$("html").addClass("has-js");
		
		$("li:last-child").addClass("last-child");
		$("li:first-child").addClass("first-child");
        
		$("input[@type=text]").addClass("text");
		$("input[@type=submit], input[@type=button]").addClass("submit");
		$("input[@type=password]").addClass("text");
		$("input[@type=file]").addClass("file");
		$("input[@type=radio]").addClass("radio");
		$("input[@type=checkbox]").addClass("checkbox");
		$("input[@type=image]").addClass("image");
        
		$("hr").wrap('<div class="hr"></div>');
	},
    
    init : function() {
        this.init_markers();
    }
    
});


$(function() {
    FlorenceBrock.init();
});