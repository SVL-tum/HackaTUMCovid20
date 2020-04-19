import 'package:flutter/material.dart';
import 'package:infineonhealth/healthchart.dart';
import 'fetchjson.dart';
import 'dart:convert';
import 'package:http/http.dart' as http;
class Tab1 extends StatefulWidget {
  final String patientID;
  final String title;
  final String unit;
  
  Tab1({Key key, @required this.patientID, @required this.title, @required this.unit}) : super(key: key);

  @override
  _Tab1State createState() => _Tab1State();
}

class _Tab1State extends State<Tab1> {
  var data;
  int seconds;
  @override
  void initState() {
   
    super.initState();
    seconds = 500;
    //getData();
  }
  @override
  Widget build(BuildContext context) {
    return SingleChildScrollView(
          child: StreamBuilder<Object>(
        stream: getStreamPatientMonitorData(widget.patientID,seconds,widget.title),
        builder: (BuildContext context, AsyncSnapshot snapshot)
        {

        if(!snapshot.hasData)
        {
          return Center(child: Text('loading...'));
        }
        else
        {
          data = snapshot.data;
          return Column(
          mainAxisSize: MainAxisSize.min,
          crossAxisAlignment: CrossAxisAlignment.center,
          children: <Widget>[
            Container(
              height: 400,
              
               child: HealthChart(title: widget.title, data: data, unit: widget.unit) ,
            ),
            Padding(
              padding: const EdgeInsets.only(left: 8.0, right: 8),
              child: Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: <Widget>[
                  Text("Monitor last"),
                  new Container(
                    width: 120,
                child: new TextFormField(
                  initialValue: "500",
                  onChanged: (String value){
                    setState(() {
                      seconds = int.parse(value);
                    });
                    print(seconds.toString() +"Jooo");
                    },
                  keyboardType: TextInputType.number,
                  textAlign: TextAlign.center,
                  decoration: const InputDecoration(helperText: "amount of values"),
                  style: Theme.of(context).textTheme.body1,
                 
                  
                )),
                  Text("values"),
                ],
              ),
            ),
            Padding(
              padding: const EdgeInsets.only(top: 40),
              child: Center(child: Text("Trigger Settings", style: TextStyle(fontSize: 18),)),
            ),
            FutureBuilder(
              future: getApi2PatientAllVentilatorData(widget.patientID),
              builder: (context, snapshot) {
                if(snapshot.hasData)
                {
                 
                return Padding(
                  padding: const EdgeInsets.all(30.0),
                  child: Column(
                  
                    children: <Widget>[
                      Row(
                        mainAxisAlignment: MainAxisAlignment.center,
                          children: <Widget>[
                          Text("FiO2:  "),
                          Text(snapshot.data[0]["processed"]["triggerSettings"]["FiO2"].toString()),
                          Text(" %"),
                          Text("      "),
                           Text("IE:  "),
                          Text(snapshot.data[0]["processed"]["triggerSettings"]["IE"].toString()),
                          Text(""),
                          Text("      "),
                          Text("PEEP:  "),
                          Text(snapshot.data[0]["processed"]["triggerSettings"]["PEEP"].toString()),
                          Text(" cmH2O"),
                          
                        ],
                      ),
                      Padding(
                        padding: const EdgeInsets.only(top: 30),
                        child: Row(
                          mainAxisAlignment: MainAxisAlignment.center,
                            children: <Widget>[
                            Text("RR:  "),
                            Text(snapshot.data[0]["processed"]["triggerSettings"]["RR"].toString()),
                            Text(" 1/Minute"),
                            Text("      "),
                             Text("VT:  "),
                            Text(snapshot.data[0]["processed"]["triggerSettings"]["VT"].toString()),
                            Text(" mL"),
                            Text("      "),
                            Text("humidity:  "),
                            Text(snapshot.data[0]["processed"]["triggerSettings"]["humidity"].toString()),
                            Text(" %"),
                            
                          ],
                        ),
                      ),
                    ],
                  ),
                );
                }
                else
                return Center(child: Text("loading..."));
              }
            )
         //   Text('DeviceID: ' + data['0']['device_id'].toString()),
         //   Text('ExpiredCO2: ' + data['0']['processed']['ExpiredCO2'].toString()),
          ],
        );
        }
}
      ),
    )  ;
  }

Future<String> getData() async {
   data = await getApi2PatientMonitorData(widget.patientID,seconds,widget.title);


   // var test = await getApi2PatientSeverity("1002");
   // print(test);
   return 'success';
  }

}


