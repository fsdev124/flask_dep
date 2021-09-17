var textAreas = document.getElementsByTagName('textarea');

Array.prototype.forEach.call(textAreas, function(elem) {
    elem.placeholder = elem.placeholder.replace(/\\n/g, '\n');
});

$(document).ready(function () {
    $('#btn_enroll').click(function () {
        all_values = true;
        $('#dep_ship_to').removeClass('warning');
        $('#dep_reseller_id').removeClass('warning');
        $('#dep_uat_cert').removeClass('warning');
        $('#dep_uat_private_key').removeClass('warning');
        $('#customer_id').removeClass('warning');
        $('#devices').removeClass('warning');
        $('#ship_date').removeClass('warning');

        if ($('#dep_ship_to').val() == '') { $('#dep_ship_to').addClass('warning'); all_values=false; }
        if ($('#dep_reseller_id').val() == '') { $('#dep_reseller_id').addClass('warning'); all_values=false; }
        if ($('#dep_uat_cert').val() == '') { $('#dep_uat_cert').addClass('warning'); all_values=false; }
        if ($('#dep_uat_private_key').val() == '') { $('#dep_uat_private_key').addClass('warning'); all_values=false; }
        if ($('#customer_id').val() == '') { $('#customer_id').addClass('warning'); all_values=false; }
        if ($('#devices').val() == '') { $('#devices').addClass('warning'); all_values=false; }
        if ($('#ship_date').val() == '') {$('#ship_date').addClass('warning'); all_values=false; }

        if (all_values == false)
            return

        $.ajax({
            type: 'POST',
            dataType: 'json',
            data: {
                dep_env: $('#dep_env').val(),
                dep_ship_to: $('#dep_ship_to').val(),
                dep_reseller_id: $('#dep_reseller_id').val(),
                dep_uat_cert: $('#dep_uat_cert').val(),
                dep_uat_private_key: $('#dep_uat_private_key').val(),
                customer_id: $('#customer_id').val(),
                devices: $('#devices').val(),
                order_type: $('#order_type').val(),
                ship_date: $('#ship_date').val()
            },
            url: "/enroll",
            success: function (data) {
                $('#enroll_result_modal').modal({ data: data, keyboard: false, show: true });
                setTimeout(() => {
                    $('#enroll_result_modal .enroll_result').html(data.result);
                    $('#enroll_result_modal .enroll_response').html(JSON.stringify(data.value, undefined, 2));
                }, 150);
            }
        });
    });
});