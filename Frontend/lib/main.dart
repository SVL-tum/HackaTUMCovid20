import 'package:flutter/material.dart';
import 'package:infineonhealth/patientScreen.dart';
import 'fetchjson.dart';
import 'tab2.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        // This is the theme of your application.
        //
        // Try running your application with "flutter run". You'll see the
        // application has a blue toolbar. Then, without quitting the app, try
        // changing the primarySwatch below to Colors.green and then invoke
        // "hot reload" (press "r" in the console where you ran "flutter run",
        // or simply save your changes to "hot reload" in a Flutter IDE).
        // Notice that the counter didn't reset back to zero; the application
        // is not restarted.
        primarySwatch: Colors.blue,
      ),
      home: MyHomePage(title: 'Patient Overview'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  MyHomePage({Key key, this.title}) : super(key: key);

  // This widget is the home page of your application. It is stateful, meaning
  // that it has a State object (defined below) that contains fields that affect
  // how it looks.

  // This class is the configuration for the state. It holds the values (in this
  // case the title) provided by the parent (in this case the App widget) and
  // used by the build method of the State. Fields in a Widget subclass are
  // always marked "final".

  final String title;

  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> with WidgetsBindingObserver {
  AppLifecycleState _notification; 
  List<String> patients;
  List<int> patientStatus;
  List<int> patientRScore;
  List<double> lastTurned;
  List<ListTile> list;
  int active;
  var data;
  bool _sent;


void didChangeAppLifecycleState(AppLifecycleState state) {
    setState(() {
      _notification = state;
      _sent = false;
    });
   // print(_notification);
   if(state.toString().contains("paused"))
   {
     setState(() {
       active = 1;
     });
   }
   
   //sendEmergencySms();
      
     }
   
   
   @override
     void initState() {
       
       super.initState();
       WidgetsBinding.instance.addObserver(this);
        setState(() {
        // data = getApi2Data();
         
         active = 0;
         _sent = false;
         
         
       });
     }
     @override
     void dispose() {
       WidgetsBinding.instance.removeObserver(this);
       super.dispose();
     }
   
   Future<Null> _onRefresh() async
   {
     setState(() {
         patients = getPatients();
         patientStatus = getPatientStatus();
         list = createList();
       });
       return null;
   }
   
     @override
     Widget build(BuildContext context) {
       // This method is rerun every time setState is called, for instance as done
       // by the _incrementCounter method above.
       //
       // The Flutter framework has been optimized to make rerunning build methods
       // fast, so that you can just rebuild anything that needs updating rather
       // than having to individually change instances of widgets.
       return Scaffold(
         
         appBar: AppBar(
           // Here we take the value from the MyHomePage object that was created by
           // the App.build method, and use it to set our appbar title.
           title: Text(widget.title),
         ),
         body:  StreamBuilder(
         stream: getStreamLData(),
         builder: (BuildContext context, AsyncSnapshot snapshot)
         {
           print(snapshot.data);
   
         if(snapshot.data == null)
         {
           return Center(child: Text('loading...'));
         }
         else
         {
           print(data);
          
             patients = getPatients();
         patientStatus = getPatientStatus();
         list = createList();
          
           print(data);
           
          return RefreshIndicator(
             onRefresh:_onRefresh ,
                   child: 
                   
               ListView(
                 
        children: 
                      
               list
               
               
               ,
             ),
           );
        
           }  // This trailing comma makes auto-formatting nicer for build methods.
         
         
     }
         ));
         }
     List<String> getPatients()
     {
        List<String> strArr = [];
        for(int i = 0; i < data.length; i++)
       {
           strArr.add(data[i]['id'].toString());
       }
   
       //List<String> mockString = ['Bed A1', 'Bed A2', 'Bed A3'];
       //return mockString;
       return strArr;
     }
   
     List<int> getPatientStatus()
     {
   
       //print(data);
       List<int> intarr = [];
       for(int i = 0; i < data.length; i++)
       {
           intarr.add(data[i]['severity']);
       }
       //List<int> mockInt = [0,1,2];
       return intarr;
     }
   
   List<int> getPatientRScore()
     {
   
       //print(data);
       List<int> intarr = [];
       for(int i = 0; i < data.length; i++)
       {
           intarr.add(data[i]['rscore']);
       }
       //List<int> mockInt = [0,1,2];
       return intarr;
     }
   
   List<double> getPatientDelta()
     {
   
       //print(data);
       List<double> doubarr = [];
       for(int i = 0; i < data.length; i++)
       {
           doubarr.add(data[i]['delta']);
       }
       //List<int> mockInt = [0,1,2];
       return doubarr;
     }
   
   
     List<ListTile> createList()
     {
       List<ListTile> tList = new List<ListTile>();
       tList.add(
          
                    ListTile(
         leading: Column(
           mainAxisAlignment: MainAxisAlignment.center,
           children: <Widget>[
             Text('Sort by/'),
             Text('PatientID')
           ],
         ),
         title: Center(
           child: 
             
             Row(
               mainAxisAlignment: MainAxisAlignment.spaceEvenly,
               children: <Widget>[
                 Container(
                   width: 70,
                   child: RaisedButton(child: Text('SAPS'),
                   color: active == 0
         ? Colors.green
         : Colors.blue
         
                   , onPressed: () {
                     if(active != 0)
                     {
                     setState(() {
                       active = 0;
                      list = createList();
                       print(active);
                     });
                     }
                   },),
                 ),
                 Container(
                   width: 110,
                   child: RaisedButton(child: Text('Last Turned'),
                   color: active == 2
         ? Colors.green
         : Colors.blue
         
                   , onPressed: () {
                     if(active != 2)
                     {
                     setState(() {
                       active = 2;
                      list = createList();
                       print(active);
                     });
                     }
                   },),
                 ),
                Container(
                  width: 90,
                  child: RaisedButton(materialTapTargetSize: MaterialTapTargetSize.shrinkWrap ,
         child: Text('Severity'),
         color: active == 1
         ? Colors.green
         : Colors.blue
         ,
          onPressed: () {
             if(active != 1)
               {
               setState(() {
                   active = 1;
                   list = createList();
                   print(active);
               });
               }
         },),
                ),
   
       
               
               ],
             ),
            
           
         ),
                    )
       );
        for(var i = 0; i < patients.length; i++)
        {
         tList.add(ListTile(
           //leading: Text(patients[i]),
         onTap: () {Navigator.push(
       context,
       MaterialPageRoute(builder: (context) => PatientScreen(patientID: patients[i],)),
     );},
     title: Row(
       children: <Widget>[
         Container(
           width: 70,
           child: Text(patients[i])),
         Container(
           alignment: Alignment.center,
           width: 70,
           child: Text(patientRScore[i].toString())),
          Container(width: 110,
          padding: EdgeInsets.only(left: 15),
          alignment: Alignment.center
          ,child: RaisedButton(
            color: Colors.grey,
            onPressed: () {
              print("pressedo");
              getApi2TurnPatient(data[i]['id'].toString());
            },
                   child: Column(
              children: <Widget>[
                Text(
                 //(lastTurned[i].toString()).toString()
                 //((DateFormat('hh:mm:ss')
                 _printDuration(Duration(seconds: double.parse(lastTurned[i].toString()).toInt()))
                ),
                Padding(
                  padding: const EdgeInsets.only(top: 8.0),
                  child: Icon(Icons.update),
                )
              ],
            ),
          )),
          Container(
             padding: EdgeInsets.only(left: 15),
            alignment: Alignment.center,
            width: 90,
            child: patientStatus[i] == 0
         ?
         Image.asset('assets/check.png', height: 40)
         
         :
         patientStatus[i] == 1
         ?
         Image.asset('assets/problem.png', height: 40)
         
         :
         Image.asset('assets/warning.png', height: 40),
          )
         //Text()
       ],
     ),
         contentPadding: EdgeInsets.only(left: 20, right: 20, top: 20),
         //trailing: 
         ));
        }
     return tList;
     }
   
   
    String _printDuration(Duration duration) {
           String twoDigits(int n) {
             if (n >= 10) return "$n";
             return "0$n";
           }
   
           String twoDigitMinutes = twoDigits(duration.inMinutes.remainder(60));
           String twoDigitSeconds = twoDigits(duration.inSeconds.remainder(60));
           return "${twoDigits(duration.inHours)}:$twoDigitMinutes:$twoDigitSeconds";
         }
   
    Future<String> getLData() async
     {
       if(active == 1)
       data = await getApi2PatientsBySeverity();
       if(active == 0)
       data = await getApi2PatientsByRScore();
       if(active == 2)
            data = await getApi2PatientsByDelta();
   
   
       print("recieving");
         
        patients = getPatients();
        patientStatus = getPatientStatus();
        patientRScore = getPatientRScore();
        lastTurned =getPatientDelta();
        list = createList();

        if(patientStatus[0] > 1 && _notification.toString().contains("paused") && _sent == false )
        {
            sendEmergencySms(patients[0]);
            setState(() {
               _sent = true;
            });
           
        }
       
       //print(data);
       return 'Success';
     }
   
   
     Stream getStreamLData()
   {
     return Stream.periodic(Duration(seconds: 1))
             .asyncMap((i) => getLData());
         
   
   }
   
    
}


