import 'package:flutter/material.dart';
import 'tab1.dart';
import 'tab2.dart';
import 'patientdata.dart';
import 'fetchjson.dart';

class PatientScreen extends StatefulWidget {
  final String patientID;
  PatientScreen({Key key, @required this.patientID}) : super(key: key);

  @override
  _PatientScreenState createState() => _PatientScreenState();
}

class _PatientScreenState extends State<PatientScreen> {
  int patientStatus;
  @override
  void initState() {
    
    super.initState();
    setState(() {
      

    });
  }
  @override
   Widget build(BuildContext context) {
    //build function returns a "Widget"
    final tabController = new DefaultTabController(
        length: 4,
        child: Scaffold(
           resizeToAvoidBottomPadding: true,
          appBar: new AppBar(
            title: Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: <Widget>[
Padding(
  padding: const EdgeInsets.only(right: 8.0),
  child:   Text(widget.patientID),
),
 StreamBuilder<Object>(
   stream: getStreamPatientSeverity(widget.patientID),
   builder: (context, snapshot) {
     if(snapshot.hasData)
     {
       print("Jo");
       print(snapshot);
       print(snapshot.data);
        return snapshot.data == 0
          ?
          Image.asset('assets/check.png', height: 25,)
          
          :
          snapshot.data == 1
          ?
          Image.asset('assets/problem.png', height: 25,)
          
          :
          Image.asset('assets/warning.png', height: 25);
   }
     
     else
     {
       print("No");
     return Text("loading...");
   }
   }
 ),
            
      RaisedButton(
        color: Colors.green,
        child: Text('Patient Data'),
        onPressed: () {
          Navigator.push(
    context,
    MaterialPageRoute(builder: (context) => PatientData(id: widget.patientID),)
  );
        },
      )

              ],
            ),

        
            bottom: new TabBar(
                indicatorColor: Colors.red,
                indicatorWeight: 2.0,
                tabs: [
                  new Tab(icon: new Icon(Icons.dvr),text: "O2"),
                  new Tab(icon: new Icon(Icons.remove_from_queue),text: "CO2"),
                  new Tab(icon: new Icon(Icons.panorama_vertical),text: "MVe"),
                  new Tab(icon: new Icon(Icons.timeline),text: "Frequency"),
               
            ]),
          ),
          body: new TabBarView(
              children: [
                new Tab1(title: "O2",patientID: widget.patientID, unit: "Expired O2 (%)",),
                new Tab1(title: "Co2",patientID: widget.patientID, unit: "Expired CO2 (%)"),
                new Tab1(title: "MVe",patientID: widget.patientID, unit: "MVe (mL)",),
                new Tab1(title: "frequency",patientID: widget.patientID, unit: "Frequency (1/minute)"),
                //new Tab2(),
              
              ]
          ),
        ),
    );
  return tabController;
    
}

  int getStatusOfPatient(String patientID)
  {
  int mockInt = 1;
  return mockInt;
  }
}