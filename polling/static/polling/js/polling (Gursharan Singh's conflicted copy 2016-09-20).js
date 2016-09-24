var selected_patients = {};
$(document).ready(function() {

/*id_hospital_name_id*/
var base_hospital_api_url = "http://127.0.0.1:9000/";
//http://localhost:9000/patients/
//127.0.0.1:8000/api-token-auth/ username='admin' password='whatever'
//
//function setHeader(xhr) {
//
//  xhr.setRequestHeader('Authorization','Token 5733d53988b231f78c703a5596370e51da027dd6');
//  xhr.setRequestHeader('Access-Control-Allow-Origin','*');
//}

var allpatients = [];




function get_patients(){
    var data = $('#id_hospital_name_id').text();
    var alldata = data.split('-');
    var username = alldata[2];
    var token = alldata[1];
    var hospitalname = alldata[0];
//Accept: "application/json"
        //Now to the ajax call and render data with check boxes ,but we are getting all patients for the time being.
    var url = base_hospital_api_url+'patients/';
    //{ 'Access-Control-Allow-Origin': '*' }
    console.log(data);
    $.ajax({
        method: 'GET',
        url: url,
        crossDomain: true,
        cache: false,
        async: true,
        headers: {
            'Authorization': 'Token 5733d53988b231f78c703a5596370e51da027dd6',
            'Accept':'application/json',
        }
    }).done(function(response){
//        alert('Hello');
//        console.log(response.results);
        output = "";

        for(var i=0;i<response.results.length;i++){
            allpatients = response.results;
//            console.log(JSON.stringify(response.results[i]));
             output += "<input class='patients' type='checkbox' name='patients_group[]' value='"+ response.results[i].Patient_ID +"'/>" + response.results[i].FullName + "<br/>";
             output += "<input type='hidden' value='"+JSON.stringify(response.results[i])+"' name='"+response.results[i].Patient_ID+"' id='"+response.results[i].Patient_ID+"'  />";
//             output += 'Insurance Details : <input class="insurance" type="input" name="insurance_group[]" value="' +'"/>' + '<br/>';

//            $('#patient_checks').append(output);
        }
        output += "<input type='button' value='Click me' class ='savedata' id = 'savedata'>";

         $('#patient_checks').append(output);


//        $('#patient_checks').text(output);
        console.log(allpatients);


//        for{
//
//            output += "<input type='hidden' id='"+ FullName + "value='"+  + "/>";
//        }
        $('#id_subject_detail').val("Full Name: " + response.results[0].FullName+",\n"+response.results[0].FullAddress);
    });
}




    $('#id_hospital_name_id').change(function() {
        console.log('jXXXjj');
        get_patients();
    });



});


 $(document).on('change','.patients', function(){
            var currentVal = $(this).val() ;
            var id ='#'+currentVal;
            if($(this).is(':checked')){
            selected_patients[id] =  $.parseJSON($(id).val());
            console.log(selected_patients);
            }else{
              delete selected_patients[id];

              console.log('Removed');

             console.log(selected_patients);
            }

    });

$(document).on('click','.savedata', function(){

             create_post();

 });




function create_post() {
    console.log("Data Going !")
    $.ajax({
        url : "/polling/savesubjectsfromhospital/", // the endpoint
        type : "POST", // http method
        data : {data:selected_patients,'csrfmiddlewaretoken':"abac"}, // data sent with the post request
        success : function(json) {
            console.log(json); // log the returned json to the console
            console.log("success"); // another sanity check
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
};
