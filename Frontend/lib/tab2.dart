import 'package:flutter/material.dart';
import 'fetchjson.dart';
import 'package:sms/sms.dart';

class Tab2 extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    // TODO: implement build

    //String message = "Patient 1002 is in critical condition";




  SmsSender sender = new SmsSender();
  String address = "+4915114374456";
 
  SmsMessage message = new SmsMessage(address, 'Patient 1002 is in critical condition!');
  message.onStateChanged.listen((state) {
    if (state == SmsMessageState.Sent) {
      print("SMS is sent!");
    } else if (state == SmsMessageState.Delivered) {
      print("SMS is delivered!");
    }
  });
  sender.sendSms(message);

    return new Center(
      child: Column(
        children: <Widget>[
          new FlatButton(onPressed: getExpiredCO2, child: Text('getExpiredCO2'),),
           new FlatButton(onPressed: getDeviceID, child: Text('getDeviceID'),),
           new FlatButton(onPressed: getApi2, child: Text('getAPI2'),),
          new Text(
            "This is Patient Data Tab",
            style: new TextStyle(fontSize: 25.0),
          ),
        ],
      ),
    );
  }

 

}

void sendEmergencySms(String id) async {
await Future.delayed(const Duration(seconds: 2), (){});
SmsSender sender = new SmsSender();
  String address = "+4915114374456";
 
  SmsMessage message = new SmsMessage(address, 'Patient ' +id+ ' is in critical condition!');
  message.onStateChanged.listen((state) {
    if (state == SmsMessageState.Sent) {
      print("SMS is sent!");
    } else if (state == SmsMessageState.Delivered) {
      print("SMS is delivered!");
    }
  });
  sender.sendSms(message);
     }    