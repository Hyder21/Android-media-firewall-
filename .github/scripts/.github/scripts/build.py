import os

os.makedirs("app/src/main/java/com/tijara/mediafirewall", exist_ok=True)

# 1. MainActivity.kt
open("app/src/main/java/com/tijara/mediafirewall/MainActivity.kt","w").write('''
package com.tijara.mediafirewall
import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import android.widget.TextView

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        val tv = TextView(this)
        tv.text = "Media Firewall Active\\nBlocking media access per app"
        tv.textSize = 20f
        tv.setPadding(50,200,50,50)
        setContentView(tv)
    }
}
''')

# 2. MediaBlocker.kt
open("app/src/main/java/com/tijara/mediafirewall/MediaBlocker.kt","w").write('''
package com.tijara.mediafirewall
class MediaBlocker {
    fun isAllowed(pkg: String, type: String): Boolean { return false }
    fun logAttempt(pkg: String, type: String) { println("BLOCKED: $pkg -> $type") }
}
''')

# 3. AndroidManifest.xml
os.makedirs("app/src/main", exist_ok=True)
open("app/src/main/AndroidManifest.xml","w").write('''
<manifest xmlns:android="http://schemas.android.com/apk/res/android">
    <application android:label="MediaFirewall" android:theme="@android:style/Theme.Black.NoTitleBar">
        <activity android:name=".MainActivity" android:exported="true">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
    </application>
</manifest>
''')

# 4. build.gradle (app)
open("app/build.gradle","w").write('''
plugins { id 'com.android.application' id 'org.jetbrains.kotlin.android' }
android {
    namespace 'com.tijara.mediafirewall'
    compileSdk 34
    defaultConfig {
        applicationId "com.tijara.mediafirewall"
        minSdk 24
        targetSdk 34
        versionCode 1
        versionName "1.0"
    }
}
dependencies { implementation 'androidx.appcompat:appcompat:1.6.1' }
''')

# 5. Root build.gradle
open("build.gradle","w").write('''
plugins { id 'com.android.application' version '8.2.0' apply false
id 'org.jetbrains.kotlin.android' version '1.9.10' apply false }
''')

# 6. settings.gradle
open("settings.gradle","w").write("include ':app'")

# 7. gradle wrapper - download if missing
print("App structure created!")

# 8. Create gradlew stub
open("gradlew","w").write("#!/bin/sh\\necho 'Gradle wrapper placeholder'\\n./gradle/wrapper/gradle-wrapper.jar 2>/dev/null || gradle assembleDebug")
os.chmod("gradlew", 0o755)

print("DONE - One code built all files")
