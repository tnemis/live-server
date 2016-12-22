function myFunction() {
	var community = new Array('BC-Others ','BC-Muslim ','MBC ','ST ','SC-Others ','SC-Arunthathiyar ')
    var community_id =  new Array('1','2','3','4','5','6')

for (i = 0; i < community.length; i++) {
                createOption(sel1, community[i], community_id[i]);
            }

}



function createOption(sel, text, value) {
        var opt = document.createElement('option');
        opt.value = value;
        opt.text = text;
        sel.options.add(opt);
    }