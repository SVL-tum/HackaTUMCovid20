import 'dart:convert';

import 'package:http/http.dart' as http;



Future<String> getData() async {
    var response = await http.get(
      Uri.encodeFull("https://jsonplaceholder.typicode.com/posts"),
      headers: {
        "Accept": "application/json"
      }
    );
    List data = json.decode(response.body);
    print(data[1]["title"]);
    
    return "Success!";
  }

    Future<String> getData2() async {
    var response = await http.get(
      Uri.encodeFull("http://api.theopenvent.com/exampledata/v2/data"),
      headers: {
        "Accept": "application/json"
      }
    );
   var data = json.decode(response.body);
    print(data['0']['device_id']);
    
    return "Success!";
  }

  Future<String> getDeviceID() async {
    var response = await http.get(
      Uri.encodeFull("http://api.theopenvent.com/exampledata/v2/data"),
      headers: {
        "Accept": "application/json"
      }
    );
   var data = json.decode(response.body);
    print(data['0']['device_id']);
    
    return "Success!";
  }

    Future<String> getExpiredCO2() async {
    var response = await http.get(
      Uri.encodeFull("http://api.theopenvent.com/exampledata/v2/data"),
      headers: {
        "Accept": "application/json"
      }
    );
   var data = json.decode(response.body);
    print(data['0']['processed']['ExpiredCO2']);
    
    return "Success!";
  }

  

   Future<String> getApi2() async {
    var response = await http.get(
      Uri.encodeFull("http://129.187.212.1:5000/patient?sorting=rscore"),
      headers: {
       // "Accept": "application/json"
      }
    );
   var data = json.decode(response.body);
   //var data = response.body;
    print(data[0]['id']);
    
    return "Success!";
  }

    Future getApi2PatientsBySeverity() async {
    var response = await http.get(
      Uri.encodeFull("http://129.187.212.1:5000/patient?sorting=severity"),
      headers: {
       // "Accept": "application/json"
      }
    );
   var data = json.decode(response.body);
   //var data = response.body;
    
    
    return data;
  }

      Future getApi2PatientsByRScore() async {
    var response = await http.get(
      Uri.encodeFull("http://129.187.212.1:5000/patient?sorting=rscore"),
      headers: {
       // "Accept": "application/json"
      }
    );
   var data = json.decode(response.body);
   //var data = response.body;
    
    
    return data;
  }

 



  Future getApi2PatientsByDelta() async {
    var response = await http.get(
      Uri.encodeFull("http://129.187.212.1:5000/patient?sorting=delta"),
      headers: {
       // "Accept": "application/json"
      }
    );
   var data = json.decode(response.body);
   //var data = response.body;
    
    
    return data;
  }
   Future getApi2PatientMonitorData(String id, int seconds, String measurement) async {
    var string = "http://129.187.212.1:5000/tdata?patientid=";
    string += id;
    string += "&seconds=";
    string += seconds.toString();
    string += "&measurement=";
    string += measurement;
    print(string);

    var response = await http.get(
      //Uri.encodeFull("http://129.187.212.1:5000/tdata?patientid=1004&seconds=500&measurement=O2"),
      Uri.encodeFull(string),
      headers: {
       // "Accept": "application/json"
      }
    );
   var data = json.decode(response.body);
   //var data = response.body;
    
    
    return data;


   }
   Future<int> getApi2PatientSeverity(String id) async {
    
    //var string = http://129.187.212.1:5000/patient_by_id?patientid=1000;
    var string = "http://129.187.212.1:5000/patient_by_id?patientid=";
    string += id;
    

    var response = await http.get(
      //Uri.encodeFull("http://129.187.212.1:5000/tdata?patientid=1004&seconds=500&measurement=O2"),
      Uri.encodeFull(string),
      headers: {
       // "Accept": "application/json"
      }
    );
   var data = json.decode(response.body);
   //var data = response.body;
    
    
    return data["severity"];
  }

Stream getStreamPatientSeverity(String id)
{
  return Stream.periodic(Duration(seconds: 5))
          .asyncMap((i) => getApi2PatientSeverity(id));
      

}    

Stream getStreamPatientMonitorData(String id, int seconds, String measurement)
{
  return Stream.periodic(Duration(seconds: 2))
          .asyncMap((i) => getApi2PatientMonitorData(id,seconds, measurement));
      

}    

Future getApi2PatientAllData(String id) async {
    
    //var string = http://129.187.212.1:5000/patient_by_id?patientid=1000;
    var string = "http://129.187.212.1:5000/patient_by_id?patientid=";
    string += id;
    

    var response = await http.get(
      //Uri.encodeFull("http://129.187.212.1:5000/tdata?patientid=1004&seconds=500&measurement=O2"),
      Uri.encodeFull(string),
      headers: {
       // "Accept": "application/json"
      }
    );
   var data = json.decode(response.body);
   print(data);
   //var data = response.body;
    
    
    return data;
  }


Future getApi2TurnPatient(String id) async {

 
  var string = "http://129.187.212.1:5000/backflip?patientid=";
    string += id;
    

    var response = await http.get(
      Uri.encodeFull(string),
      headers: {
       // "Accept": "application/json"
      }
    );
   
   //var data = response.body;
    
    
    return "Success";


}

  Future getApi2PatientAllVentilatorData(String id) async {
    
    //var string = http://129.187.212.1:5000/patient_by_id?patientid=1000;
    var string = "http://129.187.212.1:5000/ventilator_by_patienid?patientid=";
    string += id;
    

    var response = await http.get(
      //Uri.encodeFull("http://129.187.212.1:5000/tdata?patientid=1004&seconds=500&measurement=O2"),
      Uri.encodeFull(string),
      headers: {
       // "Accept": "application/json"
      }
    );
   var data = json.decode(response.body);
   print(data);
   //var data = response.body;
    
    
    return data;
  }