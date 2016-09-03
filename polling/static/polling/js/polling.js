$(document).ready(function() {

/*id_hospital_name_id*/
var base_hospital_api_url = "http://127.0.0.1:9000/";
//http://localhost:9000/patients/
//127.0.0.1:8000/api-token-auth/ username='admin' password='whatever'
function get_patients(){
    var data = $('#id_hospital_name_id').val();
    var alldata = data.split('-');
    var username = alldata[2];
    var token = alldata[1];
    var hospitalname = alldata[0];

        //Now to the ajax call and render data with check boxes ,but we are getting all patients for the time being.
    var url = base_hospital_api_url+'patients/'

    console.log(data);
    $.ajax({
        type: 'GET',
        url: url,
        headers: {
            'authorization': 'Token 5733d53988b231f78c703a5596370e51da027dd6',

        }
    }).done(function(data){
        console.log(data);
    });
}
$('#id_hospital_name_id').change(function() {
    get_patients();
});


});