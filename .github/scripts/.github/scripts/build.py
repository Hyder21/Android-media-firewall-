import os
print("Starting build")

# Make folders
os.makedirs("app/src/main/java/com/tijara/mediafirewall", exist_ok=True)
os.makedirs("app/src/main", exist_ok=True)

# Create files - super safe
with open("app/src/main/java/com/tijara/mediafirewall/MainActivity.kt","w") as f:
    f.write("package com.tijara.mediafirewall\nclass MainActivity\n")

with open("app/src/main/AndroidManifest.xml","w") as f:
    f.write("<manifest></manifest>")

with open("app/build.gradle","w") as f:
    f.write("plugins { id 'com.android.application' }")

with open("build.gradle","w") as f:
    f.write("// root")

with open("settings.gradle","w") as f:
    f.write("include ':app'")

print("DONE - No error")
