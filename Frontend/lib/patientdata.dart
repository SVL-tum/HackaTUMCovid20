import 'package:flutter/material.dart';
import 'fetchjson.dart';
import 'package:sms/sms.dart';
class PatientData extends StatelessWidget {
final String id;
  const PatientData({Key key, @required this.id}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Patient Data"),
      ),
          body: FutureBuilder(
            future: getApi2PatientAllData(id),
            builder: (context, snapshot) {
              if(!snapshot.hasData)
              {
                return ListView(
        children: <Widget>[
              Padding(
                padding: const EdgeInsets.only(left: 20.0, right: 20),
                child: ListTile(
                  title: Text('Data'),
                  trailing: Text('Info'),
                ),
              )
        ],
      );
              }
              else              
              {
                
                         return Padding(
                           padding: const EdgeInsets.only(left: 20, right: 20),
                           child: ListView(
        children: <Widget>[
             
                ListTile(
                  title: Text('Data', style: TextStyle(fontSize: 18),),
                  trailing: Text('Info', style: TextStyle(fontSize: 18)),
                ),
                ListTile(
                  title: Text('ID'),
                  trailing: Text(snapshot.data["id"].toString()),
                ),
              
              ListTile(
                  title: Text('Name'),
                  trailing: Text(snapshot.data["name"].toString()),
                ),
              
              ListTile(
                  title: Text('Age'),
                  trailing: Text(snapshot.data["age"].toString()),
                ),
              
              ListTile(
                  title: Text("Smoker"),
                  trailing: Text(snapshot.data["smoker"].toString()),
                ),
              
              ListTile(
                  title: Text('BMI'),
                  trailing: Text(snapshot.data["bmi"].toString()),
                ),
                ListTile(
                  title: Text('SAPS'),
                  trailing: Text(snapshot.data["rscore"].toString()),
                ),              

               ListTile(
                  title: Text('Severity'),
                  trailing: Text(snapshot.data["severity"].toString()),
                ),
                 ListTile(
                  title: Text('state'),
                  trailing: Text(snapshot.data["state"].toString()),
                ),
                 ListTile(
                  title: Text('last time turned over'),
                  trailing: Text(snapshot.data["last_time_wendet"].toString()),
                ),
                 ListTile(
                  title: Text('delta'),
                  trailing: Text(snapshot.data["delta"].toString()),
                ),
              
        ],
      ),
                         );
              }
              
            }
          ),
    );
  }



}