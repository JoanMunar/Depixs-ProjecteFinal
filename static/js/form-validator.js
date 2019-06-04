//------------------FORM VALIDATOR----------------------------
function isValidEmailAddress(emailAddress) {
    var pattern = /^([a-z\d!#$%&'*+\-\/=?^_`{|}~\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]+(\.[a-z\d!#$%&'*+\-\/=?^_`{|}~\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]+)*|"((([ \t]*\r\n)?[ \t]+)?([\x01-\x08\x0b\x0c\x0e-\x1f\x7f\x21\x23-\x5b\x5d-\x7e\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]|\\[\x01-\x09\x0b\x0c\x0d-\x7f\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]))*(([ \t]*\r\n)?[ \t]+)?")@(([a-z\d\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]|[a-z\d\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF][a-z\d\-._~\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]*[a-z\d\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])\.)+([a-z\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]|[a-z\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF][a-z\d\-._~\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]*[a-z\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])\.?$/i;
    return pattern.test(emailAddress);
}

function isValidImport(moneyImport) {
    var pattern = /^[0-9]*\.[0-9]{2}$/i
    return pattern.test(moneyImport);
}

function isValidPhone(phone, digits) {
    var pattern = /^\d{9}$/;
    return pattern.test(phone);
}

function isValidUrl(url) {
    return /^(https?|s?ftp):\/\/(((([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(%[\da-f]{2})|[!\$&'\(\)\*\+,;=]|:)*@)?(((\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])\.(\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])\.(\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])\.(\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5]))|((([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.)+(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.?)(:\d*)?)(\/((([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(%[\da-f]{2})|[!\$&'\(\)\*\+,;=]|:|@)+(\/(([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(%[\da-f]{2})|[!\$&'\(\)\*\+,;=]|:|@)*)*)?)?(\?((([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(%[\da-f]{2})|[!\$&'\(\)\*\+,;=]|:|@)|[\uE000-\uF8FF]|\/|\?)*)?(#((([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(%[\da-f]{2})|[!\$&'\(\)\*\+,;=]|:|@)|\/|\?)*)?$/i.test(url);
}

function correct_field(input){
    // $(input).css('border-color', '');
    // $(input).css('border-color', '#e4e4e4');
    $(input).removeClass('border-color-3');
    $(input).closest('div').find('.text-danger').remove();
}

function wrong_field(input, msg){
    $(input).closest('div').find('.text-danger').remove();
    // $(input).css('border', '1px solid #ea7066');
    $(input).addClass('border-color-3');
    $(input).closest('div').append('<p class="text-danger">'+msg+'</p>')
}

function correct_field_2(input){
    $(input).closest('label').css('border-color', '#ccc');
}

function wrong_field_2(input, msg){
    $(input).closest('div').css('border', '1px solid #ea7066');
    $(input).closest('div').css('border-radius', '5px');
    $(input).closest('div').css('padding', '5px');
    $(input).closest('div').append('<p class="text-danger" style="padding-top: 15px;">'+msg+'</p>')

}


var required_field_msg = 'Este campo es obligatorio';
var wrong_email_format = 'Formato de email incorrecto. Ej: info@caloolu.com';
var wrong_import_format = 'Formato de número incorrecto. Ej: 20,00';
var wrong_password_validation = 'Las contraseñas deben coincidir';
var wrong_url_format = 'El formato es incorrecto. Ej: http://www.yoomedoo.com/';
var wrong_phone_format = 'El teléfono es incorrecto. Se requieren 9 digitos';
var submit = true;


$('form.validate').submit(function () {
    submit = true;

    $(this).find('input').each(function(){
        var type = $(this).attr('type');
        var value = $(this).val();

        if ($(this).hasClass('required')){

            if (type == 'text'){
                if (value == null || value.length == 0){
                    wrong_field(this, required_field_msg);
                    submit = false;
                }else{
                    correct_field(this);
                }
            }

            if (type == 'tel'){
                if (value == null || value.length == 0){
                    wrong_field(this, required_field_msg);
                    submit = false;
                }else{
                    var digits = $(this).attr('data-digits');
                    if(!isValidPhone($(this).val(), digits)){
                        wrong_field(this, wrong_phone_format);
                        submit = false;
                    }else{
                        correct_field(this);
                    }
                }
            }

            if (type == 'radio'){
                var group_name = $(this).attr('name');
                var okey = false;
                var radio_buttons = $(form).find('input[name=' + group_name + ']');
                for (var i = 0; i < radio_buttons.length; i++) {
                    if (radio_buttons[i].checked) {
                        okey = true;
                        break;
                    }
                }
                if (okey){
                    correct_field(this);
                }else{
                    wrong_field(this, required_field_msg);
                    submit = false;
                }
            }

            if (type == 'checkbox'){
                if($(this).hasClass('group-required')) {
                    var parent = $(this).closest('.div-group-required');
                    var labels = parent.find("label.active");
                    var nLabels = labels.length;
                    if (nLabels > 0) {
                        parent.find('.group-required-msg').hide();
                        for (var n = 0; n <= nLabels; n++) {
                            correct_field_2(labels[n]);
                        }
                    } else {
                        parent.find('.group-required-msg').show();
                        wrong_field_2(parent.find('label'));
                        submit = false;
                    }
                }else {
                    if(!$(this).hasClass('free')) {
                        if($(this).is(':checked')) {
                            correct_field_2(this);
                        }else{
                            wrong_field_2(this, required_field_msg);
                            submit = false;
                        }
                    }
                }
            }

            if (type == 'email'){
                if( value == null || value.length == 0){
                    wrong_field(this, required_field_msg);
                    submit = false;
                }else{
                    if(!isValidEmailAddress($(this).val())){
                        wrong_field(this, wrong_email_format);
                        submit = false;
                    }else{
                        correct_field(this);
                    }
                }
            }

            if (type == 'url'){
                if(value == null || value.length == 0){
                    wrong_field(this, required_field_msg);
                    submit = false;
                }else{
                    if(isValidUrl($(this).val())) {
                        correct_field(this);
                    }else{
                        wrong_field(this, wrong_url_format);
                        submit = false;
                    }
                }
            }


            if (type == 'password'){
                if (value == null || value.length == 0){
                    wrong_field(this, required_field_msg);
                    submit = false;
                }else{
                    if($(this).hasClass('duplicate-password')){
                        var repeat_password = $($(this).data('duplicate_password')).val();
                        if (value != repeat_password){
                            wrong_field(this, wrong_password_validation);
                            wrong_field($($(this).data('duplicate_password')), wrong_password_validation);
                            submit = false;
                        }else{
                            correct_field(this);
                            correct_field($($(this).data('duplicate_password')));
                        }
                    }else{
                        correct_field(this);
                    }
                }
            }

            if (type == 'number'){
                if(value == null || value.length == 0){
                    wrong_field(this, required_field_msg);
                    submit = false;
                }else{
                    if($(this).hasClass('import')) {
                        if (!isValidImport($(this).val())) {
                            wrong_field(this, wrong_import_format);
                            submit = false;
                        } else {
                            correct_field(this);
                        }
                    }else{
                        correct_field(this);
                    }
                }
            }

            if (type == 'date'){
                if (value == null || value.length == 0){
                    wrong_field(this, required_field_msg);
                    submit = false;
                }else{
                    correct_field(this);
                }
            }

        }

        if (!($(this).hasClass('required')) && $(this).hasClass('validate')){
            if (type == 'tel'){
                if (value.length > 0){
                    var digits = $(this).attr('data-digits');
                    if(!isValidPhone($(this).val(), digits)){
                        wrong_field(this, wrong_phone_format);
                        submit = false;
                    }else{
                        correct_field(this);
                    }
                }else{
                    correct_field(this);
                }
            }
        }

    });

    $(this).find('textarea').each(function(){

        if ($(this).hasClass('required')){
            var value = $(this).val();
            if (value == null || value.length == 0) {
                wrong_field(this, required_field_msg);
                submit = false;
            }else{
                correct_field(this);
            }
        }
    });

    $(this).find('select').each(function(){

        if ($(this).hasClass('required')){
            var value = $(this).val();

            if (value == 'none' || !value){
                wrong_field(this, required_field_msg);
                submit = false;
            }else{
                correct_field(this);
            }
        }
    });


    console.log(submit);

    return submit;


});