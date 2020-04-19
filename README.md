# HackaTUMCovid20
Infineon Project Backbone Python Data analysis

Link to APK: https://syncandshare.lrz.de/getlink/fiRNvKLNrZH6kzeLAfhJgSkt/app.apk 

Backend Code runs on Python 

Hybrid Frontend Code can be compiled to both an Android and iOS application using Flutter, for easy installation on Android the .apk file is provided above

For demonstration purposes a video of the app and its funtionalities is further provided in infineonhealth.mkv
  
  
  
  
  
* Frontend Features (For the whole appflow please watch provided mkv video)    
   * Screen 1:  
     *  Overview of all patients, realtime monitoring of Last Turned, SAPS and Sevirity Score (calculated by Backend)    
     *  Buttons for turning patients and updating information on the backend     
   * Screen 2:
     * Realt time, dynmaic chart of a patient's health data
     * 4 different tabs with different data
     * User can input amount of last values to be displayed, chart automatically adjusts
     * Trigger settings listed below the chart
     * Real Time Monitoring of Severity score on the top of the screen
   * Screen 3
     * Detailed Patient Information
   * App in Background
     * constanly listening to changes in patient's severity status
     * sending sms to emergency contact when patient's status gets critical
