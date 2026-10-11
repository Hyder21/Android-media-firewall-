import os, pathlib
p = pathlib.Path

p("app/src/main/java/com/tijara/mediafirewall").mkdir(parents=True, exist_ok=True)

open("app/src/main/java/com/tijara/mediafirewall/MainActivity.kt","w").write("""
package com.tijara.mediafirewall
import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import android.widget.TextView
class MainActivity : AppCompatActivity() {
 override fun onCreate(s: Bundle?) {
  super.onCreate(s)
  val t=TextView(this)
  t.text="Media Firewall\\nActive"
  t.textSize=22f
  t.setPadding(50,250,50,50)
  setContentView(t)
 }
}
""")

open("app/src/main/AndroidManifest.xml","w").write("""<manifest xmlns:android="http://schemas.android.com/apk/res/android"><application android:label="MediaFirewall" android:theme="@android:style/Theme.Black.NoTitleBar"><activity android:name=".MainActivity" android:exported="true"><intent-filter><action android:name="android.intent.action.MAIN"/><category android:name="android.intent.category.LAUNCHER"/></intent-filter></activity></application></manifest>""")

open("app/build.gradle","w").write("""
plugins { id 'com.android.application'; id 'org.jetbrains.kotlin.android' }
android { namespace 'com.tijara.mediafirewall'; compileSdk 34; defaultConfig { applicationId "com.tijara.mediafirewall"; minSdk 24; targetSdk 34; versionCode 1; versionName "1.0" } }
dependencies { implementation 'androidx.appcompat:appcompat:1.6.1' }
""")

open("build.gradle","w").write("""plugins { id 'com.android.application' version '8.2.0' apply false; id 'org.jetbrains.kotlin.android' version '1.9.10' apply false }""")
open("settings.gradle","w").write("include ':app'")
open("gradle.properties","w").write("org.gradle.jvmargs=-Xmx2g")
print("CREATED")
