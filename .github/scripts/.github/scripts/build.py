import pathlib
pathlib.Path("app/src/main/java/com/mediafirewall/app").mkdir(parents=True, exist_ok=True)
open("settings.gradle","w").write("include ':app'\n")
open("build.gradle","w").write("buildscript{repositories{google();mavenCentral()}dependencies{classpath 'com.android.tools.build:gradle:8.1.4'}}allprojects{repositories{google();mavenCentral()}}")
open("app/build.gradle","w").write("plugins{id 'com.android.application'}\nandroid{namespace 'com.mediafirewall.app';compileSdk 34;defaultConfig{applicationId 'com.mediafirewall.app';minSdk 24;targetSdk 34}}\n")
open("app/src/main/AndroidManifest.xml","w").write('<?xml version="1.0" encoding="utf-8"?><manifest xmlns:android="http://schemas.android.com/apk/res/android"><application android:label="MediaFirewall"><activity android:name=".MainActivity" android:exported="true"><intent-filter><action android:name="android.intent.action.MAIN"/><category android:name="android.intent.category.LAUNCHER"/></intent-filter></activity></application></manifest>')
open("app/src/main/java/com/mediafirewall/app/MainActivity.java","w").write('package com.mediafirewall.app; public class MainActivity extends android.app.Activity {}')
