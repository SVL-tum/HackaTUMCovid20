import 'package:syncfusion_flutter_charts/charts.dart';
import 'package:flutter/material.dart';
import 'package:intl/intl.dart';

class HealthChart extends StatefulWidget {
  var data;
  String title;
  String unit;
  HealthChart({Key key, @required this.data, @required this.title, @required this.unit}) : super(key: key);

  @override
  _HealthChartState createState() => _HealthChartState();
}

class _HealthChartState extends State<HealthChart> {
  @override
 Widget build(BuildContext context) {
   print(widget.data[0]);
   
  return Scaffold(
    body: Center(
        child: Container(
          padding: EdgeInsets.only(right: 10),
          child:  SfCartesianChart(
            
            
            
                       primaryXAxis: CategoryAxis(),
            // Chart title
            title: ChartTitle(text: widget.unit),
            // Enable legend
            legend: Legend(isVisible: false, title: LegendTitle(text: 'Timestamp')),
            // Enable tooltip
            tooltipBehavior: TooltipBehavior(enable: true),
            
            series: <LineSeries<HealthData, String>>[
              LineSeries<HealthData, String>(
                
                dataSource:  generateHealthData(),
                xValueMapper: (HealthData health, _) => health.time,
                yValueMapper: (HealthData health, _) => health.value,
                // Enable data label
                dataLabelSettings: DataLabelSettings(isVisible: false)
 
              )
            ]
          )
        )
      )
  );
}

generateHealthData()
{
  List<HealthData> lList = [];
  for(int i = 0; i < widget.data["measurements"].length;i++)
  {
    
var date = DateTime.fromMillisecondsSinceEpoch(widget.data["timestamps"][i]*1000);
//var formattedDate = DateFormat.ms().format(date).toString();
 // var formattedDate = date.hour.toString() +":" + date.minute.toString() +":"+ date.second.toString();
 // print(date.toString().substring(11,19));
    lList.add(HealthData(date.toString().substring(11,19), widget.data["measurements"][i]));
  }
  return lList;
}
}
class HealthData {
  HealthData(this.time, this.value);
  final String time;
  final double value;
}
