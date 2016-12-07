function OnLoad() {                
    var options = {
        sourceLanguage:
        google.elements.transliteration.LanguageCode.ENGLISH,
        destinationLanguage:
        [google.elements.transliteration.LanguageCode.TAMIL],
        shortcutKey: 'ctrl+g',
        transliterationEnabled: true
    };

    var control = new google.elements.transliteration.TransliterationControl(options);
    control.makeTransliteratable(["transliterateTextarea"]);
    var keyVal = 32; // Space key
    $("#name").on('keydown', function(event) {
        if(event.keyCode === 32) {
            var engText = $("#name").val() + " ";
            var engTextArray = engText.split(" ");
            $("#transliterateTextarea").val($("#transliterateTextarea").val() + engTextArray[engTextArray.length-2]);

            document.getElementById("transliterateTextarea").focus();
            $("#transliterateTextarea").trigger ( {
                type: 'keypress', keyCode: keyVal, which: keyVal, charCode: keyVal
            } );
        }
    });

    $("#transliterateTextarea").bind ("keyup",  function (event) {
        setTimeout(function(){ $("#name").val($("#name").val() + " "); document.getElementById("name").focus()},0);
    });
} //end onLoad function

google.setOnLoadCallback(OnLoad);

